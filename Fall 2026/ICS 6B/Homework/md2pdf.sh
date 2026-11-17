#!/usr/bin/env bash
#
# md2pdf.sh — render a markdown homework file to PDF, one problem per page.
#
# Usage:
#   ./md2pdf.sh "Homework 6.md" [output.pdf]
#
# Converts Obsidian-style image links `![[file.png]]` to standard images,
# starts each `# Problem` header on a new page, and preserves line breaks
# inside derivations. Replaces the output file if it already exists.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <input.md> [output.pdf]" >&2
  exit 1
fi

input="$1"
output="${2:-${input%.md}.pdf}"

if [[ ! -f "$input" ]]; then
  echo "Error: input file not found: $input" >&2
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
filter="$script_dir/pagebreak.lua"

# Build a temp markdown file with Obsidian image links converted.
tmp_md="$(mktemp)"
trap 'rm -f "$tmp_md"' EXIT

sed 's/!\[\[\([^]]*\)\]\]/![\1](\1)/g' "$input" > "$tmp_md"

pandoc "$tmp_md" \
  -f markdown+hard_line_breaks \
  -o "$output" \
  --pdf-engine=xelatex \
  --lua-filter="$filter" \
  -V geometry:margin=1in

echo "Wrote $output"
