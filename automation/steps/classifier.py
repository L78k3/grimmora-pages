import json
from pathlib import Path
from automation.ollama_client import OllamaClient

def load_manifest(manifest_path: str = "automation/manifest.json") -> dict:
    path = Path(manifest_path)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"entities": [], "by_name": {}, "by_alias": {}}

def classify_entities(entities: list[dict], narrative_text: str, current_entry: str) -> dict:
    """
    Takes a list of entities (e.g., from linker.py), cross-references the manifest,
    and uses the LLM to classify existing entities as needing updates or not.
    """
    manifest = load_manifest()
    by_name = manifest.get("by_name", {})
    by_alias = manifest.get("by_alias", {})
    
    results = {
        "new": [],      # Needs page creation
        "updates": [],  # Existing, needs append
        "ignored": []   # Existing, passing mention
    }

    prompt_template = Path("automation/prompts/classifier.md").read_text(encoding="utf-8")
    client = OllamaClient()

    for entity in entities:
        # Resolve canonical name using the manifest
        raw_name = entity.get("canonical_name", "").strip()
        norm_name = raw_name.lower()
        
        canonical_name = None
        if norm_name in by_name:
            canonical_name = by_name[norm_name]["canonical_name"]
        elif norm_name in by_alias:
            canonical_name = by_alias[norm_name]

        if not canonical_name:
            results["new"].append(entity)
            continue

        # Entity exists. Check if significant via LLM.
        # Replace placeholders in prompt template
        prompt = prompt_template.replace("{entity_name}", canonical_name).replace("{text}", narrative_text)
        prompt = prompt.replace("[[Entry XX]]", f"[[{current_entry}]]")
        
        try:
            print(f"Asking LLM to classify existing entity: {canonical_name}...")
            response_text = client.generate(prompt=prompt)
            
            # Clean potential markdown wrapping from LLM output
            clean_json = response_text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            classification = json.loads(clean_json)

            if classification.get("classification") == "significant":
                results["updates"].append({
                    "canonical_name": canonical_name,
                    "summary": classification.get("summary", "")
                })
            else:
                results["ignored"].append(canonical_name)
                
        except Exception as e:
            print(f"⚠️ Error classifying {canonical_name}: {e}")
            # If LLM fails, default to ignoring to be safe, or handle via orchestrator
            results["ignored"].append(canonical_name)

    return results

if __name__ == "__main__":
    # Mock data to test the logic
    sample_text = "Gage walked through Durvish City without stopping. Later, he spoke with Lavender about the Grey Pearl, which began to glow ominously."
    
    mock_entities = [
        {"canonical_name": "Durvish City", "display_text": "Durvish City"},
        {"canonical_name": "Lavender", "display_text": "Lavender"},
        {"canonical_name": "Grey Pearl", "display_text": "Grey Pearl"},
        {"canonical_name": "Captain Voss", "display_text": "Captain Voss"} # Assume this isn't in manifest
    ]
    
    # We assume 'Entry 46' is the current entry
    print("Starting classification test...")
    results = classify_entities(mock_entities, sample_text, "Entry 46")
    
    print("\n=== CLASSIFICATION RESULTS ===")
    print(json.dumps(results, indent=2))