# Location Conversion Workflow Reference

## Context

This is a PC-facing D&D vault for a campaign in Grimmora, published with Quartz v4. The vault documents our party's journey from the player character perspective (specifically Gage's view), so it only contains information the PCs would know.

## Vault Setup

- **Platform:** Obsidian with Quartz v4 publishing
- **Quartz Version:** 4.5.0
- **Base URL:** https://l78k3.github.io/grimmora-pages
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
content/
├── World/
│   └── Grimmora/
│       ├── Locations/
│       │   ├── Cities/
│       │   ├── Towns/
│       │   ├── Villages/
│       │   ├── Buildings/
│       │   ├── Districts/
│       │   ├── Landmarks/
│       │   ├── Dungeons-and-Lairs/
│       │   └── Maps/
│       ├── Regions/
│       ├── Concepts/
│       ├── Items/
│       ├── Abilities/
│       └── Organizations/
├── System/
│   └── Templates/
│       ├── Location - City.md
│       ├── Location - Town.md
│       ├── Location - Village.md
│       ├── Location - Building.md
│       ├── Location - District.md
│       ├── Location - Dungeon.md
│       ├── Location - Landmark.md
│       └── Location - Region.md
├── Campaigns/
└── Reference/
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

### 2. Status Callouts

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

### 3. Content Guidelines

- Only include information the PCs would know
- Write from party perspective ("we", "our")
- Reference chronicle entries when describing events
- Use wikilinks for all related content: `[[Location]]`, `[[NPC]]`, `[[Item]]`
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

- Use simple wikilinks: `[[Page Name]]`
- For display text: `[[Page Name|Display Text]]`
- Quartz with ObsidianFlavoredMarkdown handles path resolution
- Images: Use `![[image-name.jpg]]` for Obsidian-style embeds

## Example Completed Files

### Best Examples by Category

**Cities:**

- `World/Grimmora/Locations/Cities/Avalon.md` - Comprehensive city with districts
- `World/Grimmora/Locations/Cities/Durvish City.md` - Quest starting location

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

#### Towns (3/3)

- [x] Durendal
- [x] Frostpeak Pass
- [x] Mightrest

#### Villages (2/2)

- [x] Pinechill
- [x] Midward

#### Landmarks (4/4)

- [x] Alpine Forest
- [x] Court of Flowers
- [x] Court of Summer and Winter
- [x] fey realm

### ⏳ Remaining Categories

#### Buildings (10 files)

- [x] Auril's Church.md
- [x] Golden Griffin.md
- [x] Jade Zephyr Casino.md
- [x] North City Gate.md
- [x] Rotunda.md
- [ ] The Tavern.md
- [ ] Village Inn.md
- [ ] mage's tower.md
- [ ] monastery.md
- [ ] temple.md

#### Districts (1 file)

- [ ] elvish quarter.md

#### Dungeons-and-Lairs (6 files)

- [ ] Dragon's Nest.md
- [ ] Orris' Secret Lair.md
- [ ] The Gladiator's Amphitheatre.md
- [ ] The Trial Chamber.md
- [ ] Vampire Mansion.md
- [ ] big house.md

## Workflow Pattern

This is the workflow that works well:

1. **Start with a category** (e.g., "Let's do Buildings")
2. **AI asks for file content:**
    
    ```bash
    cat content/World/Grimmora/Locations/Buildings/Building-Name.md
    ```
    
3. **User pastes the file content**
4. **AI converts to template format** with proper frontmatter and structure
5. **User copies result back to file**
6. **Move to next file in category**
7. **Repeat until category complete**

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

1. **Provide context:**
    
    - "I'm organizing a D&D campaign vault in Obsidian published with Quartz v4"
    - "I need help converting location files to standardized templates"
2. **Share this reference file:**
    
    - Copy/paste this entire file, OR
    - Provide the path and ask AI to read it
3. **State current progress:**
    
    - "I've completed Cities, Towns, Villages, and Landmarks"
    - "Next I need to do Buildings (10 files)"
4. **Request to continue:**
    
    - "Can you help me convert the Buildings category using the same workflow?"
5. **AI will ask for first file:**
    
    ```bash
    cat content/World/Grimmora/Locations/Buildings/FirstBuilding.md
    ```
    

## Party Members (for reference)

- [[Gage]] - Main perspective (our PC)
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

_Last Updated: October 14, 2025_ _Next Category: Buildings (10 files)_