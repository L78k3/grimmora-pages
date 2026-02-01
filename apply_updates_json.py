import os
import json

# CONFIGURATION
STAGING_FILE = "_staging.json"
VAULT_ROOT = os.getcwd()

def apply_updates():
    print(f"🔍 Reading structured updates from {STAGING_FILE}...")
    
    if not os.path.exists(STAGING_FILE):
        print(f"❌ Error: {STAGING_FILE} not found.")
        return

    try:
        with open(STAGING_FILE, "r", encoding="utf-8") as f:
            updates = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON Error: The LLM output was not valid JSON.\nDetails: {e}")
        return

    print(f"found {len(updates)} updates to apply.\n")

    for item in updates:
        # Normalize path
        raw_path = item.get("path", "")
        clean_path = raw_path.strip().replace("/", os.sep).replace("\\", os.sep)
        full_path = os.path.join(VAULT_ROOT, clean_path)
        
        # Content to write
        text_content = item.get("content", "")
        mode = item.get("mode", "append")

        # Security check
        if VAULT_ROOT not in os.path.abspath(full_path):
            print(f"🚫 SKIPPING unsafe path: {clean_path}")
            continue

        try:
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            if mode == "create" or not os.path.exists(full_path):
                with open(full_path, "w", encoding="utf-8") as target:
                    target.write(text_content)
                print(f"✨ CREATED: {clean_path}")
            
            elif mode == "append":
                with open(full_path, "a", encoding="utf-8") as target:
                    # Ensure we start on a new line
                    target.write(f"\n{text_content}")
                print(f"✅ APPENDED: {clean_path}")

        except Exception as e:
            print(f"❌ FAILED: {clean_path} | {e}")

    print("\nDone!")

if __name__ == "__main__":
    apply_updates()