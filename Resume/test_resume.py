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


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
