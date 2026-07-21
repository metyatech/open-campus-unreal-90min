from __future__ import annotations

import json
from pathlib import Path

GUIDE = Path("content/docs/student-guide/index.mdx")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def verify_callout(path: str, expected_count: int) -> None:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("annotationMode") != "callout":
        raise SystemExit(f"{path}: annotationMode must be callout")
    action_count = sum(
        1
        for annotation in data.get("annotations", [])
        if annotation.get("role") == "action"
    )
    if action_count != expected_count:
        raise SystemExit(
            f"{path}: expected {expected_count} action callouts, found {action_count}"
        )


text = GUIDE.read_text(encoding="utf-8")

text = replace_once(
    text,
    '''<Action img="./img/bp-jump-pad-add-overlap-event.webp" alt="BP_JumpPad の Components で Collision を右クリックし、Add Event から Add OnComponentBeginOverlap を選ぶスクリーンショット">
  Components の `Collision` を右クリックし、`Add Event`、`Add OnComponentBeginOverlap` の順にクリックします。
</Action>''',
    '''<Action img="./img/bp-jump-pad-add-overlap-event.webp" alt="BP_JumpPad の Components で、① Collision、② Add Event、③ Add OnComponentBeginOverlap が示されているスクリーンショット">
  ① Components の `Collision` を右クリックし、② `Add Event`、③ `Add OnComponentBeginOverlap` の順にクリックします。
</Action>''',
    "overlap action",
)

text = replace_once(
    text,
    '''<Action img="./img/bp-jump-pad-add-cast-to-character.webp" alt="BP_JumpPad の Event Graph で Other Actor から Cast To Character を追加するスクリーンショット">
  `Other Actor` のピンからドラッグし、検索欄に `Cast To Character` と入力して、`Cast To Character` を追加します。
</Action>''',
    '''<Action img="./img/bp-jump-pad-add-cast-to-character.webp" alt="BP_JumpPad の Event Graph で、① Other Actor のピン、② ドロップ先、③ 検索欄、④ Cast To Character の候補が示されているスクリーンショット">
  ① `Other Actor` のピンからドラッグし、② 空いている場所へドロップします。③ 検索欄に `Cast To Character` と入力し、④ `Cast To Character` を選びます。
</Action>''',
    "cast action",
)

text = replace_once(
    text,
    '''<Action img="./img/bp-jump-pad-add-launch-character.webp" alt="BP_JumpPad の Event Graph で As Character の青いピンからドラッグし、Launch Character を検索して追加するスクリーンショット">
  `As Character` の青いピンからドラッグし、`Launch Character` を検索して追加します。
</Action>''',
    '''<Action img="./img/bp-jump-pad-add-launch-character.webp" alt="BP_JumpPad の Event Graph で、① As Character の青いピン、② ドロップ先、③ 検索欄、④ Launch Character の候補が示されているスクリーンショット">
  ① `As Character` の青いピンからドラッグし、② 空いている場所へドロップします。③ 検索欄に `Launch Character` と入力し、④ `Launch Character` を選びます。
</Action>''',
    "launch action",
)

required_fragments = [
    "① Components の `Collision` を右クリックし、② `Add Event`、③ `Add OnComponentBeginOverlap`",
    "① `Other Actor` のピンからドラッグし、② 空いている場所へドロップします。③ 検索欄に `Cast To Character` と入力し、④ `Cast To Character` を選びます。",
    "① `As Character` の青いピンからドラッグし、② 空いている場所へドロップします。③ 検索欄に `Launch Character` と入力し、④ `Launch Character` を選びます。",
]
for fragment in required_fragments:
    if text.count(fragment) != 1:
        raise SystemExit(f"required numbered fragment missing or duplicated: {fragment}")

for forbidden in [
    "`On Component Begin Overlap (Collision)` の白い実行ピンを",
    "`Cast To Character` の成功時の白い実行ピンを",
]:
    if forbidden in text:
        raise SystemExit(f"manual auto-connection instruction must not exist: {forbidden}")

verify_callout(
    "content/docs/student-guide/shots/bp-jump-pad-add-overlap-event.shot.json",
    3,
)
verify_callout(
    "content/docs/student-guide/shots/bp-jump-pad-add-cast-to-character.shot.json",
    4,
)
verify_callout(
    "content/docs/student-guide/shots/bp-jump-pad-add-launch-character.shot.json",
    4,
)

GUIDE.write_text(text, encoding="utf-8", newline="\n")
