# Contributing

Thanks for your interest in contributing to `open-campus-unreal-90min`.

## Scope

This repository stores the course content consumed by
`metyatech/course-docs-site` for a 90-minute Unreal Engine open campus lesson.
Keep changes content-first and aligned with the shared site runtime.

## Setup

1. Install Node.js.
2. Run `git submodule update --init --recursive`.
3. Run `compose-agentsmd`.
4. Run `git config core.hooksPath .githooks`.

## Local Preview

Preview the site through `course-docs-site`:

1. Clone `metyatech/course-docs-site`.
2. Run `npm install` in that repo.
3. Start the dev server with
   `COURSE_CONTENT_SOURCE=../open-campus-unreal-90min npm run dev`.

## Verification

Run the full verification suite before each commit:

- `npx markdownlint-cli "**/*.md" --config .markdownlint.json --ignore AGENTS.md --ignore agent-rules-private/**`
- `compose-agentsmd`

If the change affects site rendering, also build through `course-docs-site` with
`COURSE_CONTENT_SOURCE` pointing to this repository before concluding.
