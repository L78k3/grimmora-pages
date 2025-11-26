# Entity Update Workflow

## Purpose
This document outlines the process for updating Entity pages (NPCs, Items, Locations, Organizations) using the narrative context from the Chronicles.

---

## 1. The Strategy
We use different methods depending on the entity type and your preference for file handling.

### Method A: The "Full File" Update (Highest Accuracy)
**Best for:** Complex lore, emotional beats, intricate scenes.
**Concept:** Identify which entries matter, then upload those full files.

1.  **Identify Mentions:**
    Use `grep -l` (list filenames only) to see which files contain the target.
    ```bash
    grep -l "ring" content/Campaigns/Campaign\ 1/Chronicles/*.md
    ```
2.  **Action:** Upload the **Current Entity File** and the specific **Chronicle Files** identified above.
3.  **Prompt:** "Update the attached entity page using the full context found in the attached chronicle entries."

### Method B: The "Grep Dump" Update (Fastest / Low Token)
**Best for:** Simple Items, Merchants, Fact-checking.
**Concept:** Extract *only* the relevant paragraphs into a single text file to save upload slots.

1.  **Create Context File:**
    Use `grep` with the `-C` flag (Context) to capture the narrative around the keyword. **Do not use standard grep**, or you will lose the story.
    ```bash
    # Capture 20 lines of context around the search term
    grep -C 20 "search term" content/Campaigns/Campaign\ 1/Chronicles/*.md > ~/grepOutputs/EntityContext.txt
    ```
2.  **Action:** Upload the **Current Entity File** and `EntityContext.txt`.
3.  **Prompt:**
    > "I have attached a text file (`EntityContext.txt`) containing grep extracts from my chronicles. Please read these extracts to understand the history and usage of [Entity Name]. Update the attached entity page with this new information."

### Method C: Concatenation Strategy (Main Characters)
**Best for:** Lavender, Gage, The Tavern (Hubs).
**Concept:** Create a Master File of *everything*.

1.  **Create Master File:**
    ```bash
    cat content/Campaigns/Campaign\ 1/Chronicles/*.md > All_Chronicles_Temp.txt
    ```
2.  **Action:** Upload **Character Page** and `All_Chronicles_Temp.txt`.
3.  **Prompt:** "Read the master chronicle file. Extract the complete arc for [Character Name] and update their page."

---

## 2. Routine Maintenance: Adding a New Chronicle
When a new session finishes (`Entry 37.md`):

1.  **Standardize:** Upload `Entry 37.md` + `Conversion-Workflow-Reference.md` to fix YAML and Links.
2.  **Ripple Update:** If a specific item was heavily used in this entry, use **Method A** (uploading just Entry 37 and the Item page) to update it immediately.