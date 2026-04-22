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
3. Create `course-docs-site/.env.course.local` with `COURSE_CONTENT_SOURCE` set to this repository.
4. Start the dev server with `npm run dev`.

Use any local path that is valid from the `course-docs-site` checkout. If the two repositories are siblings, `../open-campus-unreal-90min` works.

## Verification

Run the full verification suite before each commit:

- `node scripts/verify.mjs`

If `course-docs-site` is not in the same workspace, set `COURSE_DOCS_SITE_DIR` to that checkout before running the verify script.
