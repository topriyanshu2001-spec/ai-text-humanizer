#!/usr/bin/env python3
"""Build the shareable single-file page from index.html.

index.html is authored for the Artifact runtime, which supplies the document
skeleton (charset, viewport, a small reset) and lifts the page's own <title>,
<meta>, <link> and <style> into the document head. This reproduces that, so
the result is one self-contained file that opens from a desktop, an email
attachment or any static host.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "index.html"
OUT = HERE / "saathi-support-chat.html"

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


def split_head(page: str) -> tuple[str, str]:
    """Pull the head elements out of the page, keeping document order."""
    head: list[str] = []
    for pattern in HEAD_ELEMENTS:
        for match in re.findall(pattern, page, re.S | re.I):
            head.append(match)
            page = page.replace(match, "", 1)
    return "\n".join("  " + h for h in head), page.strip()


def main() -> None:
    head, body = split_head(SRC.read_text(encoding="utf-8"))
    OUT.write_text(
        f"<!doctype html>\n<html lang=\"en\">\n<head>\n{RESET}\n{head}\n</head>\n"
        f"<body>\n{body}\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
