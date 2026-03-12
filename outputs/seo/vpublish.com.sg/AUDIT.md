# SEO Audit — vpublish.com.sg
**Audited:** 2026-03-11
**Business:** Visual Publish — Printing Company, Singapore
**Platform:** WordPress 6.5.7 on Apache

---

## SEO Health Score: 29 / 100

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Technical SEO | 28/100 | 25% | 7.0 |
| Content Quality | 30/100 | 25% | 7.5 |
| On-Page SEO | 15/100 | 20% | 3.0 |
| Schema / Structured Data | 35/100 | 10% | 3.5 |
| Performance (CWV) | 40/100 | 10% | 4.0 |
| Images | 80/100 | 5% | 4.0 |
| AI Search Readiness | 10/100 | 5% | 0.5 |
| **TOTAL** | | | **29.5** |

---

## Summary

Visual Publish has not received meaningful SEO attention in at least 7 years — the sitemap, schema, and analytics setup all bear 2018 timestamps or legacy configurations. The site is almost certainly invisible in organic search.

**Critical finding:** Universal Analytics (UA-22427905-20) was shut down July 2023. The site has had zero tracking for ~3 years. Nobody knows how much traffic it receives.

### Issue Scorecard

| Issue | Severity | Category |
|-------|----------|----------|
| No meta descriptions (all pages) | Critical | On-Page |
| Dead Universal Analytics | Critical | Analytics |
| Invalid schema GeoCoordinates | Critical | Schema |
| Homepage title has zero keywords | Critical | On-Page |
| 404 URL in sitemap | Critical | Technical |
| Sitemap 7+ years stale | High | Technical |
| Sitemap www/non-www mismatch | High | Technical |
| Robots.txt references wrong sitemap | High | Technical |
| TTFB 918ms (no caching) | High | Performance |
| Homepage only 301 words | High | Content |
| Contact page only 77 words | High | Content |
| Schema @context using HTTP | High | Schema |
| Schema name is domain not brand | High | Schema |
| Schema URLs using HTTP + www | High | Schema |
| Duplicate titles (2 pages) | High | On-Page |
| Near-duplicate URL pair (sticker pages) | High | Technical |
| Homepage 2× H1 tags | High | On-Page |
| About Us 0× H1 tags | High | On-Page |
| No HSTS header | High | Security |
| No OG/Twitter Card meta | Medium | On-Page |
| No blog/content section | Medium | Content |
| No contextual internal linking | Medium | On-Page |
| XML-RPC link exposed in HTML | Medium | Security |
| WordPress version in asset URLs | Medium | Security |
| IE conditional comments in HTML | Low | Technical |
| No WebP image formats | Low | Performance |
| No FAQ schema | Low | Schema |
| No breadcrumb schema | Low | Schema |

---

## Technical SEO — 28/100

### Crawlability
| Check | Status | Detail |
|-------|--------|--------|
| Homepage accessible | ✅ Pass | HTTP 200 |
| HTTPS redirect | ✅ Pass | HTTP → HTTPS working |
| www → non-www | ✅ Pass | 301 to non-www canonical |
| robots.txt | ⚠️ Warning | References `www.vpublish.com.sg/sitemap.xml` — should be non-www |
| Sitemap | ⚠️ Warning | Exists but all dates are 2018-09-25 |
| 404 in sitemap | ❌ Fail | `/services/` returns 404; listed in sitemap |
| URL consistency | ❌ Fail | Sitemap uses www URLs; site is non-www |

### Indexability
| Check | Status | Detail |
|-------|--------|--------|
| Canonicals | ⚠️ Mixed | Present on most pages but inconsistent |
| Sticker duplicate | ❌ Fail | `/sticker-printing-services-singapore/` and `/sticker-printing-singapore/` — near-identical, one canonicalises to the other |
| Printing services redirect | ❌ Fail | `/printing-services-singapore/` 301s to `/offset-printing-singapore/` — sitemap lists both as separate pages |
| `/services/sticker-printing/` canonical | ❌ Fail | Points to `/printing-services/sticker-printing/` — non-existent URL |
| Sitemap freshness | ❌ Fail | All `lastmod` dates: 2018-09-25 |
| Sitemap count | ⚠️ Warning | ~11 URLs only |

### Security Headers
| Header | Status |
|--------|--------|
| HTTPS / TLS | ✅ Active |
| HSTS | ❌ Missing |
| X-Frame-Options | ❌ Missing |
| X-Content-Type-Options | ❌ Missing |
| Content-Security-Policy | ❌ Missing |
| Referrer-Policy | ❌ Missing |

Other: WordPress version visible in asset URLs (`?ver=6.5.7`). `/xmlrpc.php` pingback link active in HTML head. IE 7/8 conditional comments still in source.

### Core Web Vitals (Estimated)
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| TTFB | ~918ms | <200ms | ❌ Poor |
| HTML size | 108KB | <50KB | ❌ Bloated |
| HTTP/2 | Enabled | — | ✅ Pass |
| Cache headers | None | Required | ❌ Fail |

TTFB of 918ms = no page caching. WordPress without a caching plugin runs PHP + DB on every request. WP Super Cache would fix this in 20 minutes.

---

## Content Quality — 30/100

### Page Inventory
| Page | Words | H1s | H2s | Meta Desc |
|------|-------|-----|-----|-----------|
| Homepage | 301 | 2 ❌ | 4 | ❌ None |
| Offset Printing | 600 | 1 ✅ | 1 | ❌ None |
| Sticker Printing (main) | 655 | 1 ✅ | 1 | ❌ None |
| Sticker Printing (alt) | 671 | 1 ✅ | 1 | ❌ None |
| About Us | 629 | 0 ❌ | 1 | ❌ None |
| Contact Us | 77 | 1 ✅ | 0 | ❌ None |
| Portfolio | 158 | 1 ✅ | 0 | ❌ None |
| /services/sticker-printing/ | 343 | 1 ✅ | 1 | ❌ None |

### E-E-A-T Assessment
| Signal | Status | Notes |
|--------|--------|-------|
| Experience | ❌ None | "15+ years" stated but no specifics — no founding story, milestones, or equipment |
| Expertise | ❌ Weak | Generic copy only — no technical knowledge demonstrated |
| Authoritativeness | ❌ Weak | No industry associations, certifications, or press mentions |
| Trust | ⚠️ Minimal | Address + phone in schema; no reviews displayed, no testimonials |
| Customer proof | ❌ None | Logo carousel exists but no named clients or case studies |
| Pricing transparency | ⚠️ Vague | H2 "What about pricing?" — no actual figures shown |

No blog or resource section. No FAQ content. Homepage copy is generic ("established & reliable" — identical to every competitor).

---

## On-Page SEO — 15/100

### Title Tags
| Page | Current Title | Issue |
|------|---------------|-------|
| Homepage | "Visual Publish" | No keywords — 14 chars |
| Offset Printing | "Offset Printing Services in Singapore – Visual Publish" | ✅ Good |
| Sticker Printing (main) | "Sticker Printing Services Singapore – Visual Publish" | ✅ Good |
| Sticker Printing (alt) | "Sticker Printing Services Singapore – Visual Publish" | ❌ Duplicate |
| Printing Services | "Offset Printing Services in Singapore – Visual Publish" | ❌ Duplicate of Offset |
| About Us | "About Us – Visual Publish" | ❌ No keywords |
| Contact | "Contact Us – Visual Publish" | ❌ No keywords |
| Portfolio | "Offset Printing Service Portfolio – Visual Publish" | ✅ Acceptable |
| /services/ | "Page not found – Visual Publish" | ❌ 404 indexed |

**Homepage fix:** `Offset & Sticker Printing Services in Singapore | Visual Publish`

**Meta descriptions:** Zero across all 10 pages audited. Google auto-generates from generic boilerplate.

**Heading issues:**
- Homepage: 2× H1 ("Home" + "Offset / Sticker Printing Services")
- About Us: 0× H1
- Contact, Portfolio: 0× H2

**OG/Social meta:** Not present on homepage. Shares on LinkedIn/Facebook render as blank links.

**Internal linking:** 100 links detected in HTML but all are navigation/footer. Zero contextual body links between service pages.

---

## Schema / Structured Data — 35/100

`LocalBusiness` schema present on every page. But multiple critical errors make it invalid.

### Current Schema (as found)
```json
{
  "@context": "http://www.schema.org",
  "@type": "LocalBusiness",
  "name": "Vpublish.com.sg",
  "url": "http://www.vpublish.com.sg/",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "159546",
    "longitude": "Singapore"
  },
  "priceRange": "1-1000",
  "telephone": "+6562732590",
  "telephone": "+6562732590"
}
```

### Errors
| Field | Problem | Fix |
|-------|---------|-----|
| `@context` | `http://www.schema.org` | → `https://schema.org` |
| `name` | "Vpublish.com.sg" (domain) | → "Visual Publish" |
| `url` | `http://www.vpublish.com.sg/` | → `https://vpublish.com.sg/` |
| `logo` / `image` | HTTP URLs | → HTTPS |
| `geo.latitude` | "159546" (postal code) | → 1.2856 |
| `geo.longitude` | "Singapore" (text) | → 103.8199 |
| `priceRange` | "1-1000" (invalid) | → "$$" |
| `telephone` | Duplicate key | Remove one |

### Missing Schema
- `PrintService` sub-type (more specific than `LocalBusiness`)
- `FAQPage` on service pages
- `BreadcrumbList` on service pages
- `AggregateRating` (when reviews are displayed)
- `BlogPosting` (when blog launches)

---

## Performance — 40/100

| Metric | Value | Benchmark |
|--------|-------|-----------|
| TTFB | 918ms | <200ms |
| HTML size | 108KB | <50KB |
| HTTP/2 | Enabled | — |
| Cache headers | None | Required |
| Image formats | JPEG/PNG (likely) | WebP preferred |

---

## Images — 80/100

Homepage: all 12 images have alt text (strongest category on the site). Other pages unverified. Image format modernisation (WebP) recommended — typically 25–35% size reduction.

---

## AI Search Readiness — 10/100

| Signal | Status |
|--------|--------|
| Structured FAQ content | ❌ None |
| Direct-answer paragraphs | ❌ None |
| Expert attribution | ❌ None |
| Schema (for AI parsing) | ❌ Invalid |
| Topic cluster depth | ❌ None |
| Brand entity clarity | ⚠️ Weak — "Visual Publish" vs "Vpublish.com.sg" |

---

## Analytics & Tracking

| Tool | Status |
|------|--------|
| Universal Analytics UA-22427905-20 | ❌ Dead — shut down July 2023 |
| Google Tag Manager GTM-PQZD52F | ✅ Firing — contents unknown |
| Google Analytics 4 | ❌ Not detected |
| Conversion tracking | ❌ Unknown |

---

## Sitemap

- Location: `https://vpublish.com.sg/sitemap.xml`
- URLs: ~11
- All `lastmod` dates: 2018-09-25
- URL format: `https://www.vpublish.com.sg/...` (www — wrong)
- Dead URL listed: `/services/` → 404
