import os
import sys
import re
from pathlib import Path
from datetime import datetime

# --- CONFIGURATION ---
# Detects the script's location to find the repo root
REPO_ROOT = Path(__file__).parent.resolve()
CONTENT_DIR = REPO_ROOT / "content"
BASE_SEARCH_DIR = CONTENT_DIR / "Campaigns" / "Campaign 1"
CHRONICLES_DIR = BASE_SEARCH_DIR / "Chronicles"
SNAPSHOT_FILE = CONTENT_DIR / "System" / "Campaign-Snapshot.md"
TEMPLATE_DIR = CONTENT_DIR / "System" / "Templates"

# Folders to ignore in the Tree View
IGNORE_DIRS = {'.git', '.obsidian', 'node_modules', 'public', 'assets', 'attachments', 'campaign_outputs', '__pycache__'}

def get_yaml_metadata(file_path):
    """
    Peeks at the first few lines of a file to extract 'type' and 'status'.
    Returns a short string like "[type: npc | status: Alive]" or "" if not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [next(f) for _ in range(15)] # Read first 15 lines to be safe
        
        # Check if file starts with YAML block
        if not lines or lines[0].strip() != "---":
            return ""
            
        data = {}
        in_yaml = False
        for i, line in enumerate(lines):
            line = line.strip()
            if i == 0 and line == "---":
                in_yaml = True
                continue
            if line == "---": 
                break
            if in_yaml and ":" in line:
                key, val = line.split(":", 1)
                data[key.strip()] = val.strip()
        
        # Build summary tag
        parts = []
        if "type" in data: parts.append(f"type: {data['type']}")
        if "status" in data: parts.append(f"status: {data['status']}")
        
        return f" [{ ' | '.join(parts) }]" if parts else ""
    except Exception:
        return ""

def natsort_key(s):
    """Natural sort key (handles Entry 1, Entry 2, Entry 10 correctly)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', str(s))]

def generate_tree(directory, prefix=""):
    """
    Recursive function to generate a tree structure with metadata.
    """
    output = []
    try:
        # Sort: Directories first, then Files. 
        # Files sorted naturally
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), natsort_key(x.name)))
        
        entries = [x for x in items if x.name not in IGNORE_DIRS and not x.name.startswith('.')]
        
        for i, path in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            
            if path.is_dir():
                output.append(f"{prefix}{connector}{path.name}/")
                extension = "    " if is_last else "│   "
                output.extend(generate_tree(path, prefix + extension))
            else:
                if path.suffix == ".md":
                    meta = get_yaml_metadata(path)
                    output.append(f"{prefix}{connector}{path.name}{meta}")
                else:
                    output.append(f"{prefix}{connector}{path.name}")
    except PermissionError:
        pass # Skip folders we can't access
                
    return output

def get_latest_entry(chronicles_dir):
    """Finds the lexically last Entry file."""
    if not chronicles_dir.exists(): return None
    entries = list(chronicles_dir.glob("Entry *.md"))
    if not entries: return None
    # Sort by the number in the filename
    entries.sort(key=lambda x: natsort_key(x.name))
    return entries[-1].name

def main():
    if not BASE_SEARCH_DIR.exists():
        print(f"❌ Error: Path not found: {BASE_SEARCH_DIR}")
        return

    # 1. DISCOVER SUBDIRECTORIES
    subdirs = [x for x in BASE_SEARCH_DIR.iterdir() if x.is_dir() and x.name not in IGNORE_DIRS]
    subdirs.sort(key=lambda x: x.name)
    
    selected_indices = set()

    # 2. SELECTION LOOP
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- Context Bomb: Directory Selector ({os.name}) ---")
        try:
            print(f"Root: {BASE_SEARCH_DIR.relative_to(REPO_ROOT)}")
        except ValueError:
            print(f"Root: {BASE_SEARCH_DIR}")
        print("----------------------------------------")
        
        for i, path in enumerate(subdirs):
            mark = "[*]" if i in selected_indices else "[ ]"
            print(f"{i}. {mark} {path.name}")
            
        print("----------------------------------------")
        print("Type numbers (e.g. '0 2') to toggle, 'a' for all, 'e' to Export.")
        choice = input("Selection: ").strip().lower()

        if choice == 'e': break
        elif choice == 'q': sys.exit()
        elif choice == 'a': 
            selected_indices = set(range(len(subdirs)))
        else:
            # Handle space-separated numbers
            parts = choice.split()
            for part in parts:
                if part.isdigit():
                    idx = int(part)
                    if 0 <= idx < len(subdirs):
                        if idx in selected_indices:
                            selected_indices.remove(idx)
                        else:
                            selected_indices.add(idx)

    # 3. GENERATE OUTPUT
    if not selected_indices:
        print("No folders selected. Exiting.")
        return

    # Construct Filename
    selected_names = [subdirs[i].name for i in selected_indices]
    safe_names = "_".join(selected_names).replace(" ", "")[:50] # Limit length
    output_file = Path.home() / f"Context_{safe_names}_Export.txt"
    
    print(f"\nGenerating: {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # HEADER
        f.write(f"### CONTEXT FILE GENERATED ON {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("### VAULT NAME: Grimmora Pages\n\n")
        
        # SECTION 0: SNAPSHOT
        f.write("### SECTION 0: CURRENT CAMPAIGN SNAPSHOT\n")
        f.write("**INSTRUCTIONS FOR THE LLM**:\n")
        f.write("1. **Request Protocol**: You have a full list of vault files in Section 1. If you need details from a file listed there that isn't in Section 2, **stop and ask me to attach it**.\n")
        f.write("2. **Schema Consistency**: Always check 'SECTION 1.5: SYSTEM TEMPLATES' before suggesting new vault entries.\n")
        f.write("3. **Chronological Anchor**: Use the final Entry in Section 2 as your primary 'Now'.\n\n")
        
        f.write("**CURRENT SNAPSHOT**:\n")
        if SNAPSHOT_FILE.exists():
            f.write(SNAPSHOT_FILE.read_text(encoding='utf-8') + "\n")
        else:
            f.write("> [!WARNING] No snapshot file found.\n")
        
        latest_entry = get_latest_entry(CHRONICLES_DIR)
        if latest_entry:
            f.write(f"\n* **Latest Entry Reference**: {latest_entry}\n")
        
        f.write("\n---\n\n")
        
        # SECTION 1: MANIFEST (With Metadata!)
        f.write("### SECTION 1: VAULT FILE MANIFEST (TREE)\n")
        f.write(f"Root: {CONTENT_DIR.name}\n")
        tree_lines = generate_tree(BASE_SEARCH_DIR) # Generating tree for the Campaign folder
        f.write("\n".join(tree_lines))
        f.write("\n\n")
        
        # SECTION 1.5: TEMPLATES
        f.write("### SECTION 1.5: SYSTEM TEMPLATES\n")
        f.write("Instruction: Use these as the gold standard for formatting new files.\n")
        if TEMPLATE_DIR.exists():
            for t_file in sorted(TEMPLATE_DIR.glob("*.md")):
                f.write(f"\n### TEMPLATE SOURCE: {t_file.name}\n")
                f.write(t_file.read_text(encoding='utf-8') + "\n")
        
        # SECTION 2: CONTENT
        f.write("\n### SECTION 2: CONTENT ENTRIES\n")
        for i in selected_indices:
            folder = subdirs[i]
            # Recursively find all MD files in selected folder
            for md_file in sorted(folder.rglob("*.md"), key=lambda x: natsort_key(x.name)):
                rel_path = md_file.relative_to(CONTENT_DIR)
                f.write(f"\n\n### SOURCE: {rel_path}\n")
                f.write(md_file.read_text(encoding='utf-8'))

    # Calculate size for display
    size_bytes = output_file.stat().st_size
    if size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.2f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.2f} MB"

    print(f"✅ Done! Size: {size_str}")

if __name__ == "__main__":
    main()