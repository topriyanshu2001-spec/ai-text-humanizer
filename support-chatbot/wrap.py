#!/usr/bin/env python3
"""Build the shareable single-file page from index.html.

index.html is authored for the Artifact runtime, which supplies the document
skeleton (charset, viewport, a small reset) and lifts the page's own <title>,
<meta>, <link> and <style> into the document head. This reproduces that, and
then inlines the web fonts as base64 so the result needs no network at all:
one file that renders identically on a laptop that has never seen it before.

    python3 wrap.py              # inline the fonts (downloads once, then cached)
    python3 wrap.py --no-fonts   # keep the Google Fonts <link> instead

Fonts are cached in .fontcache/ so rebuilds work offline.
"""
import base64
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "saathi-support-chat.html"
CACHE = HERE / ".fontcache"

# latin-ext is what carries the rupee sign (U+20B9), so the prices keep their
# typeface instead of falling back mid-sentence.
SUBSETS = ("latin", "latin-ext")

# A desktop UA, or Google serves the ttf fallback stylesheet instead of woff2.
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Elements that belong in <head>, in the order they should appear there.
HEAD_ELEMENTS = (
    r"<title>.*?</title>",
    r"<meta\b[^>]*>",
    r"<link\b[^>]*>",
    r"<style>.*?</style>",
)

RESET = """  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <style>
    :root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px) }
    body { margin: 0; font: 14px system-ui, sans-serif }
    img { max-width: 100% }
    [hidden] { display: none !important }
  </style>"""


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read()


def cached(url: str) -> bytes:
    """Download a font file once; reuse it on later builds."""
    CACHE.mkdir(exist_ok=True)
    blob = CACHE / url.rsplit("/", 1)[-1]
    if not blob.exists():
        blob.write_bytes(fetch(url))
    return blob.read_bytes()


def inline_fonts(link: str) -> str:
    """Turn a Google Fonts <link> into a <style> of base64 @font-face rules."""
    href = re.search(r'href="([^"]+)"', link).group(1).replace("&amp;", "&")
    css = fetch(href).decode()

    faces = []
    for subset, block in re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{[^}]*\})", css, re.S):
        if subset not in SUBSETS:
            continue
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        data = base64.b64encode(cached(url)).decode()
        faces.append(block.replace(url, f"data:font/woff2;base64,{data}"))

    if not faces:
        raise ValueError(f"no {'/'.join(SUBSETS)} faces found in {href}")
    print(f"  inlined {len(faces)} font faces")
    return "<style>\n" + "\n".join(faces) + "\n</style>"


def split_head(page: str) -> tuple[list[str], str]:
    """Pull the head elements out of the page, keeping document order."""
    head: list[str] = []
    for pattern in HEAD_ELEMENTS:
        for match in re.findall(pattern, page, re.S | re.I):
            head.append(match)
            page = page.replace(match, "", 1)
    return head, page.strip()


def main() -> None:
    head, body = split_head(SRC.read_text(encoding="utf-8"))

    if "--no-fonts" not in sys.argv:
        for i, el in enumerate(head):
            if "fonts.googleapis.com" in el:
                try:
                    head[i] = inline_fonts(el)
                except Exception as exc:                       # offline, or Google changed the CSS
                    print(f"  fonts not inlined ({exc}); keeping the stylesheet link")
                break

    OUT.write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n'
        + RESET + "\n"
        + "\n".join("  " + h for h in head)
        + f"\n</head>\n<body>\n{body}\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
