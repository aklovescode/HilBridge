# Fix Plan: Commit Options Fail When GitHub API Is Rate-Limited

## 1. Bug Summary

The commit filter dropdown can fail to show recent commit options when GitHub returns `403 rate limit exceeded`. The UI surfaces the backend warning as `Could not load GitHub commits: 403 rate limit exceeded`, and the user is left with only `Staged Local Changes` when staged files exist.

Impact: users cannot select recent committed changes for diff visualization even though the local checkout already has the commit history needed by `git diff-tree`.

## 2. Relevant Specs

- `spec/capabilities/Commit_Diff_Visualization.md`: guarantees users can choose recent GitHub commits by message and timestamp and inspect staged changes.
- `spec/flows/Visualize_Commit_Changes.md`: defines `POST /api/commit-options` as the dropdown-loading path before `POST /api/graph`.
- `spec/contracts/Commit_Filter_Options.md`: defines staged and commit option shapes, states commit options come from GitHub, and notes `GITHUB_TOKEN` may be used for private repos or higher rate limits.
- `spec/modules/Git_Adapter.md`: assigns git/GitHub metadata loading responsibilities to the backend adapter.
- `spec/modules/Backend_Graph_API.md`: requires `/api/commit-options` to return options, GitHub metadata, and bounded warnings.

## 3. Intended Behavior

The commit filter should remain usable for local repositories. Users should be able to choose recent commit options by message and timestamp whenever the local checkout contains those commits, because the actual graph diff path uses local `git diff-tree` and filters options to commits that exist locally.

GitHub metadata is useful for remote URLs and private/remote-aware context, but a GitHub API rate-limit response should not prevent local commit history from populating the dropdown.

## 4. Root Cause Analysis

Observed path:

1. The frontend calls `POST /api/commit-options` from `frontend/src/App.tsx`.
2. `backend/src/server.ts` builds options by adding staged entries from local `git diff --cached --name-status -M`.
3. It then calls `fetchGitHubCommitOptions`.
4. `fetchGitHubCommitOptions` requests `https://api.github.com/repos/<owner>/<repo>/commits`.
5. When GitHub returns non-OK, including `403 rate limit exceeded`, the backend pushes a warning and returns no commit options.
6. The frontend shows the warning under the dropdown and has no committed options to offer.

The invariant breaks in `backend/src/server.ts`: committed options are coupled to the GitHub REST API even though local git has the required sha, message, and commit timestamp. Runtime evidence from this checkout showed `GITHUB_TOKEN` is unset, while `git log -5 --pretty=format:'%H%x09%cI%x09%s'` successfully returns recent local commits.

## 5. Proposed Fix

Implement a backend fallback that sources commit options from local git when GitHub commit loading fails or is unavailable.

File-centric steps:

- `backend/src/server.ts`
  - Add a helper such as `readLocalCommitOptions(repoPath, limit, github, warnings)` that runs `git log -n <limit> --pretty=format:%H%x00%cI%x00%s`.
  - Convert each local commit to `{ kind: "commit", sha, message, committedAt, url? }`.
  - Build `url` locally with `githubCommitUrl(github, sha)` when a GitHub web URL is known.
  - In `buildCommitOptions`, keep staged-option behavior unchanged, then use GitHub options when available; if GitHub returns none because of API failure/rate limit, fall back to local git options.
  - Preserve bounded warnings so the UI can still report that GitHub API metadata could not be loaded.
  - Avoid duplicate commit options if both GitHub and local sources are combined.

- `spec/contracts/Commit_Filter_Options.md`
  - Update behavior to say committed options may be loaded from local git when GitHub metadata is unavailable or rate-limited.
  - Clarify that `GITHUB_TOKEN` improves GitHub API metadata/limits but is not required for local commit options.

- `spec/flows/Visualize_Commit_Changes.md`
  - Update the commit-options flow to show local git commit-log fallback.

- `spec/modules/Git_Adapter.md`
  - Add responsibility for reading recent local commits with `git log`.

No frontend state change is required for the minimal fix, because the existing `CommitFilterOption` shape already supports locally-derived options and the existing warning display can continue to show GitHub API degradation.

## 6. Risk Assessment

If parsing `git log` output is wrong, the dropdown could show malformed commit labels or hashes that fail later in `git diff-tree`.

If fallback ordering is wrong, local commits could replace richer GitHub API options even when the API succeeds, or duplicate entries could appear.

If URL construction is wrong, changed nodes may open an invalid GitHub commit page, though graph diffing would still work locally.

## 7. Validation / Handoff

Implementation should validate:

- `npm run typecheck`
- `npm run build`
- With `GITHUB_TOKEN` unset, force or simulate a GitHub API failure/rate-limit path and confirm `POST /api/commit-options` still returns recent commit options from local `git log`.
- Confirm the current staged behavior remains unchanged: `Staged Local Changes` appears only when `git diff --cached --name-status -M` returns entries.
- Confirm selecting a locally-derived commit still calls `POST /api/graph` with `diffTarget: "commit"` and the selected sha, and changed nodes are marked.
- Confirm warnings remain bounded and the UI can show GitHub API degradation without losing local commit options.

No dedicated docs validation command exists in this repo; run the build/typecheck commands above after the spec updates.

**Ready for approval**
