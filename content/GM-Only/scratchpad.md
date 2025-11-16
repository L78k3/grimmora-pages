

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