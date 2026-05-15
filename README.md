# open-campus-unreal-90min

Unreal Engine 5.x と Blueprint を使った、オープンキャンパス向け 90 分体験授業の
course content repository です。

この repo は **content-only** です。共有サイト runtime は
`metyatech/course-docs-site` を使い、この repo の `content/` と `site.config.ts`
を読み込んで Vercel へ deploy します。

## Overview

- 対象: 主に高校既卒以上の初学者
- 授業時間: 90 分
- 形式: Unreal Engine 5.x / Third Person template / Blueprint
- 到達点: ミニゲームを 1 本完成させ、ゲームの基本構造を理解する

## Site Preview

`course-docs-site` を clone して、この repo を content source として指定します。

```sh
git clone https://github.com/metyatech/course-docs-site.git
cd course-docs-site
npm install
```

`course-docs-site/.env.course.local` に `COURSE_CONTENT_SOURCE` を設定してから `npm run dev` を実行してください。

```sh
# In course-docs-site/.env.course.local
COURSE_CONTENT_SOURCE=../path-to-open-campus-unreal-90min
```

course-docs 系 content repo は public / private を問わず、この local path source 方式で統一しています。
Use any local path that is valid from the `course-docs-site` checkout. If the two repositories are siblings, that can be `../open-campus-unreal-90min`.

この教材の `教員ガイド` と `セットアップ・トラブル対応` をローカルで確認する場合は、
`course-docs-site/.env.local` に `ADMIN_MODE_TOKEN` も設定してから `npm run dev` を起動してください。

## Repository Setup

この repo 自体の hook 用セットアップです。

```sh
git submodule update --init --recursive
compose-agentsmd
git config core.hooksPath .githooks
```

## Verification

この repo から canonical verify entrypoint を実行します。

```sh
node scripts/verify.mjs
```

What it does:

- checks that every `<Exercise>` is titled by the immediately preceding Markdown heading and has no `title` prop
- runs `markdownlint` for this repository
- locates a local `course-docs-site` checkout automatically when the repos live in the same workspace
- runs `course-docs-site` lint and `build:verified` with `COURSE_CONTENT_SOURCE` set to this repository

If `course-docs-site` is not in the same workspace, set `COURSE_DOCS_SITE_DIR` in your shell or terminal session to that checkout before running `node scripts/verify.mjs`.

Automatic discovery looks for a local checkout named `course-docs-site` while walking up parent directories from this repository.

`compose-agentsmd` を実行して [AGENTS.md](./AGENTS.md) を再生成したうえで commit
してください。

## Deploy (Vercel)

deploy は GitHub Actions から Vercel CLI を使って行います。Vercel の GitHub 連携は使いません。
設定は [`.github/workflows/deploy-vercel.yml`](./.github/workflows/deploy-vercel.yml) にあります。

必要な GitHub Actions secrets:

- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

## Project Files

- `content/`: サイト表示用の教材ページ（MDX）
- `scripts/verify.mjs`: canonical verification entrypoint for local delivery checks
- `public/`: 画像や favicon などの静的ファイル
- `site.config.ts`: `course-docs-site` に読み込ませる講義別設定
- `.github/workflows/`: CI / deploy workflows
- `.githooks/`: local pre-commit hook
- `.tasks.jsonl`: committed task-tracker state
- `agent-ruleset.json`: rule composition source
- `agent-rules-private/`: shared private authoring rules submodule

## Versioning

この repository は SemVer を使います。

- Patch: 誤字修正、文面改善、非破壊の運用メモ追加
- Minor: 既存運用を壊さない新教材や追加手順の追加
- Major: 情報構造変更、既存 URL の削除、授業運用の前提変更

## Official References

- [Unreal Engine 5.6 インストール（公式）](https://dev.epicgames.com/documentation/ja-jp/unreal-engine/install-unreal-engine?application_version=5.6)
- [Unreal Engine 5.6 オフラインインストーラー（公式）](https://dev.epicgames.com/documentation/en-us/unreal-engine/offline-installer-of-unreal-engine?application_version=5.6)
- [Academic Installation（公式・UE4.27、学内展開の注意点参考）](https://dev.epicgames.com/documentation/en-us/unreal-engine/academic-installation?application_version=4.27)

## Compliance

- [AGENTS.md](./AGENTS.md)
- [LICENSE](./LICENSE)
- [SECURITY.md](./SECURITY.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- [CHANGELOG.md](./CHANGELOG.md)
