# Location Conversion Workflow Reference

## Context

This is a PC-facing D&D vault for a campaign in Grimmora, published with Quartz v4. The vault documents our party's journey from the player character perspective (specifically Gage's view), so it only contains information the PCs would know.

## Vault Setup

- **Platform:** Obsidian with Quartz v4 publishing
    
- **Quartz Version:** 4.5.0
    
- **Base URL:** [https://l78k3.github.io/grimmora-pages](https://l78k3.github.io/grimmora-pages)
    
- **Perspective:** Player-facing (not DM notes)
    

## File Paths

### Windows Format

```
C:\Users\SyncthingServiceAcct\DnD\Documents\DnD\dnd\quartz\content\
```

### WSL Format

```
/mnt/c/Users/SyncthingServiceAcct/DnD/Documents/DnD/dnd/quartz/content/
```

### Relative Paths (from content/)

All paths below use relative format from the `content/` directory.

## Folder Structure

```
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
│       │   │       ├── GageGreenGatherSheet20231024.pdf
│       │   │       ├── GageGreenGatherSheet20240323.pdf
│       │   │       ├── GageGreenGatherSheet20250423.pdf
│       │   │       └── character-0.1.pdf
│       │   ├── Lavender
│       │   │   ├── Lavender.md
│       │   │   └── b. Inventory.md
│       │   ├── Marianne.md
│       │   ├── Temerity.md
│       │   └── Theren.md
│       ├── Chronicles
│       │   ├── Entry 1.md
│       │   ├── Entry 10.md
│       │   ├── Entry 11.md
│       │   ├── Entry 12.md
│       │   ├── Entry 13.md
│       │   ├── Entry 14.md
│       │   ├── Entry 15.md
│       │   ├── Entry 16.md
│       │   ├── Entry 17.md
│       │   ├── Entry 18.md
│       │   ├── Entry 19.md
│       │   ├── Entry 2.md
│       │   ├── Entry 20.md
│       │   ├── Entry 21.md
│       │   ├── Entry 22.md
│       │   ├── Entry 23.md
│       │   ├── Entry 24.md
│       │   ├── Entry 25.md
│       │   ├── Entry 26.md
│       │   ├── Entry 27.md
│       │   ├── Entry 28.md
│       │   ├── Entry 29.md
│       │   ├── Entry 3.md
│       │   ├── Entry 30.md
│       │   ├── Entry 31.md
│       │   ├── Entry 32.md
│       │   ├── Entry 33.md
│       │   ├── Entry 4.md
│       │   ├── Entry 5.md
│       │   ├── Entry 6.md
│       │   ├── Entry 7.md
│       │   ├── Entry 8.md
│       │   └── Entry 9.md
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
│       │   ├── Auril.md
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
│           ├── Session 20231228.md
│           ├── Session 20240104.md
│           ├── Session 20240210.md
│           ├── Session 20240323.md
│           ├── Session 20240330.md
│           ├── Session 20240406.md
│           ├── Session 20240527.md
│           ├── Session 20240608.md
│           ├── Session 20240629.md
│           ├── Session 20240720.md
│           ├── Session 20240727.md
│           ├── Session 20240803.md
│           ├── Session 20240831.md
│           ├── Session 20241026.md
│           ├── Session 20241228.md
│           └── Session 20250215.md
├── Character Creation Guidelines Uwendale Military Outpost.md
├── GM-Only
│   ├── GM Tools
│   │   ├── Quick References
│   │   └── Random Tables
│   ├── Session Prep
│   │   └── Session Prep for Uwendale Oneshot.md
│   ├── Uwendale
│   │   ├── 00 Morning at Uwendale.md
│   │   ├── 01 Farm Assault or Border Intrigue.md
│   │   ├── 02-a Defend Farm, Discover Kidnapping.md
│   │   ├── 02-b Investigate Agents, Learn of Cave.md
│   │   ├── 03 Track to mountain cave.md
│   │   ├── 04 Cave Exploration & Rescue.md
│   │   └── Encounter Chart.canvas
│   └── World Secrets
│       └── Valoran
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
│       ├── Location - Region.md
│       ├── Location - Town.md
│       ├── Location - Village.md
│       ├── Location.md
│       ├── NPC.md
│       ├── Ongoing Thread.md
│       ├── Quest.md
│       └── Session.md
├── Uwendale
│   ├── Characters
│   │   ├── HalTorrendall.pdf
│   │   ├── SunTzu.pdf
│   │   └── liraDewcap.pdf
│   └── Some content idk.md
├── World
│   ├── Grimmora
│   │   ├── Abilities
│   │   │   ├── confoundment spell.md
│   │   │   └── hideous laughter.md
│   │   ├── Concepts
│   │   │   ├── Ice Wolves.md
│   │   │   ├── Lady Rose.md
│   │   │   ├── Pellor.md
│   │   │   ├── Pseudodragon.md
│   │   │   ├── Snow-Blindness.md
│   │   │   ├── The Curse.md
│   │   │   ├── The Gladiator Wight.md
│   │   │   ├── dimensional sucker.md
│   │   │   ├── dryads.md
│   │   │   ├── eladrin.md
│   │   │   ├── griffin.md
│   │   │   ├── half-orc.md
│   │   │   ├── hellish rebuke.md
│   │   │   ├── hellish-rebuke.md
│   │   │   ├── moon elf.md
│   │   │   ├── necromancers.md
│   │   │   ├── spectres.md
│   │   │   └── tiefling.md
│   │   ├── Items
│   │   │   ├── Auril's Wall.md
│   │   │   ├── Blue Communication Stone.md
│   │   │   ├── Crystal Orbs.md
│   │   │   ├── Dragon Meat.md
│   │   │   ├── Potion of Fire Breathing.md
│   │   │   ├── crossbow.md
│   │   │   ├── health potions.md
│   │   │   ├── scrying pool.md
│   │   │   └── teleportation rune.md
│   │   ├── Locations
│   │   │   ├── Buildings
│   │   │   │   ├── Auril's Church.md
│   │   │   │   ├── Golden Griffin.md
│   │   │   │   ├── Jade Zephyr Casino.md
│   │   │   │   ├── North City Gate.md
│   │   │   │   ├── Rotunda.md
│   │   │   │   ├── The Tavern.md
│   │   │   │   ├── mage's tower.md
│   │   │   │   ├── monastery.md
│   │   │   │   └── temple.md
│   │   │   ├── Cities
│   │   │   │   ├── Arcadia.md
│   │   │   │   ├── Avalon.md
│   │   │   │   ├── Bridgeport.md
│   │   │   │   └── Durvish City.md
│   │   │   ├── Districts
│   │   │   │   └── elvish quarter.md
│   │   │   ├── Dungeons-and-Lairs
│   │   │   │   ├── Dragon's Nest.md
│   │   │   │   ├── Orris' Secret Lair.md
│   │   │   │   ├── The Gladiator's Amphitheatre.md
│   │   │   │   ├── The Trial Chamber.md
│   │   │   │   └── Vampire Mansion.md
│   │   │   ├── Landmarks
│   │   │   │   ├── Alpine Forest.md
│   │   │   │   ├── Court of Flowers.md
│   │   │   │   ├── Court of Summer and Winter.md
│   │   │   │   └── fey realm.md
│   │   │   ├── Maps
│   │   │   │   ├── GRIMMORA_UPDATED.jpg
│   │   │   │   └── Maps.canvas
│   │   │   ├── Towns
│   │   │   │   ├── Bremen.md
│   │   │   │   ├── Durendal.md
│   │   │   │   ├── Frostpeak Pass.md
│   │   │   │   └── Mightrest.md
│   │   │   └── Villages
│   │   │       ├── Midward.md
│   │   │       └── Pinechill.md
│   │   ├── Organizations
│   │   │   ├── House Locke.md
│   │   │   ├── The Order of the Ancient Fable.md
│   │   │   └── The Order.md
│   │   ├── Regions
│   │   │   ├── Avalonean Empire.md
│   │   │   └── The Frost.md
│   │   └── grimmora-index.md
│   └── Valoran
│       ├── Abilities
│       ├── Concepts
│       ├── Items
│       │   └── petricite.md
│       ├── Locations
│       │   ├── Demacia.md
│       │   ├── Demacian Capital.md
│       │   ├── Maps
│       │   ├── Noxus.md
│       │   ├── The Freljord.md
│       │   └── Uwendale.md
│       └── Organizations
├── assets
│   ├── City_of_Avalon.jpg
│   └── GRIMMORA_UPDATED.jpg
├── attachments
│   ├── 1zp0i32g 1.webp
│   ├── 1zp0i32g 2.webp
│   ├── 1zp0i32g 3.webp
│   ├── 1zp0i32g 4.webp
│   ├── 1zp0i32g 5.webp
│   ├── 1zp0i32g 6.webp
│   ├── 1zp0i32g.webp
│   ├── GRIMMORA_UPDATED.jpg
│   ├── icon.webp
│   └── iconRetry.jpg
├── campaign_outputs
│   └── Campaign_1.txt
├── content-README.md
└── index.md

50 directories, 234 files

```

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

### 1. YAML Frontmatter

Every location needs proper frontmatter:

YAML

```
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

### 2. Status Callouts

Use callouts to indicate visit status:

**For visited locations:**

Markdown

```
> [!info] Visited
> **When:** [[Entry X]] or session reference
> **Region:** [[Region Name]]
```

**For unvisited locations:**

Markdown

```
> [!warning] Unvisited
> The party has not yet traveled to this location.
```

**For dangerous locations:**

Markdown

```
> [!danger] Danger Level
> Brief warning about threats
```

### 3. Content Guidelines

- Only include information the PCs would know
    
- Write from party perspective ("we", "our")
    
- Reference chronicle entries when describing events
    
- Use wikilinks for all related content: [[Location]], [[NPC]], [[Item]]
    
- Include "Our Experience" section for visited locations
    
- Leave sections empty rather than inventing information
    

### 4. Standard Sections

Most locations should have:

- **Overview** - General description
    
- **Geography** - Physical location, climate, terrain
    
- **Points of Interest** - Key locations within
    
- **Notable NPCs** - People encountered
    
- **History** - Background information (if known)
    
- **Travel Connections** - How it connects to other places
    
- **Our Experience** - What happened during visits
    
- **Related links at bottom** - Cross-references
    

### 5. Linking Format

- Use simple wikilinks: [[Page Name]]
    
- For display text: [[Page Name|Display Text]]
    
- Quartz with ObsidianFlavoredMarkdown handles path resolution
    
- Images: Use ![[image-name.jpg]] for Obsidian-style embeds
    

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

### ✅ Completed Categories

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

- [x] Auril's Church.md
    
- [x] Golden Griffin.md
    
- [x] Jade Zephyr Casino.md
    
- [x] North City Gate.md
    
- [x] Rotunda.md (Corrected from duplicate)
    
- [x] The Tavern (Mightrest).md (Renamed from The Tavern.md)
    
- [x] Village Inn.md (Processed - marked for deletion as duplicate)
    
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
    
- [x] big house.md (Processed - marked for deletion as duplicate)
    

## Workflow Pattern

This is the workflow that works well:

1. **Start with a category** (e.g., "Let's do Buildings")
    
2. AI asks for file content:
   ```
   bash cat content/World/Grimmora/Locations/Buildings/Building-Name.md
   ```
3. **User pastes the file content**
    
4. **AI converts to template format** with proper frontmatter and structure
    
5. **User copies result back to file**
    
6. **Move to next file in category**
    
7. **Repeat until category complete**
    

### Tips for Efficiency

- Do entire categories at once (all Cities, all Towns, etc.)
    
- If a file has no content, AI can check chronicle entries:
    
        bash     grep -C 3 -r "LocationName" content/Campaigns/Campaign\ 1/Chronicles/    
    
- For images, use ![[image.jpg]] format with files in appropriate folders
    
- Keep a running checklist and update after each session
    

## Technical Notes

### Quartz Configuration

- Plugin.ObsidianFlavoredMarkdown() - Handles wikilinks
    
- Plugin.Assets() - Copies images during build
    
- baseUrl: "[https://l78k3.github.io/grimmora-pages](https://l78k3.github.io/grimmora-pages)"
    

### Image Paths

Images work best when:

- Placed in a dedicated location (like `content/assets/`)
    
- Referenced with wikilink syntax: ![[image.jpg]]
    
- Quartz resolves paths automatically during build
    

### Building & Testing

Bash

```
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

Bash

```
find content/World/Grimmora/Locations -name "*.md"
```

**Search content:**

Bash

```
grep -r "search term" content/Campaigns/Campaign\ 1/Chronicles/
```

**List directory:**

Bash

```
ls content/World/Grimmora/Locations/Cities/
```

## Resuming in a New Chat

To resume this workflow in a new chat session:

1. Provide context:
    
        - "I'm organizing a D&D campaign vault in Obsidian published with Quartz v4"
    
        - "I need help converting location files to standardized templates"
    
2. Share this reference file:
    
        - Copy/paste this entire file, OR
    
        - Provide the path and ask AI to read it
    
3. State current progress:
    
        - "I've completed Cities, Towns, Villages, and Landmarks"
    
        - "Next I need to do Buildings (10 files)"
    
4. Request to continue:
    
        - "Can you help me convert the Buildings category using the same workflow?"
    
5. AI will ask for first file:
    
        bash     cat content/World/Grimmora/Locations/Buildings/FirstBuilding.md    
    

## Party Members (for reference)

- [[Gage]]
    
- [[Lavender]]
    
- [[Temerity]]
    
- [[Theren]]
    
- [[Marianne]]
    
- [[Anaphel]] - Joined in Pinechill
    

## Key NPCs & Concepts

- [[Lady Bromelia]] - Kidnapping started our quest
    
- [[Halsin]] - Druid leader in Avalon
    
- [[Summer]] and [[Winter]] - Fey court rulers
    
- [[Vampire Lord]] - Defeated in Mightrest
    
- [[necromancers]] - Occupy Arcadia
    
- [[Ice Wolves]] - Threat in Alpine Forest
    

---

Last Updated: October 25, 2025

Next Category: All location categories complete. Next step: YAML refactoring of Chronicles.