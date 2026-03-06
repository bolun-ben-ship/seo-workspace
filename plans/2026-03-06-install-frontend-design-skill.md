# Plan: Install Frontend Design Skill

**Created:** 2026-03-06
**Status:** Implemented
**Request:** Install the frontend-design skill from `frontend-design/` into `.claude/skills/` and update all relevant workspace files to reflect its presence.

---

## Overview

### What This Plan Accomplishes

Installs the `frontend-design` skill — which already exists as a downloaded package in `frontend-design/skills/frontend-design/SKILL.md` — into the workspace's canonical skill location at `.claude/skills/frontend-design/`. Updates `CLAUDE.md` to document the skill so future sessions are aware of it and can use it.

### Why This Matters

Skills only trigger and become discoverable when they live in `.claude/skills/`. The skill is currently sitting in a package directory (`frontend-design/`) that Claude does not scan for skills. Moving it to the correct location makes it active and available for all frontend work.

---

## Current State

### Relevant Existing Structure

- `frontend-design/` — downloaded skill package (not the install location)
  - `frontend-design/skills/frontend-design/SKILL.md` — the actual skill file to install
  - `frontend-design/.claude-plugin/plugin.json` — plugin metadata (not needed post-install)
  - `frontend-design/README.md`, `CHANGELOG.md`, `LICENSE.md`, `SECURITY.md`, `demo.gif` — package docs (not part of the skill itself)
- `.claude/skills/` — canonical skill location; contains 13 SEO skills, skill-creator, mcp-integration
- `CLAUDE.md` — documents workspace structure and available skills; must stay current

### Gaps or Problems Being Addressed

- The `frontend-design` SKILL.md is in a package subdirectory (`frontend-design/skills/frontend-design/`) — not in `.claude/skills/` — so it is invisible to Claude and won't trigger
- `CLAUDE.md` has no mention of the frontend-design skill
- The workspace structure table in `CLAUDE.md` does not list the `frontend-design/` package directory or the installed skill

---

## Proposed Changes

### Summary of Changes

- Create `.claude/skills/frontend-design/` directory by placing `SKILL.md` there
- Copy the SKILL.md content from the package source into the installed location
- Update `CLAUDE.md`: workspace structure tree, key directories table, and add a Frontend Design Skills section

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `.claude/skills/frontend-design/SKILL.md` | Installed skill — triggers Claude to use distinctive, production-grade frontend design patterns when building UI components, pages, or apps |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `CLAUDE.md` | Add `frontend-design` to the `.claude/skills/` tree; add `frontend-design/` package dir to workspace structure; add Frontend Design Skill section documenting its purpose and trigger conditions |

### Files to Delete (if any)

None. The `frontend-design/` package directory should be kept as the source/reference package.

---

## Design Decisions

### Key Decisions Made

1. **Copy, don't move**: Keep the `frontend-design/` package directory intact. It contains README, CHANGELOG, LICENSE, and demo assets that are useful reference material. The installed skill at `.claude/skills/frontend-design/SKILL.md` is the active copy.

2. **SKILL.md only — no sub-resources**: The frontend-design skill has no `scripts/`, `references/`, or `assets/` subdirectories in the package. The SKILL.md is self-contained. Install only the SKILL.md.

3. **Update CLAUDE.md fully**: Three areas need updating — the directory tree, the key directories table, and a new Frontend Design Skills section parallel to the existing SEO Skills section.

### Alternatives Considered

- **Symlink instead of copy**: Not viable on Windows (the target platform for this workspace).
- **Point skills to `frontend-design/skills/`**: Claude only scans `.claude/skills/` — changing the scan path is not within scope and would break conventions.

### Open Questions (if any)

None — the skill is complete and self-contained. No user input required before implementation.

---

## Step-by-Step Tasks

### Step 1: Install the SKILL.md into `.claude/skills/frontend-design/`

Read the source SKILL.md from the package, then write it to the canonical skill location.

**Actions:**

- Read `frontend-design/skills/frontend-design/SKILL.md` (already done during research — content confirmed)
- Write the file content to `.claude/skills/frontend-design/SKILL.md` (creating the directory implicitly)

**Files affected:**

- `.claude/skills/frontend-design/SKILL.md` (new file)

---

### Step 2: Update `CLAUDE.md` — Workspace Structure tree

Add `frontend-design` to the `.claude/skills/` directory tree listing, and add `frontend-design/` as a root-level package directory entry.

**Actions:**

- In the `## Workspace Structure` code block, add `│   │   └── frontend-design/   # Distinctive, production-grade UI generation` inside the skills listing
- Add `├── frontend-design/` as a root-level entry with a note that it is the source package for the installed skill

**Files affected:**

- `CLAUDE.md`

---

### Step 3: Update `CLAUDE.md` — Key directories table

Add a row for the installed skill location and the package directory.

**Actions:**

- Add row: `.claude/skills/frontend-design/` | Frontend design skill — triggers on UI/frontend build requests
- Add row: `frontend-design/` | Source package for the frontend-design skill (README, CHANGELOG, demos)

**Files affected:**

- `CLAUDE.md`

---

### Step 4: Update `CLAUDE.md` — Add Frontend Design Skill section

Add a new top-level section documenting the frontend-design skill, parallel in style to the existing `## SEO Skills` section.

**Actions:**

- Add `## Frontend Design Skill` section after the SEO Skills section
- Document: what it does, when it triggers, example prompts, and where the SKILL.md lives
- Keep it concise — the skill itself has full instructions

**Content to add:**

```markdown
## Frontend Design Skill

This workspace includes the **frontend-design** skill for generating distinctive, production-grade frontend interfaces. The skill is at `.claude/skills/frontend-design/SKILL.md`.

### What It Does

Creates production-ready UI code (HTML/CSS/JS, React, Vue, etc.) with:
- Bold, intentional aesthetic direction — avoids generic AI-generated aesthetics
- Distinctive typography and color palettes
- High-impact animations and micro-interactions
- Context-aware, memorable design choices

### When It Triggers

Claude automatically uses this skill when asked to build frontend components, pages, or applications. Example prompts:
- "Create a dashboard for a music streaming app"
- "Build a landing page for an AI security startup"
- "Design a settings panel with dark mode"

### Source Package

The original downloaded package lives in `frontend-design/` and includes README, CHANGELOG, LICENSE, and a demo GIF for reference.
```

**Files affected:**

- `CLAUDE.md`

---

### Step 5: Verify installation

Confirm the skill is correctly installed and CLAUDE.md is accurate.

**Actions:**

- Read `.claude/skills/frontend-design/SKILL.md` and confirm content matches source
- Read updated `CLAUDE.md` and confirm all three updates are present and consistent
- Confirm the skill frontmatter has valid `name` and `description` fields (required for triggering)

**Files affected:**

- None (read-only verification)

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` — primary reference document updated in Steps 2-4
- `.claude/skills/` — the skill directory scanned by Claude Code at session start

### Updates Needed for Consistency

- No other files reference `.claude/skills/` by enumeration — only `CLAUDE.md` does, so only it needs updating.

### Impact on Existing Workflows

- No existing workflows are affected. This is a pure addition.
- The skill auto-triggers on frontend requests — no new slash commands are introduced.

---

## Validation Checklist

- [ ] `.claude/skills/frontend-design/SKILL.md` exists and contains valid YAML frontmatter with `name: frontend-design` and a `description` field
- [ ] SKILL.md body content matches the source at `frontend-design/skills/frontend-design/SKILL.md`
- [ ] `CLAUDE.md` workspace structure tree includes `frontend-design/` under `.claude/skills/`
- [ ] `CLAUDE.md` key directories table includes entries for both `.claude/skills/frontend-design/` and `frontend-design/` (package)
- [ ] `CLAUDE.md` has a `## Frontend Design Skill` section with description, triggers, and source package note
- [ ] No existing CLAUDE.md content was accidentally removed or altered

---

## Success Criteria

The implementation is complete when:

1. `.claude/skills/frontend-design/SKILL.md` exists with complete, valid content
2. `CLAUDE.md` accurately reflects the new skill in structure, table, and dedicated section
3. A fresh `/prime` session would correctly identify and describe the frontend-design skill as available

---

## Notes

- The `frontend-design/` package directory should not be deleted — it serves as the source of record and contains useful supplementary material (README, demo)
- If the skill is ever updated upstream, the update workflow is: replace `frontend-design/` package contents, then re-copy the SKILL.md to `.claude/skills/frontend-design/SKILL.md`
- The skill has no bundled resources (no scripts/, references/, assets/) — if a future version adds them, they should be installed alongside the SKILL.md in `.claude/skills/frontend-design/`

---

## Implementation Notes

**Implemented:** 2026-03-06

### Summary

- Created `.claude/skills/frontend-design/SKILL.md` with full content copied from `frontend-design/skills/frontend-design/SKILL.md`
- Updated `CLAUDE.md` workspace structure tree to include `frontend-design/` under `.claude/skills/` and as a root-level package directory
- Updated `CLAUDE.md` key directories table with two new rows
- Added `## Frontend Design Skill` section to `CLAUDE.md` after the SEO Skills section

### Deviations from Plan

None.

### Issues Encountered

None. The skill was confirmed active immediately after installation — it appeared in the system skills list before CLAUDE.md was even updated.
