#!/usr/bin/env bash
# Build solutions.pdf from every .py file, one file per page break,
# in commit order (NeetCode first, then Codility; see pdf_order.py).
# Non-ASCII characters are mapped to ASCII first, since enscript can't render UTF-8.
set -euo pipefail
cd "$(dirname "$0")"

OUT="${1:-solutions.pdf}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 -I pdf_order.py | while IFS= read -r f; do
    printf '\f### %s\n\n' "$f"
    cat "$f"
    echo
done | sed -e 's/⚠️/(!)/g; s/⚠/(!)/g; s/📌/*/g; s/→/->/g; s/←/<-/g; s/↑/^/g;
               s/−/-/g; s/–/-/g; s/≤/<=/g; s/≥/>=/g; s/²/^2/g; s/·/-/g;
               s/─/-/g; s/│/|/g; s/[┌┐└┘┬┴├┤┼]/+/g' > "$TMP/all.txt"

enscript -q -Epython --color -fCourier9 \
    --header='NeetCode + Codility Solutions||Page $% of $=' \
    -p "$TMP/all.ps" "$TMP/all.txt"
ps2pdf "$TMP/all.ps" "$OUT"
echo "wrote $OUT"
