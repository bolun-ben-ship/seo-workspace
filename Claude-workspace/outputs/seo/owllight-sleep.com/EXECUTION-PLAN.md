# Execution Plan: owllight-sleep.com
**Date:** 2026-03-04 | **Horizon:** March 2026 – February 2027

Everything is prioritised. Start at the top — nothing below Phase 1 Week 1 matters until crawling is fixed.

---

## Critical Path

```
[Fix Cloudflare] → [robots.txt accessible] → [Submit sitemap] → [GSC data flows]
       └──────────→ [AI crawlers access site] → [AI citation possible]

[Install reviews app] → [10+ reviews/product] → [AggregateRating schema] → [Star ratings in SERPs]

[Author bio created] → [Add to all posts] → [E-E-A-T baseline] → [Blog content ranks]

[Comparison content] → [Link outreach] → [Editorial backlinks] → [DA increases] → [Competitive keywords unlock]
```

---

## Phase 1: Foundation (Weeks 1–4, March 2026)

*Nothing else reaches its potential until these are done.*

### Week 1 — Technical Emergency

**DAY 1-2: Fix Cloudflare** ← START HERE
- [ ] Cloudflare → Security → Bots → Bot Fight Mode → enable verified bots allowlist
- [ ] Add WAF Custom Rule: `Known Bots = true` → Action: Skip all security rules
- [ ] Verify: `curl -I https://www.owllight-sleep.com/robots.txt` returns `HTTP/2 200`
- [ ] Verify: `curl https://www.owllight-sleep.com/sitemap.xml` returns XML
- **Time:** 1-2 hrs | **Owner:** Developer / site admin

**DAY 2-3: robots.txt**
- [ ] Read `robots.txt` content once accessible
- [ ] Confirm no `Disallow: /` or blocks on key directories
- [ ] Confirm `Sitemap:` directive is present
- [ ] Add explicit allowances for GPTBot, ClaudeBot, PerplexityBot
- **Time:** 30 min

**DAY 3-4: Google Search Console**
- [ ] Verify GSC ownership
- [ ] Submit sitemap: `https://www.owllight-sleep.com/sitemap.xml`
- [ ] Request manual indexing for 5 pages: Homepage, Tulip product, Topper product, Showroom, Woosa post
- **Time:** 1 hr

**DAY 4-5: URL Audit**
- [ ] Audit all URLs — map which use `/en/` prefix vs which don't
- [ ] Check Shopify Markets / language app settings
- [ ] Decide: commit to `/en/` with hreflang, OR remove and standardise to `/blogs/`
- [ ] Plan 301 redirects (do NOT implement yet — Week 3)
- **Time:** 2-3 hrs

### Week 2 — Analytics & Baseline

- [ ] Confirm GA4 is installed and tracking correctly
- [ ] Set up GSC keyword tracking for Tier 1 keywords
- [ ] Run PageSpeed Insights for homepage + Tulip product page — **document the scores as baseline**
- [ ] Submit to Bing Webmaster Tools
- **Time:** 3-4 hrs

### Week 3 — On-Page Quick Wins

- [ ] Update `/collections` title → "Mattresses & Sleep Products Singapore | Owllight"
- [ ] Update showroom page title → "Mattress Showroom Singapore | 22 Sin Ming Lane | Owllight"
- [ ] Update Woosa post title → "Woosa Mattress Review vs Owllight Tulip | Singapore 2026"
- [ ] Add placeholder author bylines to all existing blog posts
- [ ] Implement 301 redirects approved in Week 1 URL audit
- **Time:** 3-4 hrs

### Week 4 — Schema Foundation

- [ ] Audit current Product schema (Google Rich Results Test)
- [ ] Install Judge.me (Shopify reviews) — free tier
- [ ] Import existing reviews from Lazada/Amazon
- [ ] Add LocalBusiness JSON-LD to showroom page
- [ ] Add Organization JSON-LD to homepage
- **Time:** 4-6 hrs

**Phase 1 done when:**
- ✅ robots.txt returns 200
- ✅ Sitemap submitted to GSC
- ✅ PageSpeed baseline documented
- ✅ Reviews app installed, import started
- ✅ Quick-win title tags updated

---

## Phase 2: Expansion (Weeks 5–12, April–May 2026)

*Build E-E-A-T foundation and publish first high-value content.*

### Week 5-6 — About Page + Author Setup

- [ ] Write and publish `/pages/about-owllight`
  - Founder back pain story, brand mission, team, showroom, milestones (Lazada #1, Dubai exhibition)
  - Organization + Person schema
  - ~800-1,000 words
- [ ] Create author profile page for primary blog writer
  - Photo, bio, credentials, LinkedIn
  - Person schema
- [ ] Link author profile from all existing blog posts
- **Time:** 6-8 hrs

### Week 7-8 — First Priority Blog Post

**"Best Mattress for Back Pain Singapore (2026 Guide)"**
- URL: `/blogs/sleep/best-mattress-for-back-pain-singapore`
- Keywords: "best mattress for back pain singapore", "orthopedic mattress singapore" (200-500/mo)
- 2,000+ words | Author byline | FAQ section (6+ questions)
- Structure: Singapore back pain context → what to look for → top picks table (Owllight #1) → FAQ
- Schema: BlogPosting, FAQPage, Person
- CTA → Tulip Mattress product page
- Submit to GSC for indexing after publish
- **Time:** 8-10 hrs

### Week 9-10 — Evergreen Buying Guide

**"Best Mattress Singapore — 2026 Buyer's Guide"**
- URL: `/pages/best-mattress-singapore` (static page, not blog — higher authority signal)
- Keyword: "best mattress singapore" (1,000-2,400/mo — top priority)
- 2,500+ words | Comparison table: Owllight vs Origin vs Woosa vs Emma vs Sealy vs King Koil
- Budget guide (under $500, $500-$1,200, $1,200+) | FAQ section (8 questions)
- Schema: Article, FAQPage
- Add "Last updated: [month/year]" — refresh quarterly
- Submit to GSC immediately after publish
- **Time:** 10-12 hrs

### Week 11-12 — Product Schema + Performance

- [ ] Once 10+ reviews collected: activate AggregateRating schema on Tulip and Topper pages
- [ ] Validate at: https://search.google.com/test/rich-results
- [ ] Address top 3 PageSpeed issues from Week 2 baseline (likely: image sizes, unused JS, LCP preload)
- [ ] Add FAQ section to Tulip product page (6-8 questions with FAQPage schema)
- **Time:** 6-8 hrs

**Phase 2 done when:**
- ✅ About page live with author bios linked
- ✅ 2 new high-value pieces published
- ✅ AggregateRating schema active (stars may take 4-6 weeks to appear in SERPs)
- ✅ PageSpeed improved vs baseline

---

## Phase 3: Scale (Weeks 13–24, June–September 2026)

*Topical authority via comparison content + link building outreach.*

### May–June: Comparison Content Sprint (4 posts)

Each post: 2,000+ words, author bio, FAQ, internal link to product page.

| Post | URL | Target Keyword | Vol |
|---|---|---|---|
| Origin Mattress Review vs Owllight | `/blogs/sleep/origin-mattress-review-singapore` | "origin mattress review singapore" | 400-900 |
| Emma Mattress Review vs Owllight | `/blogs/sleep/emma-mattress-review-singapore` | "emma mattress review singapore" | 300-700 |
| Best Hybrid Mattress Singapore 2026 | `/blogs/sleep/best-hybrid-mattress-singapore` | "hybrid mattress singapore" | 500-1,200 |
| Best Mattress Under $1,000 Singapore | `/blogs/sleep/best-mattress-under-1000-singapore` | "mattress under 1000 singapore" | 100-300 |

### June–July: Refresh Existing Posts

- [ ] Expand Woosa review to 2,000+ words (migrate URL, add comparison table, FAQ, author)
- [ ] Expand Sealy vs Simmons to include Owllight comparison (migrate URL, add FAQ, author)
- [ ] Implement 301 redirects from old `/en/blogs/` URLs to new `/blogs/sleep/` URLs
- **Time:** 4-5 hrs each

### July–September: Link Building (Start Now, Sustain Through Month 12)

- [ ] Identify editorial contacts at: sethlui.com, thesmartlocal.com, bestinsingapore.co, weavvehome.com, modernhome.sg
- [ ] Prepare outreach kit: brand overview, product specs, 100-night trial offer, CertiPUR-US cert, Lazada #1 proof
- [ ] Offer product sample for review + high-res photography
- [ ] Target: 3 editorial features by end of Phase 3
- [ ] Complete Google Business Profile (if not done)
- **Time:** 8 hrs/month ongoing

### August–September: Educational Content (4 posts)

| Post | URL | Target Keyword |
|---|---|---|
| How to Choose a Mattress Singapore | `/blogs/sleep/how-to-choose-mattress-singapore` | "how to choose mattress singapore" |
| Mattress Firmness Guide | `/blogs/sleep/mattress-firmness-guide` | "mattress firmness guide" |
| Latex vs Hybrid Mattress Singapore | `/blogs/sleep/latex-vs-hybrid-mattress-singapore` | "latex vs hybrid mattress singapore" |
| Mattress Topper vs New Mattress | `/blogs/sleep/mattress-topper-vs-new-mattress` | "mattress topper vs new mattress" |

**Phase 3 done when:**
- ✅ 15+ blog posts published
- ✅ 3 competitor comparisons live (Origin, Emma, Woosa)
- ✅ 1+ editorial backlink from Singapore media
- ✅ Organic sessions: 3,000-5,000/month
- ✅ Top 10 for 10+ target keywords

---

## Phase 4: Authority (Months 7–12, October 2026 – February 2027)

*Compound the content, dominate back care niche, capture seasonal traffic.*

### October–November

- [ ] Best Mattress for HDB Singapore (`/blogs/sleep/best-mattress-hdb-singapore`)
- [ ] Sleeping Position Guide for Back Pain (`/blogs/sleep/sleeping-position-back-pain-guide`)
- [ ] Create `/pages/mattress-trial-singapore` — standalone 100-night trial page
- [ ] "Mattress Sale Singapore 2026" — publish early November for year-end shopping
- [ ] GSC review: identify new keyword opportunities from 6 months of data
- [ ] Pursue 2 more editorial mentions

### November–December

- [ ] Implement ProductGroup schema for size variants (Single/Queen/King)
- [ ] Add OfferShippingDetails schema → Google Merchant Center eligibility
- [ ] Implement `llms.txt` at site root
- [ ] Submit to Google Merchant Center (free Shopping listings)
- [ ] Mattress Warranty Singapore post (`/blogs/sleep/mattress-warranty-singapore`)
- [ ] How Long Does a Mattress Last (`/blogs/sleep/how-long-does-mattress-last`)

### January–February 2027

- [ ] Full SEO audit — compare all metrics against Phase 1 baseline
- [ ] Refresh all comparison posts: update 2027 dates, current prices
- [ ] Identify 5 new keyword opportunities from 12 months of GSC search query data
- [ ] Set Year 2 KPI targets
- [ ] Audit `/en/` hreflang strategy if international expansion is active

**Phase 4 done when:**
- ✅ 28+ published pieces
- ✅ 5+ editorial backlinks
- ✅ Top 5 for "best mattress for back pain singapore"
- ✅ Top 10 for "best mattress singapore"
- ✅ Organic sessions: 10,000-15,000/month
- ✅ Google Shopping listings active

---

## Full Content Calendar

| Month | Piece | Priority | Type |
|---|---|---|---|
| March W1-2 | About Owllight page | Critical | Static page |
| March W3-4 | Best mattress for back pain SG | Critical | Blog |
| April W1-2 | Mattress topper for back pain | High | Blog |
| April W3-4 | Best Mattress Singapore guide | Critical | Static page |
| May W1 | Origin mattress review | High | Blog |
| May W3 | Emma mattress review | High | Blog |
| June W1 | Best hybrid mattress SG | High | Blog |
| June W3 | Best mattress under $1,000 | High | Blog |
| July W1 | Woosa review (migrate + expand) | High | Refresh |
| July W3 | Sealy vs Simmons (migrate + expand) | High | Refresh |
| August W1 | How to choose mattress SG | Medium | Blog |
| August W3 | Mattress firmness guide | Medium | Blog |
| September W1 | Latex vs hybrid mattress SG | Medium | Blog |
| September W3 | Topper vs new mattress | Medium | Blog |
| October W1 | Best mattress for HDB SG | Medium | Blog |
| October W3 | Sleeping position back pain | Medium | Blog |
| November W1 | Mattress sale SG 2026 | High (seasonal) | Blog |
| November W3 | Mattress warranty SG | Low | Blog |
| December W1 | How long does mattress last | Low | Blog |
| December W3 | Refresh Best Mattress SG guide | High | Refresh |

**Total: 18 new + 2 refreshes = 20 pieces, ~2/month**

### Content Standards (apply to every piece)

1. Minimum 1,500 words (2,000+ for comparison posts)
2. Named author with bio — no anonymous content in this YMYL-adjacent niche
3. Every comparison post must CTA-link to a product page
4. Singapore-first framing: HDB context, climate, Lazada/local availability
5. Add "Last updated: [month/year]" — refresh annually minimum

### Author Setup (Do Before First Post)

1. Create author profile page with photo, bio, credentials, LinkedIn link
2. Implement Person schema on author page
3. Apply author to all new AND existing blog posts retroactively
4. If no in-house expert: partner with a Singapore physiotherapist for "Reviewed by" credits on back care content

---

## KPI Tracking Schedule

| Metric | Tool | Frequency |
|---|---|---|
| Organic sessions | GA4 | Weekly |
| Keyword rankings | GSC / Semrush | Bi-weekly |
| Indexed pages | GSC Coverage | Weekly (Phase 1-2) |
| Core Web Vitals | GSC / PageSpeed | Monthly |
| Backlinks earned | Ahrefs / Semrush | Monthly |
| Review count + rating | Judge.me dashboard | Weekly |
| Rich results status | GSC Enhancements | Monthly |

---

## Quick Reference: ROI by Action

| Action | Time to Impact | Effort | ROI |
|---|---|---|---|
| Fix Cloudflare | 1-2 days | 1 hr | Critical / foundational |
| Submit sitemap | 1 week | 30 min | High |
| AggregateRating schema | 4-6 weeks | 4 hrs | High — CTR uplift |
| "Best mattress for back pain SG" post | 4-8 weeks | 10 hrs | High |
| "Best Mattress Singapore" guide | 6-12 weeks | 12 hrs | Very high |
| Competitor comparison posts | 8-16 weeks | 8 hrs each | High |
| Editorial link outreach | 3-6 months | 8 hrs/month | Very high (slow build) |
| Core Web Vitals fixes | 2-4 weeks | Variable | Medium-High |
