# Plan: Install seo-keywords Skill

**Created:** 2026-03-06
**Status:** Implemented
**Request:** Install the seo-keywords skill from Bolun-boop/aexphl-claude-workspace into this workspace and wire it into the SEO orchestrator and CLAUDE.md

---

## Overview

### What This Plan Accomplishes

Installs the `seo-keywords` skill (2 files) into `.claude/skills/seo-keywords/`, adds proper YAML frontmatter matching workspace conventions, registers the new `/seo keywords` command in the SEO orchestrator's routing table, and updates CLAUDE.md to document the new skill.

### Why This Matters

Keyword research is a critical SEO workflow gap — the existing suite covers audits, technical checks, content, schema, and GEO, but has no dedicated keyword research output. This skill fills that gap with structured keyword tables (primary targets, long-tail, PAA, AI search queries) and outputs to `outputs/seo/<domain>/KEYWORD-RESEARCH.md`.

---

## Current State

### Relevant Existing Structure

```
.claude/skills/
  seo/SKILL.md                    ← orchestrator — routes all /seo commands
  seo-audit/SKILL.md
  seo-technical/SKILL.md
  seo-content/SKILL.md
  seo-schema/SKILL.md
  seo-images/SKILL.md
  seo-sitemap/SKILL.md
  seo-geo/SKILL.md
  seo-plan/SKILL.md
  seo-programmatic/SKILL.md
  seo-competitor-pages/SKILL.md
  seo-hreflang/SKILL.md
  seo-page/SKILL.md
  seo/references/                 ← reference files loaded on-demand
CLAUDE.md                         ← documents all skills and commands
```

Each sub-skill follows this pattern:
- YAML frontmatter block (`---`) with `name:` and `description:` fields
- Main skill content below the frontmatter
- Optional `references/` subdirectory for on-demand reference files

### Gaps or Problems Being Addressed

- No `/seo keywords` command exists in the workspace
- `seo/SKILL.md` Quick Reference table has no keyword research row
- CLAUDE.md SEO Skills table has no keyword research entry
- The skill from the source repo has no YAML frontmatter — needs to be added before install

---

## Proposed Changes

### Summary of Changes

- Create `.claude/skills/seo-keywords/SKILL.md` with proper frontmatter + full skill content
- Create `.claude/skills/seo-keywords/references/keyword-methodology.md` with full reference content
- Edit `.claude/skills/seo/SKILL.md` — add `/seo keywords <url>` row to Quick Reference table
- Edit `CLAUDE.md` — add `seo-keywords` to SEO commands table and architecture section

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `.claude/skills/seo-keywords/SKILL.md` | Main skill — keyword research process, 4 keyword tables, output spec |
| `.claude/skills/seo-keywords/references/keyword-methodology.md` | Reference — intent classification, difficulty estimation, volume tiers, AI query patterns, gap signals |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `.claude/skills/seo/SKILL.md` | Add `/seo keywords <url>` row to Quick Reference table |
| `CLAUDE.md` | Add `seo-keywords` row to SEO commands table; mention in architecture section |

### Files to Delete (if any)

None.

---

## Design Decisions

### Key Decisions Made

1. **Add YAML frontmatter to SKILL.md**: The source repo's SKILL.md has no frontmatter. All skills in this workspace have `name:` and `description:` frontmatter. Adding it ensures the skill is discoverable and matches workspace conventions.

2. **Keep reference file in `references/` subdirectory**: Matches the pattern used by `seo/references/` — reference files are loaded on-demand rather than at startup, keeping context lean.

3. **Command syntax `/seo keywords <url>`**: Consistent with all other `/seo <subcommand> <url>` patterns in the orchestrator.

4. **Output path `outputs/seo/<domain>/KEYWORD-RESEARCH.md`**: Already specified in the skill itself; consistent with existing outputs like `AUDIT-FINDINGS.md` and `STRATEGY.md`.

### Alternatives Considered

- **Installing without frontmatter**: Rejected — would be inconsistent with all other skills and reduce discoverability.
- **Placing methodology content inline in SKILL.md**: Rejected — the skill already references `references/keyword-methodology.md` by name; splitting keeps the main skill file readable and matches the workspace's on-demand loading pattern.

### Open Questions (if any)

None — all decisions can be made from existing patterns.

---

## Step-by-Step Tasks

### Step 1: Create `.claude/skills/seo-keywords/SKILL.md`

Create the skill file with YAML frontmatter added above the existing content from the source repo.

**Actions:**

- Create the file at `.claude/skills/seo-keywords/SKILL.md`
- Add YAML frontmatter block matching workspace convention (name, description, allowed-tools)
- Paste full skill content below the frontmatter

**Full file content:**

```markdown
---
name: seo-keywords
description: >
  Keyword research and gap analysis for any website. Generates four structured
  keyword tables: primary targets, long-tail (transactional + informational),
  People Also Ask questions, and AI search (GEO) queries. Analyzes competitor
  keyword gaps and outputs to KEYWORD-RESEARCH.md. Use when user says "keyword
  research", "keyword gap", "keywords", "what keywords", "PAA", "long-tail
  keywords", or "AI search queries".
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - WebSearch
---

# SEO Keywords — Keyword Research & Gap Analysis

## Process

### Step 0: Load Existing Outputs

Check for prior work — do NOT re-derive what already exists:

- `outputs/seo/<domain>/FULL-AUDIT-REPORT.md` or `AUDIT-FINDINGS.md`
  - Extract: detected business type, thin content pages, on-page SEO findings, current keyword usage, content gaps
- `outputs/seo/<domain>/SEO-STRATEGY.md` or `STRATEGY.md`
  - Extract: target audience, competitor list, content pillars, keyword gaps already identified

If no audit exists, proceed without it but note the gap and recommend running `/seo audit <url>` afterward.

### Step 1: Analyze the Website

Use `scripts/seo/fetch_page.py` to fetch the homepage and up to 10 key pages (services, products, about, blog).

Extract:
- Current page titles, H1s, meta descriptions — what keywords the site already targets
- Content themes and topic clusters present
- Business type (cross-check or detect): SaaS / local / ecommerce / publisher / agency
- Missing topic areas obvious from the site's own positioning
- Internal link anchor text patterns

### Step 2: Competitor Research

Identify top 5 competitors (use audit output if available; otherwise infer from industry + location signals).

For each competitor, fetch their homepage and key pages. Extract:
- Keywords they prominently target (titles, H1s, headings)
- Topic clusters they cover that the subject site does not
- Content types present (blog, FAQs, case studies, location pages)
- Schema types implemented
- AI-citability signals (structured Q&A, definitions, statistics)

Build a **gap map**: topics/keywords competitors rank for that the subject site does not cover.

### Step 3: Keyword Generation

Using the website analysis + competitor gap map, generate keywords across all four categories below. Use WebSearch to validate current search trends and verify estimated volumes.

**Search intent classification:**
- `[T]` Transactional — user ready to buy / sign up / contact
- `[I]` Informational — user researching, learning
- `[N]` Navigational — branded / direct

**Volume estimation tiers** (use when live data unavailable):
| Tier | Monthly Searches |
|------|-----------------|
| High | 10,000+ |
| Medium | 1,000–9,999 |
| Low | 100–999 |
| Niche | <100 |

See `references/keyword-methodology.md` for intent signals, difficulty estimation, and AI keyword patterns.

### Step 4: Build the Four Keyword Tables

Deduplicate across all four tables before finalizing — no keyword should appear in more than one table.

Rank each table by **Priority Score** = combination of:
1. Search volume (higher = better)
2. Keyword difficulty (lower = better opportunity)
3. Strategic fit (aligns with business goals or fills a clear gap)
4. Competitive advantage (underserved by competitors)

#### Table 1: Primary Keyword Targets

Broad-to-mid keyword targets the site should pursue as core pages or content pillars.

| Priority | Keyword | Intent | Est. Volume | Difficulty | Rationale | Why It Will Work |
|----------|---------|--------|-------------|------------|-----------|-----------------|
| 1 | ... | [T/I/N] | High/Med/Low | High/Med/Low | Gap vs competitors / missing from site / differentiator | ... |

**Rationale column must include one of:**
- "Competitor gap" — top competitors rank for this, subject site does not
- "Missing from site" — clearly relevant to the business but absent from current content
- "Differentiator" — unique angle the site has that competitors don't exploit
- "High intent, low competition" — volume opportunity with weak incumbent results

#### Table 2: Long-Tail Keywords

Specific, lower-volume, higher-conversion-rate phrases. Split into two sections.

**Transactional (buy / hire / book / sign up intent):**

| Priority | Keyword | Est. Volume | Difficulty | Rationale |
|----------|---------|-------------|------------|-----------|

**Informational (learn / how / what / why intent):**

| Priority | Keyword | Est. Volume | Difficulty | Rationale |
|----------|---------|-------------|------------|-----------|

#### Table 3: People Also Ask (PAA) Questions

Questions that appear in Google's PAA boxes for the site's primary topic area. These drive featured snippets and answer-box placements.

| Priority | Question | Parent Topic | Est. PAA Frequency | Content Format to Target |
|----------|----------|-------------|-------------------|--------------------------|
| 1 | "How do I...?" | [topic] | High/Med/Low | Definition / Step-by-step / Comparison |

Content format guidance:
- **Definition** — 40-60 word direct answer paragraph
- **Step-by-step** — numbered list, 3-7 steps
- **Comparison** — pros/cons table or side-by-side
- **List** — bullet list of items/options

#### Table 4: AI Search (GEO) Keywords

Queries optimized for AI Overview inclusion, ChatGPT web search, and Perplexity citations. These differ from traditional keywords — they are question-first, entity-dense, and favor structured factual content.

| Priority | Query Phrase | AI Platform Target | Query Type | Citability Strategy |
|----------|-------------|-------------------|------------|---------------------|
| 1 | "What is the best...?" | AI Overviews / Perplexity / ChatGPT | Comparison / Definition / How-to | Add FAQ schema / Add statistics / Use definition format |

Query types:
- **Comparison** — "X vs Y", "best X for Y" — target with structured comparison content
- **Definition** — "What is X" — target with clear, quotable definitions
- **How-to** — "How to X" — target with step-by-step structured content
- **Recommendation** — "Best X" — target with ranked lists and supporting evidence

### Step 5: Output

Save to `outputs/seo/<domain>/KEYWORD-RESEARCH.md`.

## Output Structure

```
outputs/seo/<domain>/KEYWORD-RESEARCH.md
```

### Report Sections

1. **Executive Summary** — business type, total keywords identified, top 3 opportunities, sources used (audit / plan / live analysis)
2. **Competitive Landscape** — brief summary of competitor keyword strategies and the most significant gaps found
3. **Table 1: Primary Keyword Targets** — core pages and pillars to build or optimize
4. **Table 2: Long-Tail Keywords** — transactional and informational split
5. **Table 3: People Also Ask** — question targets for featured snippets
6. **Table 4: AI Search Keywords** — GEO-optimized query targets
7. **Implementation Notes** — which keywords map to existing pages (optimize) vs. need new pages (create), and quick-win recommendations

## Quality Rules

- Tables must be deduplicated across all four — scan for overlap before finalizing
- Every keyword in Table 1 must have a filled Rationale and "Why It Will Work" column
- Minimum keyword counts: Table 1 = 15+, Table 2 = 20+ (10 per type), Table 3 = 10+, Table 4 = 10+
- Do not include branded competitor keywords (e.g., "[CompetitorName] alternative" belongs in seo-competitor-pages, not here)
- Volume estimates must use the tier system if live data is unavailable — never leave blank
- AI keywords (Table 4) must be phrased as natural language queries, not keyword fragments

## Reference

See `references/keyword-methodology.md` for:
- Detailed search intent classification signals
- Keyword difficulty estimation methodology
- AI search query pattern library
- Volume estimation cross-reference guide
```

**Files affected:**

- `.claude/skills/seo-keywords/SKILL.md`

---

### Step 2: Create `.claude/skills/seo-keywords/references/keyword-methodology.md`

Create the reference file with the full content from the source repo.

**Actions:**

- Create the file at `.claude/skills/seo-keywords/references/keyword-methodology.md`
- Paste full content as retrieved from source repo (no modifications needed)

**Full file content:**

```markdown
# Keyword Research Methodology

## Table of Contents
1. [Search Intent Classification](#search-intent-classification)
2. [Keyword Difficulty Estimation](#keyword-difficulty-estimation)
3. [Volume Estimation Guide](#volume-estimation-guide)
4. [AI Search Query Patterns](#ai-search-query-patterns)
5. [Keyword Gap Analysis Signals](#keyword-gap-analysis-signals)

---

## Search Intent Classification

### Transactional [T] — Signals
User is ready to act. High commercial value.

**Trigger words:** buy, hire, get, book, schedule, quote, pricing, cost, sign up, try, demo, download, order, purchase, near me, best [X] for [Y]

**Examples:**
- "hire seo agency cape town"
- "buy standing desk online"
- "book yoga class johannesburg"
- "seo services pricing"

**Content to target:** Service pages, product pages, pricing pages, booking/contact pages

---

### Informational [I] — Signals
User is learning or researching. Lower immediate conversion but builds authority and feeds PAA/AI Overviews.

**Trigger words:** how, what, why, when, guide, tutorial, tips, examples, vs, difference between, is it worth, should I, best way to

**Examples:**
- "how to improve core web vitals"
- "what is e-e-a-t in seo"
- "difference between on-page and off-page seo"
- "is programmatic seo worth it"

**Content to target:** Blog posts, guides, FAQs, comparison articles, resource pages

---

### Navigational [N] — Signals
User knows where they want to go. Usually branded.

**Trigger words:** [brand name], [brand] login, [brand] pricing, [brand] contact

**Note:** Navigational keywords for competitors belong in seo-competitor-pages, not here.

---

## Keyword Difficulty Estimation

When live difficulty data (Ahrefs/SEMrush) is unavailable, estimate from SERP signals:

| Difficulty | SERP Signals |
|------------|-------------|
| **High** | Top 10 dominated by DA 60+ domains, exact-match rich results, major brands present (Forbes, Wikipedia, Healthline, etc.) |
| **Medium** | Mix of established and smaller sites in top 10, some listicles and blog posts ranking alongside big brands |
| **Low** | Smaller/niche sites ranking, some thin content in top 10, few or no exact-match domains |
| **Very Low** | Weak results in top 10, questions answered poorly, no dedicated pages targeting the phrase |

**Opportunity signal:** Low/Very Low difficulty + Medium/High volume = prioritize immediately

---

## Volume Estimation Guide

### Tier Definitions
| Tier | Monthly Searches | When to Use |
|------|-----------------|-------------|
| High | 10,000+ | Core industry terms, broad informational queries |
| Medium | 1,000–9,999 | Specific service/product terms, targeted informational |
| Low | 100–999 | Long-tail transactional, location-specific, niche queries |
| Niche | <100 | Hyper-specific, brand + modifier, very local |

### Volume Estimation Heuristics (no tool access)
- Broad 1-2 word industry terms (e.g., "seo agency") → High
- 3-4 word service terms with location (e.g., "seo agency cape town") → Medium/Low
- Question-format informational (e.g., "how to do keyword research") → Medium
- Specific long-tail transactional (e.g., "affordable seo for small law firms") → Low/Niche
- PAA-style questions → estimate based on whether the parent topic is High/Medium

---

## AI Search Query Patterns

AI Overviews, ChatGPT search, and Perplexity favor:

### Pattern 1: Comparison Queries
Structure: "Best [X] for [use case]" / "[X] vs [Y]"

Content strategy: Structured comparison with clear winner declarations, data-backed claims, pros/cons format

Examples:
- "best seo tools for small businesses"
- "wordpress vs webflow for seo"
- "local seo vs national seo"

### Pattern 2: Definition Queries
Structure: "What is [concept]" / "What does [term] mean"

Content strategy: Clear 1-2 sentence definition at page top, followed by elaboration. Use definition schema where appropriate.

Examples:
- "what is e-e-a-t"
- "what is keyword cannibalization"
- "what does domain authority mean"

### Pattern 3: How-To Queries
Structure: "How to [achieve outcome]" / "How do I [action]"

Content strategy: Numbered steps, each step with a clear action verb, total steps visible early, include time estimate

Examples:
- "how to do a technical seo audit"
- "how to fix crawl errors in google search console"
- "how to write a meta description"

### Pattern 4: Recommendation Queries
Structure: "What [tool/service/approach] should I use for [context]"

Content strategy: Direct recommendation with reasoning, followed by alternatives with context

Examples:
- "what seo tool should i use for a small budget"
- "what schema markup should a restaurant use"

### Citability Boosters for AI Platforms
- Include a direct, quotable answer in the first 100 words of the page
- Add statistics with source citations (AI platforms prefer cited data)
- Use FAQ sections with clear Q&A format
- Implement FAQ schema (for appropriate page types)
- Use HowTo schema where applicable
- Ensure AI crawlers are not blocked: check robots.txt for GPTBot, ClaudeBot, PerplexityBot

---

## Keyword Gap Analysis Signals

When analyzing competitors to find gaps for the subject site:

### High-Priority Gap Signals
1. Competitor has a dedicated page for a topic; subject site has nothing
2. Competitor targets keyword in H1/title; subject site only mentions it in passing
3. Multiple competitors cover a topic; subject site ignores it entirely
4. Topic is clearly in the site's wheelhouse but no content exists

### Medium-Priority Gap Signals
1. Subject site covers topic superficially; competitors have comprehensive guides
2. Subject site lacks the question-format version of a topic they cover declaratively
3. Subject site missing location-qualified versions of service keywords (for local businesses)

### Low-Priority Gap Signals
1. Competitor covers niche adjacent topic unlikely to convert
2. Gap exists but difficulty is High and site has Low/Med domain authority

### Differentiation Opportunities
Look for keywords where:
- Competitors rank but their content is outdated (>2 years old, pre-2024 AI search changes)
- Competitors rank with thin/low-quality content that could easily be outranked
- Subject site has unique credentials, data, or expertise no competitor can replicate
- Local market or niche where national competitors rank but local intent is underserved
```

**Files affected:**

- `.claude/skills/seo-keywords/references/keyword-methodology.md`

---

### Step 3: Update the SEO Orchestrator

Add `/seo keywords <url>` to the Quick Reference table in `.claude/skills/seo/SKILL.md`.

**Actions:**

- Read `.claude/skills/seo/SKILL.md`
- Add one row to the Quick Reference table after the `/seo hreflang` row:
  ```
  | `/seo keywords <url>` | Keyword research & gap analysis — 4 keyword tables + competitor gaps |
  ```

**Files affected:**

- `.claude/skills/seo/SKILL.md`

---

### Step 4: Update CLAUDE.md

Add `seo-keywords` to the SEO Skills section in `CLAUDE.md`.

**Actions:**

- Read `CLAUDE.md`
- In the **SEO Commands** table, add one row after the `/seo hreflang` row:
  ```
  | `/seo keywords <url>`         | Keyword research & gap analysis (primary, long-tail, PAA, AI search)   |
  ```
- In the **SEO Architecture** bullet list, update the sub-skills count from "12 specialized skills" to "13 specialized skills" and add `seo-keywords` to the Sub-skills description line

**Files affected:**

- `CLAUDE.md`

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` — lists all SEO commands; must reflect the new skill
- `.claude/skills/seo/SKILL.md` — orchestrator routing table; must include the new command

### Updates Needed for Consistency

- The orchestrator's description in its YAML frontmatter says "Orchestrates 12 specialized sub-skills" — update count to 13
- CLAUDE.md skill count reference (if present) should be updated to match

### Impact on Existing Workflows

- Adds a new `/seo keywords <url>` command — no existing commands are changed or removed
- The skill references `scripts/seo/fetch_page.py` which already exists in `scripts/seo/`
- Output goes to `outputs/seo/<domain>/KEYWORD-RESEARCH.md` — consistent with existing output naming

---

## Validation Checklist

- [ ] `.claude/skills/seo-keywords/SKILL.md` exists and has valid YAML frontmatter
- [ ] `.claude/skills/seo-keywords/references/keyword-methodology.md` exists
- [ ] `.claude/skills/seo/SKILL.md` Quick Reference table includes `/seo keywords <url>` row
- [ ] `CLAUDE.md` SEO Commands table includes `/seo keywords <url>` row
- [ ] No existing files were unintentionally modified
- [ ] Skill file references `references/keyword-methodology.md` correctly (relative path)

---

## Success Criteria

The implementation is complete when:

1. `/seo keywords <url>` is a recognized command in the orchestrator routing table
2. Both skill files exist at the correct paths with correct content
3. CLAUDE.md accurately documents the new skill in the commands table

---

## Notes

- The source skill references `WebSearch` in its process (Step 3) — the frontmatter `allowed-tools` list includes `WebSearch` to enable this
- The skill integrates cleanly with existing audit outputs: if `AUDIT-FINDINGS.md` or `STRATEGY.md` exist, Step 0 pulls from them to avoid re-deriving known facts
- Future enhancement: could add a `/seo keywords generate` variant (no URL, brief-only mode) for planning keyword strategy before a site is built

---

## Implementation Notes

**Implemented:** 2026-03-06

### Summary

- Created `.claude/skills/seo-keywords/SKILL.md` with YAML frontmatter and full skill content
- Created `.claude/skills/seo-keywords/references/keyword-methodology.md` with full reference content
- Added `/seo keywords <url>` row to Quick Reference table in `.claude/skills/seo/SKILL.md`
- Updated sub-skill count from 12 → 13 in orchestrator body text and frontmatter description
- Added `/seo keywords <url>` row to SEO Commands table in `CLAUDE.md`
- Updated sub-skill count from 12 → 13 in CLAUDE.md SEO Architecture section
- Updated total skill count from 13 → 14 in CLAUDE.md SEO Skills intro line
- Added `seo-keywords/` entry to workspace structure tree in CLAUDE.md

### Deviations from Plan

None.

### Issues Encountered

None.
