# Implementation Plan — vpublish.com.sg
**Generated:** 2026-03-11
**Starting Score:** 29/100 → **Target:** 65/100 (Month 3) → 78/100 (Month 12)

---

## Strategic Position

Visual Publish competes in a two-tier Singapore printing market:
- **Tier 1** (Gogoprint, VistaPrint): E-commerce-first, high domain authority, consumer/SME focus
- **Tier 2** (Print City, OneDayPrint): Local specialists with active blogs, GBP presence, managed SEO

Visual Publish currently sits below both tiers. The path up is not to outspend Tier 1 on product catalog SEO. It's to own the **B2B commercial printing content** narrative that no competitor holds — educational content for marketing managers, procurement teams, and agency creatives.

### Competitor Snapshot

| Competitor | Keyword Dominance | Content | Weakness VP Can Exploit |
|---|---|---|---|
| Gogoprint | Name cards, stickers, brochures | Product pages only | No educational content; consumer-only |
| Print City | Offset, brochures, events | Active blog, agency-managed | Less depth on corporate/commercial angle |
| OneDayPrint | Sticker specialist, urgency focus | Blog + case studies | Narrow service range; consumer tone |
| VistaPrint | Name cards, SME marketing | SME education blog | Generic; premium-priced; not local |
| Universal Print | Commercial offset, B2B | No content — invisible | VP can own this space first |

**The gap:** No Singapore printer produces quality technical content for B2B buyers. This is fast to rank and directly supports commercial intent.

### KPI Targets

| Metric | Now | Month 3 | Month 6 | Month 12 |
|--------|-----|---------|---------|----------|
| SEO Score | 29/100 | 55/100 | 68/100 | 78/100 |
| Organic sessions | Unknown (no tracking) | Measurable | +20% vs baseline | +80% vs baseline |
| Target keywords Top 20 | ~0 | 3–5 | 8–12 | 20–30 |
| Blog posts | 0 | 0 | 4 | 12 |
| GBP reviews (new) | 0 | +5 | +15 | +30 |
| Directory citations | Unknown | 5 | 10 | 20 |
| Schema rich results | 0 | 1 | 3 | 5+ |

---

## Phase 1 — Foundation (Weeks 1–4)
**Goal:** Remove everything blocking the site. Restore data. No creative work.
**Score impact:** 29 → 52

### Week 1 — Analytics, Titles, Meta Descriptions
*Estimated time: 4–6 hours*

| Task | How | Time |
|------|-----|------|
| Create GA4 property; add GA4 tag in GTM (GTM-PQZD52F); remove dead UA tag | GTM > Tags > New > GA4 Configuration | 1–2h |
| Add contact form + phone click conversion events in GA4 | GTM event triggers | 1h |
| Fix homepage title → `Offset & Sticker Printing Services Singapore \| Visual Publish` | WP Admin > SEO plugin or theme | 5m |
| Write and publish meta descriptions for all pages (see below) | WP Admin > Yoast/RankMath per page | 1–2h |
| Remove `/services/` 404 from sitemap | WP sitemap settings or manual XML edit | 15m |

**Meta descriptions to write:**

| Page | Description (≤155 chars) |
|------|--------------------------|
| Homepage | "Visual Publish offers offset, sticker, and brochure printing in Singapore. 15+ years experience. Call +65 6273 2590 or request a quote today." |
| Offset Printing | "Professional offset printing in Singapore for brochures, catalogues, and high-volume runs. Competitive rates, 15+ years experience. Get a quote." |
| Sticker Printing | "Custom sticker printing in Singapore — vinyl, waterproof, die-cut, and roll stickers. Fast turnaround, quality finish. Request a quote from Visual Publish." |
| About Us | "Visual Publish is a trusted Singapore printing company with 15+ years of experience in offset, digital, and specialty printing. Henderson Industrial Park." |
| Contact | "Contact Visual Publish at +65 6273 2590 or visit us at Henderson Industrial Park. Get a printing quote for offset, sticker, or brochure printing in Singapore." |
| Portfolio | "View Visual Publish's printing portfolio — brochures, name cards, stickers, and offset samples from our 15+ years of Singapore printing work." |

---

### Week 2 — Schema, Headings, Duplicate URLs
*Estimated time: 2–3 hours*

| Task | How | Time |
|------|-----|------|
| Fix schema: `@context` → `https://schema.org` | Theme functions.php or schema plugin | 30m |
| Fix schema: `name` → "Visual Publish" | Same edit | 5m |
| Fix schema: all URLs to `https://vpublish.com.sg/` | Same edit | 5m |
| Fix schema: `geo.latitude` → 1.2856, `geo.longitude` → 103.8199 | Same edit | 5m |
| Fix schema: `priceRange` → "$$"; remove duplicate `telephone` key | Same edit | 5m |
| Remove H1 "Home" from homepage (keep H1 "Offset / Sticker Printing Services") | Theme template or page builder | 15m |
| Add H1 to About Us: "About Visual Publish — Singapore Printing Since [year]" | WP page editor | 10m |
| 301 redirect `/sticker-printing-services-singapore/` → `/sticker-printing-singapore/` | .htaccess or Redirection plugin | 10m |
| 301 redirect `/printing-services-singapore/` → `/offset-printing-singapore/` | .htaccess or Redirection plugin | 10m |

**Corrected schema block:**
```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "PrintService"],
  "name": "Visual Publish",
  "url": "https://vpublish.com.sg/",
  "telephone": "+6562732590",
  "openingHours": "Mo-Fr 09:00-19:00",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Blk 203A, #05-01 Henderson Industrial Park, Henderson Road",
    "addressLocality": "Singapore",
    "postalCode": "159546",
    "addressCountry": "SG"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 1.2856,
    "longitude": 103.8199
  },
  "logo": "https://vpublish.com.sg/wp-content/uploads/2016/10/logo.png"
}
```

---

### Week 3 — Performance, Security, Sitemap, robots.txt
*Estimated time: 2 hours*

| Task | How | Time |
|------|-----|------|
| Install WP Super Cache; enable simple mode | WP Plugins > Add New | 20m |
| Test TTFB after caching: `curl -s https://vpublish.com.sg/ -o /dev/null -w "TTFB: %{time_starttransfer}s\n"` | Terminal | 5m |
| Fix robots.txt: change `www.vpublish.com.sg/sitemap.xml` → `vpublish.com.sg/sitemap.xml` | cPanel file manager or WP editor | 5m |
| Regenerate sitemap with non-www URLs and fresh lastmod dates | Yoast/RankMath sitemap regenerate | 15m |
| Submit sitemap to Google Search Console | GSC > Sitemaps | 5m |
| Add security headers to `.htaccess` (see below) | cPanel or FTP | 15m |
| Block xmlrpc.php in `.htaccess` | Same file | 5m |
| Remove WP version from asset URLs | functions.php: `remove_action('wp_head', 'wp_generator');` | 10m |

**Security headers for `.htaccess`:**
```apache
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>

<Files xmlrpc.php>
    Order Deny,Allow
    Deny from all
</Files>
```

---

### Week 4 — Homepage & Analytics Verification
*Estimated time: 3–4 hours*

| Task | How | Time |
|------|-----|------|
| Rewrite homepage copy to 600w+ with clear value prop | WP page editor | 2–3h |
| Add OG meta tags to homepage | Yoast/RankMath > Social tab | 30m |
| Expand Contact page to 300w+ (add Henderson location context, hours, quote process) | WP page editor | 1h |
| Expand About page with E-E-A-T signals (founding year, equipment, team) | WP page editor | 1–2h |
| Verify GA4 is recording sessions | GA4 Realtime report | 10m |
| Connect GA4 to Google Search Console | GA4 > Admin > Search Console linking | 10m |

---

## Phase 2 — Content Depth (Weeks 5–12)
**Goal:** Build service page authority. Launch GBP. Secure directory citations.
**Score impact:** 52 → 65

### Site Architecture (Target State)

**Recommended URL structure:**
```
/
├── /services/                    (hub — 400w overview)
│   ├── /services/offset-printing/     (800w+, FAQ, schema)
│   ├── /services/sticker-printing/    (800w+, FAQ, schema)
│   ├── /services/name-card-printing/  (NEW — 800w+, FAQ)
│   ├── /services/brochure-printing/   (NEW — 800w+, FAQ)
│   ├── /services/envelope-printing/   (NEW — 500w)
│   └── /services/bindery-services/    (NEW — 500w)
├── /portfolio/                   (400w+ with image captions)
├── /about/                       (600w+, E-E-A-T signals)
├── /faq/                         (600w+ hub, PAA targets)
├── /contact/                     (300w+, map, hours)
└── /blog/                        (Phase 3+)
```

**Redirects to implement when restructuring URLs:**

| From | To | Type |
|------|----|------|
| /offset-printing-singapore/ | /services/offset-printing/ | 301 |
| /sticker-printing-singapore/ | /services/sticker-printing/ | 301 |
| /printing-portfolio/ | /portfolio/ | 301 |
| /about-us/ | /about/ | 301 |
| /contact-us/ | /contact/ | 301 |

> If URL restructure is too disruptive, keep current URLs and build new pages at new paths. Either is valid — consistency matters more than the specific path.

### Weeks 5–6 — Expand Core Service Pages

| Task | Target | Time |
|------|--------|------|
| Expand offset printing page to 800–1000w | /offset-printing-singapore/ | 3–4h |
| Add 5-question FAQ to offset page | Same page | 1h |
| Add FAQPage schema to offset page | Dev | 30m |
| Expand sticker printing page to 800–1000w | /sticker-printing-singapore/ | 3–4h |
| Add 5-question FAQ to sticker page | Same page | 1h |
| Add FAQPage schema to sticker page | Dev | 30m |

**Offset printing FAQ targets:** What is offset printing? / Minimum print run? / Offset vs digital — which should I use? / How long does it take? / What file formats do you accept?

**Sticker printing FAQ targets:** What types of stickers do you print? / Are vinyl stickers waterproof? / Minimum order quantity? / How long do outdoor stickers last? / What materials are available?

### Weeks 7–8 — New Service Pages

| Page | Keyword Target | Word Count | Time |
|------|---------------|-----------|------|
| /services/name-card-printing/ | "name card printing singapore" | 800w+ | 4–5h |
| /services/brochure-printing/ | "brochure printing singapore" | 800w+ | 4–5h |
| /services/ hub | "printing services singapore" | 400w | 1h |
| /services/envelope-printing/ | "envelope printing singapore" | 500w | 2h |
| /services/bindery-services/ | "bindery services singapore" | 500w | 2h |
| /faq/ hub | PAA questions | 600w+ | 2h |
| /portfolio/ with captions | "printing portfolio singapore" | 400w+ | 2h |

Add BreadcrumbList schema and contextual body links (each service page links to 2 related service pages) across all new pages.

### Weeks 9–10 — Google Business Profile

| Task | Time |
|------|------|
| Claim/verify GBP (video verification now standard) | 1–2h |
| Set exact hours: Mon–Fri 09:00–19:00 | 10m |
| Upload 10+ photos: facility, equipment, finished products | 1h |
| Add all services as GBP service entries | 30m |
| Enable WhatsApp messaging | 15m |
| Write GBP description (750 chars, include primary keywords) | 30m |
| Respond to all existing reviews | 30m |
| Set up post-job review request template (WhatsApp/email) | 1h |

**NAP consistency — use exactly this across all platforms:**
- Name: Visual Publish
- Address: Blk 203A, #05-01 Henderson Industrial Park, Henderson Road, Singapore 159546
- Phone: +65 6273 2590
- Website: https://vpublish.com.sg/

### Weeks 11–12 — Directory Citations

Priority order for citation submission:

| Directory | URL | Action |
|-----------|-----|--------|
| Best in Singapore | bestinsingapore.co/best-printing-services-singapore | Submit for listing |
| Pullupstand | pullupstand.com/blogs/blog/best-printing-company-singapore | Email for inclusion |
| MeowPrint | meowprint.sg/blog/printing-services-singapore | Outreach for mention |
| Sethlui | sethlui.com/best-printing-shop-guide-singapore | Submit for feature |
| Yelp Singapore | yelp.com | Create/claim listing |
| StreetDirectory | streetdirectory.com | Create/claim listing |
| SGPBusiness | sgpbusiness.com | Create listing |

These roundup sites are also AI citation sources — appearing in them is a dual-purpose SEO + GEO action.

---

## Phase 3 — Blog Launch (Months 4–6)
**Goal:** Rank for informational queries. Build topical authority. Target PAA placements.
**Score impact:** 65 → 72

### Content Calendar

| Month | Post | Target Keyword | Word Count | Difficulty |
|-------|------|---------------|-----------|------------|
| July 2026 | "Offset Printing vs Digital Printing: Which is Right for Your Project?" | offset vs digital printing | 1,500w | Medium |
| Aug 2026 | "The Complete Guide to Name Card Printing in Singapore (2026)" | name card printing guide | 1,500w | Low |
| Sep 2026 | "How to Prepare Print-Ready Files: The Complete Checklist" | how to prepare print ready files | 1,200w | Very Low |
| Oct 2026 | "Paper Weight Guide: Understanding GSM for Printing" | paper weight gsm guide | 1,000w | Very Low |
| Nov 2026 | "Sticker Materials Guide: Vinyl, Paper, or Polyester?" | sticker material guide singapore | 1,200w | Low |
| Dec 2026 | "Corporate Printing Checklist for Marketing Teams" | corporate printing singapore | 1,200w | Medium |
| Jan 2027 | "Brochure Sizes, Folds, and Specifications in Singapore" | brochure printing singapore specs | 1,000w | Low |
| Feb 2027 | "How to Brief a Printer: A Guide for Marketing Managers" | how to brief a printer | 1,000w | Very Low |

**Content quality rules for every piece:**
- [ ] Direct answer in first 100 words (answer-first format)
- [ ] Contains at least one specific, verifiable claim (turnaround time, minimum quantity, spec)
- [ ] No generic language without supporting evidence
- [ ] Internal links to 2+ related service pages
- [ ] FAQ section with FAQPage schema
- [ ] CTA at end (quote request, phone number)
- [ ] Meta description within 155 chars

**Seasonal content opportunities:** National Day (Aug) — sticker/flag printing; Year-end (Nov–Dec) — corporate card and event printing; New Year (Jan) — name card refresh campaigns.

---

## Phase 4 — Scale (Months 7–12)
**Goal:** Compound authority, accumulate reviews, expand rankings.
**Score impact:** 72 → 78

| Quarter | Key Milestones |
|---------|---------------|
| Q3 2026 | 3 blogs live; 10+ citations; 10+ new GBP reviews; 5 keywords in Top 20 |
| Q4 2026 | 6 blogs live; AggregateRating schema (if reviews displayed); 20+ citations |
| Q1 2027 | 9 blogs live; 1 "best of" backlink secured; organic traffic measurably up vs Month 3 |
| Q2 2027 | 12 blogs live; content refresh cycle begins (update top posts with new data) |

**Additional Phase 4 tasks:**
- Convert images to WebP (WebP Express plugin — auto-converts JPEG/PNG, ~30% size saving)
- Add breadcrumb schema across all service pages
- Add AggregateRating schema when Google reviews are displayed on-site
- Update WordPress to current version (6.7.x+) — test on staging first
- Remove IE conditional comments from theme templates

---

## Resource Requirements

| Phase | Hours/Week | Total |
|-------|-----------|-------|
| Phase 1 (Weeks 1–4) | 5–8h | ~25h |
| Phase 2 (Weeks 5–12) | 4–6h | ~40h |
| Phase 3 (Months 4–6) | 3–4h | ~40h |
| Phase 4 (Months 7–12) | 2–3h/month | ~15h |
| **Year 1 total** | | **~120h** |

**Tools required (all free):**
- Google Search Console + GA4
- GTM (already active)
- Yoast SEO or RankMath (free tier)
- WP Super Cache
- WebP Express (Phase 4)

**Developer needed for:** .htaccess edits, schema hardcode fixes, PHP functions.php changes, URL redirects.

---

## Milestone Checklist

### Month 1
- [ ] GA4 live and recording
- [ ] All pages have meta descriptions
- [ ] Homepage title includes keywords
- [ ] Schema is valid (test: validator.schema.org)
- [ ] TTFB below 200ms
- [ ] Sitemap submitted to Search Console

### Month 3
- [ ] All core service pages at 800w+ with FAQ sections
- [ ] GBP verified and fully optimised
- [ ] 5 new Google reviews
- [ ] 3 directory citations secured
- [ ] Contextual internal linking across all service pages
- [ ] SEO score ≥ 55/100

### Month 6
- [ ] Blog live with 3+ posts
- [ ] 1 "best of" directory listing secured
- [ ] 10+ new Google reviews
- [ ] Organic impressions growing month-over-month (verified in GSC)
- [ ] SEO score ≥ 65/100

### Month 12
- [ ] 12 blog posts published
- [ ] 5+ target keywords in Top 20
- [ ] 20+ directory citations
- [ ] Organic traffic measurably higher than Month 3 baseline
- [ ] SEO score ≥ 78/100
