#!/usr/bin/env python3
"""
build_site.py — Project ASI reader
==================================
Generate ONE self-contained, offline `index.html` over `LEARNING/**/*.md`,
styled exactly like the "hy" philosophy reader:

  - a distraction-free reading view (only the body text is on screen)
  - an invisible top-left hamburger opening a left overlay drawer with ALL
    controls: theme (dark / light / sepia), body font (serif / sans),
    text-size / line-spacing / width sliders, full-width toggle, reset,
    edge-tap paging toggle, and the grouped tab list + filter
  - edge-tap paging (touch) and ← / → arrow-key paging (desktop)
  - [[wiki-links]] AND relative `*.md` links wired to switch tabs in-page
  - inline parenthetical glosses muted; `::: key/example/warn/note` callouts;
    `{: .lead}` / `{: .keyline}` components

Output is fully self-contained (CSS + JS inline, markdown pre-rendered) and
works offline. Files/dirs whose name starts with `_` are skipped.

Requirements:  Python 3.8+  and  `pip install markdown`
Usage:         py -3 build_site.py            (run from the repo root)
"""

import html
import os
import re
import sys

try:
    import markdown as md_lib
except ImportError:
    sys.exit("Missing dependency. Install it with:  py -3 -m pip install markdown")

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_ROOT = os.path.join(ROOT, "LEARNING")
OUTPUT = os.path.join(ROOT, "index.html")
BRAND = "Project ASI — Approaches to AGI"
PAGE_TITLE = "Project ASI — Approaches to AGI"

# Sidebar group order = the reading order. "__top__" = top-level LEARNING/*.md maps.
# v3.0 (investigation-first): one clean staircase — the map, then ① the shared base,
# then ② the approaches. (Old learn-first shelves live hidden in LEARNING/_legacy/.)
GROUP_ORDER = [
    ("__top__", "★ Start here — the map"),
    ("10-how-ai-works-today", "① How AI works today"),
    ("20-the-approaches", "② The approaches to AGI"),
    ("40-the-verdict", "③ The verdict — judging the map"),
]
GROUP_LABEL = dict(GROUP_ORDER)
GROUP_RANK = {g: i for i, (g, _) in enumerate(GROUP_ORDER)}
# Preferred order for the top-level maps (the spine first, then the deltas feed, then the index).
TOP_ORDER = ["APPROACHES_TO_AGI", "WHATS_NEW", "CONCEPT_REGISTRY"]

WIKILINK_RE = re.compile(r"\[\[([^\]\|]+?)(?:\|([^\]]+))?\]\]")
NUM_RE = re.compile(r"^(\d+)")
# Inline parenthetical glosses/asides — muted. No nested parens/brackets/angles/newlines,
# so it never spans a wiki-link, an HTML tag, or a markdown link's (url).
GLOSS_RE = re.compile(r"\(([^()\[\]<>\n]{1,240}?)\)")
# Relative markdown links to another content file -> rewrite to an in-page tab switch.
MDLINK_HREF_RE = re.compile(r'href="([^"#]+?\.md)(#[^"]*)?"')


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def read_text(path: str) -> str:
    with open(path, "rb") as fh:
        raw = fh.read()
    for enc in ("utf-8", "cp1252"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def prettify(stem: str) -> str:
    s = re.sub(r"^\d+[_-]*", "", stem)
    return s.replace("_", " ").replace("-", " ").strip() or stem


def read_title(path: str, stem: str) -> str:
    try:
        for line in read_text(path).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return prettify(stem)


def slugify(rel_noext: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", rel_noext).strip("_")


# ---- block normalization (insert blank lines between differing block types) ----
_LIST_RE = re.compile(r"(?:[-*+]\s)|(?:\d+[.)]\s)")
_HR_RE = re.compile(r"(?:-{3,}|\*{3,}|_{3,})$")


def _block_type(line: str) -> str:
    s = line.strip()
    if s == "":
        return "blank"
    if s.startswith("#"):
        return "heading"
    if _HR_RE.fullmatch(s):
        return "hr"
    body = line.lstrip()
    if body.startswith(">"):
        return "quote"
    if _LIST_RE.match(body):
        return "list"
    return "para"


def normalize_md(text: str) -> str:
    lines = text.split("\n")
    out = []
    for line in lines:
        t = _block_type(line)
        if out:
            pt = _block_type(out[-1])
            if pt != "blank" and t != "blank" and pt != t:
                out.append("")
        out.append(line)
    return "\n".join(out)


CALLOUT_OPEN_RE = re.compile(r"^:::\s*([a-zA-Z][\w-]*)\s*(.*?)\s*$")


def expand_callouts(text: str) -> str:
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = CALLOUT_OPEN_RE.match(lines[i])
        if m:
            cls = m.group(1).lower()
            arg = m.group(2).strip()
            j = i + 1
            body = []
            while j < len(lines) and lines[j].strip() != ":::":
                body.append(lines[j])
                j += 1
            if cls in ("vocab", "details"):
                summary = arg or ("Words &amp; phrases" if cls == "vocab" else "More")
                out.append('<details class="vocab" markdown="1">')
                out.append(f"<summary>{summary}</summary>")
                out.append("")
                out.extend(body)
                out.append("")
                out.append("</details>")
            else:
                out.append(f'<div class="callout {cls}" markdown="1">')
                out.append("")
                out.extend(body)
                out.append("")
                out.append("</div>")
            i = j + 1
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def make_md():
    return md_lib.Markdown(extensions=["extra", "sane_lists", "md_in_html"])


# --------------------------------------------------------------------------- #
# Collect content
# --------------------------------------------------------------------------- #
def collect():
    entries = []
    for dirpath, dirnames, filenames in os.walk(CONTENT_ROOT):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("_") and not d.startswith("."))
        for name in sorted(filenames):
            if not name.endswith(".md") or name.startswith("_"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, CONTENT_ROOT).replace("\\", "/")
            stem = name[:-3]
            parts = rel.split("/")
            group = "__top__" if len(parts) == 1 else parts[0]
            m = NUM_RE.match(stem)
            full = read_title(path, stem)
            entries.append({
                "path": path,
                "rel": rel,
                "stem": stem,
                "group": group,
                "num": int(m.group(1)) if m else 10 ** 9,
                "badge": (m.group(1) if m else ""),
                "tabid": slugify(rel[:-3]),
                "full_title": full,
                "title": full,
            })
    return entries


def order_key(e):
    if e["group"] == "__top__":
        rank = TOP_ORDER.index(e["stem"]) if e["stem"] in TOP_ORDER else 500
        return (rank, e["stem"].lower())
    return (e["num"], e["stem"].lower())


def group_rank(g):
    return GROUP_RANK.get(g, 1000 + hash(g) % 1000)


# --------------------------------------------------------------------------- #
# Render one file's markdown -> HTML (wiki-links, relative md-links, glosses)
# --------------------------------------------------------------------------- #
def render_body(md, entry, stem_to_tabid, tabid_to_title):
    text = normalize_md(expand_callouts(read_text(entry["path"])))

    # 1) stash [[wiki-links]] as paren-free placeholders so gloss/convert leave them alone
    stash = []

    def wl(m):
        stem = m.group(1).strip()
        alias = m.group(2)
        tid = stem_to_tabid.get(stem)
        if tid:
            label = alias or tabid_to_title.get(tid, prettify(stem))
            tip = tabid_to_title.get(tid, stem)
            anchor = (f'<a class="wikilink" data-target="{html.escape(tid)}" '
                      f'href="#{html.escape(tid)}" title="{html.escape(tip)}">'
                      f'{html.escape(label)}</a>')
        else:
            label = alias or prettify(stem)
            anchor = (f'<span class="wikilink missing" title="not yet written: '
                      f'{html.escape(stem)}">{html.escape(label)}</span>')
        stash.append(anchor)
        return f"\x00WL{len(stash) - 1}\x00"

    text = WIKILINK_RE.sub(wl, text)

    # 2) markdown -> HTML
    body = md.reset().convert(text)

    # 3) gloss parentheticals (on HTML; GLOSS_RE stops at <>()[], so tags/urls are safe)
    body = GLOSS_RE.sub(lambda m: '<span class="gloss">(' + m.group(1) + ')</span>', body)

    # 4) rewrite relative *.md links to in-page tab switches
    def rel(m):
        base = os.path.basename(m.group(1))[:-3]
        tid = stem_to_tabid.get(base)
        if tid:
            return f'href="#{html.escape(tid)}" data-target="{html.escape(tid)}" class="wikilink"'
        return m.group(0)

    body = MDLINK_HREF_RE.sub(rel, body)

    # 5) restore stashed wiki-link anchors
    for i, anchor in enumerate(stash):
        body = body.replace(f"\x00WL{i}\x00", anchor)
    return body


# --------------------------------------------------------------------------- #
# Page assembly
# --------------------------------------------------------------------------- #
def sidebar_group(label, items):
    links = []
    for tabid, badge, title, full in items:
        badge_html = f'<span class="num">{html.escape(badge)}</span>' if badge else ""
        links.append(
            f'<a class="tab" data-target="{html.escape(tabid)}" href="#{html.escape(tabid)}" '
            f'title="{html.escape(full)}">{badge_html}<span class="tab-title">{html.escape(title)}</span></a>'
        )
    return (f'<details class="group" open><summary>{html.escape(label)}'
            f'<span class="group-count">{len(items)}</span></summary>\n'
            f'<div class="group-body">{"".join(links)}</div></details>')


def _pager_link(entry, cls, before, after):
    if not entry:
        return '<span class="pager-spacer"></span>'
    return (f'<a class="{cls}" data-target="{html.escape(entry["tabid"])}" '
            f'href="#{html.escape(entry["tabid"])}" title="{html.escape(entry["full_title"])}">'
            f'{before}<span>{html.escape(entry["title"])}</span>{after}</a>')


def article(entry, body_html, prev=None, nxt=None):
    pager = ('<nav class="pager">'
             + _pager_link(prev, "pager-prev", "← ", "")
             + _pager_link(nxt, "pager-next", "", " →")
             + '</nav>')
    return (f'<article class="doc" id="doc-{html.escape(entry["tabid"])}" '
            f'data-tabid="{html.escape(entry["tabid"])}">{body_html}{pager}</article>')


def render_page(sidebar_html, sections_html, initial_tabid):
    return (PAGE_TEMPLATE
            .replace("__PAGE_TITLE__", html.escape(PAGE_TITLE))
            .replace("__BRAND__", html.escape(BRAND))
            .replace("__SIDEBAR__", sidebar_html)
            .replace("__SECTIONS__", sections_html)
            .replace("__INITIAL__", html.escape(initial_tabid)))


def build():
    entries = collect()
    if not entries:
        sys.exit(f"No .md content found under {CONTENT_ROOT}")

    # global lookup: basename stem -> tabid, tabid -> short title
    stem_to_tabid = {e["stem"]: e["tabid"] for e in entries}
    tabid_to_title = {e["tabid"]: e["title"] for e in entries}

    # group + order
    groups = {}
    for e in entries:
        groups.setdefault(e["group"], []).append(e)
    ordered_groups = sorted(groups.items(), key=lambda kv: group_rank(kv[0]))
    for _, items in ordered_groups:
        items.sort(key=order_key)

    # flat reading order (for pager)
    flat = [e for _, items in ordered_groups for e in items]

    md = make_md()
    id2body = {e["tabid"]: render_body(md, e, stem_to_tabid, tabid_to_title) for e in flat}

    sections = []
    for idx, e in enumerate(flat):
        prev = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx < len(flat) - 1 else None
        sections.append(article(e, id2body[e["tabid"]], prev, nxt))

    sidebar_blocks = []
    for g, items in ordered_groups:
        label = GROUP_LABEL.get(g, g.replace("-", " ").title())
        rows = [(e["tabid"], e["badge"], e["title"], e["full_title"]) for e in items]
        sidebar_blocks.append(sidebar_group(label, rows))

    initial = ""
    for e in flat:
        if e["stem"] == "APPROACHES_TO_AGI":
            initial = e["tabid"]
            break
    if not initial and flat:
        initial = flat[0]["tabid"]

    page = render_page("\n".join(sidebar_blocks), "\n".join(sections), initial)
    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"Built {os.path.basename(OUTPUT)}  —  {len(flat)} files across {len(ordered_groups)} groups")
    for g, items in ordered_groups:
        print(f"  {GROUP_LABEL.get(g, g):<28} {len(items):>3}")


# --------------------------------------------------------------------------- #
# HTML / CSS / JS template (tokens: __PAGE_TITLE__ __BRAND__ __SIDEBAR__ __SECTIONS__ __INITIAL__)
# (verbatim from the "hy" reader, so the look & feel matches the philosophy site)
# --------------------------------------------------------------------------- #
PAGE_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" id="tcMeta" content="#1b1c1e">
<title>__PAGE_TITLE__</title>
<style>
:root{
  --content-font: 18px;
  --content-width: 760px;
  --content-leading: 1.66;
  --ui-font: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --read-font: Georgia,"Iowan Old Style","Palatino Linotype",Palatino,"Times New Roman",serif;
}
html[data-theme="light"]{
  --bg:#fbfbf9; --bg-2:#f2f1ec; --panel:#ffffff; --text:#1d1d1f; --muted:#6b6b6f;
  --border:#e4e2db; --accent:#8a5a2b; --accent-soft:#f0e6da; --quote:#f6f3ec; --shadow:rgba(0,0,0,.08);
}
html[data-theme="dark"]{
  --bg:#1b1c1e; --bg-2:#232427; --panel:#202123; --text:#e3e2df; --muted:#9a9a9e;
  --border:#34353a; --accent:#d8a566; --accent-soft:#2c2a26; --quote:#26272a; --shadow:rgba(0,0,0,.4);
}
html[data-theme="sepia"]{
  --bg:#f3e7cf; --bg-2:#ece0c4; --panel:#f7eed9; --text:#46392a; --muted:#8c7a59;
  --border:#dccaa3; --accent:#9c5a25; --accent-soft:#ecdcbd; --quote:#efe4ca; --shadow:rgba(90,70,30,.14);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%}
body{background:var(--bg);color:var(--text);font-family:var(--ui-font);
  display:flex;flex-direction:column;height:100vh;height:100dvh;overflow:hidden}

.hamburger{position:fixed;top:0;left:0;z-index:50;width:46px;height:46px;border:0;
  background:transparent;color:var(--muted);font-size:1.2rem;line-height:1;cursor:pointer;
  display:flex;align-items:center;justify-content:center;opacity:0;
  transition:opacity .25s;-webkit-tap-highlight-color:transparent;touch-action:manipulation;
  text-shadow:0 0 5px var(--bg),0 0 5px var(--bg),0 0 5px var(--bg)}
.hamburger:hover,.hamburger:focus-visible{opacity:.85;outline:none}
.hamburger.hint{opacity:.55}
body:not(.sidebar-collapsed) .hamburger{opacity:0;pointer-events:none}

.btn{-webkit-appearance:none;appearance:none;border:1px solid var(--border);background:var(--bg-2);color:var(--text);
  border-radius:8px;padding:.4rem .6rem;font-size:.85rem;cursor:pointer;line-height:1;touch-action:manipulation;
  display:inline-flex;align-items:center;justify-content:center;gap:.3rem;transition:background .15s,border-color .15s}
.btn:hover{border-color:var(--accent);background:var(--accent-soft)}
.btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}

.shell{display:flex;flex:1;min-height:0;position:relative}
.scrim{position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:60;opacity:0;visibility:hidden;
  transition:opacity .25s,visibility .25s}
body:not(.sidebar-collapsed) .scrim{opacity:1;visibility:visible}
.sidebar{position:fixed;top:0;left:0;bottom:0;z-index:70;width:min(340px,86vw);
  background:var(--bg-2);border-right:1px solid var(--border);box-shadow:4px 0 28px var(--shadow);
  overflow-y:auto;-webkit-overflow-scrolling:touch;padding:.4rem .65rem 2rem;
  transform:translateX(-100%);transition:transform .25s ease}
body:not(.sidebar-collapsed) .sidebar{transform:none}
.sidebar-head{display:flex;align-items:center;gap:.5rem;padding:.35rem .15rem .5rem;
  position:sticky;top:0;background:var(--bg-2);z-index:1}
.sidebar-head .brand{font-weight:700;font-size:1rem;flex:1;min-width:0;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.closeSidebar{-webkit-appearance:none;appearance:none;border:0;background:transparent;color:var(--muted);
  font-size:1.5rem;line-height:1;cursor:pointer;padding:.05rem .4rem;border-radius:8px;touch-action:manipulation}
.closeSidebar:hover{color:var(--text);background:var(--accent-soft)}

.panel{display:flex;flex-direction:column;gap:.45rem;padding:.55rem;margin:.1rem 0 .7rem;
  border:1px solid var(--border);border-radius:11px;background:var(--panel)}
.panel-row{display:flex;align-items:center;gap:.5rem}
.panel-lbl{font-size:.82rem;color:var(--muted);flex:1;min-width:0}
.panel-row .btn{flex:0 0 auto}
.panel-row .wide{flex:1}
.seg{display:inline-flex;border:1px solid var(--border);border-radius:8px;overflow:hidden;background:var(--bg-2)}
.seg button{-webkit-appearance:none;appearance:none;border:0;background:transparent;color:var(--text);
  font-size:.8rem;padding:.4rem .55rem;cursor:pointer;line-height:1;min-height:34px;touch-action:manipulation}
.seg button + button{border-left:1px solid var(--border)}
.seg button.active{background:var(--accent);color:#fff}

.slider-row{display:flex;flex-direction:column;gap:.2rem;padding:.05rem 0}
.slider-row label{display:flex;justify-content:space-between;align-items:baseline;
  font-size:.82rem;color:var(--muted)}
.slider-row .val{color:var(--text);font-variant-numeric:tabular-nums;font-size:.8rem}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:28px;background:transparent;
  cursor:pointer;touch-action:manipulation}
input[type=range]:focus{outline:none}
input[type=range]::-webkit-slider-runnable-track{height:6px;border-radius:6px;background:var(--border)}
input[type=range]::-moz-range-track{height:6px;border-radius:6px;background:var(--border)}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:20px;height:20px;
  border-radius:50%;background:var(--accent);border:2px solid var(--panel);margin-top:-7px;
  box-shadow:0 1px 3px var(--shadow)}
input[type=range]::-moz-range-thumb{width:20px;height:20px;border-radius:50%;background:var(--accent);
  border:2px solid var(--panel);box-shadow:0 1px 3px var(--shadow)}

.edge-flash{position:fixed;top:0;bottom:0;width:36px;z-index:55;pointer-events:none;opacity:0;
  transition:opacity .12s ease}
.edge-flash.show{opacity:.85}
.edge-flash.left{left:0;background:linear-gradient(to right,var(--accent-soft),transparent)}
.edge-flash.right{right:0;background:linear-gradient(to left,var(--accent-soft),transparent)}
.filter{width:100%;padding:.5rem .6rem;margin:.1rem 0 .6rem;border:1px solid var(--border);
  border-radius:8px;background:var(--panel);color:var(--text);font-size:16px;-webkit-appearance:none}
.group{margin-bottom:.25rem;border-radius:8px}
.group>summary{cursor:pointer;list-style:none;padding:.4rem .55rem;font-weight:600;font-size:.82rem;
  color:var(--muted);text-transform:uppercase;letter-spacing:.4px;border-radius:6px;
  display:flex;align-items:center;gap:.4rem}
.group>summary::-webkit-details-marker{display:none}
.group>summary:before{content:"▸";font-size:.7rem;transition:transform .15s}
.group[open]>summary:before{transform:rotate(90deg)}
.group>summary:hover{background:var(--accent-soft)}
.group-count{margin-left:auto;font-size:.7rem;background:var(--border);color:var(--muted);
  border-radius:10px;padding:.05rem .4rem}
.group-body{display:flex;flex-direction:column;gap:1px;padding:.1rem 0 .35rem}
.tab{display:flex;align-items:baseline;gap:.5rem;padding:.4rem .55rem;border-radius:7px;
  text-decoration:none;color:var(--text);font-size:.9rem;line-height:1.3}
.tab:hover{background:var(--accent-soft)}
.tab.active{background:var(--accent);color:#fff}
.tab.active .num{color:#fff;opacity:.85}
.tab .num{font-size:.72rem;color:var(--muted);min-width:1.6em;font-variant-numeric:tabular-nums;font-weight:600}
.tab-title{flex:1}

.main{flex:1;min-width:0;overflow-y:auto;-webkit-overflow-scrolling:touch;scroll-behavior:smooth}
.content{max-width:var(--content-width);margin:0 auto;padding:2.4rem 1.6rem 6rem;
  font-family:var(--read-font);font-size:var(--content-font);line-height:var(--content-leading);color:var(--text);
  overflow-wrap:break-word}
body.full-width .content{max-width:none}
.doc{display:none}
.doc.active{display:block;animation:fade .2s ease}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

.content h1{font-size:2em;line-height:1.15;margin:.1em 0 .2em;font-family:var(--ui-font);letter-spacing:-.015em}
.content h1 + p{font-size:1.16em;line-height:1.5;color:var(--muted);margin:.15em 0 1.5em}
.content h1 + p em{color:var(--muted);font-style:italic}
.content h2{font-size:1.42em;line-height:1.22;margin:2.5em 0 .6em;font-family:var(--ui-font);
  font-weight:700;letter-spacing:-.01em}
.content h2::before{content:"";display:block;width:46px;height:3px;border-radius:2px;
  background:var(--accent);margin:0 0 .75em}
.content h3{font-size:1.16em;margin:1.7em 0 .45em;font-family:var(--ui-font);font-weight:700;
  color:var(--accent);letter-spacing:-.005em}
.content p{margin:.75em 0}
.content a{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--accent-soft)}
.content a:hover{border-bottom-color:var(--accent)}
.content blockquote{margin:1.5em 0;padding:.1em 0 .1em 1.25em;background:transparent;
  border-left:3px solid var(--accent);border-radius:0;font-size:1.14em;line-height:1.5;
  font-style:italic;color:var(--text)}
.content blockquote p{margin:.4em 0}
.content ul,.content ol{padding-left:1.4em;margin:.7em 0}
.content li{margin:.4em 0}
.content li>ul,.content li>ol{margin:.35em 0}
.content hr{border:0;border-top:1px solid var(--border);margin:1.6em 0}

.content .gloss{color:var(--muted)}
.content blockquote .gloss,.content h1 + p .gloss{color:inherit;opacity:.7}

.content .lead{font-size:1.14em;line-height:1.55;color:var(--text);margin:.2em 0 1em}
.content .keyline{font-size:1.16em;font-weight:600;line-height:1.5;color:var(--text);
  border-left:3px solid var(--accent);padding:.05em 0 .05em .9em;margin:1.2em 0}
.content .callout{margin:1.3em 0;padding:.85em 1.05em .95em;border-radius:11px;
  border:1px solid var(--border);border-left-width:4px;background:var(--bg-2)}
.content .callout>:first-child{margin-top:0}
.content .callout>:last-child{margin-bottom:0}
.content .callout::before{display:block;font-family:var(--ui-font);font-size:.68rem;
  letter-spacing:.7px;text-transform:uppercase;font-weight:700;margin-bottom:.45em;opacity:.95}
.content .callout.key{border-left-color:var(--accent);background:var(--accent-soft)}
.content .callout.key::before{content:"Key idea";color:var(--accent)}
.content .callout.example{border-left-color:#5a86c4}
.content .callout.example::before{content:"Example";color:#5a86c4}
.content .callout.warn{border-left-color:#c4715a}
.content .callout.warn::before{content:"Careful";color:#c4715a}
.content .callout.note{border-left-color:var(--muted)}
.content .callout.note::before{content:"Aside";color:var(--muted)}

.content details.vocab{margin:1.8em 0 .5em;border:1px solid var(--border);border-radius:11px;
  background:var(--bg-2);overflow:hidden}
.content details.vocab>summary{cursor:pointer;list-style:none;font-family:var(--ui-font);
  font-weight:700;font-size:.95rem;color:var(--accent);padding:.8em 1em}
.content details.vocab>summary::-webkit-details-marker{display:none}
.content details.vocab>summary::before{content:"▸  ";font-size:.85em;color:var(--muted)}
.content details.vocab[open]>summary::before{content:"▾  "}
.content details.vocab[open]>summary{border-bottom:1px solid var(--border)}
.content details.vocab ul{padding:.6em 1.2em .8em 1.7em;margin:0}
.content details.vocab li{margin:.45em 0}
.content code{background:var(--bg-2);padding:.1em .35em;border-radius:5px;font-size:.9em}
.content pre{background:var(--bg-2);padding:.9em 1em;border-radius:9px;overflow-x:auto;font-size:.86em}
.content pre code{background:transparent;padding:0}
.content strong{font-weight:700}
.content img{max-width:100%;height:auto}
.content table{display:block;max-width:100%;overflow-x:auto;border-collapse:collapse;font-size:.92em}
.content th,.content td{border:1px solid var(--border);padding:.35em .6em;text-align:left;vertical-align:top}
.content th{background:var(--bg-2)}
.wikilink{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--accent-soft);cursor:pointer}
.wikilink:hover{border-bottom-color:var(--accent)}
.wikilink.missing{color:var(--muted);border-bottom:1px dotted var(--muted);cursor:help}

.pager{display:flex;gap:1rem;margin-top:3.2rem;padding-top:1.3rem;border-top:1px solid var(--border);
  font-family:var(--ui-font);font-size:.9rem}
.pager a{display:inline-flex;align-items:center;gap:.4rem;max-width:48%;color:var(--accent);
  text-decoration:none;border:1px solid var(--border);border-radius:9px;padding:.55rem .75rem;
  background:var(--bg-2);line-height:1.25}
.pager a:hover{border-color:var(--accent);background:var(--accent-soft)}
.pager a span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pager .pager-next{margin-left:auto;text-align:right}
.pager-spacer{flex:1}
.empty{color:var(--muted);text-align:center;margin-top:4rem;font-family:var(--ui-font)}

@media (max-width:680px){
  .btn{padding:.55rem .7rem;font-size:.95rem;min-height:42px}
  .seg button{min-height:42px;padding:.5rem .6rem}
  input[type=range]{height:40px}
  input[type=range]::-webkit-slider-thumb{width:24px;height:24px;margin-top:-9px}
  input[type=range]::-moz-range-thumb{width:24px;height:24px}
  .closeSidebar{font-size:1.7rem;padding:.1rem .5rem}
  .tab{padding:.6rem .6rem}
  .group>summary{padding:.55rem .55rem}
  .content{padding:2rem .95rem 4.5rem}
  .pager{flex-wrap:wrap;gap:.6rem}
  .pager a{max-width:100%;flex:1 1 100%}
  .pager .pager-next{margin-left:0;justify-content:flex-end}
}
</style>
</head>
<body class="sidebar-collapsed">
<button class="hamburger" id="toggleSidebar" aria-label="Open menu" title="Menu">☰</button>

<div class="shell">
  <div class="scrim" id="scrim"></div>
  <nav class="sidebar" id="sidebar" aria-label="Menu and reading settings">
    <div class="sidebar-head">
      <span class="brand">__BRAND__</span>
      <button class="closeSidebar" id="closeSidebar" aria-label="Close menu" title="Close">×</button>
    </div>
    <div class="panel">
      <div class="panel-row">
        <span class="panel-lbl">Theme</span>
        <span class="seg" id="themeSeg">
          <button type="button" data-theme="dark" title="Dark">Dark</button>
          <button type="button" data-theme="light" title="Light">Light</button>
          <button type="button" data-theme="sepia" title="Warm / sepia">Sepia</button>
        </span>
      </div>
      <div class="panel-row">
        <span class="panel-lbl">Body font</span>
        <span class="seg" id="fontSeg">
          <button type="button" data-font="serif" title="Serif (Georgia)">Serif</button>
          <button type="button" data-font="sans" title="Sans-serif">Sans</button>
        </span>
      </div>
      <div class="slider-row">
        <label for="fontRange">Text size <span class="val" id="fontVal">19</span></label>
        <input type="range" id="fontRange" min="11" max="80" step="1" aria-label="Text size">
      </div>
      <div class="slider-row">
        <label for="leadRange">Line spacing <span class="val" id="leadVal">1.66</span></label>
        <input type="range" id="leadRange" min="1" max="4" step="0.05" aria-label="Line spacing">
      </div>
      <div class="slider-row">
        <label for="widthRange">Width <span class="val" id="widthVal">860</span></label>
        <input type="range" id="widthRange" min="340" max="3000" step="20" aria-label="Reading width">
      </div>
      <div class="panel-row">
        <button class="btn wide" id="widthFull" title="Fill the screen width">⇔ Full width</button>
        <button class="btn" id="resetReading" title="Reset font, size, spacing &amp; width">Reset</button>
      </div>
      <div class="panel-row">
        <span class="panel-lbl">Edge-tap pages</span>
        <button class="btn" id="edgeToggle" title="Tap the far left / right screen edge to turn pages">On</button>
      </div>
    </div>
    <input class="filter" id="filter" type="search" placeholder="Filter…" autocomplete="off">
    __SIDEBAR__
  </nav>
  <main class="main" id="main">
    <div class="content" id="content">
      __SECTIONS__
    </div>
  </main>
</div>

<script>
(function(){
  var INITIAL = "__INITIAL__";
  var root = document.documentElement, body = document.body;
  var LS = window.localStorage;
  function $(id){return document.getElementById(id);}

  function getNum(k,d){var v=parseFloat(LS.getItem(k));return isNaN(v)?d:v;}
  var FONT_MIN=11,  FONT_MAX=80;
  var WIDTH_MIN=340, WIDTH_MAX=3000;
  var LEAD_MIN=1.0, LEAD_MAX=4.0;
  var DEF_FONT=19, DEF_WIDTH=860, DEF_LEAD=1.66, DEF_FAM='serif';
  var SERIF='Georgia,"Iowan Old Style","Palatino Linotype",Palatino,"Times New Roman",serif';
  var SANS='-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif';
  var font  = Math.min(FONT_MAX,  Math.max(FONT_MIN,  getNum('pa-font', DEF_FONT)));
  var width = Math.min(WIDTH_MAX, Math.max(WIDTH_MIN, getNum('pa-width', DEF_WIDTH)));
  var lead  = Math.min(LEAD_MAX,  Math.max(LEAD_MIN,  getNum('pa-leading', DEF_LEAD)));
  var theme = LS.getItem('pa-theme') || 'dark';
  var fam   = LS.getItem('pa-fontfam')==='sans' ? 'sans' : 'serif';
  var fullw = LS.getItem('pa-fullwidth')==='1';
  var edges = LS.getItem('pa-edgetap')!=='0';

  body.classList.add('sidebar-collapsed');

  function preserveScroll(fn){
    var main=$('main'), doc=document.querySelector('.doc.active'), anchor=null, off=0;
    if(doc){
      var top=main.getBoundingClientRect().top;
      var els=doc.querySelectorAll('h1,h2,h3,h4,h5,p,li,blockquote,div.callout,ul,ol,pre,table,hr,details,img');
      for(var i=0;i<els.length;i++){var r=els[i].getBoundingClientRect();
        if(r.bottom>top+2){anchor=els[i];off=r.top-top;break;}}
    }
    fn();
    if(anchor){
      var prev=main.style.scrollBehavior; main.style.scrollBehavior='auto';
      var nt=anchor.getBoundingClientRect().top-main.getBoundingClientRect().top;
      main.scrollTop += (nt-off); main.style.scrollBehavior=prev;
    }
  }

  function segActive(id,attr,val){var s=$(id); if(!s) return;
    Array.prototype.forEach.call(s.querySelectorAll('button'),function(b){
      b.classList.toggle('active', b.getAttribute(attr)===val);});}
  function setRange(id,v){var r=$(id); if(r && parseFloat(r.value)!==v) r.value=v;}

  function widthOut(){var v=$('widthVal'); if(v) v.textContent = fullw ? 'Max' : width;}
  function setFont(px){font=Math.min(FONT_MAX,Math.max(FONT_MIN,Math.round(px)));
    root.style.setProperty('--content-font',font+'px'); LS.setItem('pa-font',font);
    var v=$('fontVal'); if(v) v.textContent=font; setRange('fontRange',font);}
  function setLead(x){lead=Math.min(LEAD_MAX,Math.max(LEAD_MIN,Math.round(x*100)/100));
    root.style.setProperty('--content-leading',lead); LS.setItem('pa-leading',lead);
    var v=$('leadVal'); if(v) v.textContent=lead.toFixed(2); setRange('leadRange',lead);}
  function setWidth(px){width=Math.min(WIDTH_MAX,Math.max(WIDTH_MIN,Math.round(px)));
    root.style.setProperty('--content-width',width+'px'); LS.setItem('pa-width',width); widthOut(); setRange('widthRange',width);}
  function setFull(on){fullw=on; body.classList.toggle('full-width',on);
    LS.setItem('pa-fullwidth',on?'1':'0'); var b=$('widthFull'); if(b) b.classList.toggle('active',on); widthOut();}
  function applyFam(){root.style.setProperty('--read-font', fam==='sans'?SANS:SERIF);
    LS.setItem('pa-fontfam',fam); segActive('fontSeg','data-font',fam);}
  function applyTheme(){root.setAttribute('data-theme',theme); LS.setItem('pa-theme',theme);
    segActive('themeSeg','data-theme',theme);
    var bg={dark:'#1b1c1e',light:'#fbfbf9',sepia:'#f3e7cf'}[theme]||'#1b1c1e';
    var m=$('tcMeta'); if(m) m.setAttribute('content',bg);}
  setWidth(width); setFont(font); setLead(lead); applyFam(); applyTheme(); setFull(fullw);

  function wireRange(id,setter){var r=$(id); if(!r) return;
    r.addEventListener('input',function(){preserveScroll(function(){setter(parseFloat(r.value));});});}
  wireRange('fontRange', setFont);
  wireRange('leadRange', setLead);
  wireRange('widthRange', function(v){ if(fullw) setFull(false); setWidth(v); });

  $('themeSeg').addEventListener('click',function(e){var b=e.target.closest('[data-theme]');
    if(!b) return; theme=b.getAttribute('data-theme'); applyTheme();});
  $('fontSeg').addEventListener('click',function(e){var b=e.target.closest('[data-font]');
    if(!b) return; preserveScroll(function(){fam=b.getAttribute('data-font'); applyFam();});});
  $('widthFull').onclick =function(){preserveScroll(function(){setFull(!fullw);});};
  $('resetReading').onclick=function(){preserveScroll(function(){
    setFull(false); fam=DEF_FAM; applyFam(); setFont(DEF_FONT); setLead(DEF_LEAD); setWidth(DEF_WIDTH);});};

  function applyEdge(){var b=$('edgeToggle'); if(b){b.textContent=edges?'On':'Off'; b.classList.toggle('active',edges);}
    LS.setItem('pa-edgetap',edges?'1':'0');}
  applyEdge();
  $('edgeToggle').onclick=function(){edges=!edges; applyEdge();};

  function openDrawer(){body.classList.remove('sidebar-collapsed');}
  function closeDrawer(){body.classList.add('sidebar-collapsed');}
  $('toggleSidebar').onclick=function(){body.classList.contains('sidebar-collapsed')?openDrawer():closeDrawer();};
  $('closeSidebar').onclick=closeDrawer;
  $('scrim').onclick=closeDrawer;
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'||e.keyCode===27){closeDrawer();return;}
    if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey) return;
    var ae=document.activeElement, tag=ae&&ae.tagName;
    if(tag==='INPUT'||tag==='TEXTAREA'||tag==='SELECT'||(ae&&ae.isContentEditable)) return;
    if(ae&&ae.closest&&ae.closest('.sidebar')) return;
    if(e.key==='ArrowLeft'||e.keyCode===37){ if(goPager('prev')) e.preventDefault(); }
    else if(e.key==='ArrowRight'||e.keyCode===39){ if(goPager('next')) e.preventDefault(); }
  });

  var ham=$('toggleSidebar'); ham.classList.add('hint');
  setTimeout(function(){ham.classList.remove('hint');},2600);

  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  function activate(tabid, push){
    var doc = document.getElementById('doc-'+tabid);
    if(!doc) return false;
    document.querySelectorAll('.doc.active').forEach(function(d){d.classList.remove('active');});
    doc.classList.add('active');
    tabs.forEach(function(t){t.classList.toggle('active', t.getAttribute('data-target')===tabid);});
    var active = document.querySelector('.tab.active');
    if(active){
      var grp = active.closest('details'); if(grp) grp.open = true;
      active.scrollIntoView({block:'nearest'});
    }
    $('main').scrollTop = 0;
    if(push!==false) history.replaceState(null,'','#'+tabid);
    return true;
  }

  document.querySelector('.shell').addEventListener('click', function(e){
    var el = e.target.closest('[data-target]');
    if(!el) return;
    e.preventDefault();
    activate(el.getAttribute('data-target'));
    closeDrawer();
  });

  function goPager(which){
    var doc=document.querySelector('.doc.active'); if(!doc) return false;
    var a=doc.querySelector(which==='prev'?'.pager-prev':'.pager-next');
    var t=a && a.getAttribute('data-target'); if(!t) return false;
    activate(t); return true;
  }

  (function(){
    var main=$('main'), pd=null;
    function flash(side){
      var d=document.createElement('div'); d.className='edge-flash '+side; document.body.appendChild(d);
      requestAnimationFrame(function(){d.classList.add('show');});
      setTimeout(function(){d.classList.remove('show');},150);
      setTimeout(function(){if(d.parentNode)d.parentNode.removeChild(d);},340);
    }
    main.addEventListener('pointerdown',function(e){
      pd={x:e.clientX,y:e.clientY,t:Date.now(),type:e.pointerType};
    },{passive:true});
    main.addEventListener('pointerup',function(e){
      var d=pd; pd=null;
      if(!edges || !d) return;
      if(d.type!=='touch') return;
      if(!body.classList.contains('sidebar-collapsed')) return;
      if(Date.now()-d.t>450) return;
      if(Math.abs(e.clientX-d.x)>12 || Math.abs(e.clientY-d.y)>12) return;
      if(window.getSelection && String(window.getSelection())) return;
      if(e.target.closest('a,button,input,textarea,select,summary,label,.wikilink')) return;
      var w=window.innerWidth, edge=Math.min(90, w*0.09);
      if(e.clientX<=edge){ if(goPager('prev')) flash('left'); }
      else if(e.clientX>=w-edge){ if(goPager('next')) flash('right'); }
    },{passive:true});
  })();

  var filter = document.getElementById('filter');
  filter.addEventListener('input', function(){
    var q = filter.value.trim().toLowerCase();
    document.querySelectorAll('.group').forEach(function(g){
      var any=false;
      g.querySelectorAll('.tab').forEach(function(t){
        var hit = t.textContent.toLowerCase().indexOf(q)>=0;
        t.style.display = hit?'':'none'; if(hit) any=true;
      });
      g.style.display = any?'':'none';
      if(q && any) g.open = true;
    });
  });

  var start = (location.hash||'').replace(/^#/,'');
  if(!start || !activate(start, false)) activate(INITIAL, false);
  window.addEventListener('hashchange', function(){
    var h=(location.hash||'').replace(/^#/,''); if(h) activate(h,false);
  });
})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # Windows consoles default to cp1252
    except Exception:
        pass
    build()
