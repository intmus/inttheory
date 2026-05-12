---
type: handoff queue
source: hub (personal-assistant)
---

# Todo Handoff — From Hub

The hub deposits items here when work in the personal-assistant repo generates a task for inttheory. The inttheory agent checks this file during open session (step 8) and surfaces new items for user review.

## How This Works

1. Hub agent writes an item here during its close session
2. Hub saves the file but does **not** commit or push this repo
3. Next open session in inttheory, the agent flags new entries
4. User reviews and confirms — confirmed items are added to `todo/todo.md`
5. Processed entries are cleared from this file

## Pending

<!-- No pending handoffs -->
