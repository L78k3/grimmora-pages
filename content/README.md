# grimmora
 Info for Beaman's specific D&D Campaign which takes place in Grimmora. I still don't think the campaign has a name! 🤯

# Contents

## Characters
Pages for each character. Pretty Simple, no structure has been defined yet for these.
**Player Characters**
```dataview
LIST
FROM "Characters"
WHERE type = "pc"
```
**Familiars**
```dataview
LIST
FROM "Characters"
WHERE type = "familiar"
```
**Non-Player Characters**
```dataview
LIST
FROM "Characters"
WHERE type = "npc"
```
## Chronicles
These are produced by Tony, they are then copy-pasted into here where sub-notes for are produced in a wiki-style linking format.

```dataview
LIST
FROM "Chronicles"
SORT file.name asc
```

## Locations
Small notes about each distinct location the party visits. 
```dataview
LIST
FROM "Locations"
```

## Sessions
Play-by-play notes, written from Luke/Gage's perspective.
```dataview
LIST
FROM "Characters/GageGreengather/SessionNotes"
```


