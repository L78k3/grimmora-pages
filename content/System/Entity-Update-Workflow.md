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
**Best for:** Processing the latest session (`Entry 39`) immediately after play.

1.  **Preparation:**
    * Run `contextbomb` in your terminal to refresh `~/Vault_Context.txt`.
2.  **Scout:**
    * Open a new chat.
    * Upload **`Entry XX.md`** AND **`Vault_Context.txt`**.
    * Paste the **Scout Prompt**.
    * *Result: A checklist of "Existing Files" and "New Files".*
3.  **Architect:**
    * Open a **new** chat (to clear the heavy context).
    * Upload the **Target Files** identified by the Scout (e.g., `Corbin.md`, `Onasea.md`) plus `Entry XX.md`.
    * Paste the **Architect Prompt**.
4.  **Execute:** Paste JSON to `update.json`, run script.

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

```bash
git add .
git commit -m "Pre-update state"
python generate_pages.py
# Check diffs. If good:
git commit -am "Automated update from Entry 38"
```

---

## 4. Manual & Research Methods

### Method D: The "Grep Dump" (Deep Research)
**Best for:** Fact-checking a minor detail across 50 files without updating them.

1.  **Create Context File:**
    Use `grep` with context (`-C`) to capture the story around a keyword.
    
    ```bash
    grep -C 20 "Ring of Orris" content/Campaigns/Campaign\ 1/Chronicles/*.md > Context.txt
    ```
    
1.  **Action:** Upload `Context.txt` to the LLM to answer specific questions ("When did we last use the Ring?").

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
    * Copy the markdown block from the LLM response.
    * Paste it manually into the character's `Biography.md` or `index.md`.

### Method F: The "Wikilink Spotter" (Formatting Assistant)
**Best for:** Ensuring your manually formatted Chronicle Entry has the correct links before you finalize it.

1.  **Preparation:** Run `contextbomb` (alias for `~/scripts/generate_context.sh`) to refresh the vault index.
2.  **Prompt:**
    * Open a new chat. Upload `Vault_Context.txt` + Your formatted `Entry XX.md`.
    * Paste the **Wikilink Spotter Prompt** (`System/Prompts/Wikilink-Spotter.md`).
3.  **Action:**
    * The LLM provides a checklist of proper nouns found in your vault (e.g., "Link 'Corbin' in Section 2").
    * You manually bracket `[[Corbin]]` in Obsidian to preserve your specific formatting.

### Workflow G: The "Profile Builder" (NPC Overhaul)
**Best for:** Generating a full wiki page for a specific NPC (e.g., Anaphel) by analysing their entire history to determine if they are a "Major" or "Minor" character.

1.  **Preparation:**
    * Run `contextbomb` (alias for `~/scripts/generate_context.sh`) to ensure the Archives are up to date.
2.  **The Chat Setup:**
    * Open a new chat.
    * **Upload:** `Vault_Context.txt` (The History).
    * **Upload:** `Templates/NPC.md` (The Structure).
    * **Upload (Optional):** The existing file (e.g., `Anaphel.md`) if you want to preserve current metadata.
3.  **The Prompt:**
    * Paste the **Grand Biographer Prompt** (`System/Prompts/Grand-Biographer.md`).
    * **Edit the Target:** Change `[[TARGET_NAME]]` to the specific NPC (e.g., `[[Anaphel]]`).
4.  **The Result:**
    * The LLM will assess the NPC's importance based on their history.
    * It produces a single Markdown code block (either the full "Gage Standard" for major NPCs or a summarized version for minor ones).
    * Copy/Paste this block into the NPC's markdown file.

### Workflow H: The "Chronicle Transformation" (Post-Session)
**Best for:** Converting raw narrative logs from Discord into vault-ready entries for Quartz.
**Concept:** Structural cleanup and wikilink integration for consistency.

1.  **Identify Source:** Download the raw session narrative (e.g., `DnD 39.docx`).
2.  **Chat Setup:**
    * Open a new chat.
    * **Upload:** The raw narrative file.
3.  **Prompt:** Paste the **Chronicle Architect Prompt** (`System/Prompts/Chronicle-Architect.md`).
4.  **Execute:**
    * Copy the resulting Markdown into a new file: `Campaigns/Campaign 1/Chronicles/Entry XX.md`.
    * **Snapshot Update:** Copy the bullet points from **Phase 4** of the LLM response and paste them into the "SECTION 0" block of your `generate_context.sh` script to keep your "Now" data current.

### Workflow I: The "Lore Forge" (New Entity Creation)
**Best for:** Creating dedicated wiki pages for new NPCs, Items, or Locations discovered during a session (e.g., Captain Voss, The Tidecaller).
**Concept:** Maintaining standard schema across all lore pages using your templates.

1.  **Identify Source:** Use a finalized Chronicle Entry (e.g., `Entry 39.md`).
2.  **Preparation:** Run `contextbomb` to ensure the latest templates from **Section 1.5** are in your export file.
3.  **Chat Setup:**
    * Open a new chat.
    * **Upload:** `Vault_Context.txt` (This provides templates and the manifest).
    * **Upload:** The specific source **Chronicle Entry** where the entity appears.
4.  **Prompt:** Paste the **Entity Extractor Prompt** (`System/Prompts/Entity-Extractor.md`).
5.  **Execute:**
    * Create the new file (e.g., `NPCs/Captain Voss.md`).
    * **Verify:** Ensure the LLM matched the YAML and heading structure from your `System/Templates`.

### Workflow J: The "Vault Audit" (Lore Cleanup)
**Best for:** Ensuring no NPCs or Items from the Chronicles have been "lost" without dedicated files.
**Concept:** Cross-referencing the Narrative Source against the File Manifest.

1.  **Preparation:** Run `contextbomb` to generate the latest index of all existing files.
2.  **Chat Setup:** 
	* Open a new chat.
    * **Upload:** `Vault_Context.txt`.
3.  **Prompt:** Paste the **Vault Auditor Prompt** (`System/Prompts/Vault-Auditor.md`).
4.  **The Result:** 
	* A list of "Untracked Entities" (People/Items mentioned in Chronicles but missing from the Manifest).
    * A list of "Dead Links" (Proper nouns that should be wikilinked but aren't).
5.  **Action:** Use Workflow I to "Forge" the missing pages identified by the Auditor.


---

### Grimmora Prompt Index

| Prompt Name             | File Path                               | Primary Trigger                                | Best Workflow                                  |
| :---------------------- | :-------------------------------------- | :--------------------------------------------- | :--------------------------------------------- |
| **Chronicle Architect** | `System/Prompts/Chronicle-Architect.md` | New narrative log from Discord.                | **Workflow H**: Raw text to Obsidian Entry.    |
| **Entity Extractor**    | `System/Prompts/Entity-Extractor.md`    | A new NPC, Item, or Location is mentioned.     | **Workflow I**: Entry to dedicated Lore Page.  |
| **Architect Prompt**    | `System/Prompts/Architect-Prompt.md`    | Need to append new events to existing files.   | **Workflows A, B, C**: Automated updates.      |
| **Scout Prompt**        | `System/Prompts/Scout-Prompt.md`        | Preparing to process a session entry.          | **Workflow B**: Identifies what to update.     |
| **Vault Auditor**       | `System/Prompts/Vault-Auditor.md`       | Vault feels messy or links are missing.        | **Workflow J**: Narrative vs. Manifest audit.  |
| **Grand Biographer**    | `System/Prompts/Grand-Biographer.md`    | Major character needs a full history overhaul. | **Workflow G**: Comprehensive profile rebuild. |
| **Context Bomb**        | `System/Prompts/Context-Bomb-Prompt.md` | Need to catch an LLM up on a character's arc.  | **Method E**: Full history backfill.           |
| **Wikilink Spotter**    | `System/Prompts/Wikilink-Spotter.md`    | Finalizing a manually written Entry.           | **Method F**: Proper noun highlighting.        |
