#!/usr/bin/env bash
# Converts every Markdown file in this directory to a PDF of the same name.
# Usage: ./build_pdfs.sh   (or: bash build_pdfs.sh)

set -euo pipefail
cd "$(dirname "$0")"

for md in *.md; do
    echo "Converting ${md} -> ${md%.md}.pdf"
    pandoc "$md" -o "${md%.md}.pdf"
done
