# AGENT.md — Guide for AI Agents

This document tells you everything you need to write new story posts, generate OG images, and keep `ranausmanai.github.io` up to date. Read it before touching any file.

---

## Site Overview

**Repo:** `ranausmanai/ranausmanai.github.io`  
**Hosting:** GitHub Pages, `main` branch, root path `/`  
**Live URL:** `https://ranausmanai.github.io`

```
/
├── index.html              ← Homepage (edit to add new post cards)
├── posts/
│   ├── under-pressure.html
│   ├── spiral-eval.html
│   └── tinyforge.html
├── og/                     ← Open Graph preview images (1200×630px PNG)
│   ├── home.png
│   ├── under-pressure.png
│   ├── spiral-eval.png
│   └── tinyforge.png
├── make_og_images.py       ← Script to regenerate OG images
└── AGENT.md                ← This file
```

---

## Design System

### Colors (CSS variables in every page)

```css
--bg:      #080c14   /* page background */
--surface: #0f1624   /* slightly lighter bg */
--card:    #141e30   /* card backgrounds */
--text:    #e8edf5   /* primary text */
--dim:     #5a6a80   /* secondary text / labels */
--dimmer:  #3a4558   /* very muted / borders */
--blue:    #4fc3f7
--red:     #ef5350
--purple:  #7c4dff
--gold:    #ffd54f
--green:   #66bb6a
--teal:    #26c6da
--orange:  #ffa726
```

### Typography

- Body / UI: **Inter** (Google Fonts, weights 300–700)
- Code / mono labels: **JetBrains Mono** (Google Fonts, weights 400, 600)
- Font import line (copy this into every `<head>`):
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  ```

### Accent Color Per Post

Each post has one accent color that drives the hero canvas, call-out borders, tag colors, and OG image. Pick from the palette:

| Post | Accent |
|------|--------|
| under-pressure | `#7c4dff` (purple) |
| spiral-eval | `#26c6da` (teal) |
| tinyforge | `#ff6b35` (fire orange — not in the root palette, used directly) |
| New posts | Pick an unused color from the palette |

---

## Writing a New Post

### 1. Story Structure and Voice

Every post tells a **story**, not a report. The arc is:

1. **Hook** — One surprising finding or image, stated plainly. No jargon.
2. **Setup** — What was the experiment? Explain the simplest version first.
3. **What we found** — Walk through results as a narrative: "Then something strange happened…"
4. **Why it matters** — One paragraph connecting the finding to something broader.
5. **How to go further** — Links to code, data, or next questions.

**Voice rules:**
- Write for a smart person who has never heard of mechanistic interpretability.
- No academic hedging ("it is possible that perhaps…"). State things directly.
- Use plain analogies before technical terms.
- Short sentences beat long ones.
- Contractions are fine ("we found", "it didn't", "that's").
- Never write "In conclusion" or "In summary".

### 2. HTML File Template

Create `posts/YOUR-SLUG.html`. Copy this skeleton and fill in the highlighted sections:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>POST TITLE — ranausmanai</title>
<meta name="description" content="ONE SENTENCE DESCRIPTION">

<!-- Open Graph -->
<meta property="og:title" content="POST TITLE">
<meta property="og:description" content="ONE SENTENCE DESCRIPTION">
<meta property="og:image" content="https://ranausmanai.github.io/og/YOUR-SLUG.png">
<meta property="og:url" content="https://ranausmanai.github.io/posts/YOUR-SLUG.html">
<meta property="og:type" content="article">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="POST TITLE">
<meta name="twitter:description" content="ONE SENTENCE DESCRIPTION (≤200 chars)">
<meta name="twitter:image" content="https://ranausmanai.github.io/og/YOUR-SLUG.png">

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
/* ── PASTE THE FULL CSS BLOCK FROM AN EXISTING POST ── */
/* Then change --accent to your post's accent color:   */
:root { --accent: #YOUR_ACCENT_COLOR; }
</style>
</head>
<body>

<canvas class="hero-canvas" id="bg"></canvas>

<nav>
  <a class="nav-back" href="../index.html">← ranausmanai</a>
  <div class="nav-links">
    <a href="https://github.com/ranausmanai" target="_blank">GitHub</a>
  </div>
</nav>

<div class="progress-bar" id="prog"></div>

<article>
  <header class="post-header">
    <div class="post-meta">
      <span class="post-tag">CATEGORY TAG</span>
      <span class="post-date">MONTH YEAR</span>
    </div>
    <h1>POST TITLE</h1>
    <p class="post-subtitle">ONE SENTENCE HOOK</p>
    <div class="post-stats">
      <div class="stat"><span>VALUE</span>LABEL</div>
      <!-- 3–5 stats from the experiment -->
    </div>
  </header>

  <!-- SECTIONS — use .content-section for each major section -->
  <section class="content-section reveal">
    <h2>Section Heading</h2>
    <p>Body copy here.</p>
  </section>

  <!-- CALLOUT BOX (use for key findings) -->
  <div class="callout reveal">
    <strong>Key finding:</strong> One clear sentence.
  </div>

  <!-- DATA TABLE -->
  <div class="data-table reveal">
    <table>
      <thead><tr><th>Column</th><th>Column</th></tr></thead>
      <tbody>
        <tr><td>Row</td><td>Value</td></tr>
      </tbody>
    </table>
  </div>

  <!-- TERMINAL BLOCK (for code/output) -->
  <div class="terminal reveal">
    <div class="terminal-bar">
      <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
      <span>output</span>
    </div>
    <pre>$ your command here
output line 1
output line 2</pre>
  </div>

  <!-- FOOTER LINKS -->
  <div class="post-footer reveal">
    <a href="https://github.com/ranausmanai/REPO" class="footer-link" target="_blank">Code on GitHub →</a>
  </div>
</article>

<footer>
  ranausmanai &nbsp;·&nbsp; <a href="https://github.com/ranausmanai">GitHub</a>
</footer>

<!-- Canvas animation (copy from existing post, change hue values to match accent) -->
<script>
/* scroll progress bar */
window.addEventListener('scroll',()=>{
  const s=document.documentElement;
  document.getElementById('prog').style.width=(s.scrollTop/(s.scrollHeight-s.clientHeight)*100)+'%';
});
/* reveal on scroll */
const obs=new IntersectionObserver(els=>els.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(e=>obs.observe(e));
/* animated canvas — copy full script from existing post */
</script>
</body>
</html>
```

### 3. CSS to Copy

Copy the entire `<style>` block from `posts/under-pressure.html` (it is the most complete reference). Then:
- Change `--accent` in `:root` to your post's accent color.
- The canvas animation hues are hardcoded in the JS script block — search for `hue:` and change the values to match your accent color (e.g., purple=260, teal=185, orange=25).

---

## Adding the Post to the Homepage

Edit `index.html`. Find the `<div class="posts-grid">` block and add a new `<a class="post-card">` inside it:

```html
<a class="post-card" href="posts/YOUR-SLUG.html">
  <div class="post-meta">
    <span class="post-tag" style="color:var(--COLORNAME);border-color:rgba(R,G,B,.3);">CATEGORY</span>
    <span class="post-date">MONTH YEAR</span>
  </div>
  <h2>POST TITLE</h2>
  <p class="post-excerpt">2–3 sentence teaser. Plain language. End on the most surprising thing.</p>
  <div class="post-stats">
    <div class="stat">Label <span>Value</span></div>
    <div class="stat">Label <span>Value</span></div>
  </div>
  <span class="read-more" style="color:var(--COLORNAME);">Read →</span>
</a>
```

To make a post the **featured (hero) post** instead, replace the existing `<a class="post-featured">` block at the top and move the old featured post down to the grid. Update the `featured-dot` text to `New post`.

---

## Generating the OG Image

Edit `make_og_images.py` and add a new `make_og()` call at the bottom:

```python
make_og("YOUR-SLUG.png",
    eyebrow="CATEGORY · DETAIL",
    title_lines=["First Line of Title", "Second Line of Title"],
    subtitle="One sentence that fits in 72 characters.",
    accent="#YOUR_ACCENT_COLOR",
    stats=[("Stat label", "Value"), ("Stat label", "Value"), ("Stat label", "Value")],
)
```

Rules for `make_og`:
- `title_lines`: 2 lines, each ≤ 22 characters (large font — keep short)
- `subtitle`: will be auto-truncated at 72 characters
- `stats`: 3 items max; `val` is displayed large (bold mono), `label` is small
- Run: `python make_og_images.py` — outputs to `og/YOUR-SLUG.png`

---

## Committing and Pushing

```bash
cd /path/to/ranausmanai.github.io

# Stage the new/changed files
git add posts/YOUR-SLUG.html og/YOUR-SLUG.png index.html

# If you updated make_og_images.py
git add make_og_images.py

# Commit
git commit -m "Add post: YOUR POST TITLE"

# Push
git push origin main
```

GitHub Pages deploys automatically within ~60 seconds of the push.

**Important:**
- Never amend published commits on main.
- Do not add Co-Authored-By lines to commits. Commits should be single-author.
- Do not commit large binary files other than the `og/` PNG images.

---

## Checklist for a New Post

- [ ] `posts/YOUR-SLUG.html` created with full HTML, CSS, JS
- [ ] OG meta tags in `<head>` (og:title, og:description, og:image, og:url, og:type)
- [ ] Twitter Card meta tags in `<head>` (twitter:card, twitter:title, twitter:description, twitter:image)
- [ ] `og/YOUR-SLUG.png` generated (1200×630px) via `make_og_images.py`
- [ ] `index.html` updated: new post card in the grid (or promoted to featured)
- [ ] All files committed and pushed to `main`
- [ ] Verify live at `https://ranausmanai.github.io/posts/YOUR-SLUG.html`
- [ ] Check OG preview at `https://cards-dev.twitter.com/validator` or `https://www.opengraph.xyz`
