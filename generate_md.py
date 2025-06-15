from datetime import datetime, timedelta
import re
import os

# === Config ===
input_file = "entries.txt"
output_folder = "markdown_posts"
start_date = datetime(2024, 4, 1)              # Updated start date
starting_entry_number = 1201                  # Updated entry number

# === Ensure Output Folder Exists ===
os.makedirs(output_folder, exist_ok=True)

# === Read File ===
with open(input_file, "r", encoding="utf-8") as f:
    raw_text = f.read()

# === Split into Entries ===
entries = re.split(r"(?=^\d{4}:\s)", raw_text, flags=re.MULTILINE)

# === Process Each Entry ===
for entry in entries:
    entry = entry.strip()
    if not entry:
        continue

    # Match exactly 4-digit entry numbers (1000–9999 range)
    match = re.match(r"^(\d{4}):", entry)
    if not match:
        print(f"Skipping invalid entry: {entry[:30]}...")
        continue

    entry_number = int(match.group(1))

    # Only allow numbers between 1201 and 1608
    if not (1201 <= entry_number <= 1608):
        print(f"Skipping entry {entry_number} (outside valid range)...")
        continue

    # Compute date based on entry offset
    date = start_date + timedelta(days=(entry_number - starting_entry_number))
    date_str = date.strftime("%Y-%m-%d")

    # Remove leading number
    entry_body = re.sub(r"^\d{4}:\s*", "", entry)

    # Write markdown
    title_line = f'title: "{entry_number}:"'
    md_content = f"""---
layout: post
{title_line}
date: {date_str}
---

{entry_body}
"""

    filename = f"{date_str}-.md"
    filepath = os.path.join(output_folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Wrote {filename}")
