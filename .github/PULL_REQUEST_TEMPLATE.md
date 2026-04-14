## Summary

<!-- 変更の概要と動機を 1〜3 行で -->

## Tutorial content changes

このリポジトリは `tutorial-authoring` スキルの原則に従って学習者向け手順を書いています。チュートリアル（`content/docs/**/*.mdx`）を変更した場合は下記を満たしてください。構造チェックは `remarkTutorialLint` が `npm run dev` / `npm run build` で自動検出します。判定が必要な項目は `REVIEW-CHECKLIST`（skill-tutorial-authoring リポジトリ）を参照。

### Automated (must pass in CI)

- [ ] `next build` が警告ゼロで通過する（tutorial-lint 含む）
- [ ] `TUTORIAL_LINT_STRICT=1` でもビルドが通る（ローカル任意、CI で検証される）

### Judgement (author self-review)

- [ ] Goal banner が未来宣言形（「〜します」「〜できるようになります」）
- [ ] 1 Action = 1 画像、画像が WHERE、テキストが WHAT
- [ ] 画像に映っているラベルをテキストで太字再掲していない（Redundancy）
- [ ] Concept は first-use の直前に配置、5 文以内（Pre-training）
- [ ] 二人称の直接話法（「〜しましょう」「確認してください」）、三人称描写を含まない（Personalization）
- [ ] Verify は観察可能な状態で記述、内部処理語（`実行されました` 等）を含まない（Generative activity）
- [ ] Signaling（太字・番号吹き出し）は学習目的に沿った要素にのみ使用
- [ ] 装飾絵文字・余談なし（Coherence）
- [ ] 画面遷移単位で Section を分割（Segmenting）

## Non-content changes

<!-- コードやインフラなど、content 以外の変更があれば記入 -->

## Notes for reviewer

<!-- レビュー時に特に見てほしい点 -->
