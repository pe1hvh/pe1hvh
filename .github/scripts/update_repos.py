"""
update_repos.py — SVG category-headers + Mermaid repo-kaarten met click-links.

Aanpak:
  - SVG headers (ongewijzigd, zien er goed uit)
  - Mermaid flowchart TD per categorie voor de repo-kaarten:
      * Wit kader met grijze rand  (identiek aan GitHub pinned-item stijl)
      * click handlers            → ECHTE hyperlinks in GitHub-rendered Mermaid
      * Hidden root-nodes R0/R1…  → kaarten per rij in dezelfde rank → naast elkaar
      * %%{init}%%                → theming (wit, #d0d7de rand, transparante verbindingen)
  - Geen <table>, geen vaste SVG-breedte, geen flex/float hacks
"""
import os, re, requests

USER        = os.environ.get("GITHUB_USER", "pe1hvh")
TOKEN       = os.environ.get("GITHUB_TOKEN", "")
README      = "README.md"
CARDS_DIR   = "cards"
START       = "<!-- REPOS_START -->"
END         = "<!-- REPOS_END -->"
SKIP_REPOS  = {"pe1hvh"}
HEADER_COLOR = "#0969da"

# ── MeshCore tekst-logo ────────────────────────────────────────────────────
_MC_SCALE = 1.8667
_MC_PATHS = '<path d="M3.277,0.053C2.829,0.053 2.401,0.41 2.321,0.851L0.013,13.623C-0.067,14.064 0.232,14.421 0.681,14.421L3.13,14.421C3.578,14.421 4.006,14.064 4.086,13.623L5.004,8.54L6.684,13.957C6.766,14.239 7.02,14.421 7.337,14.421L10.58,14.421C10.897,14.421 11.217,14.239 11.401,13.957L15.043,8.513L14.119,13.623C14.038,14.064 14.338,14.421 14.787,14.421L17.236,14.421C17.684,14.421 18.112,14.064 18.192,13.623L20.5,0.851C20.582,0.41 20.283,0.053 19.834,0.053L16.69,0.053C16.373,0.053 16.053,0.235 15.87,0.517L9.897,9.473C9.803,9.616 9.578,9.578 9.528,9.41L7.074,0.517C6.992,0.235 6.738,0.053 6.421,0.053L3.277,0.053Z"/><path d="M21.146,14.421C21.146,14.421 33.257,14.421 33.257,14.421C33.526,14.421 33.784,14.205 33.831,13.942L34.337,11.128C34.385,10.863 34.206,10.649 33.936,10.649L25.519,10.649C25.429,10.649 25.37,10.576 25.385,10.488L25.635,9.105C25.65,9.017 25.736,8.944 25.826,8.944L32.596,8.944C32.865,8.944 33.123,8.728 33.171,8.465L33.621,5.974C33.669,5.709 33.49,5.495 33.221,5.495L26.45,5.495C26.361,5.495 26.301,5.423 26.317,5.335L26.584,3.852C26.599,3.764 26.685,3.691 26.775,3.691L35.192,3.691C35.462,3.691 35.719,3.476 35.767,3.21L36.258,0.498C36.306,0.235 36.126,0.019 35.857,0.019L23.746,0.019C23.297,0.019 22.867,0.378 22.788,0.819L20.474,13.621C20.396,14.062 20.695,14.421 21.146,14.421Z"/><path d="M45.926,14.419L45.926,14.421L46.346,14.421C48.453,14.421 50.465,12.742 50.839,10.67L51.081,9.327C51.456,7.256 50.05,5.576 47.943,5.576L41.455,5.576C41.186,5.576 41.007,5.363 41.054,5.097L41.218,4.192C41.266,3.927 41.524,3.713 41.793,3.713L50.569,3.713C51.018,3.713 51.446,3.356 51.526,2.915L51.9,0.85C51.98,0.407 51.68,0.05 51.232,0.05L41.638,0.05C39.531,0.05 37.519,1.73 37.145,3.801L36.88,5.267C36.505,7.339 37.91,9.018 40.018,9.018L46.506,9.018C46.775,9.018 46.954,9.231 46.907,9.497L46.785,10.176C46.737,10.441 46.479,10.655 46.21,10.655L37.189,10.655C36.741,10.655 36.313,11.012 36.233,11.453L35.841,13.621C35.761,14.062 36.061,14.419 36.51,14.419L45.926,14.419Z"/><path d="M68.008,0.046C68.008,0.046 65.296,0.046 65.296,0.046C64.847,0.046 64.42,0.403 64.34,0.844L63.532,5.31C63.517,5.398 63.431,5.469 63.341,5.469L58.085,5.469C57.995,5.469 57.936,5.398 57.951,5.31L58.758,0.844C58.837,0.403 58.539,0.046 58.09,0.046L55.378,0.046C54.93,0.046 54.502,0.403 54.422,0.844L52.112,13.623C52.032,14.064 52.331,14.421 52.78,14.421L55.492,14.421C55.941,14.421 56.369,14.064 56.449,13.623L57.272,9.074C57.287,8.986 57.373,8.914 57.462,8.914L62.719,8.914C62.809,8.914 62.868,8.985 62.853,9.074L62.032,13.623C61.952,14.064 62.252,14.421 62.7,14.421L65.413,14.421C65.861,14.421 66.289,14.064 66.369,13.623L68.678,0.844C68.755,0.403 68.457,0.046 68.008,0.046Z"/><path d="M72.099,14.421C72.099,14.421 80.066,14.421 80.066,14.421C80.515,14.421 80.943,14.064 81.022,13.623L81.414,11.453C81.494,11.012 81.194,10.655 80.746,10.655L73.828,10.655C73.559,10.655 73.38,10.441 73.427,10.176L74.51,4.215C74.558,3.951 74.815,3.736 75.082,3.736L82,3.736C82.448,3.736 82.876,3.379 82.956,2.938L83.34,0.817C83.42,0.376 83.12,0.019 82.672,0.019L74.724,0.019C72.622,0.019 70.614,1.691 70.236,3.757L68.965,10.665C68.587,12.738 69.99,14.421 72.099,14.421Z"/><path d="M97.176,-0C97.176,0 88.882,0 88.882,0C86.775,0 84.763,1.68 84.389,3.751L83.139,10.67C82.765,12.741 84.169,14.421 86.277,14.421L94.571,14.421C96.678,14.421 98.69,12.741 99.064,10.67L100.314,3.751C100.689,1.68 99.284,-0 97.176,-0ZM94.798,10.178C94.75,10.443 94.492,10.657 94.223,10.657L87.978,10.657C87.709,10.657 87.529,10.443 87.577,10.178L88.659,4.192C88.707,3.927 88.964,3.713 89.234,3.713L95.477,3.713C95.747,3.713 95.926,3.927 95.878,4.192L94.798,10.178Z"/><path d="M101.284,14.421L103.995,14.421C104.443,14.421 104.871,14.065 104.951,13.624L105.43,10.97C105.446,10.882 105.531,10.81 105.621,10.81L108.902,10.806C109.064,10.806 109.2,10.886 109.267,11.018L110.813,14.035C110.992,14.392 111.319,14.434 112.303,14.419C112.88,14.426 113.756,14.382 115.169,14.382C115.623,14.382 115.902,13.907 115.678,13.51L113.989,10.569C113.945,10.491 113.993,10.386 114.086,10.34C115.39,9.707 116.423,8.477 116.681,7.055L117.27,3.785C117.646,1.713 116.242,0.033 114.134,0.033L103.884,0.033C103.436,0.033 103.008,0.39 102.928,0.831L100.616,13.623C100.536,14.064 100.836,14.421 101.284,14.421L101.284,14.421ZM106.73,3.791C106.745,3.703 106.831,3.631 106.921,3.631L112.225,3.631C112.626,3.631 112.891,3.949 112.821,4.343L112.431,6.494C112.359,6.885 111.979,7.204 111.58,7.204L106.276,7.204C106.186,7.204 106.127,7.133 106.142,7.043L106.73,3.791Z"/><path d="M118.277,14.421C118.277,14.421 130.388,14.421 130.388,14.421C130.657,14.421 130.915,14.205 130.963,13.942L131.468,11.128C131.516,10.863 131.337,10.649 131.068,10.649L122.65,10.649C122.56,10.649 122.501,10.576 122.516,10.488L122.766,9.105C122.781,9.017 122.867,8.944 122.957,8.944L129.728,8.944C129.997,8.944 130.254,8.728 130.302,8.465L130.753,5.974C130.801,5.709 130.621,5.495 130.352,5.495L123.581,5.495C123.492,5.495 123.432,5.423 123.448,5.335L123.715,3.852C123.73,3.764 123.816,3.691 123.906,3.691L132.324,3.691C132.593,3.691 132.851,3.476 132.898,3.21L133.389,0.498C133.437,0.235 133.257,0.019 132.988,0.019L120.877,0.019C120.428,0.019 119.999,0.378 119.919,0.819L117.605,13.621C117.527,14.062 117.827,14.421 118.277,14.421Z"/>'

CATEGORIES = {
    "MeshCore": {
        "repos": {"meshcore-gui","meshcore-ble-connect","meshcore-bridge",
                  "meshcore-observer","meshcore_py"},
        "label": "MeshCore", "icon": None,
    },
    "Morse & CW": {
        "repos": {"configurable_morse_code_interface","VBand_interface","cw_lcwo_pcw_interface"},
        "label": "Morse &amp; CW — Interfaces",
        "icon": (
            '<rect x="2" y="32" width="36" height="5" rx="2.5"/>'
            '<rect x="17" y="22" width="6" height="10" rx="1"/>'
            '<rect x="4" y="17" width="30" height="5" rx="2.5"/>'
            '<circle cx="31" cy="19.5" r="5.5"/>'
            '<rect x="27" y="13" width="9" height="3" rx="1.5" opacity="0.75"/>'
            '<rect x="4" y="22" width="7" height="3" rx="1" opacity="0.75"/>'
        ),
    },
    "Arduino": {
        "repos": {"frequency-generator","platformIO2arduinoIDE","measure_bouncing"},
        "label": "Arduino — Projects",
        "icon": (
            '<circle cx="13" cy="20" r="12" stroke="white" stroke-width="3" fill="none"/>'
            '<circle cx="27" cy="20" r="12" stroke="white" stroke-width="3" fill="none"/>'
            '<line x1="8" y1="20" x2="18" y2="20" stroke="white" stroke-width="3" stroke-linecap="round"/>'
            '<line x1="13" y1="15" x2="13" y2="25" stroke="white" stroke-width="3" stroke-linecap="round"/>'
            '<line x1="22" y1="20" x2="32" y2="20" stroke="white" stroke-width="3" stroke-linecap="round"/>'
        ),
    },
    "Google Timeline": {
        "repos": {"Timeline-GPX-Exporter","TimeLine2MariaDB"},
        "label": "Google Timeline — Exporters",
        "icon": (
            '<path d="M10 24 C5 24 2 20 2 16 C2 10 10 2 10 2 C10 2 18 10 18 16 C18 20 15 24 10 24Z"/>'
            '<circle cx="10" cy="15" r="4" fill="#0969da"/>'
            '<path d="M30 24 C25 24 22 20 22 16 C22 10 30 2 30 2 C30 2 38 10 38 16 C38 20 35 24 30 24Z"/>'
            '<circle cx="30" cy="15" r="4" fill="#0969da"/>'
            '<path d="M18 16 Q24 6 22 16" stroke="white" stroke-width="2" fill="none" stroke-dasharray="3,3"/>'
        ),
    },
    "Other": {
        "repos": set(), "label": "Other — Projects",
        "icon": (
            '<rect x="4" y="6" width="32" height="28" rx="3" stroke="white" stroke-width="2.5" fill="none"/>'
            '<line x1="4" y1="14" x2="36" y2="14" stroke="white" stroke-width="2"/>'
            '<circle cx="10" cy="10" r="2"/><circle cx="17" cy="10" r="2"/><circle cx="24" cy="10" r="2"/>'
            '<rect x="9" y="19" width="22" height="2.5" rx="1.2"/>'
            '<rect x="9" y="25" width="16" height="2.5" rx="1.2"/>'
        ),
    },
}

# Taalkleur als gekleurde emoji-cirkel (werkt overal zonder CSS)
LANG_DOT = {
    "Python":"🔵","C++":"🔴","C":"⚫","PHP":"🟣",
    "JavaScript":"🟡","TypeScript":"🔵","Shell":"🟢",
    "HTML":"🟠","CSS":"🟣","Makefile":"🟤",
}


def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"','&quot;')


def cat_slug(c):
    return c.lower().replace(" ","-").replace("&","en")


def fetch_repos():
    hdrs = {"Accept":"application/vnd.github+json"}
    if TOKEN: hdrs["Authorization"] = f"Bearer {TOKEN}"
    repos, url = [], f"https://api.github.com/users/{USER}/repos"
    params = {"per_page":100,"sort":"updated"}
    while url:
        r = requests.get(url, headers=hdrs, params=params, timeout=15)
        r.raise_for_status()
        repos.extend(r.json())
        url = r.links.get("next",{}).get("url")
        params = {}
    return [r for r in repos if r["name"] not in SKIP_REPOS]


def make_header_svg(cat):
    """SVG categorie-header banner (ongewijzigd)."""
    cfg  = CATEGORIES[cat]
    W, H = 812, 56
    if cat == "MeshCore":
        body = (
            f'<g transform="translate(12,14) scale({_MC_SCALE})" fill="white">{_MC_PATHS}</g>'
            '<text x="274" y="36"'
            ' font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif"'
            ' font-size="17" font-weight="400" fill="white" opacity="0.85">&#8212; LoRa Mesh Networking</text>'
        )
    else:
        body = (
            f'<g transform="translate(10,8)" fill="white">{cfg["icon"]}</g>'
            f'<text x="62" y="36"'
            f' font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif"'
            f' font-size="19" font-weight="700" fill="white">{cfg["label"]}</text>'
        )
    return (
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{W}" height="{H}" rx="8" fill="{HEADER_COLOR}"/>{body}</svg>'
    )


def write_headers():
    """Schrijf alleen de categorie header-SVG's."""
    os.makedirs(CARDS_DIR, exist_ok=True)
    for cat in CATEGORIES:
        path = os.path.join(CARDS_DIR, f"header-{cat_slug(cat)}.svg")
        open(path, "w", encoding="utf-8").write(make_header_svg(cat))
    print(f"{len(CATEGORIES)} header-SVG's geschreven.")


def categorize(repos):
    assigned, result = set(), {cat:[] for cat in CATEGORIES}
    for cat, cfg in CATEGORIES.items():
        if cat == "Other": continue
        for repo in repos:
            if repo["name"] in cfg["repos"]:
                result[cat].append(repo); assigned.add(repo["name"])
    for repo in repos:
        if repo["name"] not in assigned:
            result["Other"].append(repo)
    return result


def _node_id(name):
    """Mermaid node-id: alleen letters, cijfers en underscore."""
    return re.sub(r"[^A-Za-z0-9]", "_", name)


def _node_label(repo):
    """
    Mermaid node-tekst met backtick-syntax (ondersteunt markdown-bold + newlines).
    Maximaal 3 regels: naam · beschrijving · meta.
    """
    name  = repo["name"]
    desc  = (repo.get("description") or "")[:55]
    lang  = repo.get("language") or ""
    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)
    dot   = LANG_DOT.get(lang, "⚪")

    meta = ""
    if lang:  meta += f"{dot} {lang}"
    if stars: meta += f"  ⭐ {stars}"
    if forks: meta += f"  ⑂ {forks}"

    # Backtick-label: Mermaid rendert ** als bold, \n als regeleinde
    return f'"`**{name}**\n{desc}\n{meta}`"'


def make_mermaid_block(repos):
    """
    Genereer een Mermaid flowchart TD block voor een lijst repos.

    Grid-techniek:
      Elke rij krijgt een onzichtbare root-node R0, R1, …
      R_i ~~~ kaart_links  en  R_i ~~~ kaart_rechts
      Beide kaarten delen daardoor dezelfde rank → verschijnen NAAST ELKAAR.
      R_i ~~~ R_{i+1} zorgt dat de rijen verticaal gestapeld worden.
    """
    lines = []

    # ── Mermaid theme: wit kader, grijze rand, geen pijlen zichtbaar ──────
    lines += [
        "%%{init: {'theme': 'base', 'themeVariables': {",
        "  'primaryColor': '#ffffff',",
        "  'primaryBorderColor': '#d0d7de',",
        "  'primaryTextColor': '#24292f',",
        "  'lineColor': 'transparent',",
        "  'fontSize': '13px'",
        "}}}%%",
        "flowchart TD",
    ]

    # ── Node definities ───────────────────────────────────────────────────
    for repo in repos:
        nid   = _node_id(repo["name"])
        label = _node_label(repo)
        lines.append(f"    {nid}{label}")

    # ── Grid via verborgen root-nodes per rij ─────────────────────────────
    rows = [repos[i:i+2] for i in range(0, len(repos), 2)]
    for ri, row in enumerate(rows):
        root = f"R{ri}"
        lines.append(f'    {root}[" "]')
        # Root verbindt beide kaarten → zelfde rank → naast elkaar
        for repo in row:
            lines.append(f"    {root} ~~~ {_node_id(repo['name'])}")
        # Vorige root ~~~ huidige root → verticale stapeling van rijen
        if ri > 0:
            lines.append(f"    R{ri-1} ~~~ {root}")
        # Root onzichtbaar
        lines.append(
            f"    style {root} fill:transparent,stroke:transparent,"
            f"color:transparent,width:0px,height:0px"
        )

    # ── Click handlers (echte links in GitHub-rendered Mermaid) ───────────
    for repo in repos:
        nid = _node_id(repo["name"])
        lines.append(f'    click {nid} href "{repo["html_url"]}" _blank')

    # ── Node stijlen: wit vlak + grijze rand (pinned-item stijl) ─────────
    for repo in repos:
        nid = _node_id(repo["name"])
        lines.append(
            f"    style {nid} fill:#ffffff,stroke:#d0d7de,stroke-width:1px,"
            f"color:#0969da,text-align:left"
        )

    return "\n".join(lines)


def build_readme_block(repos):
    grouped = categorize(repos)
    parts   = []
    for cat, group in grouped.items():
        if not group: continue
        slug = cat_slug(cat)

        # SVG categorie-header (ongewijzigd)
        parts.append(f'\n<img src="cards/header-{slug}.svg" width="812"/>\n')

        # Mermaid kaarten-blok
        mermaid_code = make_mermaid_block(group)
        parts.append("```mermaid")
        parts.append(mermaid_code)
        parts.append("```\n")

    return "\n".join(parts)


def update_readme(repos):
    with open(README, encoding="utf-8") as fh:
        content = fh.read()
    pattern = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL)
    if not pattern.search(content):
        raise ValueError(f"Markers niet gevonden in {README}")
    block = (
        f"{START}\n"
        f"<!-- {len(repos)} repos — auto-updated by GitHub Actions -->\n"
        f"{build_readme_block(repos)}\n"
        f"{END}"
    )
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(pattern.sub(block, content))
    print("README.md bijgewerkt.")


if __name__ == "__main__":
    print(f"Repositories ophalen voor {USER}...")
    repos = fetch_repos()
    print(f"{len(repos)} repos gevonden.")
    write_headers()
    update_readme(repos)
