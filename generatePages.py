import json
import os
import re
from pathlib import Path

# --- CONFIGURATION ---
CONTENT_DIR = Path("content")
TEMPLATE_DIR = CONTENT_DIR / "System" / "Templates"

# Search paths for existing files
SEARCH_DIRS = [
    CONTENT_DIR / "Campaigns",
    CONTENT_DIR / "World"
]

# Output paths for NEW files
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
    for search_path in SEARCH_DIRS:
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                return Path(root) / filename
    return None

def update_frontmatter(content, updates):
    """Updates YAML frontmatter keys using Regex."""
    for key, new_value in updates.items():
        pattern = rf"^(\s*{key}\s*:\s*).*$"
        if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
            replacement = f"{key}: {new_value}"
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.IGNORECASE)
            print(f"    - Updated Frontmatter: {key} -> {new_value}")
        else:
            print(f"    ⚠️ Key '{key}' not found in frontmatter. Skipping.")
    return content

def append_to_section(content, header, new_text):
    """Inserts text after a specific markdown header."""
    lines = content.splitlines()
    header_index = -1
    
    # Find Header
    for i, line in enumerate(lines):
        # Loose match to catch ## History vs ## History with Party
        if line.strip().lower().startswith(header.lower().replace("## ", "").strip()): 
             # Or exact match on markdown syntax
             pass
        if header.lower() in line.lower():
            header_index = i
            break
    
    if header_index != -1:
        lines.insert(header_index + 1, new_text)
        print(f"    - Appended to {header}")
        return "\n".join(lines)
    else:
        print(f"    ⚠️ Header '{header}' not found. Appending to bottom.")
        return content + f"\n\n{header}\n{new_text}"

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
        # V3 Logic: Updates are nested dictionaries/lists, not flat keys
        frontmatter_updates = entry.get("frontmatter_updates", {})
        section_appends = entry.get("section_appends", [])

        file_path = find_file(filename)
        if not file_path:
            print(f"❌ Could not find {filename} to update.")
            continue
            
        print(f"🔄 Processing {filename}...")
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if frontmatter_updates:
            content = update_frontmatter(content, frontmatter_updates)
            
        for append in section_appends:
            content = append_to_section(content, append["header"], append["content"])
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    main()
