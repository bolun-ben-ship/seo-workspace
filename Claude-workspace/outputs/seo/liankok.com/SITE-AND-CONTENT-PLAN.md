# Site Structure & Content Plan: liankok.com
**Date:** 2026-03-04

---

## Part 1: Site Structure

### Pages to Delete or Noindex (Do This First)

**Delete — Demo/Template Pages (wrong industry or theme leftovers):**
```
/sample-page-2/          WordPress default
/home-page-two/          Theme demo
/rtl-homepage/           Theme demo
/onepage-home/           Theme demo
/blog-grid/              Theme demo (duplicate of /blog-2/)
/vehicle-wiring/         Automotive — wrong industry
/tire-balance/           Automotive — wrong industry
/clutch-replacement/     Automotive — wrong industry
/engine-replace/         Automotive — wrong industry
/team/                   Empty demo (repurpose or delete)
/team-details/           Empty demo
/testimonials/           Empty demo (repurpose or delete)
/portfolio-details/      Empty demo
/pricing/                Demo
/service/                Demo (repurpose or delete)
/service-details/        Demo
/filter-check-up/        Demo
/better-performance/     Demo
/chch/                   Unknown — investigate
/2802-2/                 Unknown — investigate
```

**Delete — Off-topic Posts:**
```
/hello-world/                                   WordPress default
/blog-standard/                                 Theme demo
/better-products-when-companies-work-together/  Generic demo
/what-can-paralegals-do-a-guide-for-lawyers/    Wrong industry (paralegal)
```

**Delete with 301 Redirects — Duplicate Pages:**
```
/about-2/     → /about/
/shop-2/      → /products/
/cart-2/      → /cart/
/checkout-2/  → /checkout/
```

**Noindex — WooCommerce Utility (keep but hide from search):**
```
/cart/
/checkout/
/accounts/
```

---

### Target Site Architecture

```
liankok.com/
│
├── /  (Homepage)
│   H1: "Singapore's Trusted ABB Authorised Electrical Distributor Since 1975"
│   Schema: LocalBusiness, Organization, WebSite
│
├── /abb-singapore/  (NEW — ABB Brand Authority Hub)
│   H1: "ABB Authorised Distributor in Singapore Since 1991"
│   2,000+ words: partnership history, product range, why choose Lian Kok
│   Schema: WebPage, Organization (with ABB brand reference)
│   └── /abb-singapore/abb-low-voltage-products/  (if needed later)
│
├── /products/  (Product Catalogue)
│   H1: "ABB Electrical Products — Singapore"
│   Schema: CollectionPage, ItemList
│   │
│   ├── /products/circuit-breakers/
│   │   Schema: CollectionPage, ItemList, BreadcrumbList
│   │   ├── /products/circuit-breakers/miniature-circuit-breakers/
│   │   ├── /products/circuit-breakers/moulded-case-circuit-breakers/
│   │   ├── /products/circuit-breakers/residual-current-devices/
│   │   ├── /products/circuit-breakers/rcbo-srcd/
│   │   └── /products/circuit-breakers/switch-disconnectors/
│   │
│   ├── /products/contactors-relays/
│   │   ├── /products/contactors-relays/af-contactors/
│   │   ├── /products/contactors-relays/thermal-overload-relays/
│   │   ├── /products/contactors-relays/electronic-overload-relays/
│   │   └── /products/contactors-relays/manual-motor-starters/
│   │
│   ├── /products/softstarters/
│   │   ├── /products/softstarters/psr-softstarter/
│   │   └── /products/softstarters/pse-softstarter/
│   │
│   ├── /products/surge-protection/
│   │
│   └── /products/wiring-accessories/
│       ├── /products/wiring-accessories/switches-sockets/
│       ├── /products/wiring-accessories/time-switches/
│       ├── /products/wiring-accessories/door-bells/
│       └── /products/wiring-accessories/safety-adaptors/
│
├── /resources/  (replaces /blog-2/)
│   H1: "Electrical Guides & Resources — Lian Kok Electrical"
│   ├── /resources/guides/
│   │   ├── /resources/guides/mcb-guide-singapore/
│   │   ├── /resources/guides/rcd-guide-singapore/
│   │   └── /resources/guides/electrical-panel-guide-singapore/
│   └── /resources/price-guides/
│       └── /resources/price-guides/abb-mcb-price-singapore/
│
├── /projects/  (Case Studies / Portfolio)
│   H1: "Our Projects — Lian Kok Electrical"
│   8–10 real project case studies
│
├── /about/
│   H1: "About Lian Kok Electrical — Singapore Since 1975"
│   1,000+ words: company history, team, ABB partnership credentials
│   Schema: AboutPage, Organization
│
├── /faq/
│   H1: "Frequently Asked Questions — ABB Products Singapore"
│   12+ Q&A pairs
│   Schema: FAQPage
│
└── /contact/
    H1: "Contact Lian Kok Electrical — Race Course Road, Singapore"
    Address, phone, Google Maps embed, hours
    Schema: ContactPage, LocalBusiness
```

---

### URL Migration Map

If restructuring from `/product/` to `/products/[category]/[product]/`, apply these 301 redirects:

| Old URL | New URL |
|---|---|
| /product/miniature-circuit-breakers-mcbs-2/ | /products/circuit-breakers/miniature-circuit-breakers/ |
| /product/sace-tmax-xt-2/ | /products/circuit-breakers/moulded-case-circuit-breakers/tmax-xt/ |
| /product/formula-mccbs/ | /products/circuit-breakers/moulded-case-circuit-breakers/formula/ |
| /product/residual-current-circuit-breakers-rccbs/ | /products/circuit-breakers/residual-current-devices/ |
| /product/residual-current-device-srcd-socket-outlet/ | /products/circuit-breakers/rcbo-srcd/ |
| /product/switch-disconnectors/ | /products/circuit-breakers/switch-disconnectors/ |
| /product/af-3-pole-contactors/ | /products/contactors-relays/af-contactors/ |
| /product/thermal-overload-relays/ | /products/contactors-relays/thermal-overload-relays/ |
| /product/electronic-overload-relays/ | /products/contactors-relays/electronic-overload-relays/ |
| /product/manual-motor-starters/ | /products/contactors-relays/manual-motor-starters/ |
| /product/psr-softstarter/ | /products/softstarters/psr-softstarter/ |
| /product/pse-softstarter/ | /products/softstarters/pse-softstarter/ |
| /product/surge-protection-devices/ | /products/surge-protection/ |
| /product/concept-bs/ | /products/wiring-accessories/switches-sockets/concept-bs/ |
| /product/inora/ | /products/wiring-accessories/switches-sockets/inora/ |
| /product/millenium/ | /products/wiring-accessories/switches-sockets/millenium/ |
| /product/metal-clad/ | /products/wiring-accessories/switches-sockets/metal-clad/ |
| /product/weatherproof/ | /products/wiring-accessories/switches-sockets/weatherproof/ |
| /product/germany-theben-24hr-segment-time-switch/ | /products/wiring-accessories/time-switches/ |
| /blog-2/ | /resources/ |

> **Note:** Only execute the URL restructure if proper 301 redirect infrastructure is in place. If dev resource is limited, optimise existing `/product/` URLs in-place — broken redirects are worse than ugly URLs.

---

### Navigation Structure

```
Main Nav:
[Products ▾] [ABB Singapore] [Resources] [Projects] [About] [Contact]

Products Mega-menu:
Circuit Breakers | Contactors & Relays | Softstarters | Surge Protection | Wiring Accessories
```

### Internal Linking Rules
- Every product page → "View all [category]" → category page
- Every blog/resource post → min 2 product page links + 1 other resource
- /about/ → /abb-singapore/ and /contact/
- /faq/ → product pages for "where to buy" answers
- /projects/ case studies → products used in each project
- Homepage → /abb-singapore/ (hero CTA or nav prominence)

---

## Part 2: Content Plan

### Content Principles
1. **ABB-first** — Every piece connects to ABB products or Lian Kok's expertise
2. **Singapore-specific** — Always include Singapore context (HDB, BCA, local climate, SS standards)
3. **Named author** — No "admin." Real staff member with photo and credentials
4. **Answers a real question** — Target queries Singapore electricians, contractors, homeowners search
5. **Minimum word counts** — Guides: 1,500+; Product posts: 800+; Product pages: 800–1,200

### Evergreen Pages (Create, Not Blog Posts)

| Page | URL | Target Keyword | Priority |
|---|---|---|---|
| ABB Singapore Hub | /abb-singapore/ | ABB Singapore | High |
| ABB Distributor Authority | /abb-singapore/abb-distributor-singapore/ | ABB authorised distributor Singapore | High |
| MCB Buying Guide | /resources/guides/mcb-guide-singapore/ | MCB guide Singapore | High |
| RCD/RCCB Guide | /resources/guides/rcd-guide-singapore/ | RCD Singapore | High |
| Electrical Panel Guide | /resources/guides/electrical-panel-guide-singapore/ | DB box Singapore | Medium |
| ABB MCB Price Reference | /resources/price-guides/abb-mcb-price-singapore/ | ABB MCB price Singapore | Medium |
| FAQ | /faq/ | Multiple long-tail | High |

### FAQ Seed Topics (for /faq/ + FAQPage schema)
1. What is an ABB Authorised Distributor?
2. Where can I buy ABB products in Singapore?
3. What is the difference between MCB and MCCB?
4. How do I choose the right MCB for my HDB flat?
5. What is a Residual Current Device (RCD)?
6. How do I know if my MCB needs replacing?
7. Does Lian Kok supply to contractors at wholesale prices?
8. What are the delivery options for ABB products in Singapore?
9. Can I walk in to purchase ABB products same day?
10. What is the ABB S200 series MCB used for?
11. What certifications do ABB MCBs have for Singapore use?
12. What is the difference between 6kA and 10kA MCBs?

---

### Content Calendar: Q1–Q4 2026

**Publishing cadence:** 2 posts/month Q1–Q2, scaling to weekly by Q3

#### Q1 — Foundation (Fix first, then publish)

**January — Technical fixes only, no new content**
- [ ] Expand existing MCB Guide to 2,500 words (currently 1,392)
- [ ] Add meta descriptions to all existing pages
- [ ] Fix H1 structure on homepage
- [ ] Update all blog authors from "admin" to named person

**February**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "ABB RCD/SRCD Socket Singapore: Complete Guide" | ABB RCD Singapore | Guide | 1,800 |
| "ABB MCB Price Guide Singapore 2026: S200 & S280 Series" | ABB MCB price Singapore | Price Guide | 2,000 |

**March**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "What is an ABB Authorised Distributor? Singapore Guide" | ABB authorised distributor Singapore | Brand Authority | 1,500 |
| "ABB AF Contactor Series: Complete Guide for Singapore Industrial Use" | ABB contactor Singapore | Product Guide | 2,000 |

---

#### Q2 — Product Depth + Comparison Content

**April**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "MCB vs MCCB Singapore: When Do You Need Each?" | MCCB vs MCB Singapore | Comparison | 2,000 |
| "ABB Tmax XT MCCB: Applications & Specifications Singapore" | ABB MCCB Singapore | Product Guide | 1,800 |

**May**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "ABB vs Schneider MCBs: Which Is Right for Your Singapore Property?" | ABB vs Schneider MCB | Comparison | 2,200 |
| "Understanding MCB Curve Types (B, C, D): Singapore Guide" | MCB curve types Singapore | Educational | 1,600 |

**June**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "ABB Surge Protection Devices: Protecting Singapore Homes & Buildings" | surge protection Singapore | Product Guide | 1,800 |
| "HDB Distribution Board Guide: Choosing the Right MCBs" | HDB DB box MCB Singapore | Consumer | 2,000 |

---

#### Q3 — Authority + Projects

**July**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "ABB Thermal Overload Relay: Selection Guide for Singapore Motors" | thermal overload relay Singapore | Product Guide | 1,600 |
| Case Study: HDB Electrical Upgrade (Race Course Road area) | [Local branded] | Case Study | 1,000 |

**August**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "Singapore Electrical Standards: IEC vs SS Standards Guide" | Singapore electrical standards | Authority | 2,000 |
| "ABB PSR/PSE Softstarters: Applications in Singapore F&B and Industrial" | ABB softstarter Singapore | Product Guide | 1,800 |

**September**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "Choosing Time Switches for Singapore: Theben vs ABB Options" | time switch Singapore | Comparison | 1,600 |
| Case Study: Singapore Commercial M&E Project | [Commercial] | Case Study | 1,200 |

---

#### Q4 — Scale + Anniversary Campaign

**October**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "Electrical Safety Checks Before Year End: Singapore Guide" | electrical safety check Singapore | Seasonal | 1,500 |
| "ABB RCBO vs RCCB Singapore: Which Do You Need?" | RCBO vs RCCB Singapore | Comparison | 1,800 |

**November**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "ABB Low Voltage Products: Full 2026 Catalogue Overview Singapore" | ABB low voltage products Singapore | Catalogue | 2,000 |
| "Electrical Distributor vs Electrical Contractor: What's the Difference?" | electrical distributor Singapore | Educational | 1,200 |

**December**
| Post | Target Keyword | Type | Words |
|---|---|---|---|
| "50 Years of Electrical Supply in Singapore: Lian Kok's Story" | Lian Kok Electrical history | Brand Story | 2,500 |
| "Best ABB Products for Singapore Renovation Projects 2027" | ABB Singapore renovation | Buying Guide | 2,000 |

---

### Content Production Standards

- **Author:** Assign one named staff member as "lead electrical expert." Create an author profile page with photo, credentials, years of experience.
- **Images:** Descriptive filenames before upload (e.g., `abb-s200-mcb-singapore.jpg`). Alt text required on every image.
- **Internal links:** Min 2 product page links + 1 resource link per post.
- **CTAs:** Each post ends with "View ABB [product] →" or "Contact us for pricing."
- **Schema:** `Article` with named author on every post; `FAQPage` on /faq/; `Product` on all product pages.
