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
