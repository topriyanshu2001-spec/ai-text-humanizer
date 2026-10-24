#!/usr/bin/env python3
"""Wrap index.html into a standalone, locally-openable page.

index.html is authored for the Artifact runtime, which supplies the
document skeleton (charset, viewport, small reset). This adds the same
skeleton so the file opens correctly from the filesystem too.
"""
from pathlib import Path

HERE = Path(__file__).parent
SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root {{ color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px) }}
  body {{ margin: 0; font: 14px system-ui, sans-serif }}
  img {{ max-width: 100% }}
  [hidden] {{ display: none !important }}
</style>
{page}
</head>
</html>
"""


def main() -> None:
    page = (HERE / "index.html").read_text(encoding="utf-8")
    out = HERE / "standalone.html"
    out.write_text(SKELETON.format(page=page), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
