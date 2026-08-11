# Optional Orchestrator Routing Patch

Patch `project-orchestrator` only after approval.

Add this near the top of the orchestrator body:

```text
For autonomous continuation, route work through `loop-controller` so every cycle runs, checks, decides, and records state before continuing.
```

Add this section before the operating loop:

```text
## #LOOP ROUTING
When the user asks to continue, automate, run a weekly check-in, monitor, or pursue a project goal, invoke `loop-controller` first. The loop controller should select the next specialist skill based on vault state and stop on real signals: completion, blocker, approval gate, budget cap, or measurement window.
```

Using loops should not bypass approval rules. Publishing, CMS changes, outreach sends, redirects/canonicals/deletions, GBP changes, and destructive actions remain approval-gated.
