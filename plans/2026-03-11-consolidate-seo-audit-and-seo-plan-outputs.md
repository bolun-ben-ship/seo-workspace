# Plan: Consolidate seo-audit and seo-plan to Single-File Output

**Created:** 2026-03-11
**Status:** Implemented
**Request:** Modify the seo-audit and seo-plan skills so each outputs exactly 1 markdown file instead of multiple separate files.

---

## Overview

### What This Plan Accomplishes

The `seo-audit` skill currently instructs Claude to write 2 output files (`FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md`). The `seo-plan` skill instructs Claude to write 5 output files (`SEO-STRATEGY.md`, `COMPETITOR-ANALYSIS.md`, `CONTENT-CALENDAR.md`, `IMPLEMENTATION-ROADMAP.md`, `SITE-STRUCTURE.md`). Both skills will be updated so each produces exactly 1 consolidated markdown file per run, with all sections merged in sequence within that single file.

### Why This Matters

Multiple output files create cleanup work after every run — as demonstrated in this session when 6 separate seo-plan files and 2 separate seo-audit files had to be manually merged into 3 consolidated files. A single output file per skill is cleaner, easier to share with clients, avoids duplication across files, and matches the pattern already used by `seo-keywords` (which outputs one `KEYWORD-RESEARCH.md`).

---

## Current State

### Relevant Existing Structure

```
.claude/skills/
  seo-audit/SKILL.md       — outputs FULL-AUDIT-REPORT.md + ACTION-PLAN.md (2 files)
  seo-plan/SKILL.md        — outputs SEO-STRATEGY.md + COMPETITOR-ANALYSIS.md +
                             CONTENT-CALENDAR.md + IMPLEMENTATION-ROADMAP.md +
                             SITE-STRUCTURE.md (5 files)
  seo-keywords/SKILL.md    — outputs KEYWORD-RESEARCH.md (1 file — correct pattern)
```

### Gaps or Problems Being Addressed

- `seo-audit` produces 2 files; the action plan content should be a section inside the audit report
- `seo-plan` produces 5 files; all strategic content should be sections inside one implementation plan
- Post-run cleanup and manual consolidation is required after every skill invocation
- Multiple files scatter related information that belongs together in one document

---

## Proposed Changes

### Summary of Changes

- Update `seo-audit/SKILL.md`: change "Output Files" section to specify a single `AUDIT.md` file; merge the action plan as a final section within that file
- Update `seo-plan/SKILL.md`: change "Output" / "Deliverables" section to specify a single `IMPLEMENTATION-PLAN.md` file; define section order for all content previously split across 5 files

### New Files to Create

None.

### Files to Modify

| File Path | Changes |
|-----------|---------|
| `.claude/skills/seo-audit/SKILL.md` | Replace "Output Files" block — change from 2 files to 1 file (`AUDIT.md`); add merged section order |
| `.claude/skills/seo-plan/SKILL.md` | Replace "Output" / "Deliverables" block — change from 5 files to 1 file (`IMPLEMENTATION-PLAN.md`); define merged section order |

### Files to Delete

None.

---

## Design Decisions

### Key Decisions Made

1. **seo-audit output filename → `AUDIT.md`**: Matches the filename already used in the vpublish.com.sg cleanup (`outputs/seo/vpublish.com.sg/AUDIT.md`), establishing a consistent naming convention going forward.

2. **seo-plan output filename → `IMPLEMENTATION-PLAN.md`**: Matches the filename already used in the vpublish.com.sg cleanup (`outputs/seo/vpublish.com.sg/IMPLEMENTATION-PLAN.md`).

3. **Merge action plan as a section inside the audit**: The action plan is derivative of the audit findings — it belongs in the same document under a clearly labelled `## Action Plan` section at the end.

4. **Merge all 5 plan deliverables into one file in logical order**: Competitor analysis → site structure → content strategy → implementation roadmap → content calendar. This preserves all content without duplication.

5. **Screenshots directory (`screenshots/`) remains unchanged**: It is a media output, not a markdown file, so it stays as-is in seo-audit.

### Alternatives Considered

- **Keep multiple files, just rename**: Rejected — this doesn't solve the cleanup problem.
- **Create a separate "merge" step at the end of each skill**: Rejected — adds complexity; better to just define one file upfront.

### Open Questions

None — both filename conventions are already validated by the vpublish.com.sg session.

---

## Content Boundary Definitions (Zero-Overlap Rules)

Three overlap risks exist between `AUDIT.md` and `IMPLEMENTATION-PLAN.md`. The skill files must encode explicit rules to prevent duplication.

### Overlap Risk 1 — Action Plan vs Implementation Roadmap

**The risk:** Both `AUDIT.md` (Action Plan section) and `IMPLEMENTATION-PLAN.md` (Implementation Roadmap section) could produce near-identical fix lists.

**Resolution — hard boundary:**
- `AUDIT.md` → Action Plan = **tactical issue register**: each issue listed with severity (Critical/High/Medium/Low), specific fix, and estimated effort. Focused on what is broken NOW. No phasing, no strategy, no timeline beyond "fix within N days/weeks."
- `IMPLEMENTATION-PLAN.md` → Implementation Roadmap = **strategic execution schedule**: phases with grouped tasks, dependencies, resource requirements, and milestone targets. References the audit findings by name (`see AUDIT.md`) but does NOT re-list individual issues. Adds what the audit cannot: sequencing rationale, phasing logic, owner assignments, and KPI milestone targets.

**Instruction to add to each skill:** seo-audit must say "Action Plan is a tactical issue register — no strategy or phasing." seo-plan must say "Implementation Roadmap does not re-list audit issues — it references AUDIT.md and defines execution phases."

### Overlap Risk 2 — Dual Executive Summaries

**The risk:** Both files open with an Executive Summary. Without explicit scope, Claude may repeat audit findings in the plan's Executive Summary.

**Resolution — hard boundary:**
- `AUDIT.md` → Executive Summary = current state diagnosis: health score, business type detected, top 5 critical issues, top 5 quick wins. Backward-looking (what we found).
- `IMPLEMENTATION-PLAN.md` → Executive Summary = strategic opportunity framing: business type, target audience, key goals, top 3 growth opportunities, phased timeline overview. Forward-looking (what we will do). Must NOT restate the health score or issue list — instead, one sentence referencing AUDIT.md: "A full site audit (AUDIT.md) identified N critical issues; this plan defines how to address them."

### Overlap Risk 3 — E-E-A-T Appears in Both Files

**The risk:** `AUDIT.md` has "E-E-A-T assessment" under Content Quality (evaluates the site's own E-E-A-T signals). `IMPLEMENTATION-PLAN.md` has "E-E-A-T signal comparison" under Competitive Analysis (compares E-E-A-T across competitors).

**Resolution — hard boundary:**
- `AUDIT.md` → E-E-A-T = site-only assessment: does the site demonstrate Experience, Expertise, Authoritativeness, Trust? Score each signal, list what's missing.
- `IMPLEMENTATION-PLAN.md` → E-E-A-T = competitor benchmarking: how do competitors demonstrate E-E-A-T that the site does not? Outputs a gap table. Does NOT re-score the site's own signals (references AUDIT.md for that).

These three rules must be written into the skill files as explicit instructions, not left to inference.

---

## Step-by-Step Tasks

### Step 1: Update seo-audit/SKILL.md — Output Section

Replace the current "Output Files" section (lines 39–43) with a single-file output definition. Also update the "Report Structure" section header to clarify it describes sections within the single file. Add an "Action Plan" section to the report structure at the end.

**Current content to replace:**

```markdown
## Output Files

- `FULL-AUDIT-REPORT.md` — Comprehensive findings
- `ACTION-PLAN.md` — Prioritized recommendations (Critical → High → Medium → Low)
- `screenshots/` — Desktop + mobile captures (if Playwright available)
```

**New content:**

```markdown
## Output

Save everything to a single file:

```
outputs/seo/<domain>/AUDIT.md
```

Optional: `screenshots/` directory for desktop + mobile captures (if Playwright available).

## Report Structure

All sections below are written into the single `AUDIT.md` file in this order:
```

Then at the end of the Report Structure section (after "AI Search Readiness"), add:

```markdown
### Action Plan
- Tactical issue register only — no strategy, no phasing, no timeline beyond "fix within N days/weeks"
- Prioritized issue list: Critical → High → Medium → Low
- Each issue: description, severity, specific fix, estimated effort
- Quick wins called out separately

> **Scope boundary:** The Action Plan lists WHAT is broken and HOW to fix each item. It does NOT define execution phases, resource allocation, or strategic sequencing — that is the role of IMPLEMENTATION-PLAN.md.
```

Also add a boundary note to the Executive Summary subsection in the Report Structure:

```markdown
### Executive Summary
- Overall SEO Health Score (0-100)
- Business type detected
- Top 5 critical issues
- Top 5 quick wins

> **Scope boundary:** This summary is a current-state diagnosis only (backward-looking). It does NOT include strategic opportunities, phasing, or KPIs — those belong in IMPLEMENTATION-PLAN.md.
```

Also add a boundary note to the Content Quality subsection:

```markdown
### Content Quality
- E-E-A-T assessment — site-only evaluation: does this site demonstrate Experience, Expertise, Authoritativeness, Trust? Score each signal, list gaps.
- Note: competitor E-E-A-T benchmarking belongs in IMPLEMENTATION-PLAN.md, not here.
- Thin content pages
- Duplicate content issues
- Readability scores
```

**Actions:**
- Read `.claude/skills/seo-audit/SKILL.md`
- Edit the "Output Files" section to the single-file format above
- Edit the "Report Structure" header line to clarify all sections go into `AUDIT.md`
- Add scope boundary note to Executive Summary subsection
- Add E-E-A-T scope note to Content Quality subsection
- Add "Action Plan" as the final subsection in the Report Structure with scope boundary note

**Files affected:**
- `.claude/skills/seo-audit/SKILL.md`

---

### Step 2: Update seo-plan/SKILL.md — Output Section

Replace the current "Output" / "Deliverables" section (lines 84–106) with a single-file output definition. Define the merged section order clearly so Claude knows exactly what to write and in what sequence.

**Current content to replace:**

```markdown
## Output

### Deliverables
- `SEO-STRATEGY.md` — Complete strategic plan
- `COMPETITOR-ANALYSIS.md` — Competitive insights
- `CONTENT-CALENDAR.md` — Content roadmap
- `IMPLEMENTATION-ROADMAP.md` — Phased action plan
- `SITE-STRUCTURE.md` — URL hierarchy and architecture

### KPI Targets
| Metric | Baseline | 3 Month | 6 Month | 12 Month |
|--------|----------|---------|---------|----------|
| Organic Traffic | ... | ... | ... | ... |
| Keyword Rankings | ... | ... | ... | ... |
| Domain Authority | ... | ... | ... | ... |
| Indexed Pages | ... | ... | ... | ... |
| Core Web Vitals | ... | ... | ... | ... |

### Success Criteria
- Clear, measurable goals per phase
- Resource requirements defined
- Dependencies identified
- Risk mitigation strategies
```

**New content:**

```markdown
## Output

Save everything to a single file:

```
outputs/seo/<domain>/IMPLEMENTATION-PLAN.md
```

## Report Structure

All sections below are written into the single `IMPLEMENTATION-PLAN.md` file in this order:

### Executive Summary
- One sentence referencing the audit: "A full site audit (AUDIT.md) identified N critical issues; this plan defines how to address them." Do NOT restate the health score or issue list.
- Business type, target audience, key goals
- Top 3 growth opportunities (forward-looking, not audit issues)
- Phased timeline overview

> **Scope boundary:** This summary is forward-looking (what we will do). It does NOT restate audit findings, health scores, or issue lists — those live in AUDIT.md.

### Competitive Analysis
- Top 5 competitors with keyword and content strategy summary
- Content gaps vs competitors
- E-E-A-T signal comparison — competitor benchmarking only: how do competitors demonstrate E-E-A-T that the site does not? Output a gap table. Do NOT re-score the site's own E-E-A-T signals — reference AUDIT.md for that.

### Site Structure
- URL hierarchy and content pillars
- Internal linking strategy
- Sitemap outline with quality gates

### Content Strategy
- Page types and estimated counts
- Blog/resource topics and publishing cadence
- E-E-A-T building plan (author bios, credentials, experience signals)

### Implementation Roadmap
- References AUDIT.md findings by name but does NOT re-list individual issues
- Groups tasks by phase with sequencing rationale, dependencies, resource requirements
- Phase 1 — Foundation (weeks 1-4): tasks, owners, success metrics
- Phase 2 — Expansion (weeks 5-12): tasks, owners, success metrics
- Phase 3 — Scale (months 4-6): tasks, owners, success metrics
- Phase 4 — Authority (months 7-12): tasks, owners, success metrics

> **Scope boundary:** This roadmap defines WHEN and HOW to execute, in phases. It does NOT re-list what is broken (that is the Action Plan in AUDIT.md). Reference the audit for the issue list; this section adds sequencing, phasing logic, and milestone targets.

### KPI Targets
| Metric | Baseline | 3 Month | 6 Month | 12 Month |
|--------|----------|---------|---------|----------|
| Organic Traffic | ... | ... | ... | ... |
| Keyword Rankings | ... | ... | ... | ... |
| Domain Authority | ... | ... | ... | ... |
| Indexed Pages | ... | ... | ... | ... |
| Core Web Vitals | ... | ... | ... | ... |

### Content Calendar
- Monthly publishing plan with topics, target keywords, and content types
- Seasonal and event-based content opportunities
```

**Actions:**
- Read `.claude/skills/seo-plan/SKILL.md`
- Replace the entire "Output" section (from `## Output` to end of file) with the new single-file format above, including all scope boundary notes

**Files affected:**
- `.claude/skills/seo-plan/SKILL.md`

---

### Step 3: Validate Both Files

Re-read both modified skill files and verify:
- Each specifies exactly 1 output markdown file
- The output path pattern is `outputs/seo/<domain>/<filename>.md`
- All content previously split across multiple files is accounted for in the merged section structure
- No references to old multi-file output names remain (`FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`, `SEO-STRATEGY.md`, `COMPETITOR-ANALYSIS.md`, `CONTENT-CALENDAR.md`, `IMPLEMENTATION-ROADMAP.md`, `SITE-STRUCTURE.md`)

**Actions:**
- Read `.claude/skills/seo-audit/SKILL.md` — confirm single output, no old filenames
- Read `.claude/skills/seo-plan/SKILL.md` — confirm single output, no old filenames

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` — does not list specific output filenames for these skills, no update needed
- `.claude/skills/seo/SKILL.md` — the SEO orchestrator routes to these skills; does not specify output filenames, no update needed

### Updates Needed for Consistency

None required — `CLAUDE.md` and the SEO orchestrator describe skill capabilities, not output filenames.

### Impact on Existing Workflows

Future runs of `/seo audit <url>` will produce `outputs/seo/<domain>/AUDIT.md` only.
Future runs of `/seo plan <type>` will produce `outputs/seo/<domain>/IMPLEMENTATION-PLAN.md` only.
The `seo-keywords` skill already produces `KEYWORD-RESEARCH.md` only — no change needed there.
All three output files then form the clean 3-file pattern: `AUDIT.md` + `IMPLEMENTATION-PLAN.md` + `KEYWORD-RESEARCH.md`.

---

## Validation Checklist

### Single-file output
- [ ] `seo-audit/SKILL.md` "Output Files" section replaced with single-file format (`AUDIT.md`)
- [ ] `seo-audit/SKILL.md` references no old filenames (`FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`)
- [ ] `seo-audit/SKILL.md` Report Structure includes "Action Plan" as final section
- [ ] `seo-plan/SKILL.md` "Output" section replaced with single-file format (`IMPLEMENTATION-PLAN.md`)
- [ ] `seo-plan/SKILL.md` references no old filenames (`SEO-STRATEGY.md`, `COMPETITOR-ANALYSIS.md`, `CONTENT-CALENDAR.md`, `IMPLEMENTATION-ROADMAP.md`, `SITE-STRUCTURE.md`)
- [ ] `seo-plan/SKILL.md` Report Structure covers all content previously in 5 separate files
- [ ] Both output path patterns use `outputs/seo/<domain>/` convention

### Zero-overlap enforcement
- [ ] `AUDIT.md` Action Plan section includes scope boundary note: tactical issue register only, no phasing
- [ ] `AUDIT.md` Executive Summary section includes scope boundary note: backward-looking diagnosis only
- [ ] `AUDIT.md` Content Quality / E-E-A-T note says: site-only evaluation, competitor E-E-A-T goes in IMPLEMENTATION-PLAN.md
- [ ] `IMPLEMENTATION-PLAN.md` Executive Summary includes reference to AUDIT.md and does not restate health score or issue list
- [ ] `IMPLEMENTATION-PLAN.md` Competitive Analysis / E-E-A-T note says: competitor benchmarking only, references AUDIT.md for site-level E-E-A-T scores
- [ ] `IMPLEMENTATION-PLAN.md` Implementation Roadmap includes scope boundary note: references AUDIT.md for issue list, does not re-list individual issues

---

## Success Criteria

1. Running `/seo audit <url>` produces exactly 1 markdown file: `outputs/seo/<domain>/AUDIT.md`
2. Running `/seo plan <type>` produces exactly 1 markdown file: `outputs/seo/<domain>/IMPLEMENTATION-PLAN.md`
3. No manual file consolidation or cleanup required after either skill runs

---

## Notes

- The `seo-keywords` skill is already compliant (outputs 1 file: `KEYWORD-RESEARCH.md`) and needs no changes.
- The 3-file pattern (`AUDIT.md`, `IMPLEMENTATION-PLAN.md`, `KEYWORD-RESEARCH.md`) is now validated by the vpublish.com.sg session and should be treated as the standard for all future SEO client outputs.
- If a future skill (e.g., `seo-competitor-pages`) also outputs multiple files, apply the same consolidation pattern.

---

## Implementation Notes

**Implemented:** 2026-03-11

### Summary

- Updated `seo-audit/SKILL.md`: replaced 2-file output (`FULL-AUDIT-REPORT.md` + `ACTION-PLAN.md`) with single `outputs/seo/<domain>/AUDIT.md`; added scope boundary notes to Executive Summary and Content Quality sections; added Action Plan as final Report Structure section with tactical scope boundary
- Updated `seo-plan/SKILL.md`: replaced 5-file output (`SEO-STRATEGY.md`, `COMPETITOR-ANALYSIS.md`, `CONTENT-CALENDAR.md`, `IMPLEMENTATION-ROADMAP.md`, `SITE-STRUCTURE.md`) with single `outputs/seo/<domain>/IMPLEMENTATION-PLAN.md`; added all section definitions with scope boundary notes on Executive Summary, E-E-A-T, and Implementation Roadmap
- Both skills now cross-reference each other by name to enforce content boundaries

### Deviations from Plan

None.

### Issues Encountered

None.
