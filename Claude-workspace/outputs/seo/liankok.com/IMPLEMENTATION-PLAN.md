# Implementation Plan: liankok.com
**Date:** 2026-03-04
**Duration:** 12 months, 4 phases

---

## Phase 1 — Foundation (Weeks 1–4)
**Goal:** Fix all critical blockers. Nothing new ranks until the site is clean.
**Effort:** ~15–20 hours total (one-time)

### Week 1: Index Cleanup
- [ ] Delete or noindex all 30+ demo/template pages (full list in SITE-AND-CONTENT-PLAN.md)
- [ ] Delete off-topic posts: `/hello-world/`, `/blog-standard/`, `/what-can-paralegals-do-a-guide-for-lawyers/`, `/better-products-when-companies-work-together/`
- [ ] Set 301 redirects: `/about-2/` → `/about/`, `/shop-2/` → `/products/`, `/cart-2/` → `/cart/`
- [ ] Noindex `/cart/`, `/checkout/`, `/accounts/` via Yoast
- [ ] Submit updated sitemap to Google Search Console

### Week 2: On-Page Essentials
- [ ] **Fix H1 on homepage** — change carousel items from H1 to H2/H3; add ONE H1: "Singapore's Trusted ABB Authorised Electrical Distributor Since 1975"
- [ ] **Add meta descriptions** to all core pages (copy below)
- [ ] **Fix page title tags** (table below)
- [ ] **Shorten blog post title** — from 88 chars to ~60: "ABB MCB Guide: Miniature Circuit Breakers in Singapore"
- [ ] **Fix robots.txt** — remove `sitemap.xml` and `sitemap.html` entries, keep only `sitemap_index.xml`
- [ ] **Change lang attribute** from `en-US` to `en-SG`

**Suggested meta descriptions:**
| Page | Copy (max 160 chars) |
|---|---|
| /about/ | "Lian Kok Electrical has been Singapore's trusted electrical solutions provider since 1975. ABB Authorised Distributor supplying quality LV products to residential, commercial and industrial clients." |
| /products/ | "Browse ABB low voltage products distributed by Lian Kok Electrical in Singapore — MCBs, RCDs, contactors, switchgear, wiring accessories and more." |
| /contact/ | "Contact Lian Kok Electrical at Block 681 Race Course Road, Singapore. Get expert advice on ABB electrical products. Call or enquire online." |
| /blog-2/ (or /resources/) | "Electrical guides and product insights from Lian Kok Electrical — Singapore's ABB Authorised Distributor since 1991." |

**Improved page title tags:**
| Page | Current | Recommended |
|---|---|---|
| /about/ | About - Lian Kok Electrical | About Lian Kok Electrical \| Singapore Electrical Distributor Since 1975 |
| /products/ | Products - Lian Kok Electrical | ABB Electrical Products Singapore \| Lian Kok Electrical |
| /contact/ | Contact - Lian Kok Electrical | Contact Us \| Lian Kok Electrical Singapore |
| /blog-2/ | Blog - Lian Kok Electrical | Electrical Guides & Resources \| Lian Kok Electrical |

### Week 3: Schema + Local SEO
- [ ] **Add LocalBusiness schema** to homepage (template below)
- [ ] **Update Yoast Organization schema** — add telephone, address, openingHours, foundingDate
- [ ] **Fix Article schema** on all blog posts — replace `"name": "admin"` with real author name
- [ ] **Create author profile page** in WordPress with real name, photo, short bio, credentials
- [ ] **Set up / complete Google Business Profile:**
  - Verify if not done
  - Categories: Primary "Electrical Equipment Supplier"; Secondary "Electrical Contractor"
  - Add all services and products
  - Upload 10+ photos (counter, products, team, ABB signage)
  - Enable WhatsApp as messaging channel
  - Add specific Singapore districts to service area (not "all of Singapore")
  - Set accurate business hours (hours = top-5 local ranking factor in 2026)

**LocalBusiness Schema (add to homepage `<head>` or via Yoast):**
```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "Store"],
  "additionalType": "https://schema.org/ElectricalContractor",
  "name": "Lian Kok Electrical",
  "description": "ABB Authorised Distributor in Singapore since 1991. Supplying quality low voltage electrical products since 1975.",
  "url": "https://liankok.com",
  "telephone": "[PHONE]",
  "email": "[EMAIL]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Block 681 Race Course Road, #01-317",
    "addressLocality": "Singapore",
    "postalCode": "210681",
    "addressCountry": "SG"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "1.3214",
    "longitude": "103.8476"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "priceRange": "$$",
  "areaServed": { "@type": "Country", "name": "Singapore" },
  "brand": { "@type": "Brand", "name": "ABB" },
  "foundingDate": "1975",
  "sameAs": [
    "https://www.facebook.com/[PAGE]",
    "[GOOGLE BUSINESS PROFILE URL]"
  ]
}
```

### Week 4: Performance + Image Alt Text
- [ ] **Install WP Rocket** (Apache server detected — not LiteSpeed, so use WP Rocket over LiteSpeed Cache)
  - Enable page caching
  - Minify CSS and JavaScript
  - Defer Facebook Pixel and WPForms scripts
- [ ] **Enable Cloudflare** (free tier) as CDN/proxy
- [ ] **Image alt text sprint — priority order:**
  1. Homepage hero/banner images (min 5)
  2. All 21 product page images
  3. About page photos
  4. Blog post images
- [ ] **Verify Google Search Console** — submit sitemap, check index coverage
- [ ] **Submit sitemap to Bing Webmaster Tools**

**Target:** TTFB < 800ms on homepage and products page

**Phase 1 Success Criteria:**
- Zero demo pages indexed
- All core pages have meta descriptions
- Homepage has exactly one H1
- LocalBusiness schema live and validated (use Google Rich Results Test)
- GBP verified, complete, photos uploaded
- TTFB < 1.0s

---

## Phase 2 — Expansion (Weeks 5–12)
**Goal:** Build product authority and content depth.
**Effort:** 4–6 hours/week

### Weeks 5–6: Product Pages
- [ ] Expand all 21 product pages from ~370 words to **800–1,200 words** each
  - Priority: MCBs → Contactors → RCDs → MCCBs → Softstarters
  - Each page structure: overview (2–3 paras) + specs table + Singapore applications + why choose + FAQ (2–4 Qs) + related products
- [ ] **Add Product schema** to all WooCommerce products via Schema Pro or Rank Math
  - Required fields: name, description, brand (ABB), image, SKU, availability
- [ ] **Complete image alt text** on all remaining images
- [ ] **Improve internal linking** — product pages → category → homepage

**Product Schema example:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "ABB S200 Miniature Circuit Breaker",
  "description": "ABB S200 series MCB for residential and commercial use in Singapore. IEC 60898 certified.",
  "brand": { "@type": "Brand", "name": "ABB" },
  "image": "https://liankok.com/wp-content/uploads/[image].jpg",
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "url": "https://liankok.com/products/circuit-breakers/miniature-circuit-breakers/",
    "priceCurrency": "SGD",
    "seller": { "@type": "Organization", "name": "Lian Kok Electrical" }
  }
}
```

### Weeks 7–8: Content Hub
- [ ] **Create `/abb-singapore/` authority page** (2,000+ words)
  - Cover: ABB partnership history, product range overview, why choose Lian Kok, certifications
  - Target keyword: "ABB Singapore", "ABB authorised distributor Singapore"
- [ ] **Expand existing MCB guide** to 2,500 words
- [ ] **Publish: ABB RCD/SRCD Guide Singapore** (1,800 words)
- [ ] **Create `/resources/` hub page** (redirect from `/blog-2/`)

### Weeks 9–10: Category Structure
- [ ] **Add product category pages** with 400+ words each (Circuit Breakers, Contactors, etc.)
- [ ] **Add CollectionPage + ItemList schema** to category pages
- [ ] **Restructure product URLs** if dev resource available (see URL migration table in SITE-AND-CONTENT-PLAN.md)

### Weeks 11–12: FAQ + About
- [ ] **Build /faq/ page** with 12 Q&As (seed topics in SITE-AND-CONTENT-PLAN.md)
- [ ] **Add FAQPage schema** to /faq/
- [ ] **Expand /about/ to 1,000+ words:**
  - Company timeline (1975 → ABB 1991 → today)
  - Named team members with roles
  - ABB authorisation credentials (photos of certificates)
  - Customers served / projects completed
- [ ] **Publish: "ABB MCB Price Guide Singapore 2026"**
- [ ] **Publish: "ABB AF Contactor Guide"**

**Phase 2 Success Criteria:**
- All 21 product pages 800+ words with Product schema
- /abb-singapore/ hub live
- /faq/ live with FAQPage schema
- 8+ total posts/guides published
- TTFB consistently < 800ms

---

## Phase 3 — Scale (Weeks 13–24)
**Goal:** Expand keyword footprint, establish content velocity, build local authority.
**Effort:** 4–6 hours/week

### Months 4–5: Comparison Content
- [ ] Publish comparison posts (see Content Calendar in SITE-AND-CONTENT-PLAN.md)
- [ ] Begin project case studies — document 3 completed projects with photos
- [ ] Add FAQ sections to top 5 product category pages

### Month 5: Link Building Sprint
- [ ] **Contact ABB Singapore** — request listing on their official Singapore distributor page
- [ ] **Submit to directories:**
  - Singapore Yellow Pages, Hotfrog Singapore
  - Singapore Business Federation, SCAL directory
  - Singapore Electrical Traders Association
- [ ] **Outreach to M&E trade publications** for editorial mentions or contributed articles
- [ ] **Customer review campaign** — target 20+ new Google reviews; respond to all within 24h

### Month 6: GEO + AI Search
- [ ] Create `llms.txt` at site root:
  ```
  # liankok.com
  ## Lian Kok Electrical
  Singapore's ABB Authorised Electrical Distributor since 1975.
  ABB partner since 1991. Physical counter at Race Course Road, Singapore.

  ## Key Pages
  - Products: https://liankok.com/products/
  - ABB Singapore: https://liankok.com/abb-singapore/
  - About: https://liankok.com/about/
  - Contact: https://liankok.com/contact/
  - Resources: https://liankok.com/resources/
  ```
- [ ] Review all content for AI-citeable structured answer format
- [ ] Ensure brand mentions use "Lian Kok Electrical is..." statement format for AI extraction

**Phase 3 Success Criteria:**
- 16+ posts/guides published
- 30+ Google reviews at 4.5+
- 10+ quality backlinks
- Top 10 for "ABB MCB Singapore" and "ABB authorised distributor Singapore"
- Listed on ABB's official Singapore distributor page

---

## Phase 4 — Authority (Months 7–12)
**Goal:** Cement category leadership, leverage 50-year anniversary.
**Effort:** ~4 hours/week ongoing

### Ongoing (Weekly)
- [ ] Publish 1 post/week from content calendar
- [ ] Respond to all Google reviews within 24 hours
- [ ] Weekly GBP posts (product spotlight, new arrivals)

### Q3 2026: Advanced Schema
- [ ] `HowTo` schema on installation/selection guides
- [ ] `Speakable` schema on key FAQ sections
- [ ] Validate all schema with Google Rich Results Test
- [ ] `Breadcrumb` schema on all pages (auto via Yoast if properly configured)

### Q4 2026: Anniversary Campaign
- [ ] "50 Years of Electrical Supply in Singapore" content piece
- [ ] Press release to Singapore business/trade media
- [ ] Anniversary landing page: timeline, achievements, customer stories
- [ ] LinkedIn campaign targeting M&E engineers and contractors

**Phase 4 Success Criteria:**
- 30+ posts published
- Top 5 for "ABB distributor Singapore"
- 50+ Google reviews
- Organic traffic +200% vs Phase 1 baseline
- Coverage in Singapore M&E trade media

---

## Schema by Page Type (Reference)

| Page | Schema Types |
|---|---|
| Homepage | LocalBusiness (ElectricalContractor), Organization, WebSite |
| /abb-singapore/ | WebPage, Organization (with ABB brand reference) |
| Product Category | CollectionPage, ItemList, BreadcrumbList |
| Individual Product | Product, Offer, Brand, BreadcrumbList |
| Blog / Resource Post | Article (named author), BreadcrumbList |
| /faq/ | FAQPage |
| /projects/ case studies | Article or CreativeWork |
| /contact/ | ContactPage, LocalBusiness |
| /about/ | AboutPage, Organization |

---

## Resource Requirements

| Resource | Phase 1 | Phase 2 | Phase 3–4 |
|---|---|---|---|
| Technical (WP/plugin config) | 8–10h | 4–6h | 2h/month |
| Content writing (per post) | 0 | 4h/post | 3–4h/post |
| Photography session | 2h | — | Quarterly |
| GBP management | 2h setup | 1h/week | 1h/week |
| Link building outreach | — | — | 2h/week |
| **Monthly budget est. (excl. staff time)** | $0–200 | $200–500 | $300–700 |

*Assumes in-house. Agency execution = 5–10x these estimates.*

---

## Tracking Setup (Do in Week 1)

- [ ] **Google Search Console** — verify domain, submit sitemap_index.xml
- [ ] **Google Analytics 4** — verify tracking firing on all pages
- [ ] **Google Business Profile Insights** — baseline views, calls, direction requests
- [ ] **Bing Webmaster Tools** — 5–10% of SG search traffic, often ignored

### Monthly Reporting Checklist
- Organic sessions vs prior month (GA4)
- Top 20 keyword positions (GSC)
- CTR by page (GSC)
- GBP: Views, calls, website clicks
- Core Web Vitals pass rate (GSC → Core Web Vitals report)
- Index coverage: pages indexed vs submitted
- New backlinks (GSC Links report or Ahrefs free)
- Google reviews count + average rating
