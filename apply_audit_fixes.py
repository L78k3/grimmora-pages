import os
import json
import shutil
import re

# CONFIGURATION
AUDIT_FILE = "_audit_report.json"
VAULT_ROOT = os.getcwd()

def clean_json_content(content):
    """Strips Markdown code blocks to ensure valid JSON parsing."""
    if "import os" in content or "def apply_fixes" in content:
        raise ValueError("The _audit_report.json file contains Python code! Please paste the LLM's JSON output instead.")
    pattern = r"```(?:json)?\s*(.*?)\s*```"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else content

def find_real_path(root, short_path):
    """
    If the exact path doesn't exist, search the vault for the filename.
    Returns the absolute path if found, or None.
    """
    # 1. Try exact match first
    exact_path = os.path.join(root, short_path)
    if os.path.exists(exact_path):
        return exact_path

    # 2. Search recursively for the filename
    target_name = os.path.basename(short_path)
    # print(f"   🔎 Searching vault for '{target_name}'...") # Uncomment for debug noise
    
    for dirpath, _, filenames in os.walk(root):
        # Skip git and obsidian folders to speed it up
        if ".git" in dirpath or ".obsidian" in dirpath:
            continue
            
        if target_name in filenames:
            return os.path.join(dirpath, target_name)
    
    return None

def apply_fixes():
    print(f"🔍 Reading audit report from {AUDIT_FILE}...")
    
    if not os.path.exists(AUDIT_FILE):
        print(f"❌ Error: {AUDIT_FILE} not found.")
        return

    try:
        with open(AUDIT_FILE, "r", encoding="utf-8") as f:
            raw = f.read()
        report = json.loads(clean_json_content(raw))
    except Exception as e:
        print(f"❌ JSON Error: {e}")
        return

    # 1. HANDLE RENAMES
    renames = report.get("renames", [])
    if renames:
        print(f"\n📂 Processing {len(renames)} Renames...")
        for item in renames:
            # Normalize slashes
            old_rel = item["current_path"].replace("/", os.sep).replace("\\", os.sep)
            new_rel = item["new_path"].replace("/", os.sep).replace("\\", os.sep)
            
            # Find the actual source file
            source_path = find_real_path(VAULT_ROOT, old_rel)

            if source_path:
                # Construct destination path (keeping the same directory as the source)
                # We trust the source directory structure over the LLM's folder guess
                source_dir = os.path.dirname(source_path)
                new_filename = os.path.basename(new_rel)
                dest_path = os.path.join(source_dir, new_filename)

                try:
                    shutil.move(source_path, dest_path)
                    print(f"✅ RENAMED: {os.path.basename(source_path)} -> {new_filename}")
                except Exception as e:
                    print(f"❌ FAILED: {old_rel} -> {e}")
            else:
                print(f"⚠️  SKIP: Could not find file '{os.path.basename(old_rel)}' anywhere in vault.")

    # 2. GENERATE TODO LIST
    critical = report.get("critical_fixes", [])
    gaps = report.get("content_gaps", [])
    
    if critical or gaps:
        todo_path = os.path.join(VAULT_ROOT, "VAULT_FIX_TODO.md")
        print(f"\n📝 Generating To-Do List: {todo_path}")
        
        with open(todo_path, "w", encoding="utf-8") as f:
            f.write("# 🛡️ Vault Audit To-Do List\n")
            f.write("> **Tip:** Click the file paths below to open them in Obsidian.\n\n")
            
            if critical:
                f.write("## 🔴 Critical Schema Fixes\n")
                for item in critical:
                    f.write(f"- [ ] [[{os.path.basename(item.get('file_path', ''))}]]\n")
                    f.write(f"    - **Issue:** {item.get('issue')}\n")
                    f.write(f"    - **Fix:** `{item.get('suggested_fix')}`\n")
                f.write("\n")
            
            if gaps:
                f.write("## 🟡 Content Gaps\n")
                for item in gaps:
                    f.write(f"- [ ] [[{os.path.basename(item.get('file_path', ''))}]]\n")
                    f.write(f"    - **Details:** {item.get('details')}\n")
                    
        print("✅ To-Do List Created.")

if __name__ == "__main__":
    apply_fixes()