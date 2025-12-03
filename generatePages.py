import json
import os
from pathlib import Path

# --- CONFIGURATION ---
CONTENT_DIR = Path("content")
TEMPLATE_DIR = CONTENT_DIR / "System" / "Templates"

# Define where to look for existing files to update
# (The script needs to find them recursively because they could be anywhere)
SEARCH_DIRS = [
    CONTENT_DIR / "Campaigns",
    CONTENT_DIR / "World"
]

# Where NEW files should go (Defaults)
NEW_FILE_DIRS = {
    "NPC": CONTENT_DIR / "Campaigns" / "Campaign 1" / "NPCs",
    "Item": CONTENT_DIR / "World" / "Grimmora" / "Items",
    "Quest": CONTENT_DIR / "Campaigns" / "Campaign 1" / "Quests",
    "Organization": CONTENT_DIR / "World" / "Grimmora" / "Organizations"
}

TEMPLATE_MAP = {
    "NPC": "NPC.md",
    "Item": "Item.md",
    "Quest": "Ongoing Thread.md",
    "Organization": "Organization.md"
}

# ------------------------------------------------------------------

def load_template(template_name):
    filename = TEMPLATE_MAP.get(template_name)
    if not filename: return None
    path = TEMPLATE_DIR / filename
    if not path.exists(): return None
    with open(path, "r", encoding="utf-8") as f: return f.read()

def fill_template(content, data):
    for key, value in data.items():
        placeholder = f"{{{{{key}}}}}"
        content = content.replace(placeholder, str(value))
    return content

def find_file(filename):
    """Recursively looks for a file in the content directories."""
    for search_path in SEARCH_DIRS:
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                return Path(root) / filename
    return None

def update_file(filepath, header, content_to_append):
    """Finds a header and appends content after it."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_index = -1
    # Try to find the exact header
    for i, line in enumerate(lines):
        if line.strip().lower() == header.lower() or line.strip().lower() == header.lower() + " with the party":
             # Loose matching to catch "## History" vs "## History with the Party"
            header_index = i
            break
    
    if header_index != -1:
        # Insert after the header
        # We look forward to see if there is content, or just insert immediately
        lines.insert(header_index + 1, content_to_append + "\n")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"🔄 Updated: {filepath.name} (Appended to {header})")
    else:
        print(f"⚠️  Warning: Header '{header}' not found in {filepath.name}. Appending to bottom.")
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"\n\n{header}\n{content_to_append}")

def main():
    json_path = Path("update.json")
    if not json_path.exists():
        print("❌ 'update.json' not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            payload = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON format: {e}")
            return

    # --- PROCESS NEW ENTRIES ---
    new_entries = payload.get("new_entries", [])
    for entry in new_entries:
        type_key = entry["template"]
        filename = entry["filename"]
        data = entry["data"]
        
        target_dir = NEW_FILE_DIRS.get(type_key)
        if not target_dir: continue
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / filename

        if target_path.exists():
            print(f"⚠️ Skipping Creation: {filename} already exists.")
            continue

        raw_template = load_template(type_key)
        if raw_template:
            final_content = fill_template(raw_template, data)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(final_content)
            print(f"✅ Created: {filename}")

    # --- PROCESS UPDATES ---
    updated_entries = payload.get("updated_entries", [])
    for entry in updated_entries:
        filename = entry["filename"]
        header = entry["section_header"]
        content = entry["content"]

        # Find where the file lives currently
        existing_path = find_file(filename)
        
        if existing_path:
            update_file(existing_path, header, content)
        else:
            print(f"❌ Could not update {filename}: File not found in vault.")

if __name__ == "__main__":
    main()
