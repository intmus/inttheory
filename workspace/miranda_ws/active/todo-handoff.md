---
type: handoff queue
status: dormant
---

# Todo Handoff — Miranda Wilson

This file receives incoming todo items from a connected hub repo. It is currently **dormant** — Miranda does not have a hub repo connected.

## How This Works (When Active)

1. Hub agent writes an item here during its close session
2. Hub saves the file but does **not** commit or push this repo
3. Next open session in inttheory, Miranda's agent flags new entries
4. Miranda reviews and confirms — confirmed items are added to `todo/todo.md`
5. Processed entries are cleared from this file

## Activation Steps

To connect a hub repo and activate this handoff file:

1. Create a personal-assistant hub repo with ACP infrastructure (see `agent-harness-impl.md` §17-18)
2. Add registry entries in both directions:
   - In the hub's `agent/toshare/registry.md`: add inttheory with `User Heading: ## Miranda Wilson`
   - In this repo's `agent/toshare/registry.md`: add the hub with `Status: Hub`
3. Add a **Close Session** section to `agent/roles/miranda/identity.md` with snapshot export steps (see Sean's identity.md for the pattern)
4. Change the `status` field in this file's frontmatter from `dormant` to `active`
5. Remove this activation instructions section

## Pending

<!-- No pending handoffs -->
