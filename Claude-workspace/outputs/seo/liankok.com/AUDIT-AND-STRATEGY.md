# SEO Audit & Strategy: liankok.com
**Date:** 2026-03-04
**Business:** Lian Kok Electrical — ABB Authorised Distributor, Singapore (est. 1975)
**Platform:** WordPress + Yoast SEO + WPForms + WooCommerce
**Industry:** Hybrid — Local Electrical Distributor + B2B/B2C Product Catalogue
**Strategy Period:** 12 months (Q1–Q4 2026)

---

## SEO Health Score: 42 / 100

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 52/100 | 25% | 13.0 |
| Content Quality | 40/100 | 25% | 10.0 |
| On-Page SEO | 35/100 | 20% | 7.0 |
| Schema / Structured Data | 45/100 | 10% | 4.5 |
| Performance (CWV) | 40/100 | 10% | 4.0 |
| Images | 5/100 | 5% | 0.25 |
| AI Search Readiness | 35/100 | 5% | 1.75 |
| **TOTAL** | | | **42** |

---

## Executive Summary

Lian Kok holds a genuinely defensible SEO position — **35 years as an ABB-exclusive authorised distributor** — that no competitor can replicate. The site, however, is built on a WordPress theme that was never properly cleaned up: 30+ demo pages (tire-balance, vehicle-wiring, paralegal guides) are actively indexed, destroying topical authority. Combined with ~95% of images missing alt text, missing meta descriptions on every core page, and multiple H1s, the site is leaving the majority of its ranking potential untapped.

The strategy is simple: **own "ABB + Singapore" search territory completely**, then layer in high-intent Singapore electrical need searches.

### Top 5 Critical Issues
1. **30+ demo/template pages indexed** — automotive, paralegal, and theme demo content actively pollutes crawl budget and confuses topic signals
2. **~95% of images missing alt text** — Products page: 51/52 images missing; MCB product page: 23/24 missing
3. **Multiple H1 tags** — homepage has 5 H1s (carousel product names); Products page has 3 H1s
4. **No meta descriptions on any core page** — About, Products, Contact, Blog, and all product pages missing
5. **Slow TTFB (1.22s homepage)** — 308KB HTML exceeds Google's 800ms threshold; root cause: page builder inline CSS + synchronous Facebook Pixel

### Top 5 Quick Wins
1. Noindex/delete all demo pages — one-time bulk action in Yoast, immediate crawl budget recovery
2. Add meta descriptions to all core pages — 5 minutes each in Yoast
3. Fix H1 to single tag — change carousel headings from H1 to H2/H3
4. Add LocalBusiness schema to homepage — one JSON-LD block (template in IMPLEMENTATION-PLAN.md)
5. Clean robots.txt — remove two redundant sitemap declarations, keep only `sitemap_index.xml`

---

## Audit Findings

### 1. Technical SEO

**Crawlability**
- robots.txt: Open to all bots (`Disallow:` empty) ✓
- HTTPS enforced with HSTS (`max-age=63072000`) ✓
- Canonical tags present and self-referencing ✓
- Three sitemap declarations in robots.txt — redundant, keep only `sitemap_index.xml` ⚠️

**Indexability — Critical**
The page sitemap contains 49 URLs, the majority leftover theme demo pages:

| Junk Pages (Live & Indexed) | Problem |
|---|---|
| `/tire-balance/`, `/vehicle-wiring/`, `/clutch-replacement/`, `/engine-replace/` | Automotive — wrong industry |
| `/home-page-two/`, `/rtl-homepage/`, `/onepage-home/`, `/sample-page-2/` | Theme demos |
| `/team/`, `/team-details/`, `/testimonials/`, `/portfolio-details/` | Empty demo pages |
| `/pricing/`, `/service/`, `/service-details/`, `/blog-grid/` | Demo pages |
| `/shop-2/`, `/cart-2/`, `/checkout-2/` | Duplicate WooCommerce pages |
| `/filter-check-up/`, `/better-performance/`, `/chch/`, `/2802-2/` | Demo/unknown |

Off-topic posts indexed: `/hello-world/`, `/blog-standard/`, `/what-can-paralegals-do-a-guide-for-lawyers/`, `/better-products-when-companies-work-together/`

Duplicate pages (both versions indexed): `/about/` + `/about-2/`, `/shop/` + `/shop-2/`, `/cart/` + `/cart-2/`

**Sitemap Structure**
9 child sitemaps via `sitemap_index.xml`. Issues:
- `categorie-sitemap.xml` and `category-sitemap.xml` both exist — likely duplicating URLs
- `cartflows_step-sitemap.xml` includes checkout funnel steps (should be noindex)
- WooCommerce cart/checkout pages indexed via page sitemap

**Security Headers**
| Header | Status |
|---|---|
| HSTS | ✓ `max-age=63072000` |
| X-Frame-Options | ✓ SAMEORIGIN |
| X-Content-Type-Options | ✓ nosniff |
| Content-Security-Policy | ⚠️ Minimal — `upgrade-insecure-requests` only |
| Referrer-Policy | ✓ strict-origin-when-cross-origin |

---

### 2. Performance (Core Web Vitals Proxy)

| Metric | Value | Target | Status |
|---|---|---|---|
| TTFB (Homepage) | 1.22s | < 0.8s | ❌ |
| TTFB (Products) | 1.22s | < 0.8s | ❌ |
| TTFB (About) | 0.49s | < 0.8s | ✓ |
| HTML Size (Homepage) | 308KB | < 100KB | ❌ Bloated |
| HTML Size (Products) | 263KB | < 100KB | ❌ Bloated |
| HTML Size (About) | 173KB | < 100KB | ❌ Bloated |

Root causes: Page builder generating massive inline CSS (WPForms CSS vars block alone is significant); Facebook Pixel loading synchronously in `<head>`; Yoast + WooCommerce JS on every page. Server is Apache — WP Rocket + Cloudflare is the right fix.

---

### 3. On-Page SEO

**Homepage**
| Element | Value | Status |
|---|---|---|
| Title (48 chars) | "Lian Kok Electrical - ABB Authorised Distributor" | ✓ Good |
| Meta Description (160 chars) | "ABB Authorised Distributor since 1991..." | ✓ Present |
| Canonical | `https://liankok.com/` | ✓ |
| H1 count | 5 H1 tags (carousel product names) | ❌ Critical |
| Lang attribute | `en-US` | ⚠️ Should be `en-SG` |
| OG tags | Present | ✓ |

**Core Pages — All Missing Meta Descriptions**
| Page | Current Title | Meta Desc |
|---|---|---|
| /about/ | "About - Lian Kok Electrical" (27 chars) | ❌ Missing |
| /products/ | "Products - Lian Kok Electrical" (30 chars) | ❌ Missing |
| /contact/ | "Contact - Lian Kok Electrical" (29 chars) | ❌ Missing |
| /blog-2/ | "Blog - Lian Kok Electrical" (26 chars) | ❌ Missing |
| /product/miniature-circuit-breakers-mcbs-2/ | "Miniature Circuit Breakers - Lian Kok Electrical" (48 chars) | ❌ Missing |

Titles are also weak — "About - Lian Kok Electrical" wastes the tag. Should be keyword-forward: "About Lian Kok Electrical | Singapore Electrical Distributor Since 1975"

**Blog Post**
- Title 88 chars — too long (Google truncates ~60 chars)
- H2 structure is excellent (what/why/how)
- 1,392 words — decent, target 2,000+ for competitive queries
- Author shows as "admin" — no E-E-A-T signal

---

### 4. Content Quality (E-E-A-T)

**What's strong:** 50+ years in business, ABB partner since 1991. These are genuinely powerful E-E-A-T signals — but they're buried in the meta description and invisible to on-page scoring.

**What's weak:**
- No staff profiles or named authors anywhere
- No certifications or credentials shown on-page
- No case studies despite a /projects/ page existing
- No customer reviews or testimonials (the /testimonials/ page is demo content)

**Thin Content Pages**
| Page | Word Count | Status |
|---|---|---|
| Contact | ~212 | ❌ Thin |
| Blog listing | ~160 | ❌ Very thin |
| MCB product page | ~370 | ❌ Thin |
| Products listing | ~582 | ⚠️ Borderline |
| About | ~617 | ⚠️ Acceptable but weak |

---

### 5. Schema / Structured Data

**Current (via Yoast)**
| Schema | Pages | Status |
|---|---|---|
| WebPage | All pages | ✓ |
| WebSite + SearchAction | Homepage | ✓ |
| Organization | Homepage | ✓ (incomplete — no address/phone/hours) |
| Article | Blog posts | ✓ (author = "admin" — problem) |
| BreadcrumbList | Product pages | ✓ |

**Missing (High Priority)**
| Schema | Priority | Impact |
|---|---|---|
| LocalBusiness (ElectricalContractor) | Critical | Local pack, Google Maps, trust signals |
| Product schema on product pages | High | Product rich results, Google Shopping |
| FAQPage on /faq/ | High | FAQ rich snippets |
| AggregateRating / Review | Medium | Star ratings in SERP |

---

### 6. Images

| Page | Total Images | Missing/Empty Alt | % |
|---|---|---|---|
| Homepage | 44 | ~40 | ~90% |
| Products | 52 | 51 | 98% |
| About | 22 | 20 | 91% |
| MCB Product Page | 24 | 23 | 96% |
| MCB Blog Post | 5 | 4 | 80% |

Additional issues: non-descriptive filenames (`Untitled-design-91.png`, `Background-7.png`) signal nothing to Google. These product photos could rank in Google Images for "ABB MCB Singapore" — currently they don't.

---

### 7. AI Search Readiness

- All bots allowed (GPTBot, ClaudeBot, PerplexityBot can crawl) ✓
- Existing blog posts have good H2 hierarchy — AI-citeable ✓
- No `llms.txt` file
- Missing: FAQ format, comparison content, "best X for Y" structures
- AI Overviews affect only ~0.14% of local keywords — low disruption risk for this vertical, but ChatGPT/Perplexity local recommendations are growing

---

## Strategic Positioning

### The Core Opportunity
Lian Kok's competitive moat is simple and defensible: **no other Singapore competitor can claim "ABB Authorised Distributor since 1991."** ElectGo sells ABB products but isn't an authorised distributor. Lim Kim Hai Electric is repositioning away from product distribution to "Beyond MRO." The entire SEO strategy flows from this single truth.

### Target Audiences
1. **Licensed Electrical Workers (LEWs) / Contractors** — Bulk ABB products, specs. High value, repeat.
2. **M&E Consultants / Engineers** — Specifying products for building projects. Need authoritative info.
3. **Facility Managers** — Replacement parts, maintenance. Need quick availability.
4. **HDB / Private Homeowners** — MCB replacement, wiring accessories. High volume, lower value.
5. **Electrical Retailers** — Wholesale. B2B relationship.

### Content Pillars
| Pillar | Focus | Keywords |
|---|---|---|
| **ABB Product Authority** | Brand hub + product pages | "ABB MCB Singapore", "ABB contactor Singapore", "ABB authorised distributor Singapore" |
| **Electrical Knowledge** | Guides, comparisons, FAQ | "MCB price Singapore", "MCB vs MCCB", "how to choose MCB Singapore" |
| **Singapore Project Showcase** | Case studies, portfolio | "[project type] electrical Singapore", "ABB installation Singapore" |
| **Local Trade Support** | Contact, location, GBP | "electrical distributor Race Course Road", "ABB stockist Singapore" |

---

## Competitor Analysis

| Competitor | Strengths | Weaknesses | Lian Kok's Edge |
|---|---|---|---|
| **ElectGo** (electgo.com) | Multi-brand, price guides, programmatic content, Cloudflare CDN | Generalist — not ABB specialists, no physical counter | ABB exclusivity + depth of partnership |
| **Lim Kim Hai Electric** (limkimhai.com.sg) | 60 years, multi-brand, rebuilt site, org schema | Pivoting away from distribution to "Beyond MRO" — topical gap opening | ABB-specific content depth; clear distributor identity |
| **Horme Singapore** (horme.com.sg) | Large B2C SKU catalogue, consumer brand | Not ABB authorised; consumer-only; no trade focus | B2B/contractor positioning; authorised credentials |
| **RS Singapore** (sg.rs-online.com) | Global authority, massive catalogue | Not local, not ABB authorised, expensive | Local physical counter; Singapore expertise; ABB authority |

**Competitive Gap Matrix**
| Opportunity | Lian Kok | ElectGo | LKH | Horme |
|---|---|---|---|---|
| ABB-specific content depth | 🔴 Weak | 🟡 Med | 🟡 Med | ❌ None |
| ABB authority hub page | ❌ Missing | ✓ Has | ✓ Has | ❌ None |
| Price guides / buying guides | ❌ Missing | ✅ Strong | 🟡 Partial | ❌ None |
| Product schema | ❌ Missing | ✅ Present | 🟡 Partial | ✅ Present |
| LocalBusiness schema | ❌ Missing | ❌ Missing | ❌ Missing | ❌ Missing |
| Physical walk-in counter | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Meta descriptions | 🔴 Missing | ✅ Good | ✅ Good | ✅ Good |
| Page speed | 🔴 1.22s | ✅ Fast | ✅ Fast | 🟡 Med |

**Content gaps no competitor covers well:**
- "ABB MCB Price Guide Singapore [year]" — ABB-specific (ElectGo's guide is generic)
- "ABB S200 Series: Complete Specifications Guide" — model depth
- "ABB Authorised Distributor Singapore: What It Means" — trust + authority
- "Choosing MCBs for Singapore HDB Distribution Boards" — homeowner volume

**Backlink targets:**
| Source | How |
|---|---|
| ABB official Singapore distributor page | Contact ABB SG marketing |
| Singapore Contractors Association (SCAL) | Member listing |
| BCA (Building & Construction Authority) | Supplier listing |
| Singapore Electrical Traders Association | Membership + directory |
| Singapore M&E trade publications | Editorial / press releases |
| Google Business Profile | Fully optimise |

---

## Keyword Strategy

### Tier 1 — Win Now (ABB + Singapore)
| Keyword | Intent | Target Page |
|---|---|---|
| ABB authorised distributor Singapore | Commercial | Homepage + /abb-singapore/ |
| ABB MCB Singapore | Commercial | /products/circuit-breakers/miniature-circuit-breakers/ |
| ABB contactor Singapore | Commercial | /products/contactors-relays/af-contactors/ |
| ABB RCD Singapore | Commercial | /products/circuit-breakers/residual-current-devices/ |
| ABB low voltage products Singapore | Commercial | /products/ |
| Lian Kok Electrical | Branded | Homepage |

### Tier 2 — 3–6 Months (Category + Singapore)
| Keyword | Intent | Target Page |
|---|---|---|
| MCB Singapore | Commercial | /products/circuit-breakers/miniature-circuit-breakers/ |
| circuit breaker Singapore | Commercial | /products/circuit-breakers/ |
| electrical distributor Singapore | Commercial | Homepage |
| contactor Singapore | Commercial | /products/contactors-relays/ |
| surge protection device Singapore | Commercial | /products/surge-protection/ |
| MCCB Singapore | Commercial | Product category page |

### Tier 3 — 6–12 Months (Educational / Long-tail)
| Keyword | Intent | Target Page |
|---|---|---|
| MCB price Singapore | Informational | /resources/price-guides/ |
| how to choose MCB Singapore | Informational | /resources/guides/mcb-guide-singapore/ |
| ABB vs Schneider MCB Singapore | Informational | /resources/ |
| HDB electrical panel Singapore | Informational | /resources/guides/electrical-panel-guide-singapore/ |
| MCCB vs MCB difference | Informational | Resources |
| ABB MCB S200 specifications | Informational | Product pages |

---

## KPI Targets

| Metric | Current (Est.) | 3 Months | 6 Months | 12 Months |
|---|---|---|---|---|
| Organic Sessions/month | Baseline TBC | +30% | +80% | +200% |
| Quality Indexed Pages | ~30 (post-cleanup) | 40 | 60 | 100+ |
| Top 10 Rankings: ABB Singapore keywords | ~5 | 15 | 30 | 50+ |
| Google Business Profile Views | Baseline TBC | Establish | +50% | +150% |
| Core Web Vitals Pass Rate | ~40% | 60% | 80% | 90%+ |
| Blog/Resource Posts Published | 3 | 8 | 16 | 30 |
| Google Reviews | TBC | 20+ | 35+ | 50+ |
| Quality Backlinks Acquired | TBC | 5 | 15 | 30+ |

---

## Issues Summary Scorecard

| Issue | Severity | Scope |
|---|---|---|
| 30+ demo/template pages indexed | 🔴 Critical | Entire site |
| Multiple H1 tags on homepage | 🔴 Critical | Homepage, Products |
| ~95% of images missing alt text | 🔴 Critical | All pages |
| Missing meta descriptions on core pages | 🔴 Critical | 5+ pages |
| Slow TTFB (1.22s) | 🟠 High | Homepage, Products |
| Bloated HTML (300KB+) | 🟠 High | All pages |
| No LocalBusiness schema | 🟠 High | Homepage |
| No Product schema | 🟠 High | 21 products |
| Off-topic content indexed | 🟠 High | 5+ pages |
| Duplicate pages indexed | 🟠 High | 6+ pages |
| Blog post titles too long (88 chars) | 🟡 Medium | Blog posts |
| Thin product pages (~370 words) | 🟡 Medium | Product pages |
| Author "admin" in Article schema | 🟡 Medium | Blog posts |
| lang="en-US" should be en-SG | 🟡 Medium | All pages |
| Three sitemap references in robots.txt | 🟡 Medium | robots.txt |
| Weak page titles (generic format) | 🟡 Medium | Core pages |
| No FAQ schema | 🟢 Low | /faq/ |
| No llms.txt | 🟢 Low | Site root |
