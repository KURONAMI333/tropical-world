# Changelog

## [1.0.0] — 2026-05-28

First public release. Datapack-only fully-submerged overworld built on Isekai API.

### World transformation
- `data/minecraft/worldgen/noise_settings/overworld.json` — overlay wrapping
  vanilla `final_density` in `min(vanilla, mask_y_range(-64, 30, +1, -1))`.
  Terrain only exists Y=-64..30; above Y=30 is void, water fills up to sea
  level Y=63.
- `data/deep_sea_world/neoforge/biome_modifier/apply_deep_sea.json`:
  - `playable_range` Y=-50..30
  - `surface_anchor: below_fluid` (water)
  - `ore_strategy: linear` — ore Y bands compressed into seabed
  - `default_structure_predicate`: y_in_range(-50,30) AND in_fluid(water)
  - per-structure: ocean_monument / shipwreck / ocean_ruin use in_fluid;
    villages / ancient_city / shipwreck_beached / buried_treasure → never
  - 21 oceanic + adjacent biomes in `applies_to`
- `data/deep_sea_world/neoforge/structure_modifier/apply_deep_sea.json` —
  clears biome filters for excluded land structures.

### Demonstrates
- `isekai_api:mask_y_range` for Y cap
- `isekai:in_fluid` SpatialPredicate
- `isekai:below_fluid` SurfaceAnchor
- `isekai:linear` RemapStrategy

### Known limitations
- "Rare island peaks above sea level" not yet implemented — the hard mask
  forbids terrain above Y=30. A future version could add `step(noise, low=mask, high=full_density)` to allow rare island chunks.
- Player spawn may land in water; bring breathing gear.
