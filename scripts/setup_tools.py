#!/usr/bin/env python3
"""
Set up project-local documentation tooling.

The initial setup downloads a pinned PlantUML jar into the repository so
documentation validation does not depend on a user-specific global path. Later
setup tasks can be added here behind explicit flags or subcommands.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_PLANTUML_VERSION = os.environ.get("PLANTUML_VERSION", "1.2025.4")
DEFAULT_PLANTUML_DEST = Path("tools") / "plantuml.jar"


def default_plantuml_url(version: str) -> str:
    return f"https://github.com/plantuml/plantuml/releases/download/v{version}/plantuml-{version}.jar"


def make_readable(path: Path) -> None:
    try:
        path.chmod(0o644)
    except OSError:
        pass


def download_with_urllib(url: str, destination: Path, *, timeout: int) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "spec-docs-tooling-setup"})

    temp_path: Path | None = None
    try:
        with urlopen(request, timeout=timeout) as response:
            with tempfile.NamedTemporaryFile(
                "wb",
                delete=False,
                dir=destination.parent,
                prefix=f".{destination.name}.",
                suffix=".download",
            ) as temp_file:
                temp_path = Path(temp_file.name)
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    temp_file.write(chunk)

        if temp_path is None or temp_path.stat().st_size == 0:
            raise RuntimeError("download produced an empty file")
        temp_path.replace(destination)
        make_readable(destination)
    except (HTTPError, URLError, TimeoutError, RuntimeError) as error:
        if temp_path and temp_path.exists():
            temp_path.unlink()
        raise RuntimeError(f"could not download {url}: {error}") from error


def download_with_curl(url: str, destination: Path, *, timeout: int) -> None:
    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError("curl is not available")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "wb",
        delete=False,
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".download",
    ) as temp_file:
        temp_path = Path(temp_file.name)

    try:
        result = subprocess.run(
            [
                curl,
                "--fail",
                "--location",
                "--show-error",
                "--silent",
                "--output",
                str(temp_path),
                url,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
        if result.returncode != 0:
            message = result.stderr.strip() or result.stdout.strip() or f"curl exited {result.returncode}"
            raise RuntimeError(message)
        if temp_path.stat().st_size == 0:
            raise RuntimeError("download produced an empty file")
        temp_path.replace(destination)
        make_readable(destination)
    except (OSError, subprocess.SubprocessError, RuntimeError) as error:
        if temp_path.exists():
            temp_path.unlink()
        raise RuntimeError(f"could not download {url} with curl: {error}") from error


def download_file(url: str, destination: Path, *, force: bool, timeout: int) -> None:
    if destination.exists() and not force:
        print(f"PlantUML already exists: {destination}")
        print("Use --force to re-download it.")
        return

    try:
        download_with_urllib(url, destination, timeout=timeout)
    except RuntimeError as python_error:
        print(f"Python download failed; retrying with curl: {python_error}", file=sys.stderr)
        try:
            download_with_curl(url, destination, timeout=timeout)
        except RuntimeError as curl_error:
            raise RuntimeError(f"{python_error}; curl fallback failed: {curl_error}") from curl_error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root. Default: parent of scripts/.",
    )
    parser.add_argument(
        "--plantuml-version",
        default=DEFAULT_PLANTUML_VERSION,
        help="PlantUML version to download. Default: %(default)s.",
    )
    parser.add_argument(
        "--plantuml-url",
        default=None,
        help="Override the PlantUML jar URL.",
    )
    parser.add_argument(
        "--plantuml-dest",
        type=Path,
        default=DEFAULT_PLANTUML_DEST,
        help="Destination path, relative to repo root unless absolute. Default: %(default)s.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even when the destination file already exists.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Download timeout in seconds. Default: %(default)s.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    destination = args.plantuml_dest if args.plantuml_dest.is_absolute() else repo_root / args.plantuml_dest
    url = args.plantuml_url or default_plantuml_url(args.plantuml_version)

    try:
        download_file(url, destination, force=args.force, timeout=args.timeout)
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    print(f"PlantUML jar ready: {destination}")
    print(f"Use it with: python3 scripts/validate_docs.py --plantuml-jar {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
