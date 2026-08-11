# Install Component: loop-controller

Use this when Emily/OpenClaw SEO skills are already installed and you want to add loop behavior without reinstalling everything.

## What it installs

```text
openclaw-skills/loop-controller/
productized-vault-system/LOOP_PROTOCOL.md  # optional system doc
```

## Safe install

1. Verify the component contains:

```text
openclaw-skills/loop-controller/SKILL.md
productized-vault-system/LOOP_PROTOCOL.md
component-manifest.json
```

2. Confirm the skills path with the user, usually:

```text
~/.openclaw/skills
```

3. Back up the current skills folder or at least the installed manifest.

4. Copy only the new skill folder:

```bash
cp -R openclaw-skills/loop-controller ~/.openclaw/skills/
```

5. If `~/.openclaw/skills/manifest.json` exists, back it up and add `loop-controller` to the `skills` array if missing; set `skill_count` to the array length.

6. Optionally copy `LOOP_PROTOCOL.md` into:

```text
~/.openclaw/emily-system/LOOP_PROTOCOL.md
```

7. Do not modify project Obsidian vaults except to create loop state files during actual use.
