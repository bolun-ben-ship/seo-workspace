# SEO Audit Findings: owllight-sleep.com
**Date:** 2026-03-04 | **Platform:** Shopify | **Market:** Singapore

---

## Health Score: 42 / 100

| Category | Score | Weight | Weighted |
|---|---|---|---|
| Technical SEO | 28/100 | 25% | 7.0 |
| Content Quality | 52/100 | 25% | 13.0 |
| On-Page SEO | 60/100 | 20% | 12.0 |
| Schema / Structured Data | 35/100 | 10% | 3.5 |
| Performance (CWV) | 40/100 | 10% | 4.0 |
| Images | 45/100 | 5% | 2.25 |
| AI Search Readiness | 30/100 | 5% | 1.5 |
| **TOTAL** | | | **43.25 / 100** |

**Top 5 critical issues:**
1. Cloudflare Managed Challenge blocks ALL crawlers — robots.txt and sitemap.xml return 403
2. robots.txt inaccessible — Google cannot read crawl directives
3. sitemap.xml inaccessible — Google page discovery frozen
4. Mixed URL structure — `/en/blogs/...` vs `/blogs/...` (duplicate content risk)
5. Absent from all major Singapore mattress roundup articles

**Top 5 quick wins:**
1. Fix Cloudflare → allow verified bots (1-2 hrs, unlocks everything)
2. Submit sitemap to Google Search Console
3. Add AggregateRating schema → star ratings in SERPs
4. Create "Best Mattress Singapore" buying guide page
5. Add author bios to all blog posts

---

## 1. Technical SEO (28/100)

### Crawlability — CRITICAL FAILURE

The site uses Cloudflare's Managed Challenge (JS challenge) on **all URLs**, returning 403 to every non-browser request:

| URL | Status |
|---|---|
| Homepage | 403 |
| `/robots.txt` | 403 |
| `/sitemap.xml` | 403 |
| Product/blog pages | 403 |

**Why this is catastrophic:** Google's documentation states that if `robots.txt` returns a 4xx (non-404) error, Googlebot delays and eventually halts crawling. The site has ~8 indexed pages because Google indexed them before this Cloudflare config was applied — not because the site is being crawled now.

**Fix:** In Cloudflare → Security → Bots, enable "Bot Fight Mode" with the verified bots allowlist enabled. Add a WAF bypass rule for Known Bots. Do NOT disable Cloudflare entirely — just exempt verified crawlers.

```
WAF Bypass Rule:
(cf.client.bot = true) → Action: Skip all security rules
```

### Indexability

- **Currently indexed:** ~8 pages (from `site:owllight-sleep.com`)
- **Expected for this store size:** 50-200+ pages
- **Gap:** Severe underindexing — almost certainly caused by Cloudflare blocking

**Known indexed pages:**
```
owllight-sleep.com/
owllight-sleep.com/collections
owllight-sleep.com/products/mattress-sale-singapore-tulip
owllight-sleep.com/products/mattress-topper-singapore-4d
owllight-sleep.com/en/blogs/best-mattress-singapore-brands/woosa-mattress-review-owllight
owllight-sleep.com/en/blogs/best-mattress-singapore-brands/sealy-vs-simmons-at-owllight
owllight-sleep.com/blogs/hybrid-mattress-brand-owllight-news
owllight-sleep.com/pages/showroom-22-sin-ming-lane
```

### URL Structure Issues

Two conflicting URL patterns exist:

| Pattern | Example |
|---|---|
| With `/en/` prefix | `/en/blogs/best-mattress-singapore-brands/woosa-mattress-review-owllight` |
| Without prefix | `/blogs/hybrid-mattress-brand-owllight-news` |

This indicates a partially implemented Shopify Markets or language app. The `/en/` prefix may be creating duplicate content without proper hreflang implementation. Must be resolved before any content migration.

### Core Web Vitals (Estimated)

Cannot measure directly (403 blocks). Estimates based on Shopify/Cloudflare patterns:

| Metric | Estimated | Benchmark |
|---|---|---|
| LCP | ⚠️ 3-5s | < 2.5s |
| INP | ❓ Unknown | < 200ms |
| CLS | ⚠️ Possible issues | < 0.1 |
| FCP | ⚠️ 2-4s | < 1.8s |
| TTFB | ✅ Good (Cloudflare CDN) | < 800ms |

Common Shopify performance killers: uncompressed hero images, third-party app scripts, large JS bundles. Run PageSpeed Insights once Cloudflare is fixed.

---

## 2. On-Page SEO (60/100)

### Title Tag Analysis

| Page | Current Title | Issue |
|---|---|---|
| Homepage | "Mattress Promotion Singapore \| Owllight Back Care Mattresses" | ⚠️ "Promotion" implies transient content |
| Tulip Mattress | "Mattress Sale Singapore \| Cooling Back Care Hybrid Mattress \| Tulip" | ⚠️ "Sale" reduces year-round relevance |
| Mattress Topper | "Mattress Topper Singapore \| Extra Firm Pro Spine & Back Care" | ✅ Strong |
| Woosa Review | "Woosa Mattress Review with Owllight's Mattress" | ❌ Missing "Singapore", weak framing |
| Showroom | "22 Sin Ming Lane Mid View City Singapore (Owllight Mattress)" | ❌ Address as title — not keyword-optimised |
| Sealy vs Simmons | "Sealy vs Simmons Mattress at Owllight" | ⚠️ Add "Singapore" |
| Collections | "All Products – Owllight-sleep" | ❌ Generic — no keyword value |

### Internal Linking

Blog posts likely do not link to product pages — a missed conversion opportunity. Every comparison post should include a clear CTA to the Tulip Mattress or Topper product page.

### Meta Descriptions

Cannot verify (403). Audit via Google Search Console once accessible.

---

## 3. Content Quality & E-E-A-T (52/100)

### Brand Overview

Owllight is a Singapore-founded back care mattress brand:
- **Tulip Hybrid Mattress** — ~$899 queen; 4D Air Fiber, 5-Zone Pro-S Spine Support, Japan Technology, CertiPUR-US
- **Mattress Topper 4D** — #1 on Lazada; extra firm, orthopedic
- **100-night trial**, physical showroom at 22 Sin Ming Lane Mid View City
- **Dubai/Middle East** expansion in progress

### E-E-A-T Scores

| Signal | Score | Notes |
|---|---|---|
| Experience | 2/5 | No customer stories, case studies, or founder story visible on-site |
| Expertise | 2/5 | No author bylines, no sleep/physio credentials cited |
| Authoritativeness | 2/5 | Lazada #1 not evidenced on-site; no editorial backlinks from SG media |
| Trustworthiness | 3/5 | CertiPUR-US, 100-night trial, showroom address — but no on-site review aggregate |

### Existing Blog Content

| Post | URL | Status |
|---|---|---|
| Woosa comparison | `/en/blogs/.../woosa-mattress-review-owllight` | Good concept — needs expansion and author bio |
| Sealy vs Simmons | `/en/blogs/.../sealy-vs-simmons-at-owllight` | Good concept — needs expansion |
| Brand launch news | `/blogs/hybrid-mattress-brand-owllight-news` | Low SEO value |

### Critical Content Gaps

1. "Best Mattress Singapore" buying guide — top priority, highest volume keyword
2. "Best Mattress for Back Pain Singapore" — core brand positioning keyword
3. About Us / founder story — required for E-E-A-T baseline
4. Hybrid Mattress Singapore category page
5. FAQ page
6. Author profile pages

---

## 4. Schema & Structured Data (35/100)

**Likely present (Shopify defaults):** Basic `Product` schema (name, price, description)

**Missing:**

| Schema | Page | Impact |
|---|---|---|
| `AggregateRating` | Product pages | ⭐ Star ratings in SERPs — high CTR uplift |
| `LocalBusiness` | Showroom page | Local search visibility |
| `Organization` | Homepage | Brand entity, Knowledge Panel |
| `BlogPosting` + `Person` | Blog posts | E-E-A-T, authorship signals |
| `FAQPage` | Products + guides | Featured snippets, AI Overviews |
| `BreadcrumbList` | All pages | Site navigation in SERPs |

**LocalBusiness JSON-LD (ready to implement):**
```json
{
  "@context": "https://schema.org",
  "@type": "FurnitureStore",
  "name": "Owllight Mattress Showroom",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "22 Sin Ming Lane #03-77A",
    "addressLocality": "Mid View City",
    "addressRegion": "Singapore",
    "postalCode": "573969",
    "addressCountry": "SG"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 1.3472, "longitude": 103.8310 }
}
```

---

## 5. AI Search Readiness (30/100)

The Cloudflare challenge blocks **all AI crawlers**:
- ❌ GPTBot (ChatGPT) — cannot index site
- ❌ ClaudeBot (Anthropic) — cannot index site
- ❌ PerplexityBot — cannot index site
- ❌ Google-Extended (AI Overviews training) — uncertain

Same Cloudflare fix resolves this. Additionally missing:
- No FAQ content for featured snippet / AI Overview extraction
- No `llms.txt` file
- Not cited in major third-party SG publications (critical for AI brand signals)

---

## 6. Performance & Images

**Performance (40/100):** Cannot audit directly. Shopify risk factors: unoptimised product images, third-party app scripts, large JS bundles. Cloudflare CDN is a positive.

**Images (45/100):** Shopify auto-converts to WebP and generates srcset ✅. Common gaps: alt text missing on product/lifestyle images, oversized source files uploaded.

---

## 7. Competitive Position

### Head-to-Head

| Factor | Owllight | Origin | Woosa | Emma | Sealy |
|---|---|---|---|---|---|
| Back care focus | ✅ Core | Partial | ❌ | ❌ | Partial |
| Price (queen hybrid) | **$899** ✅ | ~$1,200 | $1,949 | ~$999 | $1,500+ |
| Trial period | **100 nights** ✅ | 100 nights | 30 nights | 100 nights | Varies |
| Singapore-founded | ✅ | ✅ | ✅ | ❌ | ❌ |
| Lazada #1 | ✅ | Unknown | ❌ | ❌ | ❌ |
| CertiPUR-US | ✅ | Unknown | Unknown | Unknown | Varies |
| Editorial roundup presence | ❌ | ✅✅✅ | ✅✅✅ | ✅✅✅ | ✅✅ |

**Owllight's moat:** Back care specialisation + price leadership + 100-night trial. No competitor owns this combination. The gap is editorial presence and content depth.

### Competitors by Threat Level

**HIGH — Origin Mattress** (originmattress.com.sg)
- Runs own `/best-mattress-singapore/` page — ranking for the highest-volume keyword
- 50+ blog articles, strong backlinks from SG lifestyle media, DA ~35-45
- Owllight advantage: Back care specialisation, ~50% cheaper, same 100-night trial

**HIGH — Emma Sleep** (emma-sleep.com.sg)
- Global domain authority (~DA 50-60) flows to SG market
- In every Singapore roundup article; heavy influencer investment
- Owllight advantage: Local Singapore brand, Lazada #1 in topper category, back care niche

**MEDIUM — Woosa** (woosa.sg)
- Premium lifestyle brand; featured in virtually all SG roundups; DA ~30-40
- Owllight advantage: $899 vs $1,949 queen (54% cheaper), 100 nights vs 30 nights trial

**MEDIUM — Sealy** (sealy.com.sg)
- 120+ years heritage, "BackCare" product line competes directly on keywords
- Owllight advantage: Price, DTC value, back care as primary (not secondary) positioning

**LOW — King Koil** (kingkoil.com.sg)
- Premium hotel-quality, $1,200-$10,000+ price range
- Claims "Official mattress of the International Chiropractors Association"
- Owllight advantage: Price, specificity of back care technology claims

### Keyword Gaps

| Keyword | Who Ranks | Gap |
|---|---|---|
| best mattress singapore | Origin, Emma, Woosa | HIGH — create definitive guide |
| mattress for back pain singapore | Various | CRITICAL — core positioning |
| hybrid mattress singapore | Origin, Emma | HIGH — needs category page |
| best orthopedic mattress singapore | Sealy, King Koil | HIGH — core positioning |
| mattress under 1000 singapore | Various | HIGH — price advantage |
| mattress 100 night trial singapore | Woosa, others | QUICK WIN |

### Backlink Gap — Top Priority Outreach Targets

| Publication | Covers Competitors | Covers Owllight? |
|---|---|---|
| sethlui.com | Origin, Emma, Woosa | Not confirmed |
| thesmartlocal.com | Multiple brands | Not confirmed |
| bestinsingapore.co | 18 brands listed | Not confirmed |
| weavvehome.com | 15 brands | Not confirmed |
| modernhome.sg | Multiple brands | Not confirmed |

Getting featured in these roundups is the single highest-leverage activity for Owllight's SEO — these articles are where Singapore consumers start their research.

### Content Quality Benchmark

To compete for "best mattress singapore" keywords, content needs:
- **1,500-2,500+ words** minimum (top-ranking articles are 3,000-4,000)
- **Named author** with relevant credentials
- **Comparison tables** with data
- **Updated date** (SG roundups refresh seasonally; Google rewards freshness)
- **Internal links** to product pages

Owllight's current blog posts are likely too short and lack E-E-A-T signals to rank competitively.
