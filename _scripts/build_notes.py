# Builds the nonlinear control notes pages; run: python _scripts/build_notes.py <vault dir> <notes dir inside vault>
import html
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from PIL import Image

if len(sys.argv) != 3:
    sys.exit("usage: python _scripts/build_notes.py <vault dir> <notes dir inside vault>")
VAULT = Path(sys.argv[1]).expanduser()
NOTES_DIR = VAULT / sys.argv[2]
SITE = Path(__file__).resolve().parents[1]
OUT_DIR = SITE / "blog/nonlinear-control"
IMG_DIR = SITE / "images/notes"
URL = "/blog/nonlinear-control/"

# lecture file date -> page title; edit titles here
TITLES = {
    "1-27": "Math Background: Norms, Open Sets and Convergence",
    "1-29": "Cauchy Sequences, Banach Spaces and Contraction Mapping",
    "2-3": "Continuity, Lipschitz Functions and Local Existence and Uniqueness",
    "2-5": "Global Existence, Gronwall–Bellman and Continuous Dependence on Initial Conditions",
    "2-10": "Energy Functions, Compactness and Lyapunov Stability Definitions",
    "2-12": "Lyapunov's Direct Method",
    "2-17": "Global Asymptotic Stability, LaSalle's Theorem and Instability",
    "2-19": "Chetaev's Theorem, Quadratic Lyapunov Functions and Linearization",
    "2-24": "Region of Attraction and Time-Varying Systems",
    "2-26": "Class K Functions, Uniform and Exponential Stability",
    "3-3": "Midterm Review",
    "3-10": "Control Lyapunov Functions and Min-Norm Control",
    "3-12": "Sontag's Formula and the Small Control Property",
    "3-17": "Backstepping",
    "3-19": "Strict-Feedback Systems and Sliding Mode Control",
    "3-31": "Sliding Mode Control: Sliding Surfaces and the Reaching Phase",
    "4-2": "Feedback Linearization and Input–Output Linearization",
    "4-9": "Relative Degree and Zero Dynamics",
    "4-14": "Zero Dynamics, Manifolds and Tangent Spaces",
    "4-16": "Vector Fields, Lie Brackets and Involutive Distributions",
    "4-21": "The Feedback Linearization Theorem and MIMO Systems",
    "4-28": "Final Exam Review",
}

UNITS = [
    ("Mathematical preliminaries and existence of solutions", 1, 4),
    ("Lyapunov stability", 5, 11),
    ("Nonlinear control design", 12, 16),
    ("Feedback linearization and geometric control", 17, 22),
]

MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def date_key(path):
    month, day = path.stem.split()[-1].split("-")
    return int(month), int(day)


def extract_math(text):
    # Obsidian-style math: $$...$$ may span lines, $...$ stays on one line
    out, maths, i = [], [], 0
    while i < len(text):
        if text.startswith("$$", i):
            j = text.find("$$", i + 2)
            if j != -1:
                maths.append(("display", text[i + 2:j]))
                out.append(f"MATHPH{len(maths) - 1}Z")
                i = j + 2
                continue
        elif text[i] == "$":
            end_of_line = text.find("\n", i)
            end_of_line = len(text) if end_of_line == -1 else end_of_line
            j = text.find("$", i + 1, end_of_line)
            if j > i + 1:
                content = text[i + 1:j]
                line_start = text.rfind("\n", 0, i) + 1
                # pipes are escaped inside markdown table cells
                if text[line_start:i].lstrip().startswith("|"):
                    content = content.replace("\\|", "|")
                maths.append(("inline", content))
                out.append(f"MATHPH{len(maths) - 1}Z")
                i = j + 1
                continue
        out.append(text[i])
        i += 1
    return "".join(out), maths


def restore_math(rendered, maths):
    def sub(match):
        kind, content = maths[int(match.group(1))]
        if kind == "display":
            return f'<span class="math-display">\\[{html.escape(content, quote=False)}\\]</span>'
        return f"\\({html.escape(content, quote=False)}\\)"
    return re.sub(r"MATHPH(\d+)Z", sub, rendered)


def copy_image(name):
    src = VAULT / name
    if not src.exists():
        sys.exit(f"missing image: {src}")
    stem = "nl-" + re.sub(r"\D", "", name)
    img = Image.open(src)
    # large photos become web-sized JPEGs, small diagrams stay PNG
    if src.stat().st_size > 150_000:
        dest = IMG_DIR / f"{stem}.jpg"
        img = img.convert("RGB")
        if img.width > 1200:
            img = img.resize((1200, round(1200 * img.height / img.width)), Image.LANCZOS)
        img.save(dest, quality=82, optimize=True, progressive=True)
    else:
        dest = IMG_DIR / f"{stem}.png"
        # re-encoding drops any embedded metadata
        img = img.convert("RGBA")
        Image.frombytes(img.mode, img.size, img.tobytes()).save(dest, optimize=True)
    return f"/images/notes/{dest.name}"


def render(text, md):
    text = re.sub(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", lambda m: f"![]({copy_image(m.group(1))})", text)
    body, maths = extract_math(text)
    return restore_math(md.render(body), maths)


def nav(lectures, k):
    parts = []
    if k > 0:
        parts.append(f'<a href="{URL}lecture-{k:02d}/">← Lecture {k}</a>')
    parts.append(f'<a href="{URL}">All notes</a>')
    if k + 1 < len(lectures):
        parts.append(f'<a href="{URL}lecture-{k + 2:02d}/">Lecture {k + 2} →</a>')
    return '<p class="note-nav">' + " · ".join(parts) + "</p>"


def main():
    md = MarkdownIt("commonmark", {"breaks": True, "html": False}).enable("table").disable("code")
    lectures = sorted(NOTES_DIR.glob("lecture *.md"), key=date_key)
    missing = [p.stem for p in lectures if p.stem.split()[-1] not in TITLES]
    if missing:
        sys.exit(f"add titles for: {missing}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for k, path in enumerate(lectures):
        n = k + 1
        month, day = date_key(path)
        title = TITLES[path.stem.split()[-1]]
        date = f"{MONTHS[month]} {day}, 2026"
        body = render(path.read_text(encoding="utf-8"), md)
        page = (
            "---\n"
            "layout: default\n"
            f'title: "Lecture {n}: {title}"\n'
            f"permalink: {URL}lecture-{n:02d}/\n"
            "mathjax: true\n"
            "---\n\n"
            f"{nav(lectures, k)}\n\n"
            f"<h1>Lecture {n}: {title}</h1>\n"
            f'<p class="note-meta">Nonlinear Control Notes · {date}</p>\n\n'
            '<div class="note-body">\n{% raw %}\n' + body + "{% endraw %}\n</div>\n\n"
            f"{nav(lectures, k)}\n"
        )
        (OUT_DIR / f"lecture-{n:02d}.html").write_text(page, encoding="utf-8")
        rows.append((n, date, title))
    index = [
        "---",
        "layout: default",
        'title: "Nonlinear Control Notes"',
        f"permalink: {URL}",
        "---",
        "",
        "# Nonlinear Control Notes",
        "",
        "*Spring 2026 · UC Berkeley*",
        "",
        "My lecture notes from a graduate course in nonlinear systems and control. They cover existence and uniqueness of solutions, Lyapunov stability, control Lyapunov functions, backstepping, sliding mode control and feedback linearization. The notes follow Khalil's *Nonlinear Systems*.",
        "",
    ]
    for unit, first, last in UNITS:
        index.append(f"### {unit}")
        index.append("")
        for n, date, title in rows[first - 1:last]:
            index.append(f"- [Lecture {n}: {title}]({URL}lecture-{n:02d}/) · *{date}*")
        index.append("")
    (OUT_DIR / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(f"built {len(rows)} lectures into {OUT_DIR}")


main()
