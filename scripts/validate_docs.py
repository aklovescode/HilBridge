#!/usr/bin/env python3
"""
Generic spec documentation validator.

Default scope: recursive ``*.md`` under ``spec/``. Hidden paths are skipped.

Checks:

* Markdown links resolve.
* The spec graph is reachable from ``spec/Vision.md`` by default.
* The conventional hierarchy has traceability:
  Vision -> Capabilities -> Flows -> Modules -> Code, with optional
  Modules/Flows -> Contracts -> Code when a stable boundary is worth
  documenting.
* Modules and contracts list real repo-relative source paths under ``## Code``.
* PlantUML fenced blocks are syntactically valid when PlantUML is available.

Use ``--no-plantuml`` when Java or the PlantUML jar is unavailable. Use
``--plantuml-only`` with explicit paths for standalone Markdown outside
``spec/``.

Exit 0 if all checks pass; exit 2 for CLI / missing-input errors; exit 1 for
validation failures.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse

DEFAULT_SPEC_DIR = "spec"
DEFAULT_ENTRYPOINT = "Vision.md"
DEFAULT_PLANTUML_RELATIVE_PATH = Path("tools") / "plantuml.jar"
DEFAULT_REQUIRED_PATHS = (
    "Vision.md",
    "doc_issues.md",
    "capabilities",
    "flows",
    "modules",
    "contracts",
    "architecture_notes",
    "domain_notes",
    "technology_notes",
)
KNOWLEDGE_NOTE_DIRS = ("architecture_notes", "domain_notes", "technology_notes")

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
CODE_BULLET_RE = re.compile(r"^\s*-\s+(.+?)\s*$")
PLANTUML_FENCE_OPEN = re.compile(r"^```\s*plantuml\s*$", re.IGNORECASE)
PLANTUML_FENCE_CLOSE = re.compile(r"^```\s*$")


@dataclass(frozen=True)
class SpecSets:
    all_files: list[Path]
    capabilities: list[Path]
    flows: list[Path]
    modules: list[Path]
    contracts: list[Path]
    test_scenarios: list[Path]
    notes: list[Path]


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def normalize_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def is_external_target(target: str) -> bool:
    parsed = urlparse(target)
    return bool(parsed.scheme) or target.startswith("//")


def is_skipped_markdown(path: Path, root: Path, skip_filenames: set[str]) -> bool:
    if path.name.startswith(".") or path.name in skip_filenames:
        return True
    if not is_relative_to(path, root):
        return True
    rel = path.relative_to(root)
    return any(part.startswith(".") for part in rel.parts)


def discover_spec_markdown(spec_root: Path, skip_filenames: set[str]) -> list[Path]:
    if not spec_root.exists():
        return []
    return sorted(
        (
            path
            for path in spec_root.rglob("*.md")
            if not is_skipped_markdown(path, spec_root, skip_filenames)
        ),
        key=lambda path: path.as_posix(),
    )


def classify_specs(files: list[Path], spec_root: Path) -> SpecSets:
    def under(dirname: str) -> list[Path]:
        base = spec_root / dirname
        return sorted(path for path in files if path.parent == base)

    notes: list[Path] = []
    for dirname in KNOWLEDGE_NOTE_DIRS:
        notes.extend(under(dirname))

    return SpecSets(
        all_files=files,
        capabilities=under("capabilities"),
        flows=under("flows"),
        modules=under("modules"),
        contracts=under("contracts"),
        test_scenarios=under("test_scenarios"),
        notes=sorted(notes),
    )


def iter_markdown_link_targets(text: str) -> list[str]:
    return [normalize_link_target(match.group(1)) for match in MARKDOWN_LINK_RE.finditer(text)]


def resolve_markdown_links(
    files: list[Path],
    repo_root: Path,
) -> tuple[dict[Path, list[Path]], list[str], int]:
    file_set = {path.resolve() for path in files}
    links: dict[Path, list[Path]] = defaultdict(list)
    errors: list[str] = []
    checked = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in iter_markdown_link_targets(text):
            if is_external_target(target) or target.startswith("#"):
                continue
            rel = target.split("#", 1)[0]
            if not rel:
                continue
            checked += 1
            resolved = (path.parent / unquote(rel)).resolve()
            if not resolved.exists():
                errors.append(f"{display_path(path, repo_root)}: broken markdown link {target!r}")
                continue
            if resolved in file_set:
                links[path.resolve()].append(resolved)

    return links, errors, checked


def reachable_from_entrypoint(
    links: dict[Path, list[Path]],
    entrypoint: Path,
) -> set[Path]:
    if not entrypoint.exists():
        return set()

    seen: set[Path] = set()
    queue: deque[Path] = deque([entrypoint.resolve()])
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        for target in links.get(current, []):
            if target not in seen:
                queue.append(target)
    return seen


def extract_code_refs(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    refs: list[str] = []
    in_code = False

    for line in lines:
        if line.strip() == "## Code":
            in_code = True
            continue
        if in_code and line.startswith("## "):
            in_code = False
            continue
        if not in_code:
            continue
        match = CODE_BULLET_RE.match(line)
        if not match:
            continue
        ref = match.group(1).strip().strip("`")
        if not ref or ref.startswith("[") or is_external_target(ref):
            continue
        refs.append(ref)

    return refs


def validate_spec_graph(
    files: list[Path],
    repo_root: Path,
    spec_root: Path,
    entrypoint: Path,
    required_paths: tuple[str, ...],
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    stats: dict[str, int] = {}
    spec = classify_specs(files, spec_root)
    file_set = {path.resolve() for path in files}
    links, link_errors, link_count = resolve_markdown_links(files, repo_root)
    errors.extend(link_errors)

    stats["markdown_files"] = len(files)
    stats["markdown_links"] = link_count
    stats["capabilities"] = len(spec.capabilities)
    stats["flows"] = len(spec.flows)
    stats["modules"] = len(spec.modules)
    stats["contracts"] = len(spec.contracts)
    stats["test_scenarios"] = len(spec.test_scenarios)
    stats["knowledge_notes"] = len(spec.notes)

    for rel_path in required_paths:
        required = spec_root / rel_path
        if not required.exists():
            errors.append(f"missing required spec path: {display_path(required, repo_root)}")

    reachable = reachable_from_entrypoint(links, entrypoint)
    stats["reachable_from_entrypoint"] = len(reachable)
    if entrypoint.exists():
        for path in sorted(path for path in files if path.resolve() not in reachable):
            errors.append(
                f"{display_path(path, repo_root)}: not reachable from {display_path(entrypoint, repo_root)}"
            )
    else:
        errors.append(f"missing entrypoint: {display_path(entrypoint, repo_root)}")

    capability_by_resolved = {path.resolve(): path for path in spec.capabilities}
    flow_by_resolved = {path.resolve(): path for path in spec.flows}
    module_by_resolved = {path.resolve(): path for path in spec.modules}
    contract_by_resolved = {path.resolve(): path for path in spec.contracts}

    cap_to_flows: dict[Path, set[Path]] = defaultdict(set)
    flow_to_modules: dict[Path, set[Path]] = defaultdict(set)
    flow_to_contracts: dict[Path, set[Path]] = defaultdict(set)
    module_to_contracts: dict[Path, set[Path]] = defaultdict(set)
    module_code_refs: dict[Path, list[str]] = {}
    contract_code_refs: dict[Path, list[str]] = {}
    source_ref_total = 0

    for capability in spec.capabilities:
        for target in links.get(capability.resolve(), []):
            if target in flow_by_resolved:
                cap_to_flows[capability].add(flow_by_resolved[target])

    for flow in spec.flows:
        for target in links.get(flow.resolve(), []):
            if target in capability_by_resolved:
                cap_to_flows[capability_by_resolved[target]].add(flow)
            if target in module_by_resolved:
                flow_to_modules[flow].add(module_by_resolved[target])
            if target in contract_by_resolved:
                flow_to_contracts[flow].add(contract_by_resolved[target])

    for module in spec.modules:
        refs = extract_code_refs(module)
        module_code_refs[module] = refs
        source_ref_total += len(refs)
        for target in links.get(module.resolve(), []):
            if target in flow_by_resolved:
                flow_to_modules[flow_by_resolved[target]].add(module)
            if target in contract_by_resolved:
                module_to_contracts[module].add(contract_by_resolved[target])

    for contract in spec.contracts:
        refs = extract_code_refs(contract)
        contract_code_refs[contract] = refs
        source_ref_total += len(refs)
        for target in links.get(contract.resolve(), []):
            if target in flow_by_resolved:
                flow_to_contracts[flow_by_resolved[target]].add(contract)
            if target in module_by_resolved:
                module_to_contracts[module_by_resolved[target]].add(contract)

    stats["source_refs"] = source_ref_total

    for capability in spec.capabilities:
        if not cap_to_flows[capability]:
            errors.append(f"{display_path(capability, repo_root)}: capability has no linked flow")

    for flow in spec.flows:
        if not flow_to_modules[flow]:
            errors.append(f"{display_path(flow, repo_root)}: flow has no linked module")

    for module in spec.modules:
        if not module_code_refs[module]:
            errors.append(f"{display_path(module, repo_root)}: module has no ## Code source paths")

    stats["flows_with_contracts"] = sum(1 for flow in spec.flows if flow_to_contracts[flow])
    stats["modules_with_contracts"] = sum(1 for module in spec.modules if module_to_contracts[module])

    for contract in spec.contracts:
        if not contract_code_refs[contract]:
            errors.append(f"{display_path(contract, repo_root)}: contract has no ## Code source paths")

    unique_refs = sorted(
        {
            ref
            for refs in list(module_code_refs.values()) + list(contract_code_refs.values())
            for ref in refs
        }
    )
    stats["unique_source_paths"] = len(unique_refs)
    for ref in unique_refs:
        if not (repo_root / ref).exists():
            errors.append(f"missing source path listed in ## Code: {ref}")

    for path in files:
        if path.resolve() not in file_set:
            errors.append(f"{path}: internal validator path classification error")

    return errors, stats


def extract_plantuml_blocks(markdown_text: str) -> list[tuple[int, str]]:
    """Return ``(start_line_1_based_for_body, raw_puml_without_fences)``."""
    lines = markdown_text.splitlines()
    blocks: list[tuple[int, str]] = []
    i = 0
    while i < len(lines):
        if PLANTUML_FENCE_OPEN.match(lines[i]):
            start_line_open_fence = i + 1
            i += 1
            block_lines: list[str] = []
            while i < len(lines) and not PLANTUML_FENCE_CLOSE.match(lines[i]):
                block_lines.append(lines[i])
                i += 1
            blocks.append((start_line_open_fence + 1, "\n".join(block_lines)))
        i += 1
    return blocks


def run_plantuml_syntax_check(
    jar_path: Path,
    puml_text: str,
) -> subprocess.CompletedProcess[str]:
    with tempfile.NamedTemporaryFile("w", suffix=".puml", delete=False) as temp_file:
        temp_file.write(puml_text)
        temp_path = Path(temp_file.name)
    try:
        return subprocess.run(
            ["java", "-jar", str(jar_path), "-syntax", str(temp_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    finally:
        try:
            temp_path.unlink()
        except OSError:
            pass


def validate_plantuml_markdown(
    rel: str,
    content: str,
    jar_path: Path,
    *,
    quiet_ok: bool = False,
) -> bool:
    blocks = extract_plantuml_blocks(content)
    if not blocks:
        return True

    if not jar_path.is_file():
        print(f"{rel}: PlantUML jar not found: {jar_path}", file=sys.stderr)
        return False

    ok_all = True
    for idx, (start_line, block_text) in enumerate(blocks, start=1):
        result = run_plantuml_syntax_check(jar_path, block_text)
        ok_diag = result.returncode == 0 and "ERROR" not in result.stdout and "ERROR" not in result.stderr
        if ok_diag:
            if not quiet_ok:
                print(f"{rel}: diagram {idx} OK (starts at line {start_line})")
            continue

        ok_all = False
        print(f"{rel}: diagram {idx} FAILED (starts at line {start_line})", file=sys.stderr)
        if result.stdout:
            print("--- stdout ---", file=sys.stderr)
            print(result.stdout, file=sys.stderr)
        if result.stderr:
            print("--- stderr ---", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
    return ok_all


def git_changed_markdown_under(repo_root: Path, root: Path) -> set[Path]:
    if not (repo_root / ".git").exists():
        return set()

    root_arg = root.relative_to(repo_root).as_posix()
    out: set[Path] = set()

    def parse_null_names(raw: bytes) -> list[str]:
        return [name for name in raw.decode().split("\0") if name.endswith(".md")]

    diff = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--name-only", "-z", "HEAD", "--", root_arg],
        capture_output=True,
    )
    if diff.returncode == 0:
        for name in parse_null_names(diff.stdout):
            path = (repo_root / name).resolve()
            if path.is_file():
                out.add(path)

    untracked = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "ls-files",
            "-o",
            "--exclude-standard",
            "-z",
            "--",
            root_arg,
        ],
        capture_output=True,
    )
    if untracked.returncode == 0:
        for name in parse_null_names(untracked.stdout):
            path = (repo_root / name).resolve()
            if path.is_file():
                out.add(path)

    return out


def run_plantuml_checks(
    paths: list[Path],
    jar_path: Path,
    repo_root: Path,
    *,
    verbose: bool,
) -> tuple[bool, int, int]:
    ok = True
    diagram_total = 0
    files_with_puml = 0
    for path in paths:
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as error:
            print(f"{path}: read error (PlantUML): {error}", file=sys.stderr)
            ok = False
            continue
        blocks = extract_plantuml_blocks(content)
        if not blocks:
            continue
        diagram_total += len(blocks)
        files_with_puml += 1
        rel = display_path(path, repo_root)
        if not validate_plantuml_markdown(rel, content, jar_path, quiet_ok=not verbose):
            ok = False
    return ok, diagram_total, files_with_puml


def run_plantuml_only(
    paths: list[Path],
    jar_path: Path,
    repo_root: Path,
    *,
    verbose: bool,
) -> int:
    if not paths:
        print("--plantuml-only requires at least one markdown file", file=sys.stderr)
        return 2
    missing = [path for path in paths if not path.is_file()]
    if missing:
        for path in missing:
            print(f"File not found: {path}", file=sys.stderr)
        return 2
    ok, diagram_total, files_with_puml = run_plantuml_checks(paths, jar_path, repo_root, verbose=verbose)
    if not ok:
        return 1
    print(f"PlantUML OK ({diagram_total} diagram(s) in {files_with_puml} file(s)).", file=sys.stderr)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root. Default: parent of scripts/.",
    )
    parser.add_argument(
        "--spec-root",
        type=Path,
        default=None,
        help="Spec/documentation root. Default: <repo-root>/spec.",
    )
    parser.add_argument(
        "--entrypoint",
        default=DEFAULT_ENTRYPOINT,
        help="Entrypoint markdown path relative to spec root. Default: %(default)s.",
    )
    parser.add_argument(
        "--required-path",
        dest="required_paths",
        action="append",
        default=None,
        help=(
            "Required path relative to spec root. May be repeated. "
            "Defaults to this project's conventional spec directories."
        ),
    )
    parser.add_argument(
        "--no-required-paths",
        action="store_true",
        help="Skip required spec path checks.",
    )
    parser.add_argument(
        "--skip-file",
        dest="skip_files",
        action="append",
        default=[],
        help="Markdown filename to skip during discovery. May be repeated.",
    )
    parser.add_argument(
        "--no-plantuml",
        action="store_true",
        help="Skip PlantUML checks when Java or the PlantUML jar is unavailable.",
    )
    parser.add_argument(
        "--plantuml-only",
        action="store_true",
        help="Validate only fenced ```plantuml``` blocks in PATHS.",
    )
    parser.add_argument(
        "--verbose-plantuml",
        action="store_true",
        help="Print one line per successful PlantUML diagram.",
    )
    parser.add_argument(
        "--plantuml-all",
        action="store_true",
        help=(
            "Run PlantUML -syntax on every validated spec file. Default: only "
            "git-changed or untracked spec/*.md when no explicit paths are passed."
        ),
    )
    parser.add_argument(
        "--plantuml-jar",
        dest="plantuml_jar",
        type=Path,
        default=None,
        help=(
            "PlantUML jar path. Defaults to env PLANTUML_JAR or "
            "<repo-root>/tools/plantuml.jar."
        ),
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files. Default: recursive spec/**/*.md.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    spec_root = (args.spec_root.resolve() if args.spec_root else repo_root / DEFAULT_SPEC_DIR)
    entrypoint = spec_root / args.entrypoint
    plantuml_jar = (
        args.plantuml_jar.resolve()
        if args.plantuml_jar
        else Path(os.environ.get("PLANTUML_JAR", repo_root / DEFAULT_PLANTUML_RELATIVE_PATH)).resolve()
    )
    required_paths = (
        tuple()
        if args.no_required_paths
        else tuple(args.required_paths) if args.required_paths else DEFAULT_REQUIRED_PATHS
    )
    skip_filenames = set(args.skip_files)

    if args.plantuml_only:
        return run_plantuml_only(
            [path.resolve() for path in args.paths],
            plantuml_jar,
            repo_root,
            verbose=args.verbose_plantuml,
        )

    if args.paths:
        files = sorted(path.resolve() for path in args.paths)
        missing = [path for path in files if not path.is_file()]
        if missing:
            for path in missing:
                print(f"File not found: {path}", file=sys.stderr)
            return 2
        outside_spec = [path for path in files if not is_relative_to(path, spec_root.resolve())]
        if outside_spec:
            for path in outside_spec:
                print(
                    f"{path}: not under {display_path(spec_root, repo_root)}/; "
                    "use --plantuml-only for standalone Markdown",
                    file=sys.stderr,
                )
            return 2
    else:
        files = discover_spec_markdown(spec_root, skip_filenames)
        if not files:
            print(f"No Markdown files found under {display_path(spec_root, repo_root)}/", file=sys.stderr)
            return 2

    spec_errors, stats = validate_spec_graph(files, repo_root, spec_root, entrypoint, required_paths)

    plantuml_ok = True
    diagram_total = 0
    files_with_puml = 0
    if not args.no_plantuml:
        puml_paths = files
        if not args.plantuml_all and not args.paths:
            changed = git_changed_markdown_under(repo_root, spec_root)
            if changed:
                puml_paths = [path for path in files if path.resolve() in changed]
                skipped = len(files) - len(puml_paths)
                if skipped > 0:
                    print(
                        "PlantUML: git-changed scope "
                        f"({len(puml_paths)} file(s), skipped {skipped} unchanged)",
                        file=sys.stderr,
                    )
            elif (repo_root / ".git").exists():
                print("PlantUML: no changed spec .md; skipping diagram checks.", file=sys.stderr)
                puml_paths = []

        plantuml_ok, diagram_total, files_with_puml = run_plantuml_checks(
            puml_paths,
            plantuml_jar,
            repo_root,
            verbose=args.verbose_plantuml,
        )
        if diagram_total > 0 and plantuml_ok:
            print(f"PlantUML: OK ({diagram_total} diagram(s) in {files_with_puml} file(s))", file=sys.stderr)

    if spec_errors:
        for msg in spec_errors:
            print(msg, file=sys.stderr)
        print(f"\n{len(spec_errors)} issue(s)", file=sys.stderr)
        return 1
    if not plantuml_ok:
        return 1

    print(
        "OK: "
        f"{stats.get('markdown_files', 0)} spec file(s), "
        f"{stats.get('markdown_links', 0)} markdown link(s), "
        f"{stats.get('reachable_from_entrypoint', 0)} reachable from entrypoint, "
        f"{stats.get('source_refs', 0)} source listing(s), "
        f"{stats.get('unique_source_paths', 0)} unique source path(s)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
