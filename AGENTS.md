# AGENTS.md

This guide applies to the whole repository. Treat it as the project-specific
handoff for the `.agents/skills/` workflows.

## Project Summary

HilBridge is a local-first TypeScript app for inspecting spec-driven
repositories as an interactive knowledge graph. It reads markdown notes from a
selected repository's `spec/` directory, derives note-to-note and note-to-code
edges, and renders the result in layered 2D, horizontal-plane, vertical-slice,
and 3D pyramid views.

The app is intended for trusted local development use. The backend reads local
files and runs local git commands against the repository path supplied by the
user.

## Stack

- TypeScript everywhere, with strict compiler settings.
- React 19 and Vite for the frontend.
- Express 5 and CORS for the local backend API.
- `gray-matter` for markdown frontmatter parsing.
- `react-force-graph-3d`, Three.js, and `three-spritetext` for the 3D view.
- Inline SVG is used for the 2D graph views.
- Node `fs/promises`, `path`, `child_process`, and `fetch` are used by the
  backend for local repository and GitHub metadata work.

## Repository Map

- `backend/src/server.ts`: Express server, graph API, markdown parsing, graph
  building, GitHub URL resolution, commit/staged diff analysis, and local git
  adapters. Most backend behavior currently lives in this file.
- `frontend/src/App.tsx`: React app shell, repository input, commit filter UI,
  graph visibility state, layered map, horizontal plane, vertical slice, and 3D
  pyramid rendering. Most frontend behavior currently lives in this file.
- `frontend/src/styles.css`: Application styling.
- `frontend/src/main.tsx`: React entrypoint.
- `shared/src/graph.ts`: Shared graph, API, GitHub, and commit-filter types.
  Update this first when backend/frontend contracts change.
- `spec/`: Durable product and implementation knowledge graph.
- `current_task/`: Task-local planning and review artifacts. Do not treat these
  files as product specs.
- `dist/`, `node_modules/`, `.code-review-graph/`: Generated or tool-managed
  output. Do not hand edit.

## Commands

- Install dependencies: `npm install`
- Run both servers: `npm run dev`
- Run backend only: `npm run dev:backend`
- Run frontend only: `npm run dev:frontend`
- Typecheck: `npm run typecheck`
- Production build: `npm run build`
- Set up project-local tooling: `npm run setup:tools`
- Validate specs/docs: `npm run validate:docs`
- Whitespace/conflict check: `git diff --check`

The frontend normally serves at `http://127.0.0.1:5173`. The backend normally
serves at `http://127.0.0.1:4317`; set `PORT` to change the backend port. Vite
proxies `/api` to the backend.

Set `GITHUB_TOKEN` before starting the backend when private repositories or
higher GitHub API rate limits are needed. Local graph extraction and local git
fallbacks should still work without a token when the selected checkout has the
needed history.

## Validation Expectations

Always run `npm run typecheck` after source changes. Run `npm run build` before
handoff for user-facing frontend changes, backend API changes, shared contract
changes, or broad refactors.

There is no dedicated test runner checked in yet. Do not add a test framework
unless the approved plan calls for it. Until tests exist, use targeted runtime
checks for risky changes:

- Backend health: `curl -s http://127.0.0.1:4317/api/health`
- Graph API: start the backend, then post to `/api/graph` with a local
  `repoPath`.
- Commit options: start the backend, then post to `/api/commit-options` with a
  local `repoPath`; verify staged changes and recent commits behave as intended.
- Frontend: start `npm run dev`, open `http://127.0.0.1:5173`, load this repo,
  and verify the affected view or control.

When `spec/` changes, run `npm run validate:docs`. The validator checks
markdown links, reachability from `spec/Vision.md`, conventional
capability/flow/module/code traceability, `## Code` source references, and
PlantUML fenced blocks when the PlantUML jar is available. Run
`npm run setup:tools` once to download `tools/plantuml.jar`; use
`python3 scripts/validate_docs.py --no-plantuml` only when Java or PlantUML is
unavailable.

## Runtime And API Notes

- `GET /api/health` returns backend health.
- `POST /api/graph` accepts `GraphRequest` and returns `GraphResponse`.
- `POST /api/commit-options` accepts `CommitOptionsRequest` and returns
  `CommitOptionsResponse`.
- `GraphRequest.diffTarget` may be `"commit"` or `"staged"`. Commit requests
  require `commitHash`.
- GitHub blob and commit URLs are derived from the selected repo's local git
  remote and branch.
- The backend uses local git commands such as `git remote get-url origin`,
  `git rev-parse --abbrev-ref HEAD`, `git diff-tree --name-status -r -M`,
  `git diff --cached --name-status -M`, and `git log`.
- Keep warnings bounded and user-readable. API failures should return useful
  messages rather than raw stack traces.

## Domain Model

The durable graph layers are:

1. Vision
2. Capability
3. Flow
4. Module
5. Contract
6. Code

Contracts are optional boundary nodes. Use them when they capture meaningful
API, data, state, integration, or compatibility traceability. A module may link
directly to code when no separate contract boundary is useful.

Cross-cutting notes live under `spec/architecture_notes/`,
`spec/domain_notes/`, and `spec/technology_notes/`. These can connect to any
layer but should not overwhelm the main hierarchy.

The parser recognizes standard markdown links, wikilinks, repo-relative source
paths in markdown text, and PlantUML markers. PlantUML is metadata only right
now; diagrams are not rendered by the app.

## Spec Conventions

- Keep `spec/Vision.md` connected to user-facing capabilities.
- Capabilities describe user-facing value and guarantees, not implementation
  details.
- Flows describe user or system journeys.
- Modules describe implementation responsibility boundaries and should include
  relevant `## Code` entries.
- Contracts describe stable data, API, state, integration, or compatibility
  boundaries when those boundaries are worth tracing independently.
- Architecture, domain, and technology notes hold cross-cutting rationale.
- Use relative markdown links for spec-to-spec relationships.
- Use repo-relative paths for source references, for example
  `frontend/src/App.tsx`.
- Keep `spec/doc_issues.md` updated for ambiguity, drift, missing traceability,
  validation gaps, and known limitations.
- When source behavior changes, update the nearest affected capability, flow,
  module, contract, or cross-cutting note in the same task unless the approved
  plan explicitly excludes docs.
- When specs change source references, verify module/contract `## Code` lists
  still match the implementation.

## Source Conventions

- Prefer existing patterns in `backend/src/server.ts`, `frontend/src/App.tsx`,
  and `shared/src/graph.ts` before introducing new abstractions.
- Keep backend/frontend API shapes synchronized through `shared/src/graph.ts`.
- Backend TypeScript uses `moduleResolution: "NodeNext"`; relative imports that
  run in Node should use `.js` extensions in source when importing TS modules.
- Frontend TypeScript uses Vite bundler resolution and React JSX.
- Preserve strict TypeScript. Avoid `any` unless wrapping a library boundary
  that has no useful type available.
- Add dependencies only when the approved plan justifies them.
- Keep local-file and git behavior explicit. Do not introduce cloud services or
  remote persistence without a plan and spec update.
- Do not commit secrets. `.env` and `.env.*` are ignored.

## Skill Workflow Guidance

- `fullstack-dev-doc` and `fullstack-dev-ideate`: update `spec/` only, then run
  `npm run validate:docs`. Stage only the docs that belong to the task.
- `fullstack-dev-plan` and `fullstack-dev-investigate`: use this file, `spec/`,
  source, and `current_task/` context to produce a concrete plan. Do not edit
  source or specs while planning.
- `fullstack-dev-implement` and `fullstack-dev-iterate`: implement the approved
  plan, update affected specs, run the required validations, and stage only
  files in scope.
- `fullstack-dev-review`: review staged changes against the approved plan,
  specs, contracts, and validations. Write `current_task/changes_summary.md`
  and do not fix code in the review step.
- `fullstack-test-plan`: write `current_task/plan.md` with exact test cases,
  framework choices, fixtures, and validation commands.
- `fullstack-test-implement`: implement only the approved test plan. Reuse
  existing project commands unless the plan adds test infrastructure.
- `fullstack-test-run`: run the requested commands, compare failures against
  specs, and write `current_task/bugs.md` without fixing code.

## Git Hygiene

The worktree may already contain user or staged changes. Inspect status before
editing, do not revert unrelated changes, and do not stage unrelated files.
When a skill requires staging at the end, stage only the files touched for that
approved task.
