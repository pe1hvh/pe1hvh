"""
update_repos.py — per-repo SVG cards + category headers, two-column table layout.
"""
import os, re, textwrap, requests

USER       = os.environ.get("GITHUB_USER", "pe1hvh")
TOKEN      = os.environ.get("GITHUB_TOKEN", "")
README     = "README.md"
CARDS_DIR  = "cards"
START      = "<!-- REPOS_START -->"
END        = "<!-- REPOS_END -->"
SKIP_REPOS = {"pe1hvh"}
HEADER_COLOR = "#0969da"

# Official MeshCore text logo (viewBox 0 0 134 15) scaled to 28px tall
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

LANG_COLORS = {
    "Python":"#3572A5","C++":"#f34b7d","C":"#555555","PHP":"#4F5D95",
    "JavaScript":"#f1e05a","TypeScript":"#3178c6","Shell":"#89e051",
    "HTML":"#e34c26","CSS":"#563d7c","Makefile":"#427819",
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
CARD_W, CARD_H, PAD = 400, 120, 16
CARD_W_FULL = 812          # wide card for single-repo categories


def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"','"&quot;"'[1:-1])


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


def make_card_svg(repo, card_w=CARD_W):
    name  = esc(repo["name"])
    desc  = repo.get("description") or ""
    lang  = repo.get("language") or ""
    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)
    fork  = repo.get("fork", False)
    lc    = LANG_COLORS.get(lang,"#8f8f8f")
    ip    = ICON_FORK if fork else ICON_REPO
    wrap_w = 48 if card_w == CARD_W else 100   # wider text wrap for full-width card
    dl    = textwrap.wrap(desc, width=wrap_w)[:2]
    style = (
        "<style>"
        ".bg{fill:#fff;stroke:#d0d7de;stroke-width:1}"
        ".nm{font:600 13px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#0969da}"
        ".dc,.mt{font:400 11px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#57606a}"
        ".ic{fill:#57606a}.fb{fill:#f6f8fa;stroke:#d0d7de;stroke-width:1}"
        ".ft{font:400 10px -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#57606a}"
        "@media(prefers-color-scheme:dark){"
        ".bg{fill:#161b22;stroke:#30363d}.nm{fill:#58a6ff}"
        ".dc,.mt{fill:#8b949e}.ic{fill:#8b949e}"
        ".fb{fill:#21262d;stroke:#30363d}.ft{fill:#8b949e}}"
        "</style>"
    )
    p = [
        f'<svg width="{card_w}" height="{CARD_H}" viewBox="0 0 {card_w} {CARD_H}" xmlns="http://www.w3.org/2000/svg">',
        style,
        f'<rect x="0" y="0" width="{card_w}" height="{CARD_H}" rx="8" class="bg"/>',
        f'<path transform="translate({PAD},{PAD}) scale(0.9)" d="{ip}" class="ic"/>',
        f'<text x="{PAD+20}" y="{PAD+13}" class="nm">{name}</text>',
    ]
    if fork:
        bx = CARD_W-58
        p += [f'<rect x="{bx}" y="{PAD-2}" width="42" height="16" rx="8" class="fb"/>',
              f'<text x="{bx+21}" y="{PAD+10}" text-anchor="middle" class="ft">fork</text>']
    for i,ln in enumerate(dl):
        p.append(f'<text x="{PAD}" y="{PAD+32+(i*16)}" class="dc">{esc(ln)}</text>')
    mx, my = PAD, CARD_H-18
    if lang:
        p += [f'<circle cx="{mx+5}" cy="{my-3}" r="5" fill="{lc}"/>',
              f'<text x="{mx+14}" y="{my}" class="mt">{esc(lang)}</text>']
        mx += len(lang)*7+22
    if stars:
        p += [f'<path transform="translate({mx},{my-11}) scale(0.8)" d="{ICON_STAR}" class="ic"/>',
              f'<text x="{mx+14}" y="{my}" class="mt">{stars}</text>']
        mx += 36
    if forks:
        p += [f'<path transform="translate({mx},{my-11}) scale(0.8)" d="{ICON_FORK}" class="ic"/>',
              f'<text x="{mx+14}" y="{my}" class="mt">{forks}</text>']
    p.append("</svg>")
    return "\n".join(p)


def write_cards(repos):
    os.makedirs(CARDS_DIR, exist_ok=True)
    existing = {f for f in os.listdir(CARDS_DIR) if f.endswith(".svg")}
    current  = {f"{r['name']}.svg" for r in repos}
    current |= {f"header-{cat_slug(c)}.svg" for c in CATEGORIES}
    for stale in existing - current:
        os.remove(os.path.join(CARDS_DIR, stale))
    # Determine which repos are alone in their category → wide card
    grouped = categorize(repos)
    single_repos = {group[0]["name"] for group in grouped.values() if len(group) == 1}
    for repo in repos:
        card_w = CARD_W_FULL if repo["name"] in single_repos else CARD_W
        open(os.path.join(CARDS_DIR,f"{repo['name']}.svg"),"w",encoding="utf-8").write(make_card_svg(repo, card_w=card_w))
    for cat in CATEGORIES:
        open(os.path.join(CARDS_DIR,f"header-{cat_slug(cat)}.svg"),"w",encoding="utf-8").write(make_header_svg(cat))
    print(f"{len(repos)} cards + {len(CATEGORIES)} headers written.")


def categorize(repos):
    assigned, result = set(), {cat:[] for cat in CATEGORIES}
    for cat,cfg in CATEGORIES.items():
        if cat=="Other": continue
        for repo in repos:
            if repo["name"] in cfg["repos"]:
                result[cat].append(repo); assigned.add(repo["name"])
    for repo in repos:
        if repo["name"] not in assigned:
            result["Other"].append(repo)
    return result


def td(repo):
    return (
        '<td width="50%" style="border:none;padding:4px;background:transparent">'
        f'<a href="{repo["html_url"]}">'
        f'<img src="cards/{repo["name"]}.svg" width="400"/></a></td>'
    )


def build_readme_block(repos):
    grouped = categorize(repos)
    parts   = []
    for cat, group in grouped.items():
        if not group: continue
        slug = cat_slug(cat)
        parts.append(f'\n<img src="cards/header-{slug}.svg" width="812"/>\n')
        parts.append(
            '<table border="0" cellspacing="4" cellpadding="0"'
            ' style="border:none;border-collapse:collapse;background:transparent">'
        )
        if len(group) == 1:
            # Single repo in category → full-width card spanning both columns
            repo = group[0]
            parts.append(
                f'<tr style="border:none;background:transparent">'
                f'<td colspan="2" style="border:none;padding:4px;background:transparent">'
                f'<a href="{repo["html_url"]}">'
                f'<img src="cards/{repo["name"]}.svg" width="812"/></a></td></tr>'
            )
        else:
            for i in range(0, len(group), 2):
                l = td(group[i])
                r = td(group[i+1]) if i+1<len(group) else '<td width="50%" style="border:none"></td>'
                parts.append(f'<tr style="border:none;background:transparent">{l}{r}</tr>')
        parts.append("</table>\n")
    return "\n".join(parts)


def update_readme(repos):
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
    with open(README,"w",encoding="utf-8") as fh:
        fh.write(pattern.sub(block, content))
    print("README.md updated.")


if __name__ == "__main__":
    print(f"Fetching repositories for {USER}...")
    repos = fetch_repos()
    print(f"{len(repos)} repos found.")
    write_cards(repos)
    update_readme(repos)