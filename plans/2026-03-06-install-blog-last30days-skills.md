# Plan: Install Blog and Research-Last30Days Skills + Delete Source Directories

**Created:** 2026-03-06
**Status:** Implemented
**Request:** Install claude-blog and last30days skills into `.claude/skills/`, rename the last30days skill folder to `research-last30days` (descriptive), and delete all source package directories (claude-blog-main/, last30days-skill-main/, frontend-design/) once skills are properly installed.

---

## Overview

### What This Plan Accomplishes

Installs two major skill packages into `.claude/skills/`: (1) `blog` — a 14-skill blog creation engine with 4 agents and a Python analysis script, and (2) `research-last30days` — a multi-source trend research skill with a Python-based search engine. After installation, all three source package directories (`claude-blog-main/`, `last30days-skill-main/`, `frontend-design/`) are deleted from the workspace root. Updates `CLAUDE.md` to document all new skills and the cleaned-up structure.

### Why This Matters

The skills are inert until placed in `.claude/skills/`. The source package directories are just staging areas — once skills are installed, they have no ongoing purpose and create clutter. The `last30days` skill name is cryptic; `research-last30days` clearly communicates what it does (research any topic across social platforms from the last 30 days).

---

## Skill Name Analysis: last30days → research-last30days

**What the skill actually does:**
- Accepts any topic as input
- Searches Reddit, X (Twitter), YouTube, TikTok, Instagram, Hacker News, Polymarket, and the web
- Filters results to the last 30 days (configurable with `--days=N`)
- Synthesizes findings into a structured research report
- Produces copy-paste-ready prompts for the topic
- Supports specialized modes: RECOMMENDATIONS, NEWS, PROMPTING, GENERAL

**Why the current name `last30days` is unclear:** It describes the time window, not the action. A new user wouldn't know from the name that this is a research/synthesis tool.

**New name: `research-last30days`** — communicates both the action (research) and the scope (last 30 days). The folder becomes `.claude/skills/research-last30days/` and the SKILL.md `name:` field is updated to `research-last30days`. The description and examples in the SKILL.md body are preserved as-is since they remain accurate.

---

## Current State

### Relevant Existing Structure

**Installed skills (`.claude/skills/`):**
- `seo/` + 12 `seo-*` sub-skills (already installed)
- `frontend-design/` (installed in previous session — source dir still exists at root)
- `mcp-integration/`, `skill-creator/`

**Installed agents (`.claude/agents/`):**
- `seo-content.md`, `seo-performance.md`, `seo-schema.md`, `seo-sitemap.md`, `seo-technical.md`, `seo-visual.md`

**Source package directories at root (to install then delete):**
- `claude-blog-main/` — blog skill package
- `last30days-skill-main/` — last30days research skill package
- `frontend-design/` — already installed; source dir to be deleted

**claude-blog-main structure (relevant parts):**
- `blog/` — main orchestrator: `SKILL.md` + `references/` (12 files) + `templates/` (12 files)
- `skills/` — 13 sub-skills: blog-analyze, blog-audit, blog-brief, blog-calendar, blog-chart, blog-geo, blog-outline, blog-repurpose, blog-rewrite, blog-schema, blog-seo-check, blog-strategy, blog-write
- `agents/` — 4 agents: blog-researcher.md, blog-reviewer.md, blog-seo.md, blog-writer.md
- `scripts/analyze_blog.py` — Python quality analysis engine
- `requirements.txt` — Python dependencies

**last30days-skill-main structure (relevant parts):**
- `SKILL.md` — skill file (name: `last30days`)
- `scripts/` — full research engine: `last30days.py` + `lib/` (22 modules) + `lib/vendor/bird-search/`

### Gaps or Problems Being Addressed

- `claude-blog` skills and agents not in `.claude/skills/` or `.claude/agents/` — invisible to Claude
- `last30days` skill and its scripts not installed — cannot be invoked
- `last30days` name is cryptic — doesn't communicate what the skill does
- Source package directories clutter the workspace root with no ongoing purpose
- `CLAUDE.md` has no mention of blog or research-last30days skills

---

## Proposed Changes

### Summary of Changes

- Install `blog` orchestrator to `.claude/skills/blog/` (SKILL.md + 12 references + 12 templates + analyze_blog.py)
- Install 13 `blog-*` sub-skills to `.claude/skills/blog-*/`
- Install 4 blog agents to `.claude/agents/`
- Install `research-last30days` skill to `.claude/skills/research-last30days/` (SKILL.md + full scripts/)
- Update installed SKILL.md `name:` field from `last30days` to `research-last30days`
- Delete source directories: `claude-blog-main/`, `last30days-skill-main/`, `frontend-design/`
- Update `CLAUDE.md`: structure tree (no source dirs), key directories table, new skill sections

### New Files to Create (Installed)

**Blog — main orchestrator:**

| Installed Path | Source |
| --- | --- |
| `.claude/skills/blog/SKILL.md` | `claude-blog-main/blog/SKILL.md` |
| `.claude/skills/blog/references/` (12 files) | `claude-blog-main/blog/references/*` |
| `.claude/skills/blog/templates/` (12 files) | `claude-blog-main/blog/templates/*` |
| `.claude/skills/blog/scripts/analyze_blog.py` | `claude-blog-main/scripts/analyze_blog.py` |

**Blog — 13 sub-skills:**

| Installed Path | Source |
| --- | --- |
| `.claude/skills/blog-analyze/SKILL.md` | `claude-blog-main/skills/blog-analyze/SKILL.md` |
| `.claude/skills/blog-audit/SKILL.md` | `claude-blog-main/skills/blog-audit/SKILL.md` |
| `.claude/skills/blog-brief/SKILL.md` | `claude-blog-main/skills/blog-brief/SKILL.md` |
| `.claude/skills/blog-calendar/SKILL.md` | `claude-blog-main/skills/blog-calendar/SKILL.md` |
| `.claude/skills/blog-chart/SKILL.md` | `claude-blog-main/skills/blog-chart/SKILL.md` |
| `.claude/skills/blog-geo/SKILL.md` | `claude-blog-main/skills/blog-geo/SKILL.md` |
| `.claude/skills/blog-outline/SKILL.md` | `claude-blog-main/skills/blog-outline/SKILL.md` |
| `.claude/skills/blog-repurpose/SKILL.md` | `claude-blog-main/skills/blog-repurpose/SKILL.md` |
| `.claude/skills/blog-rewrite/SKILL.md` | `claude-blog-main/skills/blog-rewrite/SKILL.md` |
| `.claude/skills/blog-schema/SKILL.md` | `claude-blog-main/skills/blog-schema/SKILL.md` |
| `.claude/skills/blog-seo-check/SKILL.md` | `claude-blog-main/skills/blog-seo-check/SKILL.md` |
| `.claude/skills/blog-strategy/SKILL.md` | `claude-blog-main/skills/blog-strategy/SKILL.md` |
| `.claude/skills/blog-write/SKILL.md` | `claude-blog-main/skills/blog-write/SKILL.md` |

**Blog — 4 agents:**

| Installed Path | Source |
| --- | --- |
| `.claude/agents/blog-researcher.md` | `claude-blog-main/agents/blog-researcher.md` |
| `.claude/agents/blog-reviewer.md` | `claude-blog-main/agents/blog-reviewer.md` |
| `.claude/agents/blog-seo.md` | `claude-blog-main/agents/blog-seo.md` |
| `.claude/agents/blog-writer.md` | `claude-blog-main/agents/blog-writer.md` |

**Research-Last30Days:**

| Installed Path | Source |
| --- | --- |
| `.claude/skills/research-last30days/SKILL.md` | `last30days-skill-main/SKILL.md` (then edit name field) |
| `.claude/skills/research-last30days/scripts/` (entire dir) | `last30days-skill-main/scripts/*` |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `.claude/skills/research-last30days/SKILL.md` | Change `name: last30days` → `name: research-last30days` in frontmatter |
| `CLAUDE.md` | Add blog and research-last30days to skills tree; remove source package dirs from root tree; update key directories table; add `## Blog Skill` section; add `## Research-Last30Days Skill` section; update Frontend Design Skill section to remove "Source Package" subsection |

### Files to Delete

| Path | Reason |
| --- | --- |
| `claude-blog-main/` (entire directory) | Skills installed; source dir no longer needed |
| `last30days-skill-main/` (entire directory) | Skill installed; source dir no longer needed |
| `frontend-design/` (entire directory) | Skill already installed in previous session; source dir no longer needed |

---

## Design Decisions

### Key Decisions Made

1. **Rename `last30days` → `research-last30days`**: The name `last30days` describes the time window but not the action. `research-last30days` is immediately understandable. Both the folder and the SKILL.md `name:` field are updated. The SKILL.md body (examples, argument-hint, path discovery) is preserved as-is since it remains functionally correct — `CLAUDE_PLUGIN_ROOT` drives script discovery, not the folder name.

2. **Blog and last30days scripts go inside their skill directories**: Both skills need their scripts co-located with SKILL.md. For `research-last30days`, the SKILL.md uses `CLAUDE_PLUGIN_ROOT` env var for script auto-discovery — the scripts MUST be inside `.claude/skills/research-last30days/scripts/`. For `blog`, `analyze_blog.py` is placed in `.claude/skills/blog/scripts/` for the same self-contained pattern.

3. **Delete all source package directories after install**: Once skills are installed in `.claude/skills/`, the source dirs (`claude-blog-main/`, `last30days-skill-main/`, `frontend-design/`) serve no purpose. Deleting them keeps the workspace root clean and avoids confusion about which copy is "active."

4. **Don't install `last30days-skill-main/variants/`**: The `variants/` folder contains alternate skill versions. Only the main SKILL.md and scripts are installed. Since the source dir is deleted, variants are simply discarded.

5. **`blog-chart` installed even though internal**: The blog orchestrator delegates to `blog-chart` for SVG chart generation — it must exist as a skill even though users don't call it directly.

### Alternatives Considered

- **Keep source dirs for reference**: Rejected per user preference. Once installed, the skills ARE the reference — the source dirs are just zip artifacts.
- **Only rename the folder, not the SKILL.md `name:` field**: Rejected — the `name` field is how Claude identifies and routes the skill. Mismatching folder and name creates inconsistency.
- **Rename `blog-*` sub-skills too** (e.g., `blog-write` → `write-blog-post`): Rejected — `blog-*` is a clear namespace prefix and the sub-names (`write`, `analyze`, `brief`, etc.) are self-explanatory in context.

### Open Questions (if any)

None — all decisions resolved. No user input required before implementation.

---

## Step-by-Step Tasks

### Step 1: Install blog main orchestrator (SKILL.md + references + templates)

Copy the blog orchestrator directory structure from source to `.claude/skills/blog/`.

**Actions:**

- Run: `cp -r "B:/Google Antigravity/RightClick-Claude-Workspace/claude-blog-main/blog/." "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/blog/"`
- Verify: `ls ".claude/skills/blog/"` shows `SKILL.md`, `references/`, `templates/`
- Verify: `ls ".claude/skills/blog/references/"` shows 12 files
- Verify: `ls ".claude/skills/blog/templates/"` shows 12 files

**Files affected:**

- `.claude/skills/blog/SKILL.md` (new)
- `.claude/skills/blog/references/` (12 new files)
- `.claude/skills/blog/templates/` (12 new files)

---

### Step 2: Install blog Python analysis script

Copy `analyze_blog.py` into a scripts/ subdirectory inside the blog skill.

**Actions:**

- Run: `mkdir -p "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/blog/scripts"`
- Run: `cp "B:/Google Antigravity/RightClick-Claude-Workspace/claude-blog-main/scripts/analyze_blog.py" "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/blog/scripts/analyze_blog.py"`
- Verify file exists

**Files affected:**

- `.claude/skills/blog/scripts/analyze_blog.py` (new)

---

### Step 3: Install 13 blog sub-skills

Copy each sub-skill SKILL.md from the source package to its own directory in `.claude/skills/`.

**Actions:**

```bash
for skill in blog-analyze blog-audit blog-brief blog-calendar blog-chart blog-geo blog-outline blog-repurpose blog-rewrite blog-schema blog-seo-check blog-strategy blog-write; do
  mkdir -p "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/$skill"
  cp "B:/Google Antigravity/RightClick-Claude-Workspace/claude-blog-main/skills/$skill/SKILL.md" \
     "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/$skill/SKILL.md"
done
```

- Verify: `ls ".claude/skills/"` shows all 13 `blog-*` directories

**Files affected:**

- `.claude/skills/blog-analyze/SKILL.md` through `.claude/skills/blog-write/SKILL.md` (13 new files)

---

### Step 4: Install 4 blog agents

Copy agent config files from source to `.claude/agents/`.

**Actions:**

```bash
for agent in blog-researcher blog-reviewer blog-seo blog-writer; do
  cp "B:/Google Antigravity/RightClick-Claude-Workspace/claude-blog-main/agents/$agent.md" \
     "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/agents/$agent.md"
done
```

- Verify: `ls ".claude/agents/"` shows all 4 `blog-*.md` files alongside existing seo agents

**Files affected:**

- `.claude/agents/blog-researcher.md` (new)
- `.claude/agents/blog-reviewer.md` (new)
- `.claude/agents/blog-seo.md` (new)
- `.claude/agents/blog-writer.md` (new)

---

### Step 5: Install research-last30days skill (SKILL.md + full scripts directory)

Copy the SKILL.md and entire scripts directory to `.claude/skills/research-last30days/`.

**Actions:**

- Run: `mkdir -p "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/research-last30days"`
- Run: `cp "B:/Google Antigravity/RightClick-Claude-Workspace/last30days-skill-main/SKILL.md" "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/research-last30days/SKILL.md"`
- Run: `cp -r "B:/Google Antigravity/RightClick-Claude-Workspace/last30days-skill-main/scripts/." "B:/Google Antigravity/RightClick-Claude-Workspace/.claude/skills/research-last30days/scripts/"`
- Verify: `ls ".claude/skills/research-last30days/"` shows `SKILL.md` and `scripts/`
- Verify: `ls ".claude/skills/research-last30days/scripts/"` shows `last30days.py`, `lib/`

**Files affected:**

- `.claude/skills/research-last30days/SKILL.md` (new)
- `.claude/skills/research-last30days/scripts/` (new directory with full contents)

---

### Step 6: Update the installed SKILL.md name field

Edit the installed SKILL.md to change `name: last30days` → `name: research-last30days`. This is required so Claude identifies the skill by its new descriptive name.

**Actions:**

- Read `.claude/skills/research-last30days/SKILL.md`
- Edit: change `name: last30days` to `name: research-last30days` in the YAML frontmatter
- Do NOT change any other fields or the body — the description, argument-hint, and body instructions remain valid

**Files affected:**

- `.claude/skills/research-last30days/SKILL.md` (modified — name field only)

---

### Step 7: Delete source package directories

Delete all three source directories. Skills are now installed — these dirs serve no further purpose.

**Actions:**

- Run: `rm -rf "B:/Google Antigravity/RightClick-Claude-Workspace/claude-blog-main"`
- Run: `rm -rf "B:/Google Antigravity/RightClick-Claude-Workspace/last30days-skill-main"`
- Run: `rm -rf "B:/Google Antigravity/RightClick-Claude-Workspace/frontend-design"`
- Verify: `ls` of workspace root shows none of these three directories remain

**Files affected:**

- `claude-blog-main/` — deleted
- `last30days-skill-main/` — deleted
- `frontend-design/` — deleted

---

### Step 8: Update CLAUDE.md — workspace structure tree

Update the tree to reflect the new skills and cleaned root (no source package dirs).

**Actions:**

In the `.claude/skills/` section, after `frontend-design/`, add:

```
│   │   ├── blog/                  # Blog orchestrator (12 commands, 12 templates, 12 references)
│   │   ├── blog-write/            # Write new blog posts from scratch
│   │   ├── blog-rewrite/          # Optimize existing posts
│   │   ├── blog-analyze/          # 100-point quality scoring
│   │   ├── blog-brief/            # Content brief generation
│   │   ├── blog-calendar/         # Editorial calendar planning
│   │   ├── blog-strategy/         # Blog strategy and topic ideation
│   │   ├── blog-outline/          # SERP-informed content outlines
│   │   ├── blog-seo-check/        # Post-writing SEO validation
│   │   ├── blog-schema/           # JSON-LD schema generation
│   │   ├── blog-repurpose/        # Cross-platform content repurposing
│   │   ├── blog-geo/              # AI citation readiness audit
│   │   ├── blog-audit/            # Full-site blog health assessment
│   │   ├── blog-chart/            # Internal SVG chart generation
│   │   └── research-last30days/   # Multi-source trend research (Reddit, X, YouTube, TikTok, HN, Polymarket)
```

In the `.claude/agents/` section, add blog agents:
```
│       ├── blog-researcher.md
│       ├── blog-writer.md
│       ├── blog-seo.md
│       └── blog-reviewer.md
```

Remove from the root tree: `├── frontend-design/`, and do NOT add `claude-blog/` or `last30days/` (source dirs are deleted).

**Files affected:**

- `CLAUDE.md`

---

### Step 9: Update CLAUDE.md — key directories table

Add rows for new installed locations. Remove rows for deleted source dirs.

**Actions:**

Add these rows:

| Directory | Purpose |
| --- | --- |
| `.claude/skills/blog/` | Blog orchestrator — routes 12 commands, holds references and templates |
| `.claude/skills/blog-*/` | 13 blog sub-skills for writing, analysis, SEO, schema, repurposing |
| `.claude/skills/research-last30days/` | Multi-source trend research skill + bundled Python scripts |
| `.claude/agents/blog-*/` | 4 blog agents: researcher, writer, SEO validator, reviewer |

Remove existing row for `frontend-design/` (source package) from the table if present.

**Files affected:**

- `CLAUDE.md`

---

### Step 10: Update CLAUDE.md — add Blog Skill section

Add a `## Blog Skill` section after `## Frontend Design Skill`. Remove "Source Package" subsection from the Frontend Design Skill section since the source dir is deleted.

**Actions:**

First, remove the "Source Package" subsection from `## Frontend Design Skill` (the `frontend-design/` source dir is being deleted).

Then insert:

```markdown
## Blog Skill

This workspace includes the **blog** skill suite for full-lifecycle blog content creation. The main orchestrator is at `.claude/skills/blog/SKILL.md`.

### What It Does

Writes, rewrites, analyzes, audits, and repurposes blog content. 12 commands covering every phase of blog production, dual-optimized for Google rankings (December 2025 Core Update, E-E-A-T) and AI citation platforms (ChatGPT, Perplexity, AI Overviews).

### Blog Commands

| Command | Description |
| --- | --- |
| `/blog write <topic>` | Write a new blog post from scratch |
| `/blog rewrite <file>` | Optimize an existing blog post |
| `/blog analyze <file>` | Quality audit with 0-100 score |
| `/blog brief <topic>` | Generate a detailed content brief |
| `/blog calendar` | Generate an editorial calendar |
| `/blog strategy <niche>` | Blog strategy and topic ideation |
| `/blog outline <topic>` | SERP-informed content outline |
| `/blog seo-check <file>` | Post-writing SEO validation |
| `/blog schema <file>` | Generate JSON-LD schema markup |
| `/blog repurpose <file>` | Repurpose for social, email, YouTube |
| `/blog geo <file>` | AI citation readiness audit |
| `/blog audit [directory]` | Full-site blog health assessment |

### Blog Architecture

- **Orchestrator** (`blog/SKILL.md`): Routes 12 commands, platform detection, quality gates
- **Sub-skills** (`blog-*/SKILL.md`): 13 specialized skills loaded on-demand
- **Agents** (`.claude/agents/blog-*.md`): 4 parallel workers (researcher, writer, SEO validator, reviewer)
- **References** (`blog/references/`): 12 on-demand reference docs (Google landscape, GEO, E-E-A-T, schema, etc.)
- **Templates** (`blog/templates/`): 12 content type templates (how-to, listicle, case study, comparison, pillar, etc.)
- **Script** (`blog/scripts/analyze_blog.py`): Python quality analysis engine (5-category, 100-point scoring)

### Python Dependencies

Install if using `blog analyze` command for advanced scoring:

```bash
pip install beautifulsoup4 textstat language-tool-python lxml
```
```

**Files affected:**

- `CLAUDE.md`

---

### Step 11: Update CLAUDE.md — add Research-Last30Days Skill section

Add a `## Research-Last30Days Skill` section after the Blog Skill section.

**Actions:**

Insert:

```markdown
## Research-Last30Days Skill

This workspace includes the **research-last30days** skill for researching any topic across multiple social and web platforms from the last 30 days. The skill is at `.claude/skills/research-last30days/SKILL.md`.

### What It Does

Researches ANY topic across Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, and the web. Filters to the last 30 days. Surfaces what people are actually discussing, recommending, betting on, and debating right now. Produces a structured report and copy-paste-ready prompts.

### How to Use

The skill is user-invocable. Type the skill name followed by a topic:

```
research-last30days AI video tools
research-last30days best project management tools
research-last30days nano banana pro prompts for Midjourney
```

### Options

- `--quick` — Faster, fewer sources
- `--deep` — Comprehensive (50-70 Reddit, 40-60 X)
- `--days=N` — Look back N days instead of 30
- `--agent` — Non-interactive mode for subagent use

### Requirements

- `OPENAI_API_KEY` — Required for Reddit search via OpenAI Responses API
- `node` and `python3` — Required binaries
- Optional: `SCRAPECREATORS_API_KEY` — TikTok/Instagram sources (100 free credits, then PAYG)
- Optional: `XAI_API_KEY` — X/Twitter sources via xAI API
```

**Files affected:**

- `CLAUDE.md`

---

### Step 12: Verify installation

Confirm all files are correctly installed and CLAUDE.md is accurate.

**Actions:**

- `ls ".claude/skills/"` — confirm `blog`, all 13 `blog-*`, `research-last30days` present
- `ls ".claude/skills/blog/"` — confirm `SKILL.md`, `references/`, `templates/`, `scripts/`
- `ls ".claude/skills/research-last30days/"` — confirm `SKILL.md` and `scripts/`
- `ls ".claude/skills/research-last30days/scripts/"` — confirm `last30days.py` and `lib/`
- `ls ".claude/agents/"` — confirm all 4 `blog-*.md` files present
- `ls` of workspace root — confirm `claude-blog-main/`, `last30days-skill-main/`, `frontend-design/` are gone
- Read `.claude/skills/research-last30days/SKILL.md` — confirm `name: research-last30days` in frontmatter
- Read `.claude/skills/blog/SKILL.md` — confirm `name: blog`

**Files affected:**

- None (read-only verification)

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` — updated in Steps 8-11
- `.claude/skills/` — scanned by Claude Code at session start
- `.claude/agents/` — agent configs loaded by Claude Code

### Updates Needed for Consistency

- `CLAUDE.md` is the only file that enumerates skill directories — only it needs updating.
- The `## Frontend Design Skill` section in CLAUDE.md references the now-deleted `frontend-design/` source dir — this subsection must be removed.

### Impact on Existing Workflows

- No existing skills or workflows are affected. Pure addition + cleanup.
- Blog skill complements existing SEO skills — `blog-geo` and `blog-audit` work well alongside `/seo geo` and `/seo audit`.
- `research-last30days` can feed research data into blog writing workflows.

---

## Validation Checklist

- [ ] `.claude/skills/blog/SKILL.md` exists with `name: blog` frontmatter
- [ ] `.claude/skills/blog/references/` contains 12 reference files
- [ ] `.claude/skills/blog/templates/` contains 12 template files
- [ ] `.claude/skills/blog/scripts/analyze_blog.py` exists
- [ ] All 13 `blog-*` sub-skill directories exist in `.claude/skills/` each with a SKILL.md
- [ ] All 4 blog agent files exist in `.claude/agents/`
- [ ] `.claude/skills/research-last30days/SKILL.md` exists with `name: research-last30days` frontmatter
- [ ] `.claude/skills/research-last30days/scripts/last30days.py` exists
- [ ] `.claude/skills/research-last30days/scripts/lib/` directory exists
- [ ] `claude-blog-main/` no longer exists in workspace root
- [ ] `last30days-skill-main/` no longer exists in workspace root
- [ ] `frontend-design/` no longer exists in workspace root
- [ ] `CLAUDE.md` structure tree has no source package dirs at root
- [ ] `CLAUDE.md` skills tree includes all blog-* skills and research-last30days
- [ ] `CLAUDE.md` has `## Blog Skill` section with 12-command table
- [ ] `CLAUDE.md` has `## Research-Last30Days Skill` section
- [ ] `CLAUDE.md` Frontend Design Skill section no longer references deleted source dir
- [ ] No other existing CLAUDE.md content removed or altered

---

## Success Criteria

The implementation is complete when:

1. All blog skills (orchestrator + 13 sub-skills), 4 agents, and Python script are installed
2. The research-last30days skill and its scripts are installed with the updated `name:` field
3. All three source package directories are deleted from the workspace root
4. `CLAUDE.md` accurately reflects the installed skills with no references to deleted dirs
5. A fresh `/prime` session correctly identifies blog (12 commands) and research-last30days as available

---

## Notes

- The `research-last30days` skill requires `OPENAI_API_KEY` for full functionality; without it, it operates in web-only mode
- The blog skill's `blog-chart` sub-skill is internal — not user-callable, but must be installed for orchestrator delegation
- `blog analyze` command works without Python deps but scoring is more accurate with `beautifulsoup4` and `textstat` installed
- If skills need updating in future, the workflow is: download new version, install files, delete downloaded package

---

## Implementation Notes

**Implemented:** 2026-03-06

### Summary

- Installed blog orchestrator to `.claude/skills/blog/` with SKILL.md, 12 references, 12 templates, and analyze_blog.py script
- Installed 13 blog sub-skills to `.claude/skills/blog-*/`
- Installed 4 blog agents to `.claude/agents/`
- Installed research-last30days skill to `.claude/skills/research-last30days/` with full scripts/ directory
- Updated SKILL.md `name:` field from `last30days` to `research-last30days`
- Deleted source directories: `claude-blog-main/`, `last30days-skill-main/`, `frontend-design/`
- Updated CLAUDE.md: skills tree (blog + research-last30days + blog agents), key directories table, removed source package dirs, removed Frontend Design "Source Package" subsection, added Blog Skill section, added Research-Last30Days Skill section

### Deviations from Plan

None.

### Issues Encountered

None. All copy operations succeeded. Skills were confirmed active in the system skills list immediately after installation.
