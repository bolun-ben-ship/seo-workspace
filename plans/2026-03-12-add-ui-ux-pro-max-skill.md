# Plan: Add UI/UX Pro Max Skill

**Created:** 2026-03-12
**Status:** Draft
**Request:** Add UI/UX Pro Max skill from https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

---

## Overview

### What This Plan Accomplishes

This plan integrates the UI/UX Pro Max skill suite into the workspace, adding comprehensive design intelligence with 67 UI styles, 161 color palettes, 57 font pairings, 161 product-type reasoning rules, 99 UX guidelines, and 25 chart types across 13 tech stacks. The skill includes an AI-powered Design System Generator that analyzes project requirements and generates complete, tailored design systems.

### Why This Matters

Currently, the workspace has a basic `frontend-design` skill that provides general guidance for creating distinctive UIs. The UI/UX Pro Max skill significantly enhances this capability by adding:

1. **Structured Design Intelligence**: Industry-specific reasoning rules that automatically recommend optimal design patterns, styles, colors, and typography based on product type
2. **Comprehensive Resources**: Extensive databases of styles, palettes, fonts, and UX best practices
3. **Multi-Stack Support**: Support for 13 technology stacks (React, Next.js, Vue, Nuxt, Svelte, SwiftUI, React Native, Flutter, HTML/Tailwind, shadcn/ui, Jetpack Compose, Astro, Nuxt UI)
4. **Design System Generation**: Automated reasoning engine that produces complete design systems with pattern recommendations, anti-patterns to avoid, and pre-delivery checklists
5. **Additional Skills**: Banner design, brand guidelines, slides design, and UI styling capabilities

This aligns with the workspace's mission to provide Claude with powerful, specialized capabilities for comprehensive project execution.

---

## Current State

### Relevant Existing Structure

```
.claude/skills/
├── frontend-design/
│   └── SKILL.md (basic distinctive UI generation guidance)
├── seo/ (14 SEO skills)
├── blog/ (13 blog skills)
└── research-last30days/
```

### Gaps or Problems Being Addressed

1. **Limited Design Guidance**: The current `frontend-design` skill provides creative direction but lacks:
   - Structured design system generation
   - Industry-specific reasoning rules
   - Comprehensive color/typography databases
   - Multi-platform support
   - UX best practice libraries

2. **No Product-Type Intelligence**: No automated matching of product types to optimal design patterns

3. **Missing Specialized Skills**: No dedicated skills for:
   - Brand guideline creation and management
   - Banner/ad design
   - Presentation/slide design
   - Design system development

4. **Limited Stack Support**: Current skill is framework-agnostic but doesn't provide stack-specific optimizations

---

## Proposed Changes

### Summary of Changes

1. Clone the UI/UX Pro Max skill repository to obtain all skill files and assets
2. Install 7 new skills (ui-ux-pro-max, design-system, design, brand, banner-design, slides, ui-styling)
3. Integrate Python scripts and data files for design system generation
4. Update CLAUDE.md to document the new capabilities
5. Test the installation and verify skill triggering

### New Files to Create

All files will be created by cloning the repository and selectively copying the skill suite:

| File Path | Purpose |
| --------- | ------- |
| `.claude/skills/ui-ux-pro-max/` | Main orchestrator skill with 67 styles, reasoning engine |
| `.claude/skills/design-system/` | Design system generation and token architecture |
| `.claude/skills/design/` | Core design skill (details TBD from repo) |
| `.claude/skills/brand/` | Brand guideline creation with scripts and templates |
| `.claude/skills/banner-design/` | Banner and ad design skill |
| `.claude/skills/slides/` | Presentation slide design skill |
| `.claude/skills/ui-styling/` | UI styling patterns and best practices |
| `src/` | Python scripts for design system generation (symlinked from skills) |

### Files to Modify

| File Path | Changes |
| --------- | ------- |
| `CLAUDE.md` | Add UI/UX Pro Max Skills section documenting all 7 skills and their capabilities |
| `CLAUDE.md` | Update Workspace Structure table to include ui-ux-pro-max skills |
| `reference/` | Potentially add Python requirements if the skill needs dependencies |

### Files to Delete (if any)

**Decision Point**: Should we replace or keep the existing `frontend-design` skill?

**Recommendation**: Keep both skills with clear differentiation:
- `frontend-design`: For creative, distinctive, bold UI generation (existing behavior)
- `ui-ux-pro-max`: For structured, industry-optimized, design-system-driven UI generation

The skills can coexist and complement each other. Update `frontend-design/SKILL.md` description to clarify when to use each.

---

## Design Decisions

### Key Decisions Made

1. **Installation Method: Git Clone + Selective Copy**
   - **Rationale**: The repository is a full workspace template, not just a skill package. We need to selectively extract the `.claude/skills/` directory and supporting `src/` scripts while avoiding duplicating unrelated files (docs, screenshots, cat-feeding-app example, etc.)

2. **Keep Existing frontend-design Skill**
   - **Rationale**: The existing skill focuses on creative, bold, distinctive aesthetics with freedom of expression. UI/UX Pro Max focuses on structured, industry-aligned, design-system-driven generation. Both approaches have value in different contexts.

3. **Install All 7 Skills from Suite**
   - **Rationale**: The skills work together as a cohesive system. Installing only `ui-ux-pro-max` would lose the specialized capabilities for brand, banners, slides, and design systems.

4. **Symlink Python Scripts from src/**
   - **Rationale**: The repository uses symlinks (`.claude/skills/ui-ux-pro-max/scripts` → `../../../src/`). We'll preserve this structure to maintain consistency with upstream updates.

5. **Add Installation Instructions to CLAUDE.md**
   - **Rationale**: Future users should know these skills exist, how they work, and when to use them vs. the existing `frontend-design` skill.

### Alternatives Considered

1. **Use CLI Installation (`uipro-cli`)**
   - **Rejected**: The CLI is designed for end-user installation in AI assistants. We're integrating into a workspace template where direct file management is more appropriate.

2. **Replace frontend-design Skill**
   - **Rejected**: Both skills serve different purposes. `frontend-design` prioritizes creativity and distinctive aesthetics; `ui-ux-pro-max` prioritizes structure and industry best practices.

3. **Install Only ui-ux-pro-max Core Skill**
   - **Rejected**: The suite's value comes from the integrated set of skills working together.

### Open Questions

1. **Python Dependencies**: Does the design system generation require Python packages? If so, should we add `reference/ui-ux-pro-max/requirements.txt`?
   - **Resolution Needed**: Inspect `src/` scripts during installation to identify dependencies

2. **Skill Description Collision**: Both `frontend-design` and `ui-ux-pro-max` might trigger on "build landing page" requests
   - **Resolution**: Update `frontend-design` description to emphasize "distinctive, bold, creative aesthetics" and deemphasize generic build requests
   - **ui-ux-pro-max** handles: structured, industry-aligned, design-system-driven generation

3. **Data File Size**: The skill includes large CSV databases (styles, colors, fonts, reasoning rules). Should we verify they don't bloat the workspace?
   - **Resolution**: Accept the files as they're essential to the skill's intelligence. Monitor workspace size if it becomes an issue.

---

## Step-by-Step Tasks

### Step 1: Clone Repository and Explore Structure

**Actions:**
- Clone the repository to a temporary location: `git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git /tmp/ui-ux-pro-max-skill`
- List the contents of `.claude/skills/` to confirm all 7 skills
- List the contents of `src/` to identify Python scripts and data files
- Read `README.md` and `CLAUDE.md` from the repo to understand installation requirements
- Check for `requirements.txt` or Python dependencies

**Files affected:**
- None (exploration only)

---

### Step 2: Copy Skills to Workspace

**Actions:**
- Copy all 7 skill directories from temp clone to workspace:
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/ui-ux-pro-max .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/design-system .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/design .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/brand .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/banner-design .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/slides .claude/skills/`
  - `cp -r /tmp/ui-ux-pro-max-skill/.claude/skills/ui-styling .claude/skills/`

**Files affected:**
- `.claude/skills/ui-ux-pro-max/SKILL.md` (new)
- `.claude/skills/ui-ux-pro-max/data/` (symlink or directory - verify)
- `.claude/skills/ui-ux-pro-max/scripts/` (symlink or directory - verify)
- `.claude/skills/design-system/SKILL.md` (new)
- `.claude/skills/design-system/data/` (new)
- `.claude/skills/design-system/references/` (new)
- `.claude/skills/design-system/scripts/` (new)
- `.claude/skills/design/SKILL.md` (new)
- `.claude/skills/brand/SKILL.md` (new)
- `.claude/skills/brand/references/` (new)
- `.claude/skills/brand/scripts/` (new)
- `.claude/skills/brand/templates/` (new)
- `.claude/skills/banner-design/SKILL.md` (new)
- `.claude/skills/banner-design/references/` (new)
- `.claude/skills/slides/SKILL.md` (new)
- `.claude/skills/ui-styling/SKILL.md` (new)

---

### Step 3: Copy Source Files and Resolve Symlinks

**Actions:**
- Copy `src/` directory to workspace root: `cp -r /tmp/ui-ux-pro-max-skill/src .`
- Verify symlinks in `.claude/skills/ui-ux-pro-max/`:
  - If `data` is a symlink, verify it points to correct location relative to workspace
  - If `scripts` is a symlink, verify it points to correct location relative to workspace
- If symlinks are broken or point to incorrect paths, update them:
  - `cd .claude/skills/ui-ux-pro-max`
  - `rm data scripts` (if symlinks)
  - `ln -s ../../../src/data data`
  - `ln -s ../../../src/scripts scripts`

**Files affected:**
- `src/` (new directory with Python scripts and data)
- `.claude/skills/ui-ux-pro-max/data` (symlink verification/update)
- `.claude/skills/ui-ux-pro-max/scripts` (symlink verification/update)

---

### Step 4: Install Python Dependencies (if required)

**Actions:**
- Inspect `src/scripts/*.py` files for import statements
- Check if repository contains `requirements.txt` or `pyproject.toml`
- If Python dependencies are required:
  - Create `reference/ui-ux-pro-max/requirements.txt` with dependencies
  - Add installation instructions to CLAUDE.md
  - Optionally run `pip install -r reference/ui-ux-pro-max/requirements.txt` to verify
- Document any required environment setup in CLAUDE.md

**Files affected:**
- `reference/ui-ux-pro-max/requirements.txt` (if Python deps exist)
- CLAUDE.md (installation instructions)

---

### Step 5: Update frontend-design Skill Description

**Actions:**
- Edit `.claude/skills/frontend-design/SKILL.md` frontmatter
- Update `description` field to clarify differentiation:
  - **Before**: "Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics."
  - **After**: "Create distinctive, bold, creative frontend interfaces with highly unique aesthetics. Use this skill when the user wants MEMORABLE, ARTISTIC, or EXPERIMENTAL UI design that breaks conventions. For structured, industry-aligned, design-system-driven generation, use ui-ux-pro-max instead. Generates creative, polished code that avoids generic AI aesthetics."

**Files affected:**
- `.claude/skills/frontend-design/SKILL.md`

---

### Step 6: Update CLAUDE.md Documentation

**Actions:**
- Add new section "UI/UX Skills" after "Frontend Design Skill" (around line 210)
- Document all 7 new skills with descriptions and capabilities
- Update Workspace Structure table to include new skills
- Add usage guidance explaining when to use `frontend-design` vs `ui-ux-pro-max`
- If Python dependencies exist, add installation instructions

**Content to add:**

```markdown
## UI/UX Pro Max Skills

This workspace includes the **UI/UX Pro Max** skill suite for comprehensive design intelligence. The suite consists of 7 specialized skills that provide structured, industry-optimized UI/UX generation with extensive databases of styles, colors, typography, and reasoning rules.

### What It Does

Generates production-ready UI/UX designs with:
- **67 UI Styles**: Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, and more
- **161 Color Palettes**: Industry-specific palettes aligned with 161 product types
- **57 Font Pairings**: Curated typography combinations with Google Fonts imports
- **161 Reasoning Rules**: Automatic design system generation based on product type
- **99 UX Guidelines**: Best practices, anti-patterns, and accessibility rules
- **25 Chart Types**: Dashboard and analytics recommendations
- **13 Tech Stacks**: React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose

### Skills in Suite

| Skill | Description |
| ----- | ----------- |
| `ui-ux-pro-max` | Main orchestrator with design system generation engine |
| `design-system` | Design system architecture, tokens, and component specs |
| `design` | Core design principles and patterns |
| `brand` | Brand guideline creation and management with scripts |
| `banner-design` | Banner and advertisement design |
| `slides` | Presentation slide design |
| `ui-styling` | UI styling patterns and best practices |

### Design System Generation

The flagship feature is the **Design System Generator** - an AI-powered reasoning engine that:
1. Analyzes project requirements and product type
2. Searches 5 databases in parallel (styles, colors, fonts, patterns, reasoning rules)
3. Applies industry-specific reasoning rules and filters anti-patterns
4. Generates complete design system with pattern, style, colors, typography, effects, anti-patterns, and pre-delivery checklist

### When to Use

**Use `ui-ux-pro-max`** when you want:
- Structured, industry-aligned design systems
- Automatic style/color/typography recommendations based on product type
- Multi-platform consistency (web, iOS, Android)
- Design systems with tokens and component libraries
- Landing pages with conversion-optimized patterns

**Use `frontend-design`** when you want:
- Bold, distinctive, memorable aesthetics
- Creative, artistic, experimental UI design
- Breaking conventions for maximum impact
- Custom, one-of-a-kind visual identities

Both skills can be used together: use `ui-ux-pro-max` for the design system foundation, then `frontend-design` for creative hero sections or distinctive components.

### Python Dependencies

[IF DEPENDENCIES EXIST, ADD:]
UI/UX Pro Max scripts require Python 3.8+ with dependencies listed in `reference/ui-ux-pro-max/requirements.txt`:

```bash
pip install -r reference/ui-ux-pro-max/requirements.txt
```
```

**Files affected:**
- `CLAUDE.md`

---

### Step 7: Test Skill Installation

**Actions:**
- Verify all SKILL.md files have valid YAML frontmatter (name, description)
- Test skill triggering by simulating requests:
  - "Build a landing page for a SaaS product" → should trigger `ui-ux-pro-max`
  - "Create a bold, artistic homepage" → should trigger `frontend-design`
  - "Generate brand guidelines for my company" → should trigger `brand`
  - "Design a slide deck" → should trigger `slides`
- Check that symlinks resolve correctly
- If Python scripts exist, test running one to verify dependencies

**Files affected:**
- None (testing only)

---

### Step 8: Clean Up Temporary Files

**Actions:**
- Remove the temporary clone: `rm -rf /tmp/ui-ux-pro-max-skill`
- Verify no unnecessary files were copied (docs, screenshots, example apps)

**Files affected:**
- None (cleanup only)

---

### Step 9: Commit Changes

**Actions:**
- Review all changes with `git status` and `git diff`
- Stage the new skills: `git add .claude/skills/ui-ux-pro-max .claude/skills/design-system .claude/skills/design .claude/skills/brand .claude/skills/banner-design .claude/skills/slides .claude/skills/ui-styling`
- Stage source files: `git add src/`
- Stage documentation: `git add CLAUDE.md`
- Stage modified frontend-design: `git add .claude/skills/frontend-design/SKILL.md`
- Stage this plan: `git add plans/2026-03-12-add-ui-ux-pro-max-skill.md`
- If Python requirements exist: `git add reference/ui-ux-pro-max/requirements.txt`
- Create commit with message:
  ```
  Add UI/UX Pro Max skill suite (7 skills)

  Integrates comprehensive design intelligence:
  - 67 UI styles, 161 color palettes, 57 font pairings
  - 161 product-type reasoning rules for design system generation
  - 99 UX guidelines, 25 chart types, 13 tech stacks

  Skills added:
  - ui-ux-pro-max: Main orchestrator with design system generator
  - design-system: Token architecture and component specs
  - design: Core design principles
  - brand: Brand guideline creation and management
  - banner-design: Banner/ad design
  - slides: Presentation design
  - ui-styling: UI styling patterns

  Updated frontend-design skill description to clarify differentiation.
  Documented integration in CLAUDE.md with usage guidelines.

  🤖 Generated with Claude Code
  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

**Files affected:**
- Git repository

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` - Documents all skills available in the workspace
- `.claude/skills/frontend-design/SKILL.md` - Currently the only design-focused skill

### Updates Needed for Consistency

1. **CLAUDE.md Workspace Structure**: Add ui-ux-pro-max skills to the table
2. **CLAUDE.md Skills Section**: Add new section documenting UI/UX Pro Max suite
3. **frontend-design SKILL.md**: Update description to clarify when to use vs ui-ux-pro-max

### Impact on Existing Workflows

**Positive Impacts:**
- Users gain access to structured design system generation
- Industry-specific reasoning rules improve design quality
- Multi-platform support enables consistent cross-platform design
- Brand, banner, and slide design capabilities are now available

**Minimal Disruption:**
- Existing `frontend-design` skill continues to work for creative, distinctive UI
- No changes to other skills (SEO, blog, research)
- Skills operate independently and can be used together

**Skill Triggering Consideration:**
- Both `frontend-design` and `ui-ux-pro-max` may trigger on UI build requests
- Updated descriptions should differentiate: `frontend-design` for creative/artistic, `ui-ux-pro-max` for structured/industry-aligned
- Claude's skill selection logic will choose based on context and description specificity

---

## Validation Checklist

How to verify the implementation is complete and correct:

- [ ] All 7 skill directories exist in `.claude/skills/`
- [ ] Each skill has a valid `SKILL.md` with YAML frontmatter (name, description)
- [ ] `src/` directory exists with Python scripts and data files
- [ ] Symlinks in `.claude/skills/ui-ux-pro-max/` resolve correctly (data, scripts)
- [ ] `CLAUDE.md` includes new "UI/UX Pro Max Skills" section
- [ ] `CLAUDE.md` Workspace Structure table updated
- [ ] `frontend-design/SKILL.md` description updated to clarify differentiation
- [ ] If Python dependencies exist, `reference/ui-ux-pro-max/requirements.txt` is created
- [ ] Test skill triggering: "Build a SaaS landing page" → triggers `ui-ux-pro-max`
- [ ] Test skill triggering: "Create a bold, artistic homepage" → triggers `frontend-design`
- [ ] Test skill triggering: "Generate brand guidelines" → triggers `brand`
- [ ] No extraneous files copied (docs, screenshots, example apps)
- [ ] Temporary clone removed
- [ ] All changes committed with descriptive message

---

## Success Criteria

The implementation is complete when:

1. **All 7 skills are installed** and accessible in `.claude/skills/` with valid SKILL.md files
2. **Supporting files are in place**: `src/` directory with scripts and data, symlinks resolved
3. **Documentation is updated**: CLAUDE.md accurately describes the new skills and when to use them
4. **Skill differentiation is clear**: `frontend-design` vs `ui-ux-pro-max` descriptions prevent confusion
5. **Skills trigger correctly**: Test prompts activate the appropriate skill
6. **Changes are committed**: All new files and modifications are tracked in git

---

## Notes

### Repository Structure Insights

The UI/UX Pro Max repository is a full workspace template (similar to this one) with:
- `.claude/skills/` - 7 skills
- `src/` - Python scripts and CSV data files
- `docs/` - Documentation (not needed in workspace)
- `screenshots/` - Images (not needed in workspace)
- `cat-feeding-app/`, `cli/`, `preview/` - Example projects (not needed in workspace)

We're selectively extracting only the skills and supporting source files.

### Symlink Strategy

The repository uses symlinks to share `src/` across multiple skills:
- `.claude/skills/ui-ux-pro-max/data` → `../../../src/data`
- `.claude/skills/ui-ux-pro-max/scripts` → `../../../src/scripts`

We'll preserve this structure to maintain consistency with upstream and enable potential future updates.

### Future Considerations

1. **Skill Updates**: Monitor the upstream repository for updates. The CLI tool (`uipro-cli`) provides version management that could be adapted for manual updates.

2. **Integration with Existing Skills**: Consider how UI/UX Pro Max could enhance:
   - SEO landing page generation (SEO + ui-ux-pro-max)
   - Blog post visual design (blog + ui-styling)
   - Brand-aligned landing pages (brand + ui-ux-pro-max)

3. **Custom Reasoning Rules**: The 161 reasoning rules are extensible. Future enhancements could add workspace-specific product types and design rules.

4. **Design System Exports**: Explore exporting generated design systems to Figma, Tailwind config, CSS variables, or design tokens.

### Related Skills

- **frontend-design**: Creative, distinctive UI generation (existing)
- **ui-ux-pro-max**: Structured, industry-aligned design (new)
- **design-system**: Design token architecture (new)
- **brand**: Brand guidelines and identity (new)

These skills form a comprehensive design toolkit covering the full spectrum from brand strategy to implementation.
