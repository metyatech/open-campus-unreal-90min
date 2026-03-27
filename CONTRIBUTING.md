# Contributing

Thanks for your interest in contributing to `open-campus-unreal-90min`.

## Scope

This repository stores the course content consumed by
`metyatech/course-docs-site` for a 90-minute Unreal Engine open campus lesson.
Keep changes content-first and aligned with the shared site runtime.

## Setup

1. Install Node.js 22 or later.
2. Run `npm install`.
3. Run `compose-agentsmd`.
4. Run `git config core.hooksPath .githooks`.

## Local Preview

Preview the site through `course-docs-site`:

1. Clone `metyatech/course-docs-site`.
2. Run `npm install` in that repo.
3. Start the dev server with
   `COURSE_CONTENT_SOURCE="github:metyatech/open-campus-unreal-90min#main" npm run dev`
   or point `COURSE_CONTENT_SOURCE` at a local clone of this repo.

## Verification

Run the full verification suite before each commit:

- `npm run verify`
- `compose-agentsmd`

If the change affects site rendering, also build through `course-docs-site` with
`COURSE_CONTENT_SOURCE` pointing to this repository before concluding.
