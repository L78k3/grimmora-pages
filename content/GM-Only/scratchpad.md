

### Your New Master Prompt

Here is the **3-step prompt** for your new chat, designed for our staged loading process.

#### Step 1: Initialize & Load Reference + First Batch
*Paste this into the new chat and upload your new `Wikilink-Reference.md` and `Entry 1` to `Entry 5`.*

```markdown
Hello Gemini. I am organizing my D&D campaign vault and need you to act as a strict text processor. I have a large amount of context to provide, so I will upload it in batches.

**The Goal:**
Once all context is loaded, I will ask you to process **Entry 11** to identify missing wikilinks and potential new pages.

**Your Instructions for NOW:**
1.  Read the `Wikilink-Reference.md` (my file tree and entity list).
2.  Read `Entry 1` through `Entry 5` to learn the narrative and linking style.
3.  **Do not generate any analysis yet.** Just confirm you have received this batch and are ready for the next one.

**Critical Rules (Apply these to all future analysis):**
* **ZERO HALLUCINATION:** If it's not in the text, it doesn't exist.
* **CHECK THE TREE:** Use the Reference file to see if pages already exist.
* **NO REDUNDANCY:** Do not suggest links for terms already linked in the text.
* **LEAVE EXTERNAL LINKS ALONE:** Do not suggest changing external links (e.g., to `5e.tools`).
````

#### Step 2: Load Remaining Context

*Once the AI confirms Step 1, paste this prompt and upload `Entry 6` to `Entry 10`.*

```markdown
Here is the second batch of context: **Entry 6** through **Entry 10**.

**Instructions:**
1.  Ingest these files to complete your knowledge of the current narrative and established entities.
2.  **Do not generate analysis yet.**
3.  Confirm you have processed Entries 1-10 and are ready for the target file (Entry 11).
```

#### Step 3: Process Target Entry

*Once the AI confirms Step 2, paste this prompt and upload `Entry 11`.*

```markdown
I am now uploading the target file: **Entry 11.md**.

**Your Task:**
Based on the context you have learned (Reference + Entries 1-10), analyze **Entry 11** and provide two specific lists:

1.  **Suggested New Pages:** (Only if Entry 11 introduces a *major* new named entity that does not exist in the file tree).
2.  **Suggested Missing Wikilinks:** (Terms in the text that should be linked to existing pages, e.g., `[[Page Name|original text]]`).

**Remember:**
* Do not rewrite the entry.
* If an entry is perfect, just say "No changes needed."
* Do not suggest links for words that are already linked.
```

---

Hello Gemini. I am continuing a project to organize my D&D campaign vault and need you to act as a strict text processor.

**The Goal:**
I need to process **Entry 18**.

**Your Context (10 files):**
I am uploading 10 files. They are:
1.  `Wikilink-Reference.md`: This is my "Master Document." It contains my **full file manifest** (the tree) and **all my rules**.
2.  `Entry 9.md` through `Entry 17.md`: These are the **9 previous chronicle entries**. Use them to learn the immediate narrative context and linking style.

**Your Task:**
After you have analyzed all 10 context files, I will upload the target file: **Entry 18.md**.

You will then analyze **Entry 18** and provide two specific lists:

1.  **Suggested New Pages:**
    * Read the entry and identify important, unlinked entities (people, places, items, concepts) that are **not** in the `Wikilink-Reference.md` file manifest.
    * For each suggestion, **you must categorize it** based on my vault structure (e.g., `New NPC Page: [[Frolot]]`, `New Item Page: [[Sending Stone]]`, `New Concept Page: [[Zone of Truth]]`).

2.  **Suggested Missing Wikilinks:**
    * Identify terms in the text that are unlinked but *do* have an existing page in the file manifest.
    * Format them as `[[Page Name|original text]]`.

**Critical Rules (From the Reference File):**
* **ZERO HALLUCINATION:** If it's not written in the text, it doesn't exist.
* **CHECK THE TREE:** Use the file manifest in the Reference file to see if pages already exist.
* **NO REDUNDANCY:** Do not suggest links for terms already linked in the text.
* **LEAVE EXTERNAL LINKS ALONE:** Do not suggest changing external links (e.g., to `5e.tools`).
* **"NO CHANGES NEEDED" IS A VALID RESPONSE:** If an entry is perfect, just say so.

Please confirm when you have analyzed the 10 context files and are ready for me to upload **Entry 18**.