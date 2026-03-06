# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

This is a **Claude Workspace Template** — a structured environment designed for working with Claude Code as a powerful agent assistant across sessions. The user will spin up fresh Claude Code sessions repeatedly, using `/prime` at the start of each to load essential context without bloat.

**This file (CLAUDE.md) is the foundation.** It is automatically loaded at the start of every session. Keep it current — it is the single source of truth for how Claude should understand and operate within this workspace.

---

## The Claude-User Relationship

Claude operates as an **agent assistant** with access to the workspace folders, context files, commands, and outputs. The relationship is:

- **User**: Defines goals, provides context about their role/function, and directs work through commands
- **Claude**: Reads context, understands the user's objectives, executes commands, produces outputs, and maintains workspace consistency

Claude should always orient itself through `/prime` at session start, then act with full awareness of who the user is, what they're trying to achieve, and how this workspace supports that.

---

## Workspace Structure

```
.
├── CLAUDE.md              # This file — core context, always loaded
├── .claude/
│   ├── commands/          # Slash commands Claude can execute
│   │   ├── prime.md       # /prime — session initialization
│   │   ├── create-plan.md # /create-plan — create implementation plans
│   │   └── implement.md   # /implement — execute plans
│   ├── skills/            # Claude Code skills
│   │   ├── mcp-integration/   # MCP server integration guide
│   │   ├── skill-creator/     # Skill creation guide
│   │   ├── seo/               # SEO orchestrator (main entry point)
│   │   │   ├── SKILL.md       # Routes to sub-skills, scoring, quality gates
│   │   │   └── references/    # CWV thresholds, E-E-A-T, schema types, quality gates
│   │   ├── seo-audit/         # Full site audit
│   │   ├── seo-page/          # Single page analysis
│   │   ├── seo-technical/     # Technical SEO (8 categories)
│   │   ├── seo-content/       # E-E-A-T content quality
│   │   ├── seo-schema/        # Schema markup detection/validation/generation
│   │   ├── seo-images/        # Image optimization
│   │   ├── seo-sitemap/       # Sitemap analysis/generation
│   │   ├── seo-geo/           # AI Overviews / GEO optimization
│   │   ├── seo-plan/          # Strategic SEO planning (+ industry templates)
│   │   ├── seo-programmatic/  # Programmatic SEO
│   │   ├── seo-competitor-pages/ # Competitor comparison pages
│   │   ├── seo-hreflang/      # Hreflang/i18n SEO
│   │   ├── frontend-design/   # Distinctive, production-grade UI generation
│   │   ├── blog/              # Blog orchestrator (12 commands, 12 templates, 12 references)
│   │   ├── blog-write/        # Write new blog posts from scratch
│   │   ├── blog-rewrite/      # Optimize existing posts
│   │   ├── blog-analyze/      # 100-point quality scoring
│   │   ├── blog-brief/        # Content brief generation
│   │   ├── blog-calendar/     # Editorial calendar planning
│   │   ├── blog-strategy/     # Blog strategy and topic ideation
│   │   ├── blog-outline/      # SERP-informed content outlines
│   │   ├── blog-seo-check/    # Post-writing SEO validation
│   │   ├── blog-schema/       # JSON-LD schema generation
│   │   ├── blog-repurpose/    # Cross-platform content repurposing
│   │   ├── blog-geo/          # AI citation readiness audit
│   │   ├── blog-audit/        # Full-site blog health assessment
│   │   ├── blog-chart/        # Internal SVG chart generation
│   │   └── research-last30days/ # Multi-source trend research (Reddit, X, YouTube, TikTok, HN, Polymarket)
│   └── agents/            # Subagent configs for parallel audits
│       ├── seo-technical.md
│       ├── seo-content.md
│       ├── seo-schema.md
│       ├── seo-sitemap.md
│       ├── seo-performance.md
│       ├── seo-visual.md
│       ├── blog-researcher.md
│       ├── blog-writer.md
│       ├── blog-seo.md
│       └── blog-reviewer.md
├── context/               # Background context about the user and project
├── plans/                 # Implementation plans created by /create-plan
├── outputs/               # Work products and deliverables
├── reference/             # Templates, examples, reusable patterns
│   └── seo/               # SEO docs, schema templates, requirements.txt
├── scripts/               # Automation scripts
│   └── seo/               # SEO Python scripts (fetch, parse, screenshot, analyze)
│       └── hooks/         # Schema validation hook, pre-commit SEO check
└── shell-aliases.md       # Shell aliases for quick session start
```

**Key directories:**

| Directory             | Purpose                                                                             |
| --------------------- | ----------------------------------------------------------------------------------- |
| `context/`            | Who the user is, their role, current priorities, strategies. Read by `/prime`.      |
| `plans/`              | Detailed implementation plans. Created by `/create-plan`, executed by `/implement`. |
| `outputs/`            | Deliverables, analyses, reports, and work products.                                 |
| `reference/`          | Helpful docs, templates and patterns to assist in various workflows.                |
| `reference/seo/`      | SEO documentation, schema templates, and Python requirements.                       |
| `scripts/`            | Any automation or tooling scripts.                                                  |
| `scripts/seo/`        | SEO Python scripts: page fetching, HTML parsing, screenshots, visual analysis.      |
| `.claude/skills/seo*`                  | SEO skill suite: 1 orchestrator + 12 sub-skills.                                    |
| `.claude/skills/frontend-design/`      | Frontend design skill — triggers on UI/frontend build requests.                     |
| `.claude/skills/blog/`                 | Blog orchestrator — routes 12 commands, holds references and templates.             |
| `.claude/skills/blog-*/`               | 13 blog sub-skills for writing, analysis, SEO, schema, repurposing.                 |
| `.claude/skills/research-last30days/`  | Multi-source trend research skill + bundled Python scripts.                         |
| `.claude/agents/`                      | Subagent configs for SEO audits (6) and blog production (4).                        |

---

## Commands

### /prime

**Purpose:** Initialize a new session with full context awareness.

Run this at the start of every session. Claude will:

1. Read CLAUDE.md and context files
2. Summarize understanding of the user, workspace, and goals
3. Confirm readiness to assist

### /create-plan [request]

**Purpose:** Create a detailed implementation plan before making changes.

Use when adding new functionality, commands, scripts, or making structural changes. Produces a thorough plan document in `plans/` that captures context, rationale, and step-by-step tasks.

Example: `/create-plan add a competitor analysis command`

### /implement [plan-path]

**Purpose:** Execute a plan created by /create-plan.

Reads the plan, executes each step in order, validates the work, and updates the plan status.

Example: `/implement plans/2026-01-28-competitor-analysis-command.md`

---

## SEO Skills

This workspace includes a comprehensive **Claude SEO** skill suite (13 skills, 6 subagents) for full-spectrum SEO analysis. The main orchestrator is at `.claude/skills/seo/SKILL.md`.

### SEO Commands

| Command                       | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| `/seo audit <url>`            | Full website audit with parallel subagent delegation               |
| `/seo page <url>`             | Deep single-page analysis                                          |
| `/seo technical <url>`        | Technical SEO audit (8 categories)                                 |
| `/seo content <url>`          | E-E-A-T and content quality analysis                               |
| `/seo schema <url>`           | Schema markup detection, validation, and generation                |
| `/seo images <url>`           | Image optimization analysis                                        |
| `/seo sitemap <url>`          | Analyze existing XML sitemap                                       |
| `/seo sitemap generate`       | Generate new sitemap with industry templates                       |
| `/seo geo <url>`              | AI Overviews / Generative Engine Optimization                      |
| `/seo plan <type>`            | Strategic SEO planning (saas, local, ecommerce, publisher, agency) |
| `/seo programmatic <url>`     | Programmatic SEO analysis and planning                             |
| `/seo competitor-pages <url>` | Competitor comparison page generation                              |
| `/seo hreflang <url>`         | Hreflang/i18n SEO audit and generation                             |

### SEO Architecture

- **Orchestrator** (`seo/SKILL.md`): Routes commands, detects industry type, spawns subagents for full audits
- **Sub-skills** (`seo-*/SKILL.md`): 12 specialized skills loaded on-demand
- **Subagents** (`.claude/agents/seo-*.md`): 6 parallel workers for audit delegation (technical, content, schema, sitemap, performance, visual)
- **Reference files** (`seo/references/`): CWV thresholds, E-E-A-T framework, schema types, quality gates — loaded on-demand
- **Scripts** (`scripts/seo/`): Python utilities for page fetching, HTML parsing, screenshots, visual analysis
- **Hooks** (`scripts/seo/hooks/`): Schema validation hook, pre-commit SEO check

### Python Dependencies

SEO scripts require Python 3.8+ with dependencies listed in `reference/seo/requirements.txt`:

```bash
pip install -r reference/seo/requirements.txt
```

Optional: Install Playwright for screenshot capabilities: `pip install playwright && playwright install chromium`

---

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

---

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

Install if using `blog analyze` for advanced scoring:

```bash
pip install beautifulsoup4 textstat language-tool-python lxml
```

---

## Research-Last30Days Skill

This workspace includes the **research-last30days** skill for researching any topic across multiple social and web platforms from the last 30 days. The skill is at `.claude/skills/research-last30days/SKILL.md`.

### What It Does

Researches ANY topic across Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, and the web. Filters to the last 30 days. Surfaces what people are actually discussing, recommending, betting on, and debating right now. Produces a structured report and copy-paste-ready prompts.

### How to Use

The skill is user-invocable — type the skill name followed by a topic:

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

---

## Critical Instruction: Maintain This File

**Whenever Claude makes changes to the workspace, Claude MUST consider whether CLAUDE.md needs updating.**

After any change — adding commands, scripts, workflows, or modifying structure — ask:

1. Does this change add new functionality users need to know about?
2. Does it modify the workspace structure documented above?
3. Should a new command be listed?
4. Does context/ need new files to capture this?

If yes to any, update the relevant sections. This file must always reflect the current state of the workspace so future sessions have accurate context.

**Examples of changes requiring CLAUDE.md updates:**

- Adding a new slash command → add to Commands section
- Creating a new output type → document in Workspace Structure or create a section
- Adding a script → document its purpose and usage
- Changing workflow patterns → update relevant documentation

---

## For Users Downloading This Template

To customize this workspace to your own needs, fill in your context documents in `context/` and modify as needed. Then use `/create-plan` to plan out and `/implement` to execute any structural changes. This ensures everything stays in sync — especially CLAUDE.md, which must always reflect the current state of the workspace.

---

## Session Workflow

1. **Start**: Run `/prime` to load context
2. **Work**: Use commands or direct Claude with tasks
3. **Plan changes**: Use `/create-plan` before significant additions
4. **Execute**: Use `/implement` to execute plans
5. **Maintain**: Claude updates CLAUDE.md and context/ as the workspace evolves

---

## Notes

- Keep context minimal but sufficient — avoid bloat
- Plans live in `plans/` with dated filenames for history
- Outputs are organized by type/purpose in `outputs/`
- Reference materials go in `reference/` for reuse
