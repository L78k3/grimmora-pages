import os
import json
from pathlib import Path
import yaml

def parse_frontmatter(file_path: Path) -> dict:
    """Extracts YAML frontmatter from a Markdown file."""
    try:
        content = file_path.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                data = yaml.safe_load(parts[1])
                return data if isinstance(data, dict) else {}
    except Exception as e:
        print(f"Warning: Could not parse frontmatter for {file_path}: {e}")
    return {}

def generate_manifest(content_dir: str = "content", output_path: str = "automation/manifest.json") -> dict:
    """
    Scans the content directory to auto-generate a fresh manifest of all canonical entities,
    aliases, and paths.
    """
    manifest = {
        "entities": [],
        "by_name": {},      # Normalized key -> entity entry
        "by_alias": {}      # Normalized alias -> canonical name
    }

    content_path = Path(content_dir)
    if not content_path.exists():
        raise FileNotFoundError(f"Content directory '{content_dir}' does not exist.")

    for root, _, files in os.walk(content_path):
        for file in files:
            if not file.endswith(".md"):
                continue

            file_path = Path(root) / file
            rel_path = file_path.relative_to(content_path).as_posix()
            
            # Skip system or non-content files
            if rel_path.startswith("System/"):
                continue

            stem = file_path.stem  # e.g. "Adalens" from "Adalens.md"
            frontmatter = parse_frontmatter(file_path)

            entity_type = frontmatter.get("type") or "unknown"
            
            # Safely handle aliases
            raw_aliases = frontmatter.get("aliases", [])
            if raw_aliases is None:
                aliases = []
            elif isinstance(raw_aliases, str):
                aliases = [raw_aliases]
            elif isinstance(raw_aliases, list):
                aliases = [str(a) for a in raw_aliases if a is not None]
            else:
                aliases = []

            # Safely handle canonical title fallback
            raw_title = frontmatter.get("title")
            if raw_title and str(raw_title).strip():
                canonical_name = str(raw_title).strip()
            else:
                canonical_name = stem

            entity_data = {
                "canonical_name": canonical_name,
                "filename": file,
                "relative_path": f"content/{rel_path}",
                "type": str(entity_type),
                "aliases": aliases
            }

            manifest["entities"].append(entity_data)

            # Map primary canonical name (lowercase)
            norm_name = canonical_name.lower().strip()
            manifest["by_name"][norm_name] = entity_data
            
            # Also map file stem if different
            norm_stem = stem.lower().strip()
            if norm_stem not in manifest["by_name"]:
                manifest["by_name"][norm_stem] = entity_data

            # Map aliases
            for alias in aliases:
                if alias and str(alias).strip():
                    norm_alias = str(alias).lower().strip()
                    manifest["by_alias"][norm_alias] = canonical_name

    # Write out manifest
    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    
    print(f"✅ Generated fresh manifest with {len(manifest['entities'])} entities at {output_path}")
    return manifest

if __name__ == "__main__":
    generate_manifest()