import re
import json
from pathlib import Path

def load_mechanics_dictionary(dictionary_path: str = "automation/dictionary/mechanics.json") -> dict:
    """Loads the term-to-URL dictionary."""
    path = Path(dictionary_path)
    if not path.exists():
        print(f"Warning: Mechanics dictionary not found at {dictionary_path}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error loading mechanics dictionary: {e}")
        return {}

def inject_external_links(text: str, dictionary_path: str = "automation/dictionary/mechanics.json") -> str:
    """
    Scans text for terms in the mechanics dictionary and replaces the first match
    with a Markdown external link [Term](URL), avoiding existing links.
    """
    mechanics = load_mechanics_dictionary(dictionary_path)
    if not mechanics:
        return text

    # Sort items by key length descending so longer phrases match before shorter substrings
    sorted_items = sorted(mechanics.items(), key=lambda item: len(item[0]), reverse=True)

    for term, url in sorted_items:
        # Regex explanation:
        # Lookbehind (?<!\[) ensures we don't re-link terms already inside [[...]] or [...]
        # \b ensures word boundaries so "hellish" doesn't match inside a larger word
        pattern = re.compile(rf'(?<!\[)\b({re.escape(term)})\b(?!\])', re.IGNORECASE)
        
        # Replace only the first occurrence
        def replace_match(match):
            original_casing = match.group(1)
            return f"[{original_casing}]({url})"

        text, count = pattern.subn(replace_match, text, count=1)

    return text

if __name__ == "__main__":
    # Sanity unit test
    sample_text = "Theren cast hellish rebuke and then used hideous laughter on the bandit."
    result = inject_external_links(sample_text)
    
    print("Original:", sample_text)
    print("Linked:  ", result)
    
    assert "[hellish rebuke](https://5e.tools/spells.html#hellish%20rebuke_phb)" in result
    assert "[hideous laughter](https://5e.tools/spells.html#tasha's%20hideous%20laughter_phb)" in result
    print("✅ External link injection unit test passed!")