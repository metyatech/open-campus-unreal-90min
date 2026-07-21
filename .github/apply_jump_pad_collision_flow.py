from pathlib import Path

path = Path('content/docs/student-guide/index.mdx')
text = path.read_text(encoding='utf-8')

start_marker = '<Section title="追加ミッション：ジャンプ台を作ろう（70〜85分）"'
end_marker = '<Section title="任意：時間が余った場合（85〜90分）"'

start = text.index(start_marker)
end = text.index(end_marker)

section = '''<Section title="追加ミッション：ジャンプ台を作ろう（70〜85分）" goal="Collision にイベントを追加し、プレイヤーを上へ飛ばすジャンプ台を完成させます">

ここまでで、最初にプレイした基本ゲームは完成です。ここからは、完成見本にはなかった新しい機能を追加します。

`BP_JumpPad` をステージに置き、Collision に触れたときの処理を追加して、プレイヤーが乗ると上へ飛ぶようにしましょう。

<Section title="1. BP_JumpPad を置く" goal="ジャンプ台をステージに配置し、まだ動かないことを確認します">

<Action img="./img/bp-jump-pad-drag-from-content-browser.png" alt="Content Drawer から BP_JumpPad をビューポートへドラッグ＆ドロップして配置するスクリーンショット">
  Content Drawer で `OpenCampus` フォルダを開き、`BP_JumpPad` をビューポートへドラッグ＆ドロップします。
</Action>

<Action>
  移動ギズモを使って、キャラクターが上に乗れる場所へ移動します。
</Action>

<Action>
  プレイして、`BP_JumpPad` の上に乗ります。
</Action>

<Verify>ジャンプ台の上に乗っても、まだ上へ飛ばなければ確認完了です。</Verify>

</Section>

<Section title="2. Collision の範囲を確認する" goal="ジャンプ台が接触を検出する範囲を確認します">

<Action>
  Content Drawer で `OpenCampus` フォルダを開き、`BP_JumpPad` をダブルクリックします。
</Action>

<Concept title="Collision とは">
`Collision` は、プレイヤーやほかの物体が触れたり、範囲内へ入ったりしたことを検出するための、見えない判定範囲です。
</Concept>

<Action img="./img/bp-jump-pad-collision-in-viewport.png" alt="BP_JumpPad の Viewport で Collision を選択し、ジャンプ台の判定範囲を確認するスクリーンショット">
  `Viewport` タブへ切り替え、Components で `Collision` をクリックします。Viewport に表示される Collision の範囲を確認します。
</Action>

<Verify>`Collision` を選択し、ジャンプ台の上部に判定範囲が設定されていることを確認できれば完了です。</Verify>

</Section>

<Section title="3. Collision に入ったときのイベントを追加する" goal="Collision に触れた瞬間から始まるイベントを追加します">

<Action img="./img/bp-jump-pad-add-overlap-event.png" alt="BP_JumpPad の Components で Collision を右クリックし、Add Event から Add OnComponentBeginOverlap を選ぶスクリーンショット">
  Components の `Collision` を右クリックし、`Add Event`、`Add OnComponentBeginOverlap` の順にクリックします。
</Action>

<Action img="./img/bp-jump-pad-begin-overlap-added.png" alt="BP_JumpPad の Event Graph に On Component Begin Overlap (Collision) が追加されたスクリーンショット">
  `On Component Begin Overlap (Collision)` が自動で追加され、Event Graph へ移動します。
</Action>

<Concept title="On Component Begin Overlap">
`On Component Begin Overlap` は、ほかの物体が Collision の範囲内へ入った瞬間に始まるイベントです。

ノード名の末尾の `(Collision)` というのは、先ほど確認した `Collision` に対するイベントだということを表しています。
</Concept>

<Verify>Event Graph に `On Component Begin Overlap (Collision)` が追加されていれば完了です。</Verify>

</Section>

<Section title="4. 触れた相手が Character か確認する" goal="ジャンプ台に触れた相手を Character として扱える場合だけ処理を進めます">

<Concept title="Other Actor">
`On Component Begin Overlap (Collision)` の `Other Actor` には、Collision に触れた相手が入ります。プレイヤーが触れた場合は、プレイヤーキャラクターが入ります。
</Concept>

<Concept title="Cast To Character">
`Cast To Character` は、触れた相手を Character として扱えるか確認するノードです。成功したときだけ Character 用の処理へ進めます。
</Concept>

<Action img="./img/bp-jump-pad-cast-character-connected.png" alt="BP_JumpPad の Event Graph で Other Actor から Cast To Character を追加し、Object と白い実行ピンが自動接続されたスクリーンショット">
  `Other Actor` のピンからドラッグし、検索欄に `Cast To Character` と入力して、`Cast To Character` を追加します。`Object` と白い実行ピンは自動でつながります。
</Action>

<Verify>`Other Actor` が `Object` につながり、白い実行線も `Cast To Character` へつながっていれば完了です。</Verify>

</Section>

<Section title="5. Launch Character を追加する" goal="Character に上方向の速度を与える処理を追加します">

<Concept title="Launch Character">
`Launch Character` は、Character に速度を与えて飛ばすノードです。今回は上方向の速度を与えて、ジャンプ台として使います。
</Concept>

<Action>
  `As Character` の青いピンからドラッグし、`Launch Character` を検索して追加します。`Target` と白い実行ピンは自動でつながります。
</Action>

<Verify>Cast が成功したあとに `Launch Character` が実行され、`As Character` が `Target` につながっていれば完了です。</Verify>

</Section>

<Section title="6. 上方向の速度を設定する" goal="プレイヤーが上へ飛ぶ強さを設定します">

<Concept title="Launch Velocity">
`Launch Velocity` は、Character をどの方向へ、どのくらいの強さで飛ばすかを表します。X と Y は水平方向、Z は上下方向です。
</Concept>

<Action>
  `Launch Character` の `Launch Velocity` で、X と Y は `0` のままにし、Z に `1200` を入力します。
</Action>

<Action>
  `Launch Character` の `Z Override` をオンにします。`XY Override` はオフのままにします。
</Action>

<Verify img="./img/bp-jump-pad-blueprint-complete.png" alt="BP_JumpPad の Event Graph で On Component Begin Overlap (Collision)、Cast To Character、Launch Character が接続され、Launch Velocity の Z が 1200 に設定された完成状態のスクリーンショット">`Launch Velocity` の Z が `1200` で、`Z Override` がオンになっていれば完了です。</Verify>

</Section>

<Section title="7. コンパイルして試す" goal="ジャンプ台に乗るとプレイヤーが上へ飛ぶことを確認します">

<Action>
  `BP_JumpPad` をコンパイルして保存し、メインエディターへ戻ります。
</Action>

<Action>
  プレイして、自分で置いたジャンプ台の上へ乗ります。
</Action>

<Recovery title="ジャンプ台に乗っても飛ばないとき">
次を順番に確認してください。

- `On Component Begin Overlap (Collision)` が追加されている
- `Other Actor` が `Cast To Character` の `Object` につながっている
- `As Character` が `Launch Character` の `Target` につながっている
- 白い実行線が途中で切れていない
- `Launch Velocity` の Z が `1200` になっている
- `Z Override` がオンになっている
</Recovery>

<Verify img="./img/bp-jump-pad-launch-in-play.png" alt="プレイ中にキャラクターが BP_JumpPad から上へ飛んでいるスクリーンショット">ジャンプ台に乗ったとき、プレイヤーが上へ飛べば追加ミッション成功です。</Verify>

</Section>

<Checkpoint>
- `BP_JumpPad` を自分でステージに置いている
- `Collision` の範囲を確認している
- `Collision` から `On Component Begin Overlap` を追加している
- ジャンプ台に触れた相手を `Cast To Character` で確認している
- `Launch Character` が Character を飛ばしている
- `Launch Velocity` の Z で上方向の強さを設定している
- プレイするとジャンプ台から上へ飛べる
</Checkpoint>

</Section>

'''

text = text[:start] + section + text[end:]
text = text.replace(
    '`Make Vector` の Z を変更し、ジャンプの高さを変えてください。',
    '`Launch Character` の `Launch Velocity` の Z を変更し、ジャンプの高さを変えてください。'
)
text = text.replace(
    '`Make Vector` の Z を変更し、コンパイルしてからプレイします。選んだ数値に応じてジャンプの高さが変われば完了です。',
    '`Launch Velocity` の Z を変更し、コンパイルしてからプレイします。選んだ数値に応じてジャンプの高さが変われば完了です。'
)

path.write_text(text, encoding='utf-8', newline='\n')
