# ⚔️ Session Morning SOP: Vault Integration

This Standard Operating Procedure (SOP) documents the transformation of raw session notes into structured campaign lore to maintain the "Gage Perspective" across the Grimmora wiki.

---

## 📋 Prompt Reference Table

| Step | Goal | Prompt File |
| :--- | :--- | :--- |
| **1. Transform** | Raw prose to structured `.md` | `Chronicle-Architect-Prompt.md` |
| **2. Scout** | Identify changed world entities | `Scout-Prompt.md` |
| **3. Architect** | Generate JSON update data | `Architect-Prompt.md` |
| **4. Forge** | Build new dedicated lore pages | `Entity-Extractor.md` |
| **5. Refine** | Formatting and bio overhauls | `Wikilink-Spotter.md` / `Grand-Biographer.md` |

---

## 🛠️ The Workflow

### Phase 1: Chronicle Transformation (Workflow H)
**Goal:** Create a structured record of the session for Quartz export.
1. **Source:** Upload the raw narrative log (e.g., `DnD 39.docx`).
2. **Execute:** Paste the **Chronicle Architect Prompt**.
3. **Vault Update:** - Save the output as `Campaigns/Campaign 1/Chronicles/Entry XX.md`.
   - **Crucial:** Copy the "Phase 4 Snapshot" to your `generate_context.sh` script to orient future AI sessions.

### Phase 2: The Wiki Scout (Workflow B)
**Goal:** Determine which specific files need technical updates.
1. **Action:** Run `contextbomb` in the terminal to refresh `Vault_Context.txt`.
2. **Execute:** Upload the new `Entry XX.md` and `Vault_Context.txt`. Paste the **Scout Prompt**.
3. **Outcome:** Use the provided terminal command to gather existing files and identify any "New Files" that lack pages.

### Phase 3: The Vault Architect (Workflow A)
**Goal:** Perform non-destructive updates to existing NPCs, Items, and Locations.
1. **Action:** Run the `gather` command from the Scout.
2. **Execute:** Upload the target entity files and the new Chronicle. Paste the **Architect Prompt**.
3. **Script Execution:**
   - Copy the JSON output to `update.json`.
   - Run `python generate_pages.py`.
   - **Verification:** Ensure bullets were appended to standard headers like `## History` or `## Lore`.

### Phase 4: Lore Forging (Workflow I)
**Goal:** Create dedicated wiki pages for brand-new entities.
1. **Action:** For each new entity, upload the Chronicle and paste the **Entity Extractor Prompt**.
2. **Execute:** Populate the YAML frontmatter and headings based on the provided System Templates.

---

## 🧹 Maintenance & Refinement

- **Wikilink Cleanup (Method F):** If links are missing, run the **Wikilink Spotter Prompt** to highlight proper nouns matching your manifest.
- **Major NPC Overhaul (Workflow G):** For NPCs with 3+ entries, use the **Grand Biographer Prompt** to generate a comprehensive "Gage Standard" biography.
- **Vault Audit (Workflow J):** Run the **Vault Auditor Prompt** to find "Ghost References" (untracked entities) or dead links.

---

## 💻 Terminal Command Cheat Sheet

| Command                    | Purpose                                                   |
| :------------------------- | :-------------------------------------------------------- |
| `contextbomb`              | Refresh the master context archive (`Vault_Context.txt`). |
| `python generate_pages.py` | Execute automated updates from `update.json`.             |
| `git diff`                 | Verify modifications before committing.                   |