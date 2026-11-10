# Resume PDF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `python resume.py resume.md` turns a Markdown resume into a one-page PDF in the approved "Modern" style, plus a first resume draft for a tutoring-center math teacher/counselor role.

**Architecture:** One script. `markdown` converts to HTML, a regex post-processes `<h3>Title | Date</h3>` into a title/date flex row, the HTML is wrapped with embedded CSS copied from mockup v3, and WeasyPrint writes the PDF.

**Tech Stack:** Python 3, `python-markdown`, `python-weasyprint` (Arch: `sudo pacman -S python-markdown python-weasyprint`).

**Spec:** `docs/superpowers/specs/2026-11-09-resume-pdf-design.md`

## Global Constraints
- Files live in `Resume/`: `resume.py`, `test_resume.py`, `resume.md`, output `resume.pdf`.
- No CLI options beyond `input.md [output.pdf]`. The default output is the input path with a `.pdf` extension.
- Accent `#1f3a5f`. Size order: name 34px > title 15px > section 14px caps + 2px navy rule > bullets 12.5px > org 11.5px italic #555 > date 11px #777. Sans-serif (Helvetica/Arial/Liberation Sans).
- Letter page with ~0.5in margins. The output must be exactly 1 page.
- Never invent facts. Unknowns stay as `TODO` text.
- Tests are plain asserts run with `python test_resume.py` (no pytest dependency).

## Review Focus
- `&`, `<` in text (e.g. "Math Teacher & Academic Counselor") must render as literal characters → test `test_ampersand_escaped`.
- `### Title` with no `|` must render as a plain title with no empty date span → test `test_title_without_date`.
- The pipe-separated contact line must stay one paragraph, not a table (tables extension stays off) → test `test_contact_line_is_paragraph`.
- Unicode en-dash `–` and `·` survive into the HTML → test `test_unicode_dates`.
- Content overflowing to page 2 → Task 2 verifies the page count is 1.

---

### Task 1: Converter `resume.py`

**Files:**
- Create: `Resume/resume.py`
- Create: `Resume/test_resume.py`
- Modify: `UCI notes/.gitignore` (create if missing): add `Resume/.superpowers/`

**Interfaces:**
- Produces: `render_html(md_text: str) -> str` (a full HTML document with embedded `<style>`); `main(argv: list[str]) -> None` (writes the PDF and prints its path).

- [ ] **Step 1: Install deps**: `sudo pacman -S --needed python-markdown python-weasyprint` (ask the user to run it with `!` if sudo prompts).
- [ ] **Step 2: Write failing tests** in `test_resume.py`, with each one called under `if __name__ == "__main__"` and printing `ok`:
```python
from resume import render_html
def test_title_date_split():
    h = render_html("### Private Tutor | 2025 – Present\n")
    assert '<span class="title">Private Tutor</span>' in h
    assert '<span class="date">2025 – Present</span>' in h
def test_title_without_date():
    h = render_html("### Volunteer\n")
    assert '<span class="title">Volunteer</span>' in h and 'class="date"' not in h
def test_ampersand_escaped():
    assert "Teacher &amp; Counselor" in render_html("# A\nTeacher & Counselor\n")
def test_contact_line_is_paragraph():
    assert "<table" not in render_html("Irvine | a@b.c | 555\n")
def test_unicode_dates():
    assert "2023 – 2024 ·" in render_html("2023 – 2024 · x\n")
```
- [ ] **Step 3: Run** `python test_resume.py` → expect ImportError.
- [ ] **Step 4: Implement `render_html`.** Use `markdown.markdown(text)` with no extensions. Replace `<h3>(.*?)</h3>` with `<div class="job"><span class="title">T</span><span class="date">D</span></div>`, splitting on the last ` | `. The first `<p>` after `<h1>` gets `class="tagline"` and the second gets `class="contact"`. A `<p><em>…</em></p>` right after a job becomes `<p class="org">…</p>`. The CSS is ported from `.superpowers/brainstorm/*/content/resume-style-v3.html` with the `@page { size: Letter; margin: 0.5in 0.6in }` rule.
- [ ] **Step 5: Implement `main`.** `weasyprint.HTML(string=html).write_pdf(out)`. If argv is missing, print usage and exit with code 2.
- [ ] **Step 6: Run** `python test_resume.py` → all `ok`.
- [ ] **Step 7: Commit** (only if the user approves committing): `git add Resume/resume.py Resume/test_resume.py .gitignore`.

### Task 2: Resume draft `resume.md` → `resume.pdf`

**Files:**
- Create: `Resume/resume.md`

**Interfaces:**
- Consumes: `python resume.py resume.md` from Task 1.

- [ ] **Step 1: Write `resume.md`** following the spec's "Resume content" section, using the spec's Markdown conventions. Sections in order: Math Achievements, Teaching Experience (RedNote 2025 – Present; Schoolhouse.world 2024 – 2026; Shanghai non-profit 2023 – 2024), Education (UC Irvine, B.S. Computer Science, Expected 2030), Skills. TODO placeholders: name, email, phone, non-profit name/subjects. 2–3 bullets per job, verb-first. The RedNote bullets cover subjects (school math, school science, AP math, AP CS A / AP CSP, SAT prep), personalized study plans, and parent progress updates.
- [ ] **Step 2: Render** with `python resume.py resume.md` → prints `resume.pdf`.
- [ ] **Step 3: Verify** that `python -c "import pypdf..."` or `pdfinfo resume.pdf | grep Pages` reports `1`. Convert to PNG (`pdftoppm -png -r 80 resume.pdf /scratch/prev`) and look at the image to check the hierarchy matches mockup v3.
- [ ] **Step 4: Commit** (only if the user approves): `git add Resume/resume.md Resume/resume.pdf`.
