# Markdown → PDF Resume + Tutoring-Center Resume — Design

## Intent
Jeremy (UCI CS freshman) wants to keep their resume as plain Markdown and get a
professional PDF from it, then use that to apply for a math teacher / academic
counselor role at a Think Academy–style tutoring center (competition + school
math, heavy parent communication, often Mandarin-speaking families).

## Goals
- One command: `python resume.py resume.md` → `resume.pdf`.
- Output matches the approved "Modern" mockup (`resume-style-v3.html`).
- A first resume draft (`resume.md`) built from Jeremy's real experience.

## Non-goals / anti-goals
- No multiple themes, config files, or CLI options beyond input (and optional output) path.
- Not a general Markdown publisher. It only needs to handle the resume conventions below.
- Anti-goal: invented facts on the resume. Anything unknown is a visible `TODO` placeholder.
- Anti-goal: a cramped or flat layout where every text level is the same size (the complaint about the first mockups).

## Approaches considered
1. **Markdown → HTML/CSS → PDF with WeasyPrint** — **chosen.** Reuses the mockup CSS directly,
   so the PDF looks the way it was approved, and the look is tweakable in one stylesheet.
   Cost: `pacman -S python-markdown python-weasyprint`.
2. Markdown → LaTeX → xelatex. No installs, but needs a hand-rolled Markdown→LaTeX translator
   with fragile escaping, and the approved CSS can't be reused.
3. pandoc + LaTeX template. Large install, and resume structure (title with right-aligned date) is awkward in pandoc.

## Design (decided)
**Look:** "Modern" v3. Sans-serif (Helvetica/Arial-like), single navy accent `#1f3a5f`, Letter size,
one page. Size hierarchy: name 34px > section header 14px caps + navy rule > job title 15px bold >
bullets 12.5px > org (11.5px italic gray) / date (11px gray). Sizes may be converted to pt for print
while keeping the same ratios.

**Markdown conventions:**
```md
# Name
Tagline line
Contact | items | separated | by pipes

## Section
### Job Title | Date range
*Organization*
- bullet
```
- `#` = name, the first two paragraphs after it = tagline and contact line.
- `##` = section header.
- `### Title | Date` → title on the left, date right-aligned.
- `*…*` paragraph directly after an `###` = org line.

**Implementation:** one file `resume.py`. It uses `markdown` to produce HTML, does a small
post-processing step for the `### Title | Date` split, wraps the result with embedded CSS, and calls
WeasyPrint `write_pdf`. A minimal assert-based self-check covers the title/date split.

## Resume content (`resume.md`)
- **Header:** name, "Math Teacher & Academic Counselor", Irvine CA, email, phone, Mandarin · English.
- **Math Achievements:** AMC 10 145/150, AMC 8 24/25, USACO Gold.
- **Teaching Experience:**
  - Private Tutor, independent (families via RedNote), 2025–Present. High school students: school
    math, school science, AP math, AP CS A / AP CSP, SAT prep. Bullets stress parent communication and
    study plans, which is the "counselor" half of the role.
  - Volunteer Tutor, Schoolhouse.world, 2024–2026. SAT Math and SAT English.
  - Remote Tutor, non-profit in Shanghai, 2023–2024.
- **Education:** UC Irvine, B.S. Computer Science, expected graduation year.
- **Skills:** Mandarin / English, subjects taught, competition math.

## Left to the builder (marked TODO in the draft for Jeremy to fill in)
- Full name, email, phone.
- Name of the Shanghai non-profit and what was taught there.
- Expected graduation year (assumed 2030).
- Student counts and AIME qualification, if any (left out unless provided).
- Exact bullet wording. Strong verbs, no invented numbers.
