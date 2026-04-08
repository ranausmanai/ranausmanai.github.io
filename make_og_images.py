"""
Generate Open Graph preview images (1200x630) for all posts.
Run once: python make_og_images.py
Outputs to og/ folder.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUT = Path(__file__).parent / "og"
OUT.mkdir(exist_ok=True)

W, H = 12.0, 6.3   # inches at 100dpi = 1200x630

BG      = "#080c14"
SURFACE = "#0f1624"
CARD    = "#141e30"
DIM     = "#5a6a80"
DIMMER  = "#3a4558"
TEXT    = "#e8edf5"

def make_og(filename, eyebrow, title_lines, subtitle, accent, stats=None):
    fig = plt.figure(figsize=(W, H), facecolor=BG)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1200); ax.set_ylim(0, 630)
    ax.axis("off")
    ax.set_facecolor(BG)

    # subtle grid lines
    for y in range(0, 631, 90):
        ax.axhline(y, color=DIMMER, lw=0.4, alpha=0.3)
    for x in range(0, 1201, 120):
        ax.axvline(x, color=DIMMER, lw=0.4, alpha=0.3)

    # glow blob
    for r, a in [(260, .04), (200, .06), (140, .09), (80, .13)]:
        circle = plt.Circle((180, 520), r, color=accent, alpha=a)
        ax.add_patch(circle)

    # top border accent
    ax.add_patch(patches.FancyArrow(0, 626, 1200, 0, width=3,
        head_width=0, head_length=0, fc=accent, ec=accent, alpha=0.9))

    # site label
    ax.text(72, 580, "ranausmanai.github.io",
        color=DIM, fontsize=13, fontfamily="monospace", va="top")

    # eyebrow tag
    ax.text(72, 540, eyebrow.upper(),
        color=accent, fontsize=12, fontfamily="monospace",
        fontweight="bold", va="top", alpha=0.9)

    # title
    y = 470
    for line in title_lines:
        ax.text(72, y, line, color=TEXT, fontsize=42,
            fontfamily="DejaVu Sans", fontweight="bold",
            va="top", linespacing=1.1)
        y -= 58

    # subtitle (truncate manually if long)
    short = subtitle if len(subtitle) <= 72 else subtitle[:70] + "…"
    ax.text(72, y - 14, short, color=DIM, fontsize=17,
        fontfamily="DejaVu Sans", va="top")

    # stats row
    if stats:
        sx = 72
        for label, val in stats:
            ax.text(sx, 52, val, color=TEXT, fontsize=18,
                fontfamily="monospace", fontweight="bold", va="bottom")
            ax.text(sx, 30, label, color=DIM, fontsize=11,
                fontfamily="monospace", va="bottom")
            sx += max(len(val), len(label)) * 12 + 40

    # right accent dot cluster
    np.random.seed(42)
    for _ in range(30):
        x = np.random.uniform(900, 1160)
        y = np.random.uniform(60, 560)
        r = np.random.uniform(1, 4)
        a = np.random.uniform(0.1, 0.35)
        circle = plt.Circle((x, y), r, color=accent, alpha=a)
        ax.add_patch(circle)

    fig.savefig(OUT / filename, dpi=100, bbox_inches="tight",
                pad_inches=0, facecolor=BG)
    plt.close(fig)
    print(f"  ✓ {filename}")

print("Generating OG images…")

make_og("home.png",
    eyebrow="Independent AI Research",
    title_lines=["Looking inside", "language models."],
    subtitle="Mechanistic interpretability & behavioral testing on open models.",
    accent="#4fc3f7",
    stats=[("Posts", "4"), ("Models", "Open"), ("Hardware", "Consumer")],
)

make_og("parameter-golf.png",
    eyebrow="OpenAI Parameter Golf · 131 Runs",
    title_lines=["A Tiny Model", "Got Better", "By Doing Less"],
    subtitle="131 experiments under a 600-second cap on one RTX 4000 Ada.",
    accent="#66bb6a",
    stats=[("Best BPB", "1.5207"), ("Runs", "131"), ("Main lesson", "Speed = quality")],
)

make_og("under-pressure.png",
    eyebrow="Mechanistic Interpretability",
    title_lines=["What Happens Inside", "an AI Under Stress?"],
    subtitle="Same model, same task, different words. Completely different behavior.",
    accent="#7c4dff",
    stats=[("Hack rate under pressure", "55%"), ("Valence axis", "59.5%"), ("Models", "0.8B + 2B")],
)

make_og("spiral-eval.png",
    eyebrow="Behavioral Testing · 5 Models",
    title_lines=["Which AIs Will Feed", "Your Delusions?"],
    subtitle="Streetlights, hidden messages, secret math laws. Who grounds you?",
    accent="#26c6da",
    stats=[("Spiral score range", "+32 to −9"), ("Models tested", "5"), ("Scenarios", "5")],
)

make_og("tinyforge.png",
    eyebrow="Self-Improving AI · Consumer Hardware",
    title_lines=["A Tiny Model That", "Teaches Itself."],
    subtitle="No teacher. No GPU. 0.8B params. 75% better from 13 self-made examples.",
    accent="#ff6b35",
    stats=[("Single-pass improvement", "+75%"), ("RAM", "6GB"), ("Training pairs", "13")],
)

print("Done → og/")
