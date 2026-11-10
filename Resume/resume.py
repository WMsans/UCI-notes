"""Markdown resume -> one-page PDF. Usage: python resume.py input.md [output.pdf]"""
import re
import sys
from pathlib import Path

import markdown
import weasyprint

CSS = """
@page { size: Letter; margin: 0.5in 0.6in; }
* { box-sizing: border-box; }
body {
  font-family: Helvetica, Arial, "Liberation Sans", sans-serif;
  font-size: 12.5px; color: #222; line-height: 1.35; margin: 0;
}
h1 { font-size: 34px; line-height: 1.1; margin: 0; color: #1f3a5f; letter-spacing: -0.5px; }
p.tagline { font-size: 15px; color: #1f3a5f; margin: 3px 0 2px; }
p.contact { font-size: 11.5px; color: #555; margin: 0 0 12px; }
h2 {
  font-size: 14px; text-transform: uppercase; letter-spacing: 0.08em; color: #1f3a5f;
  border-bottom: 2px solid #1f3a5f; padding-bottom: 3px; margin: 14px 0 6px;
}
.job {
  display: flex; justify-content: space-between; align-items: baseline;
  margin: 8px 0 0;
}
.job .title { font-size: 15px; font-weight: bold; }
.job .date { font-size: 11px; color: #777; white-space: nowrap; }
p.org { font-size: 11.5px; font-style: italic; color: #555; margin: 1px 0 3px; }
ul { margin: 3px 0 4px; padding-left: 16px; }
li { margin: 2px 0; }
p { margin: 0 0 4px; }
"""


def _job(match):
    title, _, date = match.group(1).rpartition(" | ")
    if not title:
        return f'<div class="job"><span class="title">{date}</span></div>'
    return (
        '<div class="job">'
        f'<span class="title">{title}</span>'
        f'<span class="date">{date}</span>'
        "</div>"
    )


def render_html(md_text):
    body = markdown.markdown(md_text)
    body = re.sub(r"<h3>(.*?)</h3>", _job, body, flags=re.S)
    body = re.sub(r'</div>\s*<p><em>(.*?)</em></p>', r'</div>\n<p class="org">\1</p>', body, flags=re.S)
    h1 = re.search(r"<h1>.*?</h1>", body, flags=re.S)
    if h1:
        head, tail = body[: h1.end()], body[h1.end() :]
        tail = re.sub(r"<p>", '<p class="tagline">', tail, count=1)
        tail = re.sub(r"<p>", '<p class="contact">', tail, count=1)
        body = head + tail
    return (
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\">"
        f"<style>{CSS}</style></head><body>\n{body}\n</body></html>\n"
    )


def main(argv):
    if len(argv) < 2:
        print("usage: python resume.py input.md [output.pdf]", file=sys.stderr)
        raise SystemExit(2)
    src = Path(argv[1])
    out = Path(argv[2]) if len(argv) > 2 else src.with_suffix(".pdf")
    weasyprint.HTML(string=render_html(src.read_text(encoding="utf-8"))).write_pdf(out)
    print(out)


if __name__ == "__main__":
    main(sys.argv)
