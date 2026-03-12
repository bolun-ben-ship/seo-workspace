---
name: seo-audit
description: >
  Full website SEO audit with parallel subagent delegation. Crawls up to 500
  pages, detects business type, delegates to 6 specialists, generates health
  score. Use when user says "audit", "full SEO check", "analyze my site",
  or "website health check".
---

# Full Website SEO Audit

## Process

1. **Fetch homepage** — use `scripts/fetch_page.py` to retrieve HTML
2. **Detect business type** — analyze homepage signals per seo orchestrator
3. **Crawl site** — follow internal links up to 500 pages, respect robots.txt
4. **Delegate to subagents** (if available, otherwise run inline sequentially):
   - `seo-technical` — robots.txt, sitemaps, canonicals, Core Web Vitals, security headers
   - `seo-content` — E-E-A-T, readability, thin content, AI citation readiness
   - `seo-schema` — detection, validation, generation recommendations
   - `seo-sitemap` — structure analysis, quality gates, missing pages
   - `seo-performance` — LCP, INP, CLS measurements
   - `seo-visual` — screenshots, mobile testing, above-fold analysis
5. **Score** — aggregate into SEO Health Score (0-100)
6. **Report** — write all findings into the single output file

## Crawl Configuration

```
Max pages: 500
Respect robots.txt: Yes
Follow redirects: Yes (max 3 hops)
Timeout per page: 30 seconds
Concurrent requests: 5
Delay between requests: 1 second
```

## Output

Save everything to a single file:

```
outputs/seo/<domain>/AUDIT.md
```

Optional: `screenshots/` directory for desktop + mobile captures (if Playwright available).

## Scoring Weights

| Category | Weight |
|----------|--------|
| Technical SEO | 25% |
| Content Quality | 25% |
| On-Page SEO | 20% |
| Schema / Structured Data | 10% |
| Performance (CWV) | 10% |
| Images | 5% |
| AI Search Readiness | 5% |

## Report Structure

All sections below are written into the single `AUDIT.md` file in this order.

### Executive Summary
- Overall SEO Health Score (0-100)
- Business type detected
- Top 5 critical issues
- Top 5 quick wins

> **Scope boundary:** This summary is a current-state diagnosis only (backward-looking). It does NOT include strategic opportunities, phasing, or KPIs — those belong in IMPLEMENTATION-PLAN.md.

### Technical SEO
- Crawlability issues
- Indexability problems
- Security concerns
- Core Web Vitals status

### Content Quality
- E-E-A-T assessment — site-only evaluation: does this site demonstrate Experience, Expertise, Authoritativeness, Trust? Score each signal, list gaps.
- Note: competitor E-E-A-T benchmarking belongs in IMPLEMENTATION-PLAN.md, not here.
- Thin content pages
- Duplicate content issues
- Readability scores

### On-Page SEO
- Title tag issues
- Meta description problems
- Heading structure
- Internal linking gaps

### Schema & Structured Data
- Current implementation
- Validation errors
- Missing opportunities

### Performance
- LCP, INP, CLS scores
- Resource optimization needs
- Third-party script impact

### Images
- Missing alt text
- Oversized images
- Format recommendations

### AI Search Readiness
- Citability score
- Structural improvements
- Authority signals

### Action Plan
- Tactical issue register only — no strategy, no phasing, no timeline beyond "fix within N days/weeks"
- Prioritized issue list: Critical → High → Medium → Low
- Each issue: description, severity, specific fix, estimated effort
- Quick wins called out separately

> **Scope boundary:** The Action Plan lists WHAT is broken and HOW to fix each item. It does NOT define execution phases, resource allocation, or strategic sequencing — that is the role of IMPLEMENTATION-PLAN.md.

## Priority Definitions

- **Critical**: Blocks indexing or causes penalties (fix immediately)
- **High**: Significantly impacts rankings (fix within 1 week)
- **Medium**: Optimization opportunity (fix within 1 month)
- **Low**: Nice to have (backlog)
