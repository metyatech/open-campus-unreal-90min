# open-campus-unreal-90min

Unreal Engine 5.x と Blueprint を使った、オープンキャンパス向け 90 分体験授業の standalone lesson package です。

この repository は docs site 依存なしで使えます。Markdown をそのまま配布・印刷・投影できます。

## Overview

- 対象: 主に高校既卒以上の初学者
- 授業時間: 90 分
- 形式: Unreal Engine 5.x / Third Person template / Blueprint
- 到達点: ミニゲームを 1 本完成させ、ゲームの基本構造を理解する

## Materials

- [lesson-overview.md](lesson-overview.md): 授業概要、到達目標、90 分タイムライン
- [student-guide.md](student-guide.md): 受講者が授業中にそのまま使う手順書
- [teacher-guide.md](teacher-guide.md): 進行台本、詰まり対応、進度差の扱い
- [setup-and-troubleshooting.md](setup-and-troubleshooting.md): 教室準備、当日スモークテスト、障害時フォールバック

## Usage

最短運用は次の順です。

1. 教員は [teacher-guide.md](teacher-guide.md) を読んで進行を決める
2. 受講者へ [student-guide.md](student-guide.md) を配布する
3. 教室準備と当日対応は [setup-and-troubleshooting.md](setup-and-troubleshooting.md) を参照する

## Setup

```sh
npm install
compose-agentsmd
git config core.hooksPath .githooks
```

## Verify

```sh
npm run verify
```

`compose-agentsmd` を実行して [AGENTS.md](AGENTS.md) を再生成したうえで commit してください。

## Environment

- Node.js 22 以上
- `compose-agentsmd` がグローバルにインストール済みであること
- Markdown を読める任意の環境で教材自体は利用可能

## Versioning

この repository は SemVer を使います。

- Patch: 誤字修正、文面改善、非破壊の運用メモ追加
- Minor: 既存運用を壊さない新教材や追加手順の追加
- Major: ファイル名変更、既存手順の削除、授業運用の前提変更

## Release

配布物は GitHub repository の履歴を正本とします。アプリ配備やサイト deploy はありません。

## Official References

- [Unreal Engine 5.6 インストール（公式）](https://dev.epicgames.com/documentation/ja-jp/unreal-engine/install-unreal-engine?application_version=5.6)
- [Unreal Engine 5.6 オフラインインストーラー（公式）](https://dev.epicgames.com/documentation/en-us/unreal-engine/offline-installer-of-unreal-engine?application_version=5.6)
- [Academic Installation（公式・UE4.27、学内展開の注意点参考）](https://dev.epicgames.com/documentation/en-us/unreal-engine/academic-installation?application_version=4.27)

## Repository Files

- `.github/workflows/`: CI, CodeQL, secret scanning
- `.githooks/`: local pre-commit hook
- `.tasks.jsonl`: committed task-tracker state
- `agent-ruleset.json`: rule composition source
- `AGENTS.md`: composed operational rules

## Compliance

- [AGENTS.md](AGENTS.md)
- [LICENSE](LICENSE)
- [SECURITY.md](SECURITY.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [CHANGELOG.md](CHANGELOG.md)
