# Chronicle Wikilinking Reference

## 1. Vault Setup & Rules

-   **Platform:** Obsidian with Quartz v4
-   **Perspective:** Player-facing (Gage's view)
-   **Language:** British English (e.g., *amphitheatre*, *armour*, *centre*)
-   **Spelling:** Use `[[Auriel|Auriel]]` for the goddess (matches file `Auriel.md`).

## 2. Folder Structure & File Manifest

This is the complete manifest of all existing files in the vault. Use this to check if a page exists before suggesting a new one.

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
│           ├── ...
├── Reference
│   ├── ...
├── System
│   ├── Conversion-Workflow-Reference.md
│   ├── Queries
│   │   ├── ...
│   └── Templates
│       ├── ...
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
    │   │   ├── moon elf.md
    │   │   ├── necromancers.md
    │   │   ├── Pellor.md
    │   │   ├── Pseudodragon.md
    │   │   ├── Snow-Blindness.md
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
    │   │   ├── health potions.md
    │   │   ├── Potion of Fire Breathing.md
    │   │   ├── scrying pool.md
    │   │   └── teleportation rune.md
    │   ├── Locations
    │   │   ├── Buildings
    │   │   │   ├── Auriel's Church.md
    │   │   │   ├── Golden Griffin.md
    │   │   │   ├── Jade Zephyr Casino.md
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
    │   │   │   ├── The Trial Chamber.md
    │   │   │   └── Vampire Mansion.md
    │   │   ├── Landmarks
    │   │   │   ├── Alpine Forest.md
    │   │   │   ├── Court of Flowers.md
    │   │   │   ├── Court of Summer and Winter.md
    │   │   │   └── fey realm.md
    │   │   ├── Maps
    │   │   │   ├── GRIMMORA_UPDATED.jpg
    │   │   │   └── Maps.canvas
    │   │   ├── Towns
    │   │   │   ├── Bremen.md
    │   │   ├── Durendal.md
    │   │   │   ├── Frostpeak Pass.md
    │   │   │   └── Mightrest.md
    │   │   └── Villages
    │   │       ├── Midward.md
    │   │       └── Pinechill.md
    │   ├── Organizations
    │   │   ├── House Locke.md
    │   │   └── The Order of the Ancient Fable.md
    │   └── Regions
    │       ├── Avalonean Empire.md
    │       └── The Frost.md
    └── ... (Other world folders)
````

## 3\. Key Entities Manifest

Use this list to check if an entity already has a page.

### Party Members

  - [[Gage]]
  - [[Lavender]]
  - [[Temerity]]
  - [[Theren]]
  - [[Mary-Ann]]
  - [[Anaphel]]

### Key NPCs

  - [[Auriel]]
  - [[Aurius]]
  - [[Bracken]]
  - [[Captain Arran]]
  - [[Cella]]
  - [[Corvus]]
  - [[First Fist]]
  - [[Florian]]
  - [[Gnome Cook]]
  - [[Gorg]]
  - [[Guardsman Floyd]]
  - [[Guido]]
  - [[Halsen]]
  - [[Ice Dragon]]
  - [[Ismay]]
  - [[Korako]]
  - [[Lady Bromelia]] -s  [[Lord Requiem]]
  - [[Mavis]]
  - [[Millicent]]
  - [[Orion]]
  - [[Orris]]
  - [[Rowan]]
  - [[Runcible]]
  - [[Summer]]
  - [[The Alchemist]]
  - [[The Clothier]]
  - [[Vampire Lord]]
  - [[Wild Wanderer]]
  - [[Winter]]
  - [[Zadhir]]
  - [[hag]]

### Key Concepts & Organizations

  - [[confoundment spell]]
  - [[dryads]]
  - [[griffin]]
  - [[hellish rebuke]]
  - [[hideous laughter]]
  - [[Ice Wolves]]
  - [[Lady Rose]]
  - [[necromancers]]
  - [[Pellor]]
  - [[Pseudodragon]]
  - [[spectres]]
  - [[The Curse]]
  - [[The Gladiator Wight]]
  - [[tiefling]]
  - [[House Locke]]
  - [[The Order of the Ancient Fable]]

### Key Events

  - [[Battle at the Big House]]
  - [[Dragon Battle]]
  - [[Gnome Confrontation]]
  - [[Magical Plague]]
  - [[Plague Investigation]]
  - [[The Trial of the Gladiator]]
  - [[Vampire Defeat]]

---