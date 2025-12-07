# Entity Update Workflow

## Purpose
This document outlines the process for updating Entity pages (NPCs, PCs, Items, Locations) using the **Automated Architect Pipeline**. It relies on the `generate_pages.py` script to perform non-destructive updates to your vault.

---

## 1. Prerequisites
Ensure you have these three components ready:
1.  **The Script:** `generate_pages.py` (Version 3) in your root folder.
2.  **The Prompt:** `System/Prompts/Architect-Prompt.md` (The Generic Version).
3.  **The Templates:** `NPC.md`, `Item.md`, `Ongoing Thread.md` (Standardized with `{{keys}}`).

---

## 2. The Workflows (Automated)

### Workflow A: The "Sniper" Update (Backfilling History)
**Best for:** Updating an existing NPC/Location with missed events from past sessions.
**Concept:** Use Obsidian's "Linked Mentions" to find relevant entries, then process them in a batch.

1.  **Identify Sources:** Open the target note (e.g., `Corbin.md`) and check **Backlinks**. Note which Entries mention him (e.g., `Entry 37`, `Entry 38`).
2.  **Gather Context:** Open a chat and upload:
    * The Target File (`Corbin.md`).
    * The Source Chronicles (`Entry 37.md`, `Entry 38.md`).
3.  **Prompt:** Paste the **Architect Prompt**.
    * *No extra typing needed. The prompt automatically detects the target and sources.*
4.  **Execute:**
    * Copy the JSON output to `update.json`.
    * Run: `python generate_pages.py`.
    * **Verify:** Check `git diff` to ensure history was appended correctly.

### Workflow B: The "New Session" Routine (Day-to-Day)
**Best for:** Processing the latest session (`Entry 38`) immediately after play.
**Concept:** The "Forward Only" approach.

1.  **Scout:** Paste `Entry 38` into a chat with the **Scout Prompt** (Optional) to identify which files need updating.
    * *Or just manually identify the key players (e.g., Gage, Corbin, The Sea Cave).*
2.  **Architect:** Upload the identified files + `Entry 38`. Run the **Architect Prompt**.
3.  **Execute:** Paste JSON to `update.json`, run script.

### Workflow C: The PC "Highlight Reel" (Main Characters)
**Best for:** Gage, Lavender, Theren.
**Concept:** We do *not* log every entry for PCs. We only log major character beats.

1.  **Target:** Update `Gage/Gage.md` (The Bio Module), *not* the Dashboard.
2.  **Prompt:** Use the Architect Prompt, but upload only the specific "Big Moment" entry.
3.  **Outcome:** The script appends a bullet to `## Biography` or `## Notable Exploits`.
    * *Example:* "Entry 38: Led the underwater escape."

---

## 3. Maintenance & Cleanliness

### The "Header Rule" (Critical)
The Python script looks for specific headers to append text. To ensure automation works, your existing files must use these standard headers:

| File Type | Standard Header | Script Behavior |
| :--- | :--- | :--- |
| **NPC** | `## History` | Appends narrative beats here. |
| **Location** | `## History` | Appends events that happened here. |
| **Item** | `## Lore` | Appends new owners or discoveries. |
| **PC (Bio)** | `## Biography` | Appends major life events. |

**Fix:** If you see `## Campaign Notes`, rename it to `## History` manually before running the script.

### The "Git Safety Net"
Always commit before running the script.

    git add .
    git commit -m "Pre-update state"
    python generate_pages.py
    # Check diffs. If good:
    git commit -am "Automated update from Entry 38"

---

## 4. Manual & Research Methods

### Method D: The "Grep Dump" (Deep Research)
**Best for:** Fact-checking a minor detail across 50 files without updating them.

1.  **Create Context File:**
    Use `grep` with context (`-C`) to capture the story around a keyword.
    
    grep -C 20 "Ring of Orris" content/Campaigns/Campaign\ 1/Chronicles/*.md > Context.txt
    
2.  **Action:** Upload `Context.txt` to the AI to answer specific questions ("When did we last use the Ring?").

### Method E: The "Context Bomb" (Full Arc Backfill)
**Best for:** Backfilling a main character with 20+ sessions of history at once.

1.  **Preparation:**
    * Run `contextbomb` in your terminal to generate `~/Vault_Context.txt`.
2.  **The Prompt:**
    * Open a new chat.
    * Upload `~/Vault_Context.txt`.
    * Copy/Paste the content of [[Context-Bomb-Prompt.md]].
    * *(Optional: Edit the "Target Character" line if backfilling someone else).*
3.  **Execution:**
    * Copy the markdown block from the AI response.
    * Paste it manually into the character's `Biography.md` or `index.md`.