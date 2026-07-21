from pathlib import Path
import subprocess


def from_main(path: str) -> str:
    return subprocess.check_output(
        ['git', 'show', f'origin/main:{path}'],
        text=True,
        encoding='utf-8',
    )


student_path = Path('content/docs/student-guide/index.mdx')
base = from_main(str(student_path))

for old, new in {
    'Step 1：テストプレイする（15〜25分）': 'Step 1：テストプレイする（10〜15分）',
    'Step 2：BP_Coin を 10 枚以上置く（25〜40分）': 'Step 2：BP_Coin を 10 枚以上置く（15〜30分）',
    'Step 3：BP_Coin を拾ったときに枚数を更新する（40〜55分）': 'Step 3：BP_Coin を拾ったときに枚数を更新する（30〜45分）',
    'Step 4：BP_Portal のクリア条件を直す（55〜70分）': 'Step 4：BP_Portal のクリア条件を直す（45〜60分）',
    'Step 5：クリアに必要なコイン数を調整する（70〜80分）': 'Step 5：クリアに必要なコイン数を調整する（60〜70分）',
}.items():
    if base.count(old) != 1:
        raise SystemExit(f'expected one timing marker: {old}')
    base = base.replace(old, new)

optional_marker = '<Section title="任意：時間が余った場合（80〜90分）"'
if base.count(optional_marker) != 1:
    raise SystemExit('original optional section marker was not found exactly once')
core, original_optional = base.split(optional_marker, 1)
original_optional = optional_marker + original_optional
original_optional = original_optional.replace(
    '<Section title="任意：時間が余った場合（80〜90分）" goal="さらにゲームの完成度を高めます">',
    '<Section title="任意：時間が余った場合（85〜90分）" goal="ジャンプ台やコインを調整し、ゲームをさらに改造します">',
    1,
)
original_optional = original_optional.replace(
    'ここからは時間が余ったときだけ進めます。ゲーム自体は Step 5 までで完成しているので、無理に進める必要はありません。余裕があれば、以下の内容でさらにゲームの完成度を高めてみましょう。',
    'ここからは時間が余ったときだけ進めます。ジャンプ台が動けば、この授業の必須部分は完了です。',
    1,
)
original_optional = original_optional.replace(
    '### 演習-発展1：コインを回転させる',
    '### 演習-発展3：コインを回転させる',
    1,
)

extensions = '''### 演習-発展1：ジャンプの強さを変える

<Exercise>

`Make Vector` の Z を変更し、ジャンプの高さを変えてください。

- `700`：低いジャンプ
- `1200`：標準のジャンプ
- `1800`：高いジャンプ

<Verify>数値を変えてコンパイルすると、ジャンプの高さが変われば成功です。</Verify>

<Hint>
Z の数値が大きいほど、上方向へ強く飛びます。
</Hint>

<Answer>
`Make Vector` の Z を変更し、コンパイルしてからプレイします。選んだ数値に応じてジャンプの高さが変われば完了です。
</Answer>

</Exercise>

### 演習-発展2：空中のコインを取れるコースを作る

<Exercise>

通常のジャンプでは届かない位置へ `BP_Coin` を1枚以上置き、ジャンプ台を使えば取れるように配置を調整してください。

<Verify>ジャンプ台から飛び、空中に置いたコインを取れれば成功です。</Verify>

<Hint>
先にジャンプ台の高さを確認し、その軌道の近くへコインを置くと調整しやすくなります。
</Hint>

<Answer>
ジャンプ台で飛んだときに通る位置へコインを移動し、プレイして実際に取れることを確認します。
</Answer>

</Exercise>

'''
original_optional = original_optional.replace(
    '### 演習-発展3：コインを回転させる',
    extensions + '### 演習-発展3：コインを回転させる',
    1,
)

jump_pad = '''<Section title="追加ミッション：ジャンプ台を作ろう（70〜85分）" goal="Blueprint に処理を追加し、プレイヤーを上へ飛ばすジャンプ台を完成させます">

ここまでで、最初にプレイした基本ゲームは完成です。ここからは、完成見本にはなかった新しい機能を追加します。

`BP_JumpPad` をステージに置き、Blueprint に処理を追加して、プレイヤーが乗ると上へ飛ぶようにしましょう。

<Section title="1. BP_JumpPad を置く" goal="ジャンプ台をステージに配置し、まだ動かないことを確認します">

<Action>
  Content Drawer で `OpenCampus` フォルダを開き、`BP_JumpPad` をビューポートへドラッグ＆ドロップします。
</Action>

<Action>
  移動ギズモを使って、キャラクターが上に乗れる場所へ移動します。
</Action>

<Action>
  プレイして、`BP_JumpPad` の上に乗ります。
</Action>

<Verify>ジャンプ台の上に乗っても、まだ通常どおり歩けるだけで上へ飛ばなければ確認完了です。</Verify>

</Section>

<Section title="2. BP_JumpPad を開く" goal="ジャンプ台の Blueprint と処理を追加する場所を確認します">

<Action>
  Content Drawer で `OpenCampus` フォルダを開き、`BP_JumpPad` をダブルクリックします。
</Action>

<Action>
  イベントグラフで、`On Component Begin Overlap` と、黄色いコメントエリア「**プレイヤーを上へ飛ばす**」を見つけます。
</Action>

<Verify>`On Component Begin Overlap` と黄色いコメントエリアを確認できれば準備完了です。</Verify>

</Section>

<Section title="3. 触れた相手が Character か確認する" goal="ジャンプ台に触れた相手を Character として扱える場合だけ処理を進めます">

<Concept title="Other Actor">
`On Component Begin Overlap` の `Other Actor` には、ジャンプ台に触れた相手が入ります。プレイヤーが触れた場合は、プレイヤーキャラクターが入ります。
</Concept>

<Concept title="Cast To Character">
`Cast To Character` は、触れた相手を Character として扱えるか確認するノードです。成功したときだけ Character 用の処理へ進めます。
</Concept>

<Action>
  `Other Actor` のピンからドラッグし、検索欄に `Cast To Character` と入力して、`Cast To Character` を追加します。
</Action>

<Action>
  `On Component Begin Overlap` の白い実行ピンを、`Cast To Character` の白い実行ピンへつなぎます。
</Action>

<Verify>`Other Actor` が `Object` につながり、白い実行線も `Cast To Character` へつながっていれば完了です。</Verify>

</Section>

<Section title="4. Launch Character を追加する" goal="Character に上方向の速度を与える処理を追加します">

<Concept title="Launch Character">
`Launch Character` は、Character に速度を与えて飛ばすノードです。今回は上方向の速度を与えて、ジャンプ台として使います。
</Concept>

<Action>
  `Cast To Character` の成功時の白い実行ピンからドラッグし、`Launch Character` を検索して追加します。
</Action>

<Action>
  `As Character` の青いピンを、`Launch Character` の `Target` へつなぎます。
</Action>

<Verify>Cast が成功したあとに `Launch Character` が実行され、`As Character` が `Target` につながっていれば完了です。</Verify>

</Section>

<Section title="5. 上方向の速度を設定する" goal="プレイヤーが上へ飛ぶための速度を作ります">

<Concept title="Vector">
Vector は、X・Y・Z の3方向をまとめた値です。Unreal Engine では、Z が上下方向です。
</Concept>

<Action>
  `Launch Character` の `Launch Velocity` ピンからドラッグし、`Make Vector` を追加します。
</Action>

<Action>
  `Make Vector` の `X` と `Y` は `0` のままにし、`Z` に `1200` を入力します。
</Action>

<Action>
  `Launch Character` の `Z Override` をオンにします。`XY Override` はオフのままにします。
</Action>

<Verify>`Make Vector` の Z が `1200` で、`Launch Velocity` につながっていれば完了です。</Verify>

</Section>

<Section title="6. コンパイルして試す" goal="ジャンプ台に乗るとプレイヤーが上へ飛ぶことを確認します">

<Action>
  `BP_JumpPad` をコンパイルして保存し、メインエディターへ戻ります。
</Action>

<Action>
  プレイして、自分で置いたジャンプ台の上へ乗ります。
</Action>

<Recovery title="ジャンプ台に乗っても飛ばないとき">
次を順番に確認してください。

- `BP_JumpPad` のコンパイルが成功している
- `Other Actor` が `Cast To Character` の `Object` につながっている
- `As Character` が `Launch Character` の `Target` につながっている
- `Make Vector` の Z が `1200` になっている
- 白い実行線が途中で切れていない
</Recovery>

<Verify>ジャンプ台に乗ったとき、プレイヤーが上へ飛べば追加ミッション成功です。</Verify>

</Section>

<Checkpoint>
- `BP_JumpPad` を自分でステージに置いている
- ジャンプ台に触れた相手を `Cast To Character` で確認している
- `Launch Character` が Character を飛ばしている
- `Make Vector` の Z で上方向の強さを設定している
- プレイするとジャンプ台から上へ飛べる
</Checkpoint>

</Section>

'''

student_path.write_text(core + jump_pad + original_optional, encoding='utf-8')

intro_path = Path('content/docs/intro/index.mdx')
intro_path.write_text(from_main(str(intro_path)), encoding='utf-8')

readme_path = Path('README.md')
readme = readme_path.read_text(encoding='utf-8').replace(
    '- 到達点: ミニゲームを完成させ、Blueprint でジャンプ台を追加してゲームの基本構造を理解する',
    '- 到達点: ミニゲームを 1 本完成させ、ゲームの基本構造を理解する',
)
readme_path.write_text(readme, encoding='utf-8')

text = student_path.read_text(encoding='utf-8')
for forbidden in [
    '基本のゲームが完成したあとは、Blueprint を使って',
    '基本のゲームが完成したら、見本にはなかった新しい機能として',
    '`Update Coins` の左右の白い実行ピンをつなぎます。',
    '自分が最後のクリア条件にしたい数値',
    '`>=` の数字を変えると、ポータルが光るために必要なコイン数も変われば',
]:
    if forbidden in text:
        raise SystemExit(f'forbidden text remains: {forbidden}')
for required in [
    '`Update Coins` の左右の白い実行ピンを、それぞれ繋ぎます。',
    '文書を「保存」するのに近い操作ですが',
    '<Section title="5-1. 3 枚でクリアできるようにする"',
    '<Section title="5-2. 自分でルールを決める"',
    '<Section title="1. BP_JumpPad を置く"',
    '自分で置いたジャンプ台の上へ乗ります。',
]:
    if required not in text:
        raise SystemExit(f'required text is missing: {required}')
