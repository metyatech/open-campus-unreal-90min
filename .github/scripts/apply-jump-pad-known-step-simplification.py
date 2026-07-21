import re
from pathlib import Path

path = Path('content/docs/student-guide/index.mdx')
text = path.read_text(encoding='utf-8')

section1_pattern = re.compile(
    r'(<Section title="1\. BP_JumpPad を置く"[^>]*>\n\n)'
    r'.*?'
    r'(\n\n<Verify>ジャンプ台の上に乗っても、まだ上へ飛ばなければ確認完了です。</Verify>)',
    re.S,
)
section1_body = '''<Action img="./img/bp-jump-pad-drag-from-content-browser.webp" alt="Content Drawer から BP_JumpPad をビューポートへドラッグ＆ドロップして配置するスクリーンショット">
  Content Drawer の `OpenCampus` フォルダにある `BP_JumpPad` を、ビューポートへドラッグ＆ドロップします。
</Action>

<Action>
  移動ギズモを使って、キャラクターが上に乗れる場所へ移動します。
</Action>

<Action>
  プレイ中にキャラクターを操作して、`BP_JumpPad` の上へ移動します。
</Action>'''
text, count = section1_pattern.subn(r'\1' + section1_body + r'\2', text, count=1)
if count != 1:
    raise SystemExit(f'expected one section 1 match, found {count}')

open_pattern = re.compile(
    r'<Action img="\./img/open-bp-jump-pad-from-content-browser\.webp"[^>]*>\n'
    r'  `BP_JumpPad` をダブルクリックします。\n'
    r'</Action>'
)
open_replacement = '''<Action>
  Content Drawer の `OpenCampus` フォルダにある `BP_JumpPad` をダブルクリックします。
</Action>'''
text, count = open_pattern.subn(open_replacement, text, count=1)
if count != 1:
    raise SystemExit(f'expected one BP_JumpPad open action match, found {count}')

section7_pattern = re.compile(
    r'(<Section title="7\. コンパイルして試す"[^>]*>\n\n)'
    r'.*?'
    r'(\n\n<Recovery title="ジャンプ台に乗っても飛ばないとき">)',
    re.S,
)
section7_body = '''コンパイルして保存し、メインエディターでプレイを開始します。

<Action>
  キャラクターを操作して、自分で置いたジャンプ台の上へ移動します。
</Action>'''
text, count = section7_pattern.subn(r'\1' + section7_body + r'\2', text, count=1)
if count != 1:
    raise SystemExit(f'expected one section 7 match, found {count}')

for value in [
    './img/bp-jump-pad-move-with-gizmo.webp',
    './img/open-bp-jump-pad-from-content-browser.webp',
    './img/bp-jump-pad-click-compile.png',
]:
    if value in text:
        raise SystemExit(f'obsolete image reference remains: {value}')

for value in [
    './img/bp-jump-pad-open-viewport-tab.webp',
    './img/bp-jump-pad-collision-in-viewport.webp',
    './img/bp-jump-pad-add-overlap-event.webp',
    './img/bp-jump-pad-add-cast-to-character.webp',
    './img/bp-jump-pad-add-launch-character.webp',
    './img/bp-jump-pad-set-launch-velocity-z.webp',
    './img/bp-jump-pad-enable-z-override.webp',
]:
    if value not in text:
        raise SystemExit(f'required new-operation image missing: {value}')

path.write_text(text, encoding='utf-8', newline='\n')
