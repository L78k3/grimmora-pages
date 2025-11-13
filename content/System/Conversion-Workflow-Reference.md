# Location Conversion Workflow Reference

## Context

This is a PC-facing D&D vault for a campaign in Grimmora, published with Quartz v4. The vault documents our party's journey from the player character perspective (specifically Gage's view), so it only contains information the PCs would know.

## Vault Setup

-   **Platform:** Obsidian with Quartz v4 publishing
-   **Quartz Version:** 4.5.0
-   **Base URL:** https://l78k3.github.io/grimmora-pages
-   **Perspective:** Player-facing (not DM notes)
-   **Language:** British English (e.g., *amphitheatre*, *armour*, *centre*)

## Folder Structure & File Manifest

This tree represents the current state of the vault. Use this to check if a page exists before suggesting a new one.

```text
content
├── Campaigns
│   └── Campaign 1
│       ├── Characters
│       │   ├── GageGreengather
│       │   │   ├── Allies & Rivals.md
│       │   │   ├── Gage.md
│       │   │   ├── Inventory.md
│       │   │   ├── Ongoing Threads.md
│       │   │   ├── Personal Quests.md
│       │   │   └── Sheet Archives
│       │   ├── Lavender
│       │   │   ├── Lavender.md
│       │   │   └── b. Inventory.md
│       │   ├── Marianne.md
│       │   ├── Temerity.md
│       │   └── Theren.md
│       ├── Chronicles
│       │   ├── Entry 1.md ... Entry 36.md
│       ├── Events
│       │   ├── Battle at the Big House.md
│       │   ├── Dragon Battle.md
│       │   ├── Gnome Confrontation.md
│       │   ├── Magical Plague.md
│       │   ├── Plague Investigation.md
│       │   ├── The Trial of the Gladiator.md
│       │   └── Vampire Defeat.md
│       ├── NPCs
│       │   ├── Anaphel.md
│       │   ├── Auriel.md
│       │   ├── Aurius.md
│       │   ├── Bracken.md
│       │   ├── Brian.md
│       │   ├── Captain Arran.md
│       │   ├── Cella.md
│       │   ├── Corvus.md
│       │   ├── Dave.md
│       │   ├── First Fist.md
│       │   ├── Florian.md
│       │   ├── Gnome Cook.md
│       │   ├── Gorg.md
│       │   ├── Guardsman Floyd.md
│       │   ├── Guido.md
│       │   ├── Halsin.md
│       │   ├── Ice Dragon.md
│       │   ├── Ismay.md
│       │   ├── Korako.md
│       │   ├── Lady Arren.md
│       │   ├── Lady Bromelia.md
│       │   ├── Lord Requiem.md
│       │   ├── Mavis.md
│       │   ├── Millicent.md
│       │   ├── Orion.md
│       │   ├── Requiem la Rouge.md
│       │   ├── Rowan.md
│       │   ├── Runcible.md
│       │   ├── Summer.md
│       │   ├── The Alchemist.md
│       │   ├── The Clothier.md
│       │   ├── Vampire Lord.md
│       │   ├── Wild Wanderer.md
│       │   ├── Winter.md
│       │   ├── Zadhir.md
│       │   ├── bandit captain.md
│       │   ├── bandits.md
│       │   ├── grand cleric.md
│       │   └── hag.md
│       └── Sessions
│           ├── Session 20231228.md ...
├── Reference
│   ├── Assassin.md
│   ├── Gloom Stalker.md
│   └── Quick Reference.md
├── System
│   ├── Conversion-Workflow-Reference.md
│   ├── Queries
│   │   ├── Allies.md
│   │   ├── Inventory.md
│   │   ├── Ongoing Threads.md
│   │   └── Quests.md
│   └── Templates
│       ├── Character.md
│       ├── Chronicle.md
│       ├── Core Framework.md
│       ├── Item.md
│       ├── Location - Building.md
│       ├── Location - City.md
│       ├── Location - District.md
│       ├── Location - Dungeon.md
│       ├── Location - Landmark.md
│       ├── Location.md
│       ├── Location - Region.md
│       ├── Location - Town.md
│       ├── Location - Village.md
│       ├── NPC.md
│       ├── Ongoing Thread.md
│       ├── Quest.md
│       └── Session.md
└── World
    ├── Grimmora
    │   ├── Abilities
    │   │   ├── confoundment spell.md
    │   │   └── hideous laughter.md
    │   ├── Concepts
    │   │   ├── dimensional sucker.md
    │   │   ├── dryads.md
    │   │   ├── eladrin.md
    │   │   ├── griffin.md
    │   │   ├── half-orc.md
    │   │   ├── hellish rebuke.md
    │   │   ├── hellish-rebuke.md
    │   │   ├── Ice Wolves.md
    │   │   ├── Lady Rose.md
    │   │   ├── moon elf.md
    │   │   ├── necromancers.md
    │   │   ├── Pellor.md
    │   │   ├── Pseudodragon.md
    │   │   ├── Snow-Blindness.md
    │   │   ├── spectres.md
    │   │   ├── The Curse.md
    │   │   ├── The Gladiator Wight.md
    │   │   └── tiefling.md
    │   ├── Items
    │   │   ├── Auriel's Wall.md
    │   │   ├── Blue Communication Stone.md
    │   │   ├── crossbow.md
    │   │   ├── Crystal Orbs.md
    │   │   ├── Dragon Meat.md
    │   │   ├── health potions.md
    │   │   ├── Potion of Fire Breathing.md
    │   │   ├── scrying pool.md
    │   │   └── teleportation rune.md
    │   ├── Locations
    │   │   ├── Buildings
    │   │   │   ├── Auriel's Church.md
    │   │   │   ├── Golden Griffin.md
    │   │   │   ├── Jade Zephyr Casino.md
    │   │   │   ├── mage's tower.md
    │   │   │   ├── monastery.md
    │   │   │   ├── North City Gate.md
    │   │   │   ├── Rotunda.md
    │   │   │   ├── temple.md
    │   │   │   └── The Tavern.md
    │   │   ├── Cities
    │   │   │   ├── Arcadia.md
    │   │   │   ├── Avalon.md
    │   │   │   ├── Bridgeport.md
    │   │   │   └── Durvish City.md
    │   │   ├── Districts
    │   │   │   └── elvish quarter.md
    │   │   ├── Dungeons-and-Lairs
    │   │   │   ├── Dragon's Nest.md
    │   │   │   ├── Orris' Secret Lair.md
    │   │   │   ├── The Gladiator's Amphitheatre.md
    │   │   │   ├── The Trial Chamber.md
    │   │   │   └── Vampire Mansion.md
    │   │   ├── Landmarks
    │   │   │   ├── Alpine Forest.md
    │   │   │   ├── Court of Flowers.md
    │   │   │   ├── Court of Summer and Winter.md
    │   │   │   └── fey realm.md
    │   │   ├── Maps
    │   │   │   ├── GRIMMORA_UPDATED.jpg
    │   │   │   └── Maps.canvas
    │   │   ├── Towns
    │   │   │   ├── Bremen.md
    │   │   │   ├── Durendal.md
    │   │   │   ├── Frostpeak Pass.md
    │   │   │   └── Mightrest.md
    │   │   └── Villages
    │   │       ├── Midward.md
    │   │       └── Pinechill.md
    │   ├── Organizations
    │   │   ├── House Locke.md
    │   │   └── The Order of the Ancient Fable.md
    │   └── Regions
    │       ├── Avalonean Empire.md
    │       └── The Frost.md
    └── Valoran
        ├── Items
        │   └── petricite.md
        └── Locations
            ├── Demacia.md
            ├── Demacian Capital.md
            ├── Noxus.md
            ├── The Freljord.md
            └── Uwendale.md
````

## Template Locations

All templates are in: `content/System/Templates/`

  - **Location - City.md** - For major cities
  - **Location - Town.md** - For smaller towns
  - **Location - Village.md** - For small settlements
  - **Location - Building.md** - For inns, shops, temples, etc.
  - **Location - District.md** - For city districts/quarters
  - **Location - Dungeon.md** - For dungeons, lairs, caves, ruins
  - **Location - Landmark.md** - For forests, mountains, special locations
  - **Location - Region.md** - For large geographical regions

## Conversion Principles

### 1\. YAML Frontmatter

Every location needs proper frontmatter:

```yaml
---
title: Location Name
type: city/town/village/building/etc.
region: "[[Region Name]]"
population: ~X,XXX (if known)
tags:
  - location/type
  - region/name
  - visited OR unvisited
---
```

### 2\. Status Callouts

Use callouts to indicate visit status:

**For visited locations:**

```markdown
> [!info] Visited
> **When:** [[Entry X]] or session reference
> **Region:** [[Region Name]]
```

**For unvisited locations:**

```markdown
> [!warning] Unvisited
> The party has not yet traveled to this location.
```

**For dangerous locations:**

```markdown
> [!danger] Danger Level
> Brief warning about threats
```

### 3\. Content Guidelines

  - Only include information the PCs would know
  - Write from party perspective ("we", "our")
  - Reference chronicle entries when describing events
  - Use wikilinks for all related content: `[[Location]]`, `[[NPC]]`, `[[Item]]`
  - Include "Our Experience" section for visited locations
  - Leave sections empty rather than inventing information

### 4\. Standard Sections

Most locations should have:

  - **Overview** - General description
  - **Geography** - Physical location, climate, terrain
  - **Points of Interest** - Key locations within
  - **Notable NPCs** - People encountered
  - **History** - Background information (if known)
  - **Travel Connections** - How it connects to other places
  - **Our Experience** - What happened during visits
  - **Related links at bottom** - Cross-references

### 5\. Linking Format

  - Use simple wikilinks: `[[Page Name]]`
  - For display text: `[[Page Name|Display Text]]`
  - Quartz with ObsidianFlavoredMarkdown handles path resolution
  - Images: Use `![[image-name.jpg]]` for Obsidian-style embeds

## Example Completed Files

### Best Examples by Category

**Cities:**

  - `World/Grimmora/Locations/Cities/Avalon.md` - Comprehensive city with districts
  - `World/Gymmora/Locations/Cities/Durvish City.md` - Quest starting location

**Towns:**

  - `World/Grimmora/Locations/Towns/Mightrest.md` - Detailed with quest resolution
  - `World/Grimmora/Locations/Towns/Frostpeak Pass.md` - Simple waystation

**Villages:**

  - `World/Grimmora/Locations/Villages/Pinechill.md` - Small settlement
  - `World/Grimmora/Locations/Villages/Midward.md` - Built from chronicle entries

**Landmarks:**

  - `World/Grimmora/Locations/Landmarks/fey realm.md` - Alternate dimension
  - `World/Grimmora/Locations/Landmarks/Alpine Forest.md` - Dangerous natural area

**Regions:**

  - `World/Grimmora/Regions/Avalonean Empire.md` - Major political region
  - `World/Grimmora/Regions/The Frost.md` - Harsh environmental region

## Current Progress

### ✔ Completed Categories

#### Regions (2/2)

  - [x] Avalonean Empire
  - [x] The Frost

#### Cities (4/4)

  - [x] Avalon
  - [x] Durvish City
  - [x] Arcadia
  - [x] Bridgeport

#### Towns (4/4)

  - [x] Durendal
  - [x] Frostpeak Pass
  - [x] Mightrest
  - [x] Bremen.md (Stub created)

#### Villages (2/2)

  - [x] Pinechill
  - [x] Midward

#### Landmarks (4/4)

  - [x] Alpine Forest
  - [x] Court of Flowers
  - [x] Court of Summer and Winter
  - [x] fey realm

#### Buildings (10/10)

  - [x] Auriel's Church.md
  - [x] Golden Griffin.md
  - [x] Jade Zephyr Casino.md
  - [x] North City Gate.md
  - [x] Rotunda.md
  - [x] The Tavern.md
  - [x] mage's tower.md
  - [x] monastery.md
  - [x] temple.md

#### Districts (1/1)

  - [x] elvish quarter.md

#### Dungeons-and-Lairs (6/6)

  - [x] Dragon's Nest.md
  - [x] Orris' Secret Lair.md
  - [x] The Gladiator's Amphitheatre.md
  - [x] The Trial Chamber.md
  - [x] Vampire Mansion.md

## Workflow Pattern

This is the workflow that works well:

1.  **Start with a category** (e.g., "Let's do Buildings")
2.  **AI asks for file content:**
    ```bash
    cat content/World/Grimmora/Locations/Buildings/Building-Name.md
    ```
3.  **User pastes the file content**
4.  **AI converts to template format** with proper frontmatter and structure
5.  **User copies result back to file**
6.  **Move to next file in category**
7.  **Repeat until category complete**

### Tips for Efficiency

  - Do entire categories at once (all Cities, all Towns, etc.)

  - If a file has no content, AI can check chronicle entries:

    ```bash
    grep -C 3 -r "LocationName" content/Campaigns/Campaign\ 1/Chronicles/
    ```

  - For images, use `![[image.jpg]]` format with files in appropriate folders

  - Keep a running checklist and update after each session

## Technical Notes

### Quartz Configuration

  - Plugin.ObsidianFlavoredMarkdown() - Handles wikilinks
  - Plugin.Assets() - Copies images during build
  - baseUrl: "https://l78k3.github.io/grimmora-pages"

### Image Paths

Images work best when:

  - Placed in a dedicated location (like `content/assets/`)
  - Referenced with wikilink syntax: `![[image.jpg]]`
  - Quartz resolves paths automatically during build

### Building & Testing

```bash
# Build for production
npx quartz build

# Test locally
npx quartz build --serve
# or
npx quartz serve

# Check version
npx quartz --version
```

### Common Commands

**Find files:**

```bash
find content/World/Grimmora/Locations -name "*.md"
```

**Search content:**

```bash
grep -r "search term" content/Campaigns/Campaign\ 1/Chronicles/
```

**List directory:**

```bash
ls content/World/Grimmora/Locations/Cities/
```

## Resuming in a New Chat

To resume this workflow in a new chat session:

1.  **Provide context:**
      - "I'm organizing a D\&D campaign vault in Obsidian published with Quartz v4"
      - "I need help converting location files to standardized templates"
2.  **Share this reference file:**
      - Copy/paste this entire file, OR
      - Provide the path and ask AI to read it
3.  **State current progress:**
      - "I've completed Cities, Towns, Villages, and Landmarks"
      - "Next I need to do Buildings (10 files)"
4.  **Request to continue:**
      - "Can you help me convert the Buildings category using the same workflow?"
5.  **AI will ask for first file:**
    ```bash
    cat content/World/Grimmora/Locations/Buildings/FirstBuilding.md
    ```

## Party Members (for reference)

  - [[Gage]]
  - [[Lavender]]
  - [[Temerity]]
  - [[Theren]]
  - [[Marianne]]
  - [[Anaphel]]

## Key NPCs & Concepts

  - [[Lady Bromelia]] - Kidnapping started our quest
  - [[Halsin]] - Druid leader in Avalon
  - [[Summer]] and [[Winter]] - Fey court rulers
  - [[Vampire Lord]] - Defeated in Mightrest
  - [[necromancers]] - Occupy Arcadia
  - [[Ice Wolves]] - Threat in Alpine Forest
  - [[Auriel]] - Goddess of Winter
  - [[Zadhir]] - Met at Jade Zephyr
  - [[Orris]] - Lavender's brother
  - [[Ismay]] - Mage in Durvish City
  - [[Gorg]] - Innkeeper in Mightrest
  - [[Korako]] - Temerity's rabbit
  - [[Runcible]] - Theren's pseudodragon
  - [[Chikatika]] - Temerity's raccoon familiar

-----

*Last Updated: Current Session*
*Next Category: All location categories complete. Next step: Chronicle Analysis (Entry 11 onwards).*