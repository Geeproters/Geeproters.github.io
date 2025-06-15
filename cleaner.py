def clean_entries_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:

        for line in infile:
            stripped = line.lstrip()
            if stripped.startswith("Composer, Lyricist") or stripped.startswith("Lyricist:"):
                continue
            if any(stripped.startswith(f"[{i}") for i in range(1, 10)):
                continue
            outfile.write(line)

if __name__ == "__main__":
    clean_entries_file("entries.txt", "cleaned_entries.txt")
