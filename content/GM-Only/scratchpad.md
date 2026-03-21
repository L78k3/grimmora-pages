# 🎒 Master Inventory

This page utilizes **Dataview** to aggregate all items found in the vault. Based on your provided YAML specification, the following query will generate a live-updating list of all items, their current owners, and their rarity.

## 📋 Live Inventory Tracker

```dataview
TABLE 
    owner AS "Held By", 
    subtype AS "Type", 
    rarity AS "Rarity", 
    description AS "Summary"
FROM "content/World/Grimmora/Items"
WHERE type = "item"
SORT owner ASC
```

