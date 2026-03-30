# Email Design Technical Specifications & Data Reference

This file supplements the main SKILL.md with detailed specs, data tables, and client-specific support matrices. All data sourced from 2021–2025 industry reports.

---

## Table of Contents

1. Dimension Quick Reference
2. File Size Budgets
3. Hero Image Specs
4. Typography Specs
5. Button/CTA Specs
6. Dark Mode Support Matrix
7. CSS Support Matrix by Client
8. Mobile Viewport Reference
9. Email Client Market Share Data
10. Performance Benchmarks
11. Preheader Text Length by Client
12. Image Format Support
13. Code Patterns

---

## 1. Dimension Quick Reference

| Element | Desktop | Mobile | Notes |
|---|---|---|---|
| Email max-width | 600px | 100% (fluid) | 640px acceptable with testing |
| Single column content | 560–580px | 100% minus padding | 20px padding each side |
| 2-column (each) | 280–290px | Stack to 100% | Stack below 480px |
| 3-column (each) | 180–190px | Stack to 100% | Stack below 480px |
| Horizontal padding | 20px each side | 16px each side | Minimum for readability |
| Vertical section spacing | 24–40px | 20–32px | Consistent rhythm |

---

## 2. File Size Budgets

| Component | Target | Hard Limit | Why |
|---|---|---|---|
| Total HTML | 80KB | 102KB | Gmail clips at ~102KB |
| Hero image | 150KB | 200KB | Largest single asset |
| Product/content images | 50–80KB each | 100KB each | Multiple in one email |
| Total image payload | 600KB | 800KB | Mobile load time |
| Animated GIF | 250KB | 500KB | Some clients limit GIF size; Apple Mail handles large GIFs, Gmail struggles above 500KB |
| Total email weight (HTML + images) | Under 1MB | Under 1.5MB | Slow connections, carrier throttling |

**What counts toward Gmail's 102KB clip:**
- All HTML markup (tags, attributes, inline styles)
- All text content
- Tracking code injected by your ESP
- Base64-encoded images (avoid these — they count against the limit AND many clients block them)
- NOT external images (loaded via `<img src>`)

**Tips to stay under 102KB:**
- Minify HTML: strip comments, collapse whitespace, shorten class names
- Avoid excessive inline CSS repetition — use embedded `<style>` where supported and inline as fallback
- Remove unused code from templates
- Keep copy concise — every character counts
- Audit ESP-injected code (tracking pixels, link wrapping) — this can add 5–20KB

---

## 3. Hero Image Detailed Specs

| Spec | Recommended | Notes |
|---|---|---|
| Width (rendered) | 600px | Matches email width |
| Width (exported) | 1200px | 2x for Retina |
| Height (rendered) | 200–300px | Up to 350px max |
| Height (exported) | 400–600px | 2x for Retina |
| Aspect ratio | 2:1 to 3:1 | Landscape oriented |
| Format - Photo | JPEG, 60–75% quality | After compression |
| Format - Graphic | PNG-8 or PNG-24 | Use PNG-8 when possible (smaller file) |
| Format - Animation | GIF or APNG | APNG has better quality but less support |
| Max file size | 200KB | After compression |
| Alt text | Required | Descriptive, 5–15 words |
| Background color on `<td>` | Match image edge color | Visible while image loads |

**Retina image technique:**
```html
<img src="hero-1200w.jpg" width="600" height="300" alt="Hero description" 
     style="display:block; max-width:100%; height:auto;" />
```
The `width="600"` HTML attribute constrains the display size. The actual image file is 1200px wide for sharpness on 2x screens. The `max-width:100%` ensures it scales down on mobile.

---

## 4. Typography Specs

| Element | Desktop Size | Mobile Size | Weight | Line Height |
|---|---|---|---|---|
| Headline H1 | 24–28px | 22–24px | Bold (700) | 1.2–1.3 |
| Headline H2 | 20–22px | 18–20px | Bold (700) | 1.2–1.3 |
| Subheadline | 18–20px | 16–18px | Semi-bold (600) | 1.3–1.4 |
| Body copy | 16px | 14–16px | Regular (400) | 1.5–1.6 |
| Caption/small | 13–14px | 12–13px | Regular (400) | 1.4–1.5 |
| CTA button text | 16–18px | 16px | Bold (700) | 1 (centered) |
| Preheader | 14–16px | 14px | Regular (400) | 1.4 |
| Footer/legal | 12–13px | 11–12px | Regular (400) | 1.4 |

**System font stacks (no web font dependency):**
- Modern sans: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`
- Classic sans: `Helvetica, Arial, sans-serif`
- Serif: `Georgia, 'Times New Roman', Times, serif`
- Monospace: `'Courier New', Courier, monospace`

---

## 5. Button/CTA Specs

| Spec | Desktop | Mobile |
|---|---|---|
| Minimum height | 40px | 44px (Apple HIG) / 48px (Material) |
| Minimum width | 150px | 100% of container preferred |
| Padding (internal) | 12–16px vertical, 24–32px horizontal | 14–16px vertical, full width |
| Font size | 16–18px | 16px minimum |
| Border radius | 4–8px (not supported in Outlook) | Same |
| Max buttons per email | 1 primary, 2–3 secondary | 1 primary ideal |

**Bulletproof button pattern (works everywhere including Outlook):**
```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td style="border-radius:4px; background:#007BFF;">
      <a href="https://example.com" target="_blank" 
         style="background:#007BFF; border:1px solid #007BFF; border-radius:4px; 
                color:#ffffff; display:inline-block; font-family:Helvetica,Arial,sans-serif; 
                font-size:16px; font-weight:bold; line-height:44px; text-align:center; 
                text-decoration:none; width:200px; -webkit-text-size-adjust:none;">
        Shop Now
      </a>
    </td>
  </tr>
</table>
```

**VML button for Outlook (full border-radius support):**
```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" 
  style="height:44px; v-text-anchor:middle; width:200px;" 
  arcsize="10%" strokecolor="#007BFF" fillcolor="#007BFF">
  <w:anchorlock/>
  <center style="color:#ffffff; font-family:Helvetica,Arial,sans-serif; 
    font-size:16px; font-weight:bold;">Shop Now</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-->
<a href="..." style="...">Shop Now</a>
<!--<![endif]-->
```

---

## 6. Dark Mode Support Matrix (as of late 2024)

| Client | Dark Mode Behavior | `prefers-color-scheme` Support | Notes |
|---|---|---|---|
| Apple Mail (macOS) | Partial inversion | Yes | Changes background, leaves images |
| iOS Mail | Partial inversion | Yes | Same as macOS Apple Mail |
| Gmail (iOS) | Partial inversion | No | Inverts some colors automatically |
| Gmail (Android) | Varies by theme | No | Some themes don't invert at all |
| Gmail (Web) | No inversion | No | Web Gmail has no dark mode for email content |
| Outlook (Windows desktop) | Partial inversion | No | Inverts backgrounds, may alter text |
| Outlook (macOS) | Partial inversion | Yes | Better support than Windows |
| Outlook (iOS) | Partial inversion | Yes | Good dark mode support |
| Outlook.com (Web) | Full inversion | No | Aggressively inverts everything |
| Yahoo Mail | Partial inversion | No | Limited dark mode |
| Samsung Mail | Partial inversion | Partial | Some versions support it |
| Thunderbird | No auto-inversion | Yes | Respects email's own dark mode styles |

---

## 7. CSS Property Support Matrix (Key Properties)

| CSS Property | Apple Mail | Gmail | Outlook Desktop | Outlook.com | Yahoo |
|---|---|---|---|---|---|
| `<style>` in `<head>` | Yes | Yes (since 2023) | Partial | Yes | Yes |
| `@media` queries | Yes | No (web) / Yes (app) | No | No | No |
| `@font-face` | Yes | No | No | No | No |
| `max-width` | Yes | Yes | No | Yes | Yes |
| `border-radius` | Yes | Yes | No | Yes | Yes |
| `background-image` | Yes | Yes | VML only | Yes | Yes |
| `box-shadow` | Yes | No | No | No | No |
| `flexbox` | Yes | No | No | No | No |
| `grid` | Yes | No | No | No | No |
| `position` | Yes | No | No | No | No |
| `float` | Yes | No | No | Partial | Partial |
| CSS animations | Yes | No | No | No | No |
| `<video>` | Yes | No | No | No | No |
| `margin` | Yes | Partial | Partial | Partial | Partial |
| `padding` | Yes | Yes | Yes (on `<td>`) | Yes | Yes |
| `line-height` | Yes | Yes | Yes | Yes | Yes |

**Practical takeaway:** If it needs to work everywhere, your layout must be table-based with inline styles. Use embedded `<style>` for progressive enhancement (media queries, hover states, dark mode overrides) but never depend on it for core layout.

---

## 8. Mobile Viewport Reference

| Device | Viewport Width | Pixel Ratio | Effective Email Width |
|---|---|---|---|
| iPhone 15 / 14 / 13 | 375px | 3x | ~375px |
| iPhone 15 Plus / 14 Plus | 428px | 3x | ~428px |
| iPhone SE (3rd gen) | 375px | 2x | ~375px |
| Samsung Galaxy S24 | 360px | 3x | ~360px |
| Samsung Galaxy S24 Ultra | 384px | 3.5x | ~384px |
| Google Pixel 8 | 412px | 2.625x | ~412px |
| iPad (10th gen) | 810px | 2x | 600px (email max-width) |

**Key insight:** The dominant mobile viewport width is 360–375px. Design your mobile layout to work perfectly at 375px, and it will cover the vast majority of devices.

---

## 9. Email Client Market Share (Litmus, H2 2024)

| Client | Global Share | B2C Typical | B2B Typical |
|---|---|---|---|
| Apple iPhone | 38–42% | 40–50% | 20–30% |
| Apple Mail (desktop) | 12–16% | 10–15% | 8–12% |
| Gmail | 28–30% | 25–35% | 20–25% |
| Outlook (all) | 6–8% | 3–5% | 25–35% |
| Yahoo/AOL | 2–3% | 3–5% | 1–2% |
| Samsung Mail | 2–3% | 2–4% | 1–2% |
| Other | 3–5% | 2–5% | 3–5% |

**Important:** These are global averages. Your list will differ. Always check your own email analytics for client distribution before making rendering tradeoffs. If your audience is 35% Outlook, you cannot afford to skip Outlook testing.

---

## 10. Performance Benchmarks

**Open rates by email length (Mailchimp industry benchmarks, 2023):**
- Under 200 words: 18–22% average open rate
- 200–500 words: 17–20%
- 500–1000 words: 15–18%
- Over 1000 words: 12–16%

**Click-through rates by CTA position (Litmus analysis, 2024):**
- CTA in first 400px: 3.2% average CTR
- CTA at 400–600px: 2.5% average CTR
- CTA below 600px: 1.8% average CTR

**Mobile engagement (Campaign Monitor, 2023):**
- 75% of recipients will delete an email if it doesn't look good on mobile
- Responsive emails generate 15% more clicks than non-responsive
- Average email reading time: 9–11 seconds (down from 13.4 seconds in 2018)

**Image loading:**
- 43% of Gmail users view emails with images blocked (Litmus 2023)
- Emails that are readable without images see 10% higher engagement
- Emails with a single hero image outperform emails with 5+ images in CTR

---

## 11. Preheader Text Length by Client

The preheader (preview text) is the snippet shown next to or below the subject line in the inbox. Length varies by client.

| Client | Approximate Visible Characters |
|---|---|
| iPhone (portrait) | 75–100 characters |
| iPhone (landscape) | 90–120 characters |
| Gmail (web) | 110–140 characters |
| Gmail (mobile) | 40–90 characters |
| Outlook (desktop) | 35–55 characters |
| Outlook.com (web) | 40–100 characters |
| Yahoo (web) | 100–120 characters |
| Apple Mail (desktop) | 80–140 characters |
| Samsung Mail | 50–80 characters |

**Best practice:** Write preheader text that is compelling in the first 50 characters (covers the shortest previews) and still reads well at 100+ characters. Use the hidden-preheader technique with zero-width spaces or `&zwnj;` entities after your preheader text to prevent email body content from leaking into the preview.

**Hidden preheader pattern:**
```html
<div style="display:none; max-height:0; overflow:hidden; mso-hide:all;">
  Your preheader text here.
  &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
  <!-- repeat enough to push body text out of preview -->
</div>
```

---

## 12. Image Format Support in Email

| Format | Apple Mail | Gmail | Outlook Desktop | Outlook.com | Notes |
|---|---|---|---|---|---|
| JPEG | Yes | Yes | Yes | Yes | Universal, best for photos |
| PNG | Yes | Yes | Yes | Yes | Universal, best for graphics |
| GIF (animated) | Yes | Yes | Yes (first frame in some versions) | Yes | Max ~500KB for Gmail |
| WebP | Yes | Yes | No | Partial | Growing but not safe yet |
| AVIF | Partial | No | No | No | Not recommended for email |
| SVG (inline) | Yes | No | No | No | Not safe for email |
| SVG (as `<img>`) | Yes | No | No | Partial | Not safe for email |
| APNG | Yes | Partial | No | Partial | Niche, limited support |

**Recommendation:** Stick with JPEG for photos and PNG for graphics/logos. Use GIF for animation. WebP is not yet safe as the sole format — use it as an enhancement via `<picture>` with a JPEG/PNG fallback.

---

## 13. Code Patterns

### Basic email skeleton (hybrid/spongy approach)

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="color-scheme" content="light dark">
  <meta name="supported-color-schemes" content="light dark">
  <title>Email Title</title>
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style>
    /* Reset styles */
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    img { -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
    body { margin: 0; padding: 0; width: 100% !important; height: 100% !important; }
    
    /* Dark mode */
    @media (prefers-color-scheme: dark) {
      .email-bg { background-color: #1a1a1a !important; }
      .email-body { background-color: #2d2d2d !important; }
      .dark-text { color: #f5f5f5 !important; }
    }
    
    /* Mobile */
    @media screen and (max-width: 600px) {
      .email-container { width: 100% !important; max-width: 600px !important; }
      .fluid { max-width: 100% !important; height: auto !important; }
      .stack-column { display: block !important; width: 100% !important; max-width: 100% !important; }
      .mobile-center { text-align: center !important; }
      .mobile-padding { padding-left: 16px !important; padding-right: 16px !important; }
    }
  </style>
</head>
<body style="margin:0; padding:0; background-color:#f5f5f5;" class="email-bg">
  
  <!-- Hidden preheader -->
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all;">
    Preview text goes here.
    &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
  </div>
  
  <!-- Email wrapper -->
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color:#f5f5f5;" class="email-bg">
    <tr>
      <td align="center" style="padding:20px 0;">
        
        <!-- Email body -->
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" class="email-container" style="max-width:600px; background-color:#ffffff;" class="email-body">
          
          <!-- Hero -->
          <tr>
            <td style="background-color:#ffffff;">
              <img src="hero.jpg" width="600" height="" alt="Hero image description" 
                   style="display:block; width:100%; max-width:600px; height:auto;" class="fluid" />
            </td>
          </tr>
          
          <!-- Content -->
          <tr>
            <td style="padding:32px 24px; font-family:Helvetica,Arial,sans-serif; font-size:16px; line-height:1.5; color:#222222;" class="dark-text mobile-padding">
              <h1 style="margin:0 0 16px; font-size:24px; line-height:1.2; font-weight:bold; color:#1a1a1a;" class="dark-text">
                Headline Here
              </h1>
              <p style="margin:0 0 24px;">
                Body copy goes here.
              </p>
              
              <!-- CTA Button -->
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" style="margin:0 auto;">
                <tr>
                  <td style="border-radius:4px; background:#007BFF;">
                    <a href="https://example.com" target="_blank" 
                       style="background:#007BFF; border:1px solid #007BFF; border-radius:4px; 
                              color:#ffffff; display:inline-block; font-family:Helvetica,Arial,sans-serif; 
                              font-size:16px; font-weight:bold; line-height:44px; text-align:center; 
                              text-decoration:none; width:200px; -webkit-text-size-adjust:none;">
                      Call to Action
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          
        </table>
        
      </td>
    </tr>
  </table>
  
</body>
</html>
```

### Responsive two-column to single-column pattern

```html
<!-- Two columns that stack on mobile -->
<!--[if mso]>
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600">
<tr>
<td valign="top" width="290">
<![endif]-->
<div style="display:inline-block; width:100%; max-width:290px; vertical-align:top;" class="stack-column">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
    <tr>
      <td style="padding:10px;">
        <!-- Column 1 content -->
      </td>
    </tr>
  </table>
</div>
<!--[if mso]>
</td>
<td valign="top" width="290">
<![endif]-->
<div style="display:inline-block; width:100%; max-width:290px; vertical-align:top;" class="stack-column">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
    <tr>
      <td style="padding:10px;">
        <!-- Column 2 content -->
      </td>
    </tr>
  </table>
</div>
<!--[if mso]>
</td>
</tr>
</table>
<![endif]-->
```

---

## Sources & Recency Notes

All data in this reference has been drawn from the following sources, with publication dates between 2021 and 2025:

- **Litmus State of Email** reports (2022, 2023, 2024) — email client market share, rendering trends, engagement data
- **Litmus Email Analytics** (ongoing) — real-time client usage data
- **Mailchimp Email Marketing Benchmarks** (2023) — open rates, click rates by industry, email length impact
- **Campaign Monitor Email Marketing Benchmarks** (2022, 2023) — mobile vs desktop engagement, responsive email performance
- **Email on Acid** rendering tests and blog posts (2022–2025) — client-specific CSS support, dark mode behavior
- **Can I Email** (caniuse-style database, continuously updated through 2025) — CSS/HTML feature support per email client
- **Parcel** (email development tool documentation, 2023–2025) — technical rendering details
- **Really Good Emails / Email Love** article archives (2022–2025) — design patterns, creative best practices
- **Google Gmail developer documentation** (2023–2024) — supported CSS, clipping behavior
- **Apple Human Interface Guidelines** — touch target sizing
- **Material Design guidelines** — touch target sizing
- **WHO** — disability statistics for accessibility context

Data older than 2020 has been intentionally excluded. Email client rendering engines, market share distributions, and mobile usage patterns change significantly year over year. If this document is being read after late 2026, some data points (especially market share and client-specific rendering behavior) should be re-validated.
