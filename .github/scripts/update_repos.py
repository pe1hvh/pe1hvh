"""
update_repos.py — generates SVG card per repo + category header SVGs,
updates README.md with inline <a><img/></a> pairs (no table, no borders).
"""

import os
import re
import textwrap
import requests

USER       = os.environ.get("GITHUB_USER", "pe1hvh")
TOKEN      = os.environ.get("GITHUB_TOKEN", "")
README     = "README.md"
CARDS_DIR  = "cards"
START      = "<!-- REPOS_START -->"
END        = "<!-- REPOS_END -->"
SKIP_REPOS = {"pe1hvh"}

HEADER_COLOR = "#0969da"   # same blue as card repo-name text — ALL headers

MESHCORE_LOGO_URL = (
    "https://raw.githubusercontent.com/meshcore-dev/MeshCore/main/logo/meshcore.svg"
)

CATEGORIES = {
    "MeshCore": {
        "repos": {
            "meshcore-gui", "meshcore-ble-connect", "meshcore-bridge",
            "meshcore-observer", "meshcore_py",
        },
        "label": "MeshCore — LoRa Mesh Networking",
        "icon": None,   # fetched at runtime
    },
    "Morse & CW": {
        "repos": {
            "configurable_morse_code_interface",
            "VBand_interface",
            "cw_lcwo_pcw_interface",
        },
        "label": "Morse & CW — Interfaces",
        "icon": """
          <rect x="2"  y="32" width="36" height="5"  rx="2.5"/>
          <rect x="17" y="22" width="6"  height="10" rx="1"/>
          <rect x="4"  y="17" width="30" height="5"  rx="2.5"/>
          <circle cx="31" cy="19.5" r="5.5"/>
          <rect x="27" y="13" width="9" height="3" rx="1.5" opacity="0.75"/>
          <rect x="4"  y="22" width="7" height="3" rx="1"   opacity="0.75"/>
        """,
    },
    "Arduino": {
        "repos": {
            "frequency-generator",
            "platformIO2arduinoIDE",
            "measure_bouncing",
        },
        "label": "Arduino — Projects",
        "icon": """
          <circle cx="13" cy="20" r="12" stroke="white" stroke-width="3" fill="none"/>
          <circle cx="27" cy="20" r="12" stroke="white" stroke-width="3" fill="none"/>
          <line x1="8"  y1="20" x2="18" y2="20" stroke="white" stroke-width="3"
                stroke-linecap="round"/>
          <line x1="13" y1="15" x2="13" y2="25" stroke="white" stroke-width="3"
                stroke-linecap="round"/>
          <line x1="22" y1="20" x2="32" y2="20" stroke="white" stroke-width="3"
                stroke-linecap="round"/>
        """,
    },
    "Google Timeline": {
        "repos": {
            "Timeline-GPX-Exporter",
            "TimeLine2MariaDB",
        },
        "label": "Google Timeline — Exporters",
        "icon": """
          <path d="M10 24 C5 24 2 20 2 16 C2 10 10 2 10 2 C10 2 18 10 18 16
                   C18 20 15 24 10 24Z"/>
          <circle cx="10" cy="15" r="4" fill="#0969da"/>
          <path d="M30 24 C25 24 22 20 22 16 C22 10 30 2 30 2 C30 2 38 10 38 16
                   C38 20 35 24 30 24Z"/>
          <circle cx="30" cy="15" r="4" fill="#0969da"/>
          <path d="M18 16 Q24 6 22 16" stroke="white" stroke-width="2"
                fill="none" stroke-dasharray="3,3"/>
        """,
    },
    "Other": {
        "repos":  set(),
        "label":  "Other — Projects",
        "icon": """
          <rect x="4"  y="6"  width="32" height="28" rx="3" stroke="white"
                stroke-width="2.5" fill="none"/>
          <line x1="4"  y1="14" x2="36" y2="14" stroke="white" stroke-width="2"/>
          <circle cx="10" cy="10" r="2"/>
          <circle cx="17" cy="10" r="2"/>
          <circle cx="24" cy="10" r="2"/>
          <rect x="9"  y="19" width="22" height="2.5" rx="1.2"/>
          <rect x="9"  y="25" width="16" height="2.5" rx="1.2"/>
        """,
    },
}

LANG_COLORS = {
    "Python":     "#3572A5",
    "C++":        "#f34b7d",
    "C":          "#555555",
    "PHP":        "#4F5D95",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "Shell":      "#89e051",
    "HTML":       "#e34c26",
    "CSS":        "#563d7c",
    "Makefile":   "#427819",
}

ICON_REPO = (
    "M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75"
    "h-2.5a.75.75 0 010-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05"
    "A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8z"
)
ICON_FORK = (
    "M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878"
    "A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 "
    "002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 "
    "015 6.25v-.878z"
)
ICON_STAR = (
    "M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279"
    "l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75"
    " 0 01-1.088-.79l.72-4.194L.873 6.374a.75.75 0 01.416-1.28l4.21-.611"
    "L7.327.668A.75.75 0 018 .25z"
)

CARD_W = 400
CARD_H = 120
PAD    = 16


# ── Helpers ───────────────────────────────────────────────────────────────────

def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


def fetch_repos() -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    repos  = []
    url    = f"https://api.github.com/users/{USER}/repos"
    params: dict = {"per_page": 100, "sort": "updated"}
    while url:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        r.raise_for_status()
        repos.extend(r.json())
        url    = r.links.get("next", {}).get("url")
        params = {}
    return [r for r in repos if r["name"] not in SKIP_REPOS]


# ── MeshCore logo ─────────────────────────────────────────────────────────────

def fetch_meshcore_icon_b64() -> str:
    """
    Fetch official MeshCore SVG, strip background, force paths to white,
    return as base64 data-URI so it can be embedded as <image/> in the header.
    """
    import base64

    try:
        r = requests.get(MESHCORE_LOGO_URL, timeout=10)
        r.raise_for_status()
        svg = r.text

        # Remove <style> blocks
        svg = re.sub(r"<style[^>]*>.*?</style>", "", svg, flags=re.DOTALL)
        # Remove background rect (first rect that has no useful stroke/path role)
        svg = re.sub(
            r'<rect[^>]*(?:width=["\']100%["\']|width=["\'][\d.]+["\'][^>]*height=["\'][\d.]+["\'])[^/]*/?>',
            "", svg,
        )
        # Force all fills to white, keep fill="none" as-is
        svg = re.sub(r'fill="(?!none)[^"]*"', 'fill="white"', svg)
        svg = re.sub(r"fill='(?!none)[^']*'", "fill='white'", svg)
        # Force all strokes to white
        svg = re.sub(r'stroke="(?!none)[^"]*"', 'stroke="white"', svg)
        svg = re.sub(r"stroke='(?!none)[^']*'", "stroke='white'", svg)

        data = base64.b64encode(svg.encode()).decode()
        return f"data:image/svg+xml;base64,{data}"

    except Exception as e:
        print(f"Warning: MeshCore logo fetch failed: {e}")
        return ""


# ── SVG generators ────────────────────────────────────────────────────────────

def make_header_svg(cat: str) -> str:
    cfg   = CATEGORIES[cat]
    label = esc(cfg["label"])
    W, H  = 812, 56

    if cat == "MeshCore":
        data_uri = fetch_meshcore_icon_b64()
        if data_uri:
            icon_elem = (
                f'<image href="{data_uri}" '
                f'x="8" y="8" width="40" height="40"/>'
            )
        else:
            # fallback: simple radio-wave icon
            icon_elem = (
                '<circle cx="20" cy="20" r="4" fill="white"/>'
                '<path d="M20 12 A8 8 0 0 1 20 28" stroke="white" stroke-width="3" fill="none"/>'
                '<path d="M20 12 A8 8 0 0 0 20 28" stroke="white" stroke-width="3" fill="none"/>'
                '<path d="M20 6 A14 14 0 0 1 20 34" stroke="white" stroke-width="3" fill="none"/>'
                '<path d="M20 6 A14 14 0 0 0 20 34" stroke="white" stroke-width="3" fill="none"/>'
            )
            icon_elem = f'<g transform="translate(10,8)" fill="white">{icon_elem}</g>'
    else:
        icon_elem = (
            f'<g transform="translate(10,8)" fill="white">'
            f'{cfg["icon"]}</g>'
        )

    return (
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink">\n'
        f'  <rect width="{W}" height="{H}" rx="8" fill="{HEADER_COLOR}"/>\n'
        f'  {icon_elem}\n'
        f'  <text x="62" y="36" '
        f'font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif" '
        f'font-size="19" font-weight="700" fill="white">{label}</text>\n'
        f'</svg>'
    )


def make_card_svg(repo: dict) -> str:
    name      = esc(repo["name"])
    desc      = repo.get("description") or ""
    lang      = repo.get("language") or ""
    stars     = repo.get("stargazers_count", 0)
    forks_cnt = repo.get("forks_count", 0)
    is_fork   = repo.get("fork", False)

    lang_color = LANG_COLORS.get(lang, "#8f8f8f")
    icon_path  = ICON_FORK if is_fork else ICON_REPO
    desc_lines = textwrap.wrap(desc, width=48)[:2]

    style = """  <style>
    .bg        { fill:#ffffff; stroke:#d0d7de; stroke-width:1; }
    .name      { font:600 13px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                 fill:#0969da; }
    .desc      { font:400 11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                 fill:#57606a; }
    .meta      { font:400 11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                 fill:#57606a; }
    .icon      { fill:#57606a; }
    .fork-bg   { fill:#f6f8fa; stroke:#d0d7de; stroke-width:1; }
    .fork-text { font:400 10px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                 fill:#57606a; }
    @media (prefers-color-scheme:dark) {
      .bg        { fill:#161b22; stroke:#30363d; }
      .name      { fill:#58a6ff; }
      .desc      { fill:#8b949e; }
      .meta      { fill:#8b949e; }
      .icon      { fill:#8b949e; }
      .fork-bg   { fill:#21262d; stroke:#30363d; }
      .fork-text { fill:#8b949e; }
    }
  </style>"""

    parts = [
        f'<svg width="{CARD_W}" height="{CARD_H}" viewBox="0 0 {CARD_W} {CARD_H}" '
        f'xmlns="http://www.w3.org/2000/svg">',
        style,
        f'<rect x="0" y="0" width="{CARD_W}" height="{CARD_H}" rx="8" class="bg"/>',
        f'<path transform="translate({PAD},{PAD}) scale(0.9)" d="{icon_path}" class="icon"/>',
        f'<text x="{PAD+20}" y="{PAD+13}" class="name">{name}</text>',
    ]

    if is_fork:
        parts += [
            f'<rect x="{CARD_W-58}" y="{PAD-2}" width="42" height="16" rx="8" class="fork-bg"/>',
            f'<text x="{CARD_W-37}" y="{PAD+10}" text-anchor="middle" class="fork-text">fork</text>',
        ]

    for i, line in enumerate(desc_lines):
        parts.append(f'<text x="{PAD}" y="{PAD+32+(i*16)}" class="desc">{esc(line)}</text>')

    mx     = PAD
    meta_y = CARD_H - 18
    if lang:
        parts.append(f'<circle cx="{mx+5}" cy="{meta_y-3}" r="5" fill="{lang_color}"/>')
        parts.append(f'<text x="{mx+14}" y="{meta_y}" class="meta">{esc(lang)}</text>')
        mx += len(lang) * 7 + 22
    if stars:
        parts.append(
            f'<path transform="translate({mx},{meta_y-11}) scale(0.8)" '
            f'd="{ICON_STAR}" class="icon"/>'
        )
        parts.append(f'<text x="{mx+14}" y="{meta_y}" class="meta">{stars}</text>')
        mx += 36
    if forks_cnt:
        parts.append(
            f'<path transform="translate({mx},{meta_y-11}) scale(0.8)" '
            f'd="{ICON_FORK}" class="icon"/>'
        )
        parts.append(f'<text x="{mx+14}" y="{meta_y}" class="meta">{forks_cnt}</text>')

    parts.append("</svg>")
    return "\n".join(parts)


# ── File writers ──────────────────────────────────────────────────────────────

def cat_slug(cat: str) -> str:
    return cat.lower().replace(" ", "-").replace("&", "en")


def write_cards(repos: list[dict]) -> None:
    os.makedirs(CARDS_DIR, exist_ok=True)
    existing = {f for f in os.listdir(CARDS_DIR) if f.endswith(".svg")}
    current  = {f"{r['name']}.svg" for r in repos}
    current |= {f"header-{cat_slug(c)}.svg" for c in CATEGORIES}
    for stale in existing - current:
        os.remove(os.path.join(CARDS_DIR, stale))
    for repo in repos:
        with open(os.path.join(CARDS_DIR, f"{repo['name']}.svg"), "w", encoding="utf-8") as fh:
            fh.write(make_card_svg(repo))
    for cat in CATEGORIES:
        with open(os.path.join(CARDS_DIR, f"header-{cat_slug(cat)}.svg"), "w", encoding="utf-8") as fh:
            fh.write(make_header_svg(cat))
    print(f"{len(repos)} card SVGs + {len(CATEGORIES)} headers written.")


# ── Categorisation ────────────────────────────────────────────────────────────

def categorize(repos: list[dict]) -> dict[str, list[dict]]:
    assigned: set[str] = set()
    result = {cat: [] for cat in CATEGORIES}
    for cat, cfg in CATEGORIES.items():
        if cat == "Other":
            continue
        for repo in repos:
            if repo["name"] in cfg["repos"]:
                result[cat].append(repo)
                assigned.add(repo["name"])
    for repo in repos:
        if repo["name"] not in assigned:
            result["Other"].append(repo)
    return result


# ── README block — NO TABLE, inline <a><img/></a> pairs ──────────────────────

def build_readme_block(repos: list[dict]) -> str:
    grouped = categorize(repos)
    parts   = []

    for cat, group in grouped.items():
        if not group:
            continue
        slug = cat_slug(cat)

        # Full-width header image
        parts.append(f'\n<img src="cards/header-{slug}.svg" width="812"/>\n')

        # Two cards per row using align="left" + br clear
        for i in range(0, len(group), 2):
            left  = group[i]
            right = group[i + 1] if i + 1 < len(group) else None

            row = (
                f'<a href="{left["html_url"]}">'
                f'<img align="left" src="cards/{left["name"]}.svg" width="400"/>'
                f'</a>'
            )
            if right:
                row += (
                    f'<a href="{right["html_url"]}">'
                    f'<img align="left" src="cards/{right["name"]}.svg" width="400"/>'
                    f'</a>'
                )
            parts.append(row)
            parts.append('<br clear="both"/>\n')

    return "\n".join(parts)


def update_readme(repos: list[dict]) -> None:
    with open(README, encoding="utf-8") as fh:
        content = fh.read()
    pattern = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    if not pattern.search(content):
        raise ValueError(f"Markers not found in {README}")
    block = (
        f"{START}\n"
        f"<!-- {len(repos)} repos — auto-updated by GitHub Actions -->\n"
        f"{build_readme_block(repos)}\n"
        f"{END}"
    )
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(pattern.sub(block, content))
    print("README.md updated.")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Fetching repositories for {USER}...")
    repos = fetch_repos()
    print(f"{len(repos)} repos found.")
    write_cards(repos)
    update_readme(repos)
