"""Plot the two 2019 department records featured on the GitHub profile."""
import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def read_counts(path: Path) -> list[int]:
    weeks = {"05": {}, "11": {}}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            code = row["department_code"]
            if row["year"] != "2019" or row["event_code"] != "210" or code not in weeks:
                continue
            week = int(row["week"])
            if week in weeks[code]:
                raise ValueError(f"Duplicate weekly record for {code}, week {week}")
            if int(row["source_rows"]) > 0:
                cases = int(row["cases"])
                if cases < 0:
                    raise ValueError(f"Negative case count for {code}, week {week}")
                weeks[code][week] = cases
            else:
                if row["cases"] or row["observation_status"] != "source_absent":
                    raise ValueError(f"Inconsistent missing record for {code}, week {week}")
                weeks[code][week] = None

    expected = range(1, 53)
    for code, records in weeks.items():
        if set(records) != set(expected):
            raise ValueError(f"Expected all 52 calendar entries for department {code}")
    if any(value is None for value in weeks["05"].values()) or any(
        value is not None for value in weeks["11"].values()
    ):
        raise ValueError("Source coverage changed. Review the comparison and figure labels.")
    return [weeks["05"][week] for week in expected]


def render(source: Path, output: Path) -> None:
    counts = read_counts(source)
    weeks = range(1, len(counts) + 1)
    ink, muted, teal = "#12343d", "#435b61", "#146970"
    paper, rule = "#fbfaf7", "#d6deda"
    fig = plt.figure(figsize=(7.0, 5.45), facecolor=paper)
    left, right = 0.066, 0.953

    def label(y, words, size, *, bold=False, align="left", color=ink):
        fig.text(left if align == "left" else right, y, words, va="center", ha=align,
                 fontsize=size, color=color, weight="bold" if bold else "normal")

    label(0.925, "Dengue reporting in Colombia", 22, bold=True)
    label(0.855, "2019  ·  Epidemiological weeks 1–52", 14, color=muted)

    label(0.752, "Antioquia", 17, bold=True)
    label(0.752, f"{sum(counts):,} recorded cases", 15, align="right", color=teal)
    label(0.68, "Weekly case counts", 12, color=muted)
    ax = fig.add_axes((0.112, 0.375, right - 0.112, 0.271), facecolor=paper)
    ax.set_xlim(0.5, 52.5)
    ax.set_ylim(0, max(counts) * 1.08)
    ax.bar(weeks, counts, width=0.80, color=teal, linewidth=0)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=rule, linewidth=0.9)
    ax.set_yticks([0, 50, 100, 150])
    ticks = [1, 13, 26, 39, 52]
    ax.set_xticks(ticks, ["1", "13", "26", "39", "52"])
    ax.tick_params(length=0, colors=muted, labelsize=12, pad=5)
    ax.spines[:].set_visible(False)
    ax.spines["bottom"].set_visible(True)
    ax.spines["bottom"].set_color(muted)

    label(0.238, "Bogotá, D.C.", 17, bold=True)
    label(0.238, "Case count unknown", 15, align="right", color=ink)
    fig.add_artist(Rectangle((0.112, 0.151), right - 0.112, 0.047,
                             transform=fig.transFigure, facecolor="#f1f1ec",
                             edgecolor="#76858a", hatch="////", linewidth=0.8))
    label(0.104, "The source has no rows for any of the 52 weeks.", 13)
    label(0.044, "INS Colombia  ·  Dengue event 210  ·  CC BY-SA 4.0", 11, color=muted)
    metadata = {
        "Title": "Dengue reporting in Colombia, epidemiological weeks 1–52 of 2019",
        "Source": "Portal de Datos Abiertos www.datos.gov.co; Instituto Nacional de Salud "
                  "(INS), Bogotá D.C. https://www.datos.gov.co/d/4hyg-wa9d",
        "Description": "The Atlas aggregated INS municipal counts by department and week "
                       "and preserved missing observations. This figure selects two places "
                       "and event 210 from the release snapshot retrieved 2 November 2026. "
                       "The original source update was 17 October 2024.",
        "Copyright": "CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/",
    }
    fig.savefig(output, format="png", dpi=200, facecolor=paper, metadata=metadata)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Atlas surveillance_weekly.csv")
    parser.add_argument("output", type=Path, help="Path for the PNG figure")
    args = parser.parse_args()
    render(args.source, args.output)
