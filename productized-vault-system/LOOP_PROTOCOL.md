# Emily Loop Protocol

Loops are the engine inside the agent:

```text
RUN → CHECK → DECIDE → repeat
```

Use `loop-controller` whenever the agent should keep working without waiting for the user to direct every sub-step.

## Persistent state

Store loop state in the active project vault:

```text
07-queue/loops/{{loop_id}}.md
08-tracking/loops/{{loop_id}}.json
```

## Decision states

- continue
- retry
- wait
- escalate
- complete
- blocked
- stop_budget

## Hard stop gates

- approval required
- missing access/tool/secret
- reviewer rejected output
- quality or reputation risk
- public publish/send/destructive change
- same blocker 3 times
- measurement window pending

## Installation note

If this protocol is added after Emily was already installed, copy `loop-controller` into `~/.openclaw/skills/` and optionally copy this file into `~/.openclaw/emily-system/LOOP_PROTOCOL.md`.
