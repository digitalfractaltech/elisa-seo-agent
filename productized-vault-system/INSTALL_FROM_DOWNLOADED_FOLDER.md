# Install Emily From a Downloaded Folder

This is the preferred operator flow when the package is downloaded somewhere first.

## Operator flow

1. User downloads or unzips the Emily package to a local folder.
2. Codex/OpenClaw checks that the folder exists and contains the expected files.
3. Codex asks the user to confirm the target OpenClaw install paths before copying anything.
4. Codex installs skills/system files.
5. Codex verifies the install and reports what was installed.

## Expected package files

The downloaded folder should contain at minimum:

```text
openclaw-skills/
OPENCLAW_INSTALL.md
productized-vault-system/
emily-openclaw-skills.zip   # optional if folder form is present
```

`openclaw-skills/manifest.json` should exist and list all skills.

## Confirmation before install

Before installation, confirm:

```text
Downloaded package folder: {{DOWNLOADED_PACKAGE_FOLDER}}
Skills install path: {{SKILLS_ROOT}}
System install path: {{SYSTEM_ROOT}}
Project vaults parent: {{OBSIDIAN_PROJECTS_ROOT}}
```

Default suggested paths:

```text
{{SKILLS_ROOT}} = /Users/<user>/.openclaw/skills
{{SYSTEM_ROOT}} = /Users/<user>/.openclaw/emily-system
{{OBSIDIAN_PROJECTS_ROOT}} = /Users/<user>/Documents/EmilyProjects
```

Do not assume these paths. Confirm them for each machine/install.

## Verification checklist

After install, verify:

- `{{SKILLS_ROOT}}/manifest.json` exists
- `{{SKILLS_ROOT}}/project-orchestrator/SKILL.md` exists
- `{{SKILLS_ROOT}}/dataforseo-rank-tracker-adapter/SKILL.md` exists
- `{{SYSTEM_ROOT}}/EMILY_PRIMARY_DIRECTIVE.md` exists
- `{{SYSTEM_ROOT}}/PROJECT_SWITCHING.md` exists
- no project-specific company/client names are hard-coded into the installed package

## Safety

- Do not delete existing skills unless the user explicitly asks.
- If a skill already exists, prefer backup/overwrite only after confirmation.
- Do not write API secrets into the skill folder, system folder, or Obsidian vault.
