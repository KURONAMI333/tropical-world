# Deep Sea World — Runtime Test Checklist

## 1. Mod load
- [ ] Both mods listed

## 2. New world

## 3. Underwater world visible
- [ ] You spawn underwater or on seabed (~Y=30 max)
- [ ] `/tp @s 0 100 0` — you're in air, no land beneath (look down for sea)
- [ ] `/tp @s 0 20 0` — back on seabed
- [ ] No terrain above Y=30 anywhere

## 4. Structure placement
- `/locate structure minecraft:ocean_monument` → coords (in water)
- `/locate structure minecraft:shipwreck` → coords (in water)
- `/locate structure minecraft:village_plains` → "Could not find" (excluded)
- `/locate structure minecraft:ancient_city` → "Could not find"
