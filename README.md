# Deep Sea World

> Overworld becomes a fully submerged ocean. Terrain is capped below sea level, oceanic structures (monuments, shipwrecks, ruins) become the world's main content. Vanilla ores compress into the seabed crust via [Isekai API](https://github.com/KURONAMI333/isekai-api).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![NeoForge 1.21.1](https://img.shields.io/badge/NeoForge-1.21.1-orange.svg)](https://neoforged.net)
[![Depends on Isekai API](https://img.shields.io/badge/Depends-Isekai%20API-9333ea)](https://github.com/KURONAMI333/isekai-api)

---

## Concept

The overworld is underwater. Less than 5% of the surface peeks above sea level. Ocean monuments, shipwrecks, and coral reefs are no longer side content — they're the world's main attraction.

Pairs naturally with diving / breathing mods (Aquatic Survival, etc.). Survival without one of those is intentionally rough.

## How it works

Datapack-only via three Isekai-driven JSON files:

1. **`data/minecraft/worldgen/noise_settings/overworld.json`** — overlay wrapping vanilla `final_density` in `min(vanilla, mask_y_range(-64, 30, +1, -1))`. Terrain capped at Y=30 (below sea level Y=63); above Y=30 is forced to void (air→water once aquifers fill).
2. **`data/deep_sea_world/neoforge/biome_modifier/apply_deep_sea.json`** — Isekai `apply_worldshape`:
   - `playable_range` Y=-50..30 with `linear` ore strategy
   - `surface_anchor: below_fluid` (water) — surface-relative features attach to seabed
   - `default_structure_predicate` requires `y_in_range(-50,30)` AND `in_fluid(water)`
   - ocean structures keep placement via `in_fluid` predicates; villages and ancient_city excluded entirely
3. **`data/deep_sea_world/neoforge/structure_modifier/apply_deep_sea.json`** — clears biome filters for villages / ancient_city.

## Demonstrates

- `isekai_api:mask_y_range` for hard Y cap
- `isekai_api:in_fluid` predicate composition
- `isekai:below_fluid` surface anchor
- `isekai:linear` ore range remap

## How to play

1. Install [Isekai API](https://github.com/KURONAMI333/isekai-api) and Deep Sea World.
2. Create a new world. You spawn underwater near a seabed peak.
3. Find a shipwreck or ocean monument as your starting base. Bring breathing gear.

## Dependencies

- NeoForge 1.21.1
- [Isekai API 1.0.0+](https://github.com/KURONAMI333/isekai-api)

## Building

```bash
./gradlew build
```

Produces `build/libs/deep_sea_world-1.0.0.jar`.

## Compatibility

Conflicts with any mod overlaying `data/minecraft/worldgen/noise_settings/overworld.json`.

## License

[MIT License](LICENSE)

## Credits

- Author: KURONAMI
- Built on [Isekai API](https://github.com/KURONAMI333/isekai-api)
