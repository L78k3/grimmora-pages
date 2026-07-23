import re
import json
import difflib
from pathlib import Path

def strip_wikilinks(text: str) -> str:
    """
    Strips Obsidian wikilink markup, restoring the underlying prose.
    - [[Canonical Page|Display Text]] -> Display Text
    - [[Canonical Page]] -> Canonical Page
    """
    # Replace piped wikilinks: [[Target|Display]] -> Display
    text = re.sub(r'\[\[[^\]\|]+\|([^\]]+)\]\]', r'\1', text)
    # Replace standard wikilinks: [[Target]] -> Target
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text

def verify_verbatim_prose(original_text: str, linked_text: str) -> tuple[bool, str]:
    """
    Compares original prose against stripped linked text.
    Returns (True, "") if identical, or (False, diff_summary) if drift occurred.
    """
    stripped = strip_wikilinks(linked_text)
    
    # Normalize Windows vs Unix line endings for diff
    norm_original = original_text.replace("\r\n", "\n").strip()
    norm_stripped = stripped.replace("\r\n", "\n").strip()

    if norm_original == norm_stripped:
        return True, ""

    # Generate diff report if failure occurs
    diff = list(difflib.ndiff(norm_original.splitlines(), norm_stripped.splitlines()))
    diff_report = "\n".join([line for line in diff if line.startswith('- ') or line.startswith('+ ')])
    return False, diff_report

def extract_first_mentions(linked_text: str) -> list[dict]:
    """
    Parses linked text and extracts all unique wikilinks created in this step.
    """
    pattern = r'\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]'
    matches = re.findall(pattern, linked_text)
    
    entities = []
    seen = set()
    for canonical, display in matches:
        target = canonical.strip()
        if target.lower() not in seen:
            seen.add(target.lower())
            entities.append({
                "canonical_name": target,
                "display_text": display.strip() if display else target
            })
    return entities

if __name__ == "__main__":
    # Sanity unit test for diff checker
    sample_original = "Then Gage spoke with Lady Rose near the docks."
    sample_valid_linked = "Then [[Gage]] spoke with [[Lavender|Lady Rose]] near the docks."
    sample_invalid_linked = "Then Gage talked to [[Lavender|Lady Rose]] near the docks." # Rephrased 'spoke with'

    valid_pass, _ = verify_verbatim_prose(sample_original, sample_valid_linked)
    invalid_pass, diff = verify_verbatim_prose(sample_original, sample_invalid_linked)

    print(f"Test Valid Link Pass: {valid_pass}")
    print(f"Test Invalid Drift Fail: {not invalid_pass}")
    if not invalid_pass:
        print(f"Diff detected correctly:\n{diff}")