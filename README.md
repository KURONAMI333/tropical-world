# Deep Sea World

> Overworld becomes a fully submerged ocean. Y -50..0 is the playable seafloor, vanilla ores compress into the seabed crust, oceanic structures become the world's core content.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![NeoForge 1.21.1](https://img.shields.io/badge/NeoForge-1.21.1-orange.svg)](https://neoforged.net)
[![Depends on Isekai API](https://img.shields.io/badge/Depends-Isekai%20API-9333ea)](https://github.com/KURONAMI333/isekai-api)

---

## Concept

The whole overworld is underwater. Less than 5% of the surface peeks above sea level — small rare islands that become precious. Ocean monuments, shipwrecks, and coral reefs are no longer side content; they're the main attraction.

Pairs naturally with diving / underwater-breathing mods (Aquatic Survival, Improved Backpacks, etc.). Note: without one of those mods, survival is rough by design.

## How it works

Deep Sea World is built on **[Isekai API](https://github.com/KURONAMI333/isekai-api)**, a neutral universal worldgen library.

The library has no concept of "submerged world" — Deep Sea World composes the `mask_y_range`, `step`, and rule-adaptation primitives that Isekai API offers, into a submerged worldshape. Any other modder can do the same with the same primitives.

## Status

**v0.1**: skeleton. `WorldshapeDescriptor` declaration + density composition land with Isekai API v0.2.

## Dependencies

- NeoForge 1.21.1
- [Isekai API](https://github.com/KURONAMI333/isekai-api) (required)

## License

[MIT License](LICENSE) — modpack inclusion welcome, no credit required.

## Credits

- Author: KURONAMI
