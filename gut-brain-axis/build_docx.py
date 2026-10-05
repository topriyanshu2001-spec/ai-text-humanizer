#!/usr/bin/env python3
"""Build a submission-shaped .docx from MANUSCRIPT.md.

    python3 build_docx.py MANUSCRIPT.md Gut_Brain_Axis_Review_v1.docx

Handles ATX headings, paragraphs, pipe tables, blockquote callouts and inline
**bold** / *italic* / <sup>.

Formatting is fixed: Times New Roman throughout, every run black (Word's built-in
Heading styles are blue Calibri Light, so headings are built by hand instead),
and double line spacing - never 1.5. Editorial callouts are carried in bold
rather than colour, and stay identifiable by their bracketed labels.
"""
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|<sup>[^<]*</sup>)")

FONT = "Times New Roman"
BLACK = RGBColor(0x00, 0x00, 0x00)


def style_run(run):
    """Every run: Times New Roman, black, including the East Asian font slot."""
    run.font.name = FONT
    run.font.color.rgb = BLACK
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)
    return run


def add_runs(par, text, bold_all=False):
    """Write text into a paragraph, honouring **bold**, *italic* and <sup>."""
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            run = par.add_run(piece[2:-2]); run.bold = True
        elif piece.startswith("<sup>") and piece.endswith("</sup>"):
            run = par.add_run(piece[5:-6]); run.font.superscript = True
        elif piece.startswith("*") and piece.endswith("*"):
            run = par.add_run(piece[1:-1]); run.italic = True
        else:
            run = par.add_run(piece)
        if bold_all:
            run.bold = True
        style_run(run)


def is_row(line):
    return line.startswith("|") and line.endswith("|")


def cells(line):
    return [c.strip() for c in line.strip("|").split("|")]


def build(md_path, out_path):
    lines = open(md_path, encoding="utf-8").read().split("\n")

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.font.color.rgb = RGBColor(0, 0, 0)
    style.paragraph_format.line_spacing = 2.0  # double; never 1.5

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip() or set(line.strip()) == {"-"}:
            i += 1
            continue

        # table
        if is_row(line) and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").strip()) <= set("-: "):
            header = cells(line)
            i += 2
            body = []
            while i < len(lines) and is_row(lines[i].rstrip()):
                body.append(cells(lines[i].rstrip()))
                i += 1
            table = doc.add_table(rows=1, cols=len(header))
            table.style = "Table Grid"
            for c, text in enumerate(header):
                cell = table.rows[0].cells[c]
                cell.text = ""
                add_runs(cell.paragraphs[0], text, bold_all=True)
            for row in body:
                rc = table.add_row().cells
                for c, text in enumerate(row[: len(header)]):
                    rc[c].text = ""
                    add_runs(rc[c].paragraphs[0], text)
            doc.add_paragraph()
            continue

        # heading
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            text = re.sub(r"\*\*|\*", "", m.group(2))
            par = doc.add_paragraph()
            if level == 1:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = par.add_run(text)
            run.bold = True
            run.font.size = Pt(14 if level == 1 else 12)
            if level >= 3:
                run.italic = True
            style_run(run)
            i += 1
            continue

        # blockquote callout -> red, so it cannot be shipped unnoticed
        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip())
                i += 1
            par = doc.add_paragraph()
            add_runs(par, " ".join(buf), bold_all=True)
            continue

        # ordinary paragraph (gather wrapped lines)
        # A numbered entry starts its own paragraph, so reference lists written
        # on consecutive lines do not collapse into one block.
        buf = [line]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith(("#", ">", "|", "---"))
            and not re.match(r"^\d+\.\s", lines[i])
        ):
            buf.append(lines[i].rstrip())
            i += 1
        text = " ".join(buf)
        par = doc.add_paragraph()
        if re.match(r"^\d+\.\s", text):  # reference entry
            par.paragraph_format.first_line_indent = Pt(-18)
            par.paragraph_format.left_indent = Pt(18)
        add_runs(par, text)

    finalise(doc)
    doc.save(out_path)
    print(f"wrote {out_path}")


def finalise(doc):
    """Sweep every run in the document, body and tables, so nothing inherits.

    Clearing a table cell leaves an empty run behind; those would otherwise
    carry the default theme font rather than Times New Roman.
    """
    def sweep(par):
        par.paragraph_format.line_spacing = 2.0  # explicit; never 1.5
        for run in par.runs:
            style_run(run)

    for par in doc.paragraphs:
        sweep(par)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for par in cell.paragraphs:
                    sweep(par)


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "MANUSCRIPT.md"
    dst = sys.argv[2] if len(sys.argv) > 2 else "MANUSCRIPT.docx"
    build(src, dst)
