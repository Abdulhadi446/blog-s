#!/usr/bin/env bash
set -euo pipefail

BLOGS_DIR="$(dirname "$0")/blogs"

if [ ! -d "$BLOGS_DIR" ]; then
  echo "ERROR: blogs directory not found at $BLOGS_DIR" >&2
  exit 1
fi

search_image() {
  local query="$1"
  local encoded
  encoded=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.argv[1]))" "$query")

  local token_url="https://duckduckgo.com/?q=${encoded}&iax=images&ia=images"
  local token
  token=$(curl -s -L -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" "$token_url" | grep -oP 'vqd=\K[^&"]+' | head -1)

  if [ -z "$token" ]; then
    echo ""
    return
  fi

  local api_url="https://duckduckgo.com/i.js?l=us-en&o=json&q=${encoded}&vqd=${token}"
  local result
  result=$(curl -s -L -H "User-Agent: Mozilla/5.0" "$api_url")

  echo "$result" | jq -r '.results[0].image // empty' 2>/dev/null
}

for blog_dir in "$BLOGS_DIR"/*/; do
  [ -d "$blog_dir" ] || continue

  blog_file="$blog_dir/blog.md"
  [ -f "$blog_file" ] || continue

  if [ -f "$blog_dir/image.png" ]; then
    echo "SKIP: $blog_dir (image.png already exists)"
    continue
  fi

  description=$(awk '/^---$/{n++; next} n==1 && /^description:/{sub(/^description: */, ""); print; exit}' "$blog_file")

  if [ -z "$description" ]; then
    echo "SKIP: $blog_dir (no description found)"
    continue
  fi

  echo "SEARCH: $blog_dir — $description"

  image_url=$(search_image "$description")

  if [ -z "$image_url" ]; then
    echo "WARN: No image found for $blog_dir"
    continue
  fi

  echo "DOWNLOAD: $image_url -> $blog_dir/image.png"
  if curl -s -L -o "$blog_dir/image.png" "$image_url"; then
    echo "OK: $blog_dir/image.png saved"
  else
    echo "ERROR: Failed to download for $blog_dir"
    rm -f "$blog_dir/image.png"
  fi
done

echo "Done."
