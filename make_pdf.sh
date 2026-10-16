#!/usr/bin/env bash
# Build solutions.pdf from every .py file, in commit order (NeetCode first,
# then Codility; see pdf_order.py). Each file starts on a new page.
# If a solution has a screenshot next to it (same name, .png), it gets its own
# page right after that solution.
# Non-ASCII characters are mapped to ASCII first, since enscript can't render UTF-8.
set -euo pipefail
cd "$(dirname "$0")"

OUT="${1:-solutions.pdf}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Landscape A4 page with the image scaled to fit under a caption.
image_page() {
    python3 -I - "$1" "$2" <<'EOF'
import sys
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1], sys.argv[2]
dpi = 150
page = Image.new("RGB", (int(11.69 * dpi), int(8.27 * dpi)), "white")
margin = int(0.5 * dpi)

draw = ImageDraw.Draw(page)
draw.text((margin, margin), "Diagram: " + src, fill="black", font=ImageFont.load_default(size=22))

img = Image.open(src).convert("RGB")
max_w, max_h = page.width - 2 * margin, page.height - 3 * margin
scale = min(max_w / img.width, max_h / img.height)
img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
page.paste(img, (margin, 2 * margin))
page.save(out, resolution=dpi)
EOF
}

# Write the order to a file first (not `< <(...)`), so the script also works
# when run as `sh make_pdf.sh`.
python3 -I pdf_order.py > "$TMP/order.txt"

parts=()
n=0
while IFS= read -r f; do
    n=$((n + 1))
    part="$TMP/$(printf '%03d' "$n")"

    # Header: "06 Trees > 19 Depth-First Search" (or "codilty"), file name as the first line.
    rel="${f#Data Structures & Algorithms/}"
    if [[ "$(basename "$f")" == cheatsheet.py ]]; then
        label="$(dirname "$rel") > Cheatsheet"
    else
        label="$(dirname "$(dirname "$rel")")"
        label="${label// \/ / > }"
        label="${label//\// > }"
    fi
    { printf '### %s\n\n' "$(basename "$f")"
      sed -e 's/⚠️/(!)/g; s/⚠/(!)/g; s/📌/*/g; s/→/->/g; s/←/<-/g; s/↑/^/g;
              s/−/-/g; s/–/-/g; s/≤/<=/g; s/≥/>=/g; s/²/^2/g; s/·/-/g;
              s/─/-/g; s/│/|/g; s/[┌┐└┘┬┴├┤┼]/+/g' "$f"
    } > "$part.txt"
    enscript -q -Epython --color -fCourier9 \
        --header="$label||Page \$% of \$=" \
        -p "$part.ps" "$part.txt"
    ps2pdf "$part.ps" "$part.pdf"
    parts+=("$part.pdf")

    png="${f%.py}.png"
    if [[ -f "$png" ]]; then
        image_page "$png" "$part-img.pdf"
        parts+=("$part-img.pdf")
    fi
done < "$TMP/order.txt"

pdfunite "${parts[@]}" "$OUT"
echo "wrote $OUT"
