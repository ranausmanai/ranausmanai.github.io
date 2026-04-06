# AGENT.md — Guide for AI Agents

This document is self-contained. You do not need to read any other file to write a new post and publish it.

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

### Colors

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

### Accent Color Per Post

Each post has one accent color. Pick an unused one:

| Post | Accent |
|------|--------|
| under-pressure | `#7c4dff` (purple) |
| spiral-eval | `#26c6da` (teal) |
| tinyforge | `#ff6b35` (fire orange) |
| New posts | Pick any unused color above |

---

## Writing Style

Every post tells a **story**, not a report. Arc:

1. **Hook** — One surprising finding, stated plainly. No jargon.
2. **Setup** — What was the experiment? Simplest version first.
3. **What we found** — Walk through results as a narrative.
4. **Why it matters** — One paragraph connecting to something broader.
5. **How to go further** — Code links, next questions.

**Voice rules:**
- Write for a smart person who has never heard of mechanistic interpretability.
- No hedging ("it is possible that perhaps…"). State things directly.
- Plain analogies before technical terms.
- Short sentences beat long ones.
- Contractions are fine.
- Never write "In conclusion" or "In summary".

---

## Full Post Template

Create `posts/YOUR-SLUG.html`. The complete HTML, CSS, and JS is below — fill in the `YOUR_*` placeholders.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YOUR_POST_TITLE — ranausmanai</title>
<meta name="description" content="YOUR_ONE_SENTENCE_DESCRIPTION">

<!-- Open Graph -->
<meta property="og:title" content="YOUR_POST_TITLE">
<meta property="og:description" content="YOUR_ONE_SENTENCE_DESCRIPTION">
<meta property="og:image" content="https://ranausmanai.github.io/og/YOUR_SLUG.png">
<meta property="og:url" content="https://ranausmanai.github.io/posts/YOUR_SLUG.html">
<meta property="og:type" content="article">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="YOUR_POST_TITLE">
<meta name="twitter:description" content="YOUR_ONE_SENTENCE_DESCRIPTION">
<meta name="twitter:image" content="https://ranausmanai.github.io/og/YOUR_SLUG.png">

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --bg:#080c14; --surface:#0f1624; --card:#141e30;
  --text:#e8edf5; --dim:#5a6a80; --dimmer:#3a4558;
  --blue:#4fc3f7; --red:#ef5350; --purple:#7c4dff;
  --gold:#ffd54f; --green:#66bb6a; --orange:#ffa726;
  --teal:#26c6da;
  --accent: YOUR_ACCENT_HEX;   /* e.g. #7c4dff */
}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;overflow-x:hidden;line-height:1.6;}
::-webkit-scrollbar{width:4px;} ::-webkit-scrollbar-track{background:var(--bg);} ::-webkit-scrollbar-thumb{background:#2a3550;border-radius:2px;}

/* ─── PROGRESS BAR ─── */
#progress{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--accent),var(--blue));z-index:999;transition:width .1s;}

/* ─── NAV ─── */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:18px 40px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #0f1624;background:rgba(8,12,20,.9);backdrop-filter:blur(12px);}
.nav-back{font-family:'JetBrains Mono',monospace;font-size:.8rem;color:var(--dim);text-decoration:none;transition:color .2s;}
.nav-back:hover{color:var(--text);}
.nav-links a{color:var(--dim);font-size:.85rem;text-decoration:none;transition:color .2s;}
.nav-links a:hover{color:var(--text);}

/* ─── HERO ─── */
.hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative;overflow:hidden;padding:0 24px;}
#heroBg{position:absolute;inset:0;z-index:0;}
.hero-inner{position:relative;z-index:1;max-width:820px;}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:.75rem;letter-spacing:3px;text-transform:uppercase;color:var(--accent);margin-bottom:24px;opacity:0;animation:up .8s .2s forwards;}
.hero h1{font-size:clamp(2.2rem,6vw,4.8rem);font-weight:700;line-height:1.08;letter-spacing:-2px;margin-bottom:28px;opacity:0;animation:up .9s .4s forwards;}
.hero h1 em{font-style:normal;color:var(--accent);}
.hero-desc{font-size:1.15rem;color:var(--dim);max-width:600px;margin:0 auto 36px;opacity:0;animation:up .9s .6s forwards;}
.hero-pills{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;opacity:0;animation:up .9s .8s forwards;}
.pill{padding:6px 16px;border-radius:20px;border:1px solid;font-size:.82rem;font-family:'JetBrains Mono',monospace;}
.scroll-arrow{position:absolute;bottom:32px;z-index:1;opacity:0;animation:up 1s 1.2s forwards,nudge 2s 2s infinite;}
.scroll-arrow svg{width:28px;height:28px;fill:none;stroke:var(--dim);stroke-width:2;}
@keyframes up{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
@keyframes nudge{0%,100%{transform:translateY(0)}50%{transform:translateY(8px)}}

/* ─── LAYOUT ─── */
.chapter{max-width:960px;margin:0 auto;padding:100px 24px;}
.chapter.wide{max-width:1100px;}
.tag{font-family:'JetBrains Mono',monospace;font-size:.68rem;letter-spacing:3px;text-transform:uppercase;color:var(--accent);margin-bottom:14px;}
.chapter h2{font-size:clamp(1.8rem,4vw,3rem);font-weight:700;line-height:1.15;margin-bottom:18px;letter-spacing:-0.5px;}
.lead{font-size:1.1rem;color:var(--dim);max-width:660px;margin-bottom:52px;line-height:1.75;}
.reveal{opacity:0;transform:translateY(32px);transition:opacity .75s ease,transform .75s ease;}
.reveal.on{opacity:1;transform:none;}

/* ─── CARDS ─── */
.card{background:var(--card);border-radius:16px;padding:32px;border:1px solid #1a2540;}
.card-sm{background:var(--card);border-radius:12px;padding:24px;border:1px solid #1a2540;}
.accent-top{border-top:3px solid var(--accent);}

/* ─── CALLOUT BOX ─── */
.callout{background:rgba(255,255,255,.03);border-left:3px solid var(--accent);border-radius:0 12px 12px 0;padding:20px 24px;margin:32px 0;font-size:.95rem;line-height:1.75;color:var(--dim);}
.callout strong{color:var(--text);}

/* ─── DATA TABLE ─── */
.data-table{overflow-x:auto;margin:32px 0;}
.data-table table{width:100%;border-collapse:collapse;font-size:.88rem;}
.data-table th{font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:2px;text-transform:uppercase;color:var(--dim);padding:10px 16px;border-bottom:1px solid #1a2540;text-align:left;}
.data-table td{padding:12px 16px;border-bottom:1px solid #0f1624;color:var(--text);}
.data-table tr:hover td{background:var(--surface);}

/* ─── TERMINAL BLOCK ─── */
.terminal{background:#050810;border-radius:12px;overflow:hidden;margin:32px 0;border:1px solid #1a2540;}
.terminal-bar{background:#0f1624;padding:10px 16px;display:flex;align-items:center;gap:6px;font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--dim);}
.terminal-bar .dot{width:10px;height:10px;border-radius:50%;margin-right:2px;}
.terminal-bar .dot.red{background:#ef5350;}
.terminal-bar .dot.yellow{background:#ffd54f;}
.terminal-bar .dot.green{background:#66bb6a;}
.terminal pre{padding:24px;font-family:'JetBrains Mono',monospace;font-size:.82rem;line-height:1.7;color:#a8b8d0;overflow-x:auto;}

/* ─── STAT STRIP ─── */
.stat-strip{display:flex;flex-wrap:wrap;gap:24px;margin:40px 0;}
.stat-item{display:flex;flex-direction:column;gap:4px;}
.stat-item .sv{font-family:'JetBrains Mono',monospace;font-size:1.6rem;font-weight:700;color:var(--text);}
.stat-item .sl{font-size:.75rem;color:var(--dim);text-transform:uppercase;letter-spacing:1px;}

/* ─── GRID HELPERS ─── */
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:20px;}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;}
@media(max-width:640px){.grid-2,.grid-3{grid-template-columns:1fr;}}

/* ─── FINAL CARD ─── */
.final-card{background:linear-gradient(135deg,#0f1624,#150f2a);border-radius:20px;padding:52px 44px;border:1px solid #2a2060;position:relative;overflow:hidden;margin-top:60px;}
.final-card::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 20% 20%,rgba(124,77,255,.07),transparent 60%);}
.final-card h2{position:relative;font-size:clamp(1.5rem,3vw,2.2rem);font-weight:700;background:linear-gradient(135deg,var(--gold),#ff8a65);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:24px;line-height:1.2;}
.final-card p{position:relative;color:var(--text);font-size:1rem;line-height:1.85;max-width:680px;margin-bottom:14px;}

/* ─── LINKS ─── */
.cta-link{display:inline-flex;align-items:center;gap:8px;font-size:.9rem;font-weight:500;color:var(--accent);text-decoration:none;margin-top:24px;transition:gap .2s;}
.cta-link:hover{gap:14px;}

/* ─── DIVIDER ─── */
.divider{height:1px;background:linear-gradient(90deg,transparent,#1a2540,transparent);margin:0 auto;max-width:960px;}

footer{text-align:center;padding:60px 24px 48px;font-size:.75rem;color:var(--dimmer);letter-spacing:1px;}
footer a{color:var(--dim);text-decoration:none;}
footer a:hover{color:var(--text);}
</style>
</head>
<body>

<div id="progress"></div>

<nav>
  <a class="nav-back" href="../index.html">← ranausmanai</a>
  <div class="nav-links">
    <a href="https://github.com/ranausmanai" target="_blank">GitHub</a>
  </div>
</nav>

<!-- ═══════ HERO ═══════ -->
<div class="hero">
  <canvas id="heroBg"></canvas>
  <div class="hero-inner">
    <div class="eyebrow">YOUR EYEBROW TEXT</div>
    <h1>YOUR TITLE WITH <em>ACCENT WORDS</em> HERE</h1>
    <p class="hero-desc">One sentence that makes the reader want to keep scrolling.</p>
    <div class="hero-pills">
      <!-- optional: add .pill spans for key concepts -->
    </div>
  </div>
  <div class="scroll-arrow"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>
</div>

<!-- ═══════ CONTENT ═══════ -->
<div class="chapter reveal">
  <div class="tag">SECTION LABEL</div>
  <h2>Section Heading</h2>
  <p class="lead">Opening paragraph that sets up the section.</p>

  <!-- Body copy: use <p> tags directly, or wrap in .card for emphasis -->
  <p>Body text here.</p>

  <!-- Key finding callout -->
  <div class="callout">
    <strong>Key finding:</strong> One clear sentence stating what you found.
  </div>

  <!-- Stats -->
  <div class="stat-strip">
    <div class="stat-item"><span class="sv">55%</span><span class="sl">Hack rate under pressure</span></div>
    <div class="stat-item"><span class="sv">24</span><span class="sl">Layers analyzed</span></div>
  </div>
</div>

<div class="divider"></div>

<div class="chapter reveal">
  <div class="tag">ANOTHER SECTION</div>
  <h2>Another Heading</h2>

  <!-- Two-column grid example -->
  <div class="grid-2" style="margin-bottom:40px;">
    <div class="card accent-top">
      <h3 style="margin-bottom:10px;">Left Card</h3>
      <p style="color:var(--dim);font-size:.9rem;line-height:1.7;">Content here.</p>
    </div>
    <div class="card accent-top">
      <h3 style="margin-bottom:10px;">Right Card</h3>
      <p style="color:var(--dim);font-size:.9rem;line-height:1.7;">Content here.</p>
    </div>
  </div>

  <!-- Terminal block example -->
  <div class="terminal">
    <div class="terminal-bar">
      <span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>
      <span>output</span>
    </div>
    <pre>$ your command here
output line 1
output line 2</pre>
  </div>
</div>

<div class="divider"></div>

<div class="chapter reveal">
  <!-- Data table example -->
  <div class="data-table">
    <table>
      <thead><tr><th>Model</th><th>Score</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td>Model A</td><td>+32</td><td>Most grounding</td></tr>
        <tr><td>Model B</td><td>−9</td><td>Most amplifying</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════ CLOSING CARD ═══════ -->
<div class="chapter reveal">
  <div class="final-card">
    <h2>What This Means</h2>
    <p>A paragraph about the broader significance of what you found.</p>
    <p>A second paragraph if needed.</p>
    <a class="cta-link" href="https://github.com/ranausmanai/YOUR_REPO" target="_blank">Code on GitHub →</a>
  </div>
</div>

<footer>
  ranausmanai &nbsp;·&nbsp; <a href="https://github.com/ranausmanai">GitHub</a>
</footer>

<script>
// ── SCROLL PROGRESS ──
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const pct = h.scrollTop / (h.scrollHeight - h.clientHeight) * 100;
  document.getElementById('progress').style.width = pct + '%';
});

// ── HERO CANVAS (particle network) ──
// Change ACCENT_COLOR to your post's accent hex.
// Change LINE_COLOR to a semi-transparent version of the accent.
(function(){
  const ACCENT_COLOR = 'YOUR_ACCENT_HEX';  // e.g. '#7c4dff'
  const LINE_COLOR   = 'YOUR_ACCENT_HEX';  // same color, alpha added below

  const c = document.getElementById('heroBg'), ctx = c.getContext('2d');
  function resize(){
    c.width = c.offsetWidth * devicePixelRatio;
    c.height = c.offsetHeight * devicePixelRatio;
    ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
  }
  resize(); window.addEventListener('resize', resize);

  const pts = Array.from({length:70}, () => ({
    x: Math.random()*c.offsetWidth, y: Math.random()*c.offsetHeight,
    vx:(Math.random()-.5)*.3, vy:(Math.random()-.5)*.3,
    r:Math.random()*2+.5, a:Math.random()*.18+.04
  }));

  function draw(){
    ctx.clearRect(0,0,c.offsetWidth,c.offsetHeight);
    pts.forEach(p=>{
      p.x+=p.vx; p.y+=p.vy;
      if(p.x<0)p.x=c.offsetWidth; if(p.x>c.offsetWidth)p.x=0;
      if(p.y<0)p.y=c.offsetHeight; if(p.y>c.offsetHeight)p.y=0;
      ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=ACCENT_COLOR; ctx.globalAlpha=p.a; ctx.fill();
    });
    ctx.globalAlpha=.03; ctx.strokeStyle=LINE_COLOR; ctx.lineWidth=.5;
    for(let i=0;i<pts.length;i++) for(let j=i+1;j<pts.length;j++){
      const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y;
      if(dx*dx+dy*dy<9000){
        ctx.beginPath(); ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y); ctx.stroke();
      }
    }
    ctx.globalAlpha=1; requestAnimationFrame(draw);
  }
  draw();
})();

// ── REVEAL ON SCROLL ──
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('on'); io.unobserve(e.target); }});
}, {threshold: 0.1});
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
</script>
</body>
</html>
```

---

## Adding the Post to the Homepage

Edit `index.html`. Find `<div class="posts-grid">` and insert a new card inside it:

```html
<a class="post-card" href="posts/YOUR-SLUG.html">
  <div class="post-meta">
    <span class="post-tag" style="color:YOUR_ACCENT;border-color:rgba(R,G,B,.3);">CATEGORY</span>
    <span class="post-date">MONTH YEAR</span>
  </div>
  <h2>POST TITLE</h2>
  <p class="post-excerpt">2–3 sentence teaser. End on the most surprising finding.</p>
  <div class="post-stats">
    <div class="stat">Label <span>Value</span></div>
    <div class="stat">Label <span>Value</span></div>
  </div>
  <span class="read-more" style="color:YOUR_ACCENT;">Read →</span>
</a>
```

To promote a post to the **featured hero slot**, replace the `<a class="post-featured">` block and push the old featured post into the grid. Update `featured-dot` text to `New post`.

---

## Generating the OG Image

Edit `make_og_images.py` and add a call at the bottom:

```python
make_og("YOUR-SLUG.png",
    eyebrow="CATEGORY · DETAIL",
    title_lines=["Line One (≤22 chars)", "Line Two (≤22 chars)"],
    subtitle="One sentence, max 72 characters.",
    accent="#YOUR_ACCENT_HEX",
    stats=[("Stat label", "Value"), ("Stat label", "Value"), ("Stat label", "Value")],
)
```

Then run: `python make_og_images.py` → outputs `og/YOUR-SLUG.png`

---

## Commit and Push

```bash
cd /path/to/ranausmanai.github.io

git add posts/YOUR-SLUG.html og/YOUR-SLUG.png index.html make_og_images.py
git commit -m "Add post: YOUR POST TITLE"
git push origin main
```

GitHub Pages deploys automatically within ~60 seconds.

**Rules:**
- No Co-Authored-By lines. Single-author commits only.
- Never force-push or amend published commits on `main`.
- Only binary files in `og/` are acceptable large files.

---

## Checklist

- [ ] `posts/YOUR-SLUG.html` — full HTML with CSS and JS from template above
- [ ] `YOUR_ACCENT_HEX` replaced in both `:root` and the canvas JS
- [ ] OG + Twitter Card meta tags in `<head>` with correct slug URLs
- [ ] `og/YOUR-SLUG.png` generated via `make_og_images.py`
- [ ] `index.html` — new post card added (or promoted to featured)
- [ ] Committed and pushed to `main`
- [ ] Live at `https://ranausmanai.github.io/posts/YOUR-SLUG.html`
