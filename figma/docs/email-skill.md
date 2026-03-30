---
name: email-design
description: "Best practices for designing high-performance HTML emails. Use this skill whenever the user asks to create, review, or optimize an email design — including newsletters, transactional emails, promotional emails, drip campaigns, or any HTML email template. Also trigger when the user mentions email performance, email rendering, email accessibility, email file size, dark mode email, mobile email optimization, hero image sizing, or email client compatibility. Use this skill even if the user just says 'email' or 'newsletter' in the context of design or development work."
---

# Email Design Best Practices (2025–2026)

This skill contains performance-driven best practices for HTML email design, compiled from industry data published between 2021 and 2025. Sources include Litmus, Mailchimp, Campaign Monitor, Email on Acid, Parcel, Can I Email, Really Good Emails, and emaillove.com research articles.

When data is cited, the approximate year of the source is noted. Anything older than 2020 has been excluded as no longer relevant to current email client rendering engines and user behavior.

For detailed technical specs and data tables, read `email-specs.md`.

---

## 1. Email Width & Layout

The standard max-width for email is **600px**. This has been the industry default for over a decade and remains the safest choice in 2025. Some brands have started pushing to **640px or even 700px**, but 600px guarantees the best rendering across the widest range of email clients (Litmus State of Email 2024).

Why 600px works: most desktop email clients render in preview panes that are roughly 600–700px wide. Gmail's web interface, Outlook desktop, and Apple Mail all handle 600px without horizontal scrolling. Going wider risks horizontal scrollbars in Outlook's preview pane and in webmail clients viewed on smaller laptop screens.

If you go wider than 600px, cap it at **640px** and test thoroughly in Outlook 2019/2021 and Outlook 365 desktop.

For mobile, your email should be fluid or responsive, collapsing to a **single column at 480px or below**. The breakpoint most commonly used is `@media screen and (max-width: 480px)` or `max-width: 600px` depending on your approach.

---

## 2. Email File Size & Weight

This is one of the most critical performance factors. Email clients clip or truncate emails that exceed certain weight thresholds, and heavier emails load slower on mobile networks, which directly impacts engagement.

**Gmail clipping threshold:** Gmail clips emails at approximately **102KB** of HTML (this is the raw HTML weight, not including images). When clipped, Gmail shows a "View entire message" link. According to Mailchimp and Litmus data (2023–2024), only about 20% of users click through to see clipped content. This means anything below the fold of a clipped email is essentially invisible.

**Target total HTML weight: under 100KB.** Ideally aim for **80KB or less** to leave headroom for tracking pixels and dynamically injected content from your ESP.

**Image weight guidelines:**
- Total image payload: aim for **under 800KB**, ideally under 600KB
- Individual hero images: keep under **200KB**
- Supporting images: keep each under **80–100KB**
- Use modern formats where supported (WebP via `<picture>` fallback), but JPEG and PNG remain the safest. Note: WebP support in email is still inconsistent — Apple Mail and Gmail web support it, but Outlook desktop does not (Can I Email, 2024)
- Always compress images. Tools like TinyPNG, Squoosh, or ImageOptim should be standard in your workflow

**Why weight matters beyond clipping:** Campaign Monitor's 2023 benchmarks showed that emails under 100KB total HTML weight had 12% higher click-through rates than those over 150KB. Heavier emails also have higher bounce rates on mobile because they take longer to render.

---

## 3. Hero Image & Above-the-Fold Design

The hero section is the most valuable real estate in any email. It needs to communicate the primary message and CTA within the first **350–500px of vertical space** (the "preview zone" — what a recipient sees before scrolling).

**Hero image dimensions:**
- **Width:** 600px (matches email width, renders at full bleed)
- **Height:** Between 200px and 350px for the hero image itself. Taller heroes push the CTA below the fold on many mobile devices
- **Retina/HiDPI:** Export at 2x (1200px wide) and constrain with `width="600"` in HTML. This ensures sharp rendering on high-density displays (iPhones, modern Android, Retina MacBooks). This is no longer optional — over 70% of email opens in 2024 were on devices with high-density screens (Litmus Email Analytics, 2024)
- **File format:** JPEG for photographic heroes (aim for 60–75% quality after compression), PNG for graphics with flat colors or transparency
- **Aspect ratio:** Landscape-oriented heroes perform best. Common ratios are 3:1 (600×200) or roughly 2:1 (600×300). Avoid tall heroes (1:1 or portrait) because they push content down

**CTA placement:** Your primary call-to-action should be visible without scrolling. On mobile (iPhone 14/15 viewport ~375×667), this means within the first ~500px of email height including the hero. On desktop preview panes, the visible area is typically 300–500px tall depending on the client. Litmus 2024 data showed that emails with the primary CTA in the first 400px of vertical space saw 28% higher click rates than those with the CTA below 600px.

**Alt text on hero images is mandatory.** Many email clients block images by default (notably Outlook desktop for external senders). Without alt text, blocked images show a blank space. With good alt text and styled `<img>` tags (background color, font styling on the alt text), the email remains usable even with images off.

---

## 4. Mobile Optimization

Mobile accounts for **roughly 60% of all email opens** as of 2024 (Litmus Email Analytics). On some B2C lists, mobile share exceeds 70%. This is the dominant reading context — designing for mobile is not optional, it is the primary design target.

**Responsive vs. fluid vs. hybrid (spongy):**
- **Responsive** (media queries): The most flexible approach. Use `@media` queries to restack columns, resize text, and swap images. Works in Apple Mail, Gmail app (iOS/Android), Samsung Mail, and most modern clients. Does NOT work in Gmail web (desktop) — Gmail strips `<style>` blocks in some contexts, though it now supports embedded `<style>` in the `<head>` as of 2023
- **Fluid** (percentage widths): Content scales proportionally. Simple but less control. Works everywhere
- **Hybrid/Spongy** (combination of fluid + conditional comments for Outlook): The most robust cross-client approach. Uses `max-width` on divs with Outlook-specific table fallbacks via `<!--[if mso]>` conditional comments. Recommended as the default approach for high-compatibility needs

**Mobile-specific sizing:**
- **Minimum touch target:** 44×44px (Apple HIG) or 48×48dp (Material Design). Buttons smaller than this cause tap errors
- **Minimum font size:** 14px for body text on mobile. iOS auto-zooms text smaller than 13px, which breaks layouts. Apple Mail specifically will scale up text if it detects small font sizes
- **CTA buttons:** Minimum 44px tall, ideally full-width on mobile (100% of container). The "bulletproof button" technique (using `<table>` + `<td>` with padding and background color instead of images) remains the most reliable across clients
- **Line height:** 1.4–1.6 for body copy on mobile for readability
- **Padding:** At minimum 16px horizontal padding on mobile. Content flush to screen edges feels cramped and reduces readability

**Single-column mobile layout** is the safest pattern. If your desktop email uses 2 or 3 columns, they should stack vertically on mobile. Multi-column layouts on mobile viewports below 480px are almost always a poor experience.

---

## 5. Dark Mode

Dark mode email rendering has become a major design consideration. As of 2024, approximately 35–40% of email opens occur in dark mode (Litmus, 2024). The challenge is that different email clients handle dark mode differently — there is no single standard.

**Three types of dark mode behavior:**
1. **No change:** The client renders the email exactly as coded (Gmail Android in some themes)
2. **Partial inversion:** The client changes background colors but leaves images alone (Outlook desktop dark mode, Apple Mail dark mode)
3. **Full inversion:** The client inverts all colors including some image backgrounds (Outlook.com dark mode, Windows Mail)

**Design strategies for dark mode:**
- **Transparent PNGs for logos:** If your logo is on a white/light background, it will look jarring in dark mode. Use transparent PNGs so the logo adapts to the background
- **Add padding/stroke to dark logos:** If your logo is dark-colored, add a thin white or light stroke/outline or a subtle glow so it remains visible on dark backgrounds
- **Use the `color-scheme` meta tag:** Add `<meta name="color-scheme" content="light dark">` and `<meta name="supported-color-schemes" content="light dark">` to signal dark mode support. Pair with `@media (prefers-color-scheme: dark)` styles for clients that support it (Apple Mail, Outlook iOS)
- **Avoid pure white backgrounds (#FFFFFF):** Use very light grays (#F5F5F5 or #FAFAFA) — they translate better in partial inversion mode
- **Avoid pure black text (#000000) on pure white backgrounds:** When inverted, these become harsh white-on-black. Use near-black (#1A1A1A or #222222) and near-white (#F5F5F5) for gentler inversion
- **Test images on dark backgrounds:** Any image with white edges or white corners will show as floating boxes in dark mode

Dark mode `@media` query support is growing but not universal. Apple Mail, Outlook iOS, and some webmail clients support it. Gmail does not fully support `prefers-color-scheme` media queries (Can I Email, 2024). The safest approach is to design emails that look acceptable in both modes without relying on the media query, and then enhance with `@media (prefers-color-scheme: dark)` where supported.

---

## 6. Typography

**Web fonts in email are partially supported.** Gmail, Outlook.com, and most Outlook desktop versions strip `@font-face` declarations. Apple Mail, iOS Mail, Samsung Mail, and Thunderbird support web fonts. Because of this split, always declare a robust fallback stack.

**Recommended font stacks:**
- Sans-serif: `font-family: 'Your Web Font', Helvetica, Arial, sans-serif;`
- Serif: `font-family: 'Your Web Font', Georgia, 'Times New Roman', serif;`

**Font sizing best practices:**
- Headlines: 22–28px (mobile: 22–24px)
- Subheadlines: 18–20px
- Body copy: 16px desktop, 14–16px mobile (never below 14px on mobile)
- Fine print/legal: 12–13px minimum
- Preheader text: 14–16px if visible, or 0px/hidden if used as preview text only

**Line length:** Aim for 45–75 characters per line for body copy. At 600px email width with 16px text, this usually works out naturally. On mobile, the narrower viewport ensures shorter lines automatically.

---

## 7. Accessibility

Email accessibility affects roughly 15% of the global population who have some form of disability (WHO). Beyond being the right thing to do, accessible emails perform better — they are easier to read, easier to act on, and render more predictably.

**Minimum requirements:**
- **`role="presentation"` on layout tables:** Screen readers will otherwise announce table structure. Add `role="presentation"` to every `<table>` used for layout (not data tables)
- **`alt` text on all images:** Descriptive for content images, empty (`alt=""`) for decorative images
- **Semantic heading structure:** Use actual heading tags where clients support them, or at minimum style text to create a clear visual hierarchy
- **Color contrast:** Minimum 4.5:1 ratio for body text, 3:1 for large text (WCAG AA). This applies in both light and dark modes
- **Language attribute:** Add `lang="en"` (or appropriate language code) to the `<html>` tag
- **Logical reading order:** The HTML source order should match the visual reading order. Screen readers follow DOM order, not visual layout
- **Don't rely on color alone:** If a link is only differentiated by color, add an underline. If a status is only shown by color (red/green), add a text label

---

## 8. Email Client Rendering Considerations

The email client landscape is fragmented. Designing for email requires understanding each client's quirks.

**Market share snapshot (Litmus Email Analytics, H2 2024):**
- Apple Mail (iPhone + Mac): ~55–60% of opens
- Gmail (web + app): ~28–30%
- Outlook (all versions): ~6–8%
- Yahoo/AOL: ~2–3%
- Other: remainder

This distribution varies dramatically by audience. B2B lists tend to skew much heavier toward Outlook (sometimes 30%+). Know your audience's client split before making rendering tradeoffs.

**Key client-specific considerations:**

**Outlook desktop (2019, 2021, Microsoft 365):** Uses Word's rendering engine. This means no `border-radius`, limited `background-image` support (use VML for Outlook backgrounds), no CSS `max-width` (Outlook ignores it — use table widths), and quirky spacing behavior. Outlook also doesn't support `<style>` in `<head>` in some configurations. Always include inline styles as a fallback.

**Gmail:** Strips `<style>` from `<head>` in some embedded/AMP contexts but generally supports embedded styles as of 2023. Gmail prefixes all class names with a random string, so avoid using IDs or complex selectors. Gmail clips at ~102KB. Gmail does not support `@import`, `@font-face`, or `position`.

**Apple Mail / iOS Mail:** The most capable email rendering engine. Supports media queries, web fonts, CSS animations, `<video>`, and dark mode media queries. Apple Mail's excellent support sometimes leads designers to build features that break everywhere else — always test in Gmail and Outlook too.

**Yahoo/AOL Mail:** Strips class names in some contexts. Generally decent CSS support but quirky. Test separately if Yahoo is a significant portion of your list.

---

## 9. Interactive & Advanced Features

Use progressively. Build the email so it works without any interactive features, then layer interactivity on top for clients that support it.

**What's safe to use broadly (2024–2025):**
- CSS hover states (all clients except Outlook desktop and most mobile clients)
- CSS transitions on non-Outlook clients
- `<video>` in Apple Mail / iOS Mail only (use a static fallback image with a play button overlay for all other clients)

**What's emerging but limited:**
- AMP for Email: Supported in Gmail and Yahoo. Allows dynamic content, forms, and live data. Requires separate AMP HTML version and sender registration. Adoption remains niche
- CSS `@keyframes` animations: Apple Mail and some webmail clients. Fun for engagement but never rely on animation to communicate critical information
- Kinetic email (CSS-only interactivity like carousels, tabs): Impressive but supported mainly in Apple Mail, iOS Mail, Samsung Mail, and Thunderbird. Gmail and Outlook don't support the necessary CSS. Always design a static fallback

---

## 10. Pre-Send Checklist

Before every send, validate the following:

1. **HTML weight:** Under 100KB (ideally under 80KB)
2. **Total image payload:** Under 800KB (ideally under 600KB)
3. **All images have alt text**
4. **Links work and have tracking parameters**
5. **Subject line + preheader preview text set** (preheader should be 40–130 characters — the visible portion varies by client and device, but 85–100 chars is the sweet spot for maximum visibility across most clients)
6. **Tested in top 3 clients for your audience** (at minimum: Apple Mail, Gmail, Outlook)
7. **Dark mode checked** (preview in at least Apple Mail dark mode and Outlook dark mode)
8. **Mobile rendering verified** at 375px width (iPhone) and 360px (Android)
9. **CTA is visible above the fold** on both mobile and desktop
10. **Spam score checked** (tools like Mail-Tester.com or your ESP's built-in checker)
11. **Unsubscribe link present and working**
12. **`role="presentation"` on layout tables for accessibility**

---

## Reference

For detailed technical specifications, dimension tables, and client support matrices, read the reference file:

→ `email-specs.md`
