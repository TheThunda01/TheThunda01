"""Plot the final-budget contrasts exported by the GFP ablation study."""
import argparse
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def render(source: Path, output: Path) -> None:
    with source.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    seeds = [row["seed"] for row in rows]
    values = [float(row["distant_minus_local_benefit"]) for row in rows]
    if not seeds or len(seeds) != len(set(seeds)) or not all(map(math.isfinite, values)):
        raise ValueError("Expected one finite contrast per seed")
    extent = max(max(map(abs, values)), 0.01)
    palette = {"ink": "#17304a", "muted": "#415b6b", "accent": "#007267"}
    fig, ax = plt.subplots(figsize=(7.2, 1.9 + 0.46 * len(rows)), layout="constrained")
    ax.set_title("Where did the combined rule help more?", loc="left", weight="bold",
                 color=palette["ink"], fontsize=18, pad=24)
    ax.text(0, 1.02, "Local examples  ←", transform=ax.transAxes, color=palette["muted"])
    ax.text(1, 1.02, "→  Distant examples", transform=ax.transAxes,
            ha="right", color=palette["muted"])
    ax.axvline(0, color=palette["ink"], lw=1, zorder=2)
    for i, value in enumerate(values):
        ax.hlines(i, min(value, 0), max(value, 0), color=palette["accent"], lw=2.5)
        ax.scatter(value, i, s=48, color=palette["accent"], zorder=3)
        direction = 1 if value >= 0 else -1
        ax.annotate(f"{value:+.3f}".replace("-", "−"), (value, i),
                    xytext=(7 * direction, 0), textcoords="offset points",
                    ha="left" if direction == 1 else "right", va="center", color=palette["ink"])
    ax.set_yticks(range(len(seeds)), [f"Seed {seed}" for seed in seeds])
    ax.set_ylim(len(seeds) - 0.45, -0.55)
    ax.set_xlim(-1.36 * extent, 1.36 * extent)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=6, symmetric=True))
    ax.set_xlabel("Difference in benefit over random selection (RMSE units)", labelpad=10)
    ax.grid(axis="x", color="#dde5e8", lw=0.8)
    ax.set_axisbelow(True)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0, pad=6, colors=palette["muted"])
    fig.savefig(output, dpi=180, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="GFP distance_benefit_contrast.csv")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    render(args.source, args.output)
