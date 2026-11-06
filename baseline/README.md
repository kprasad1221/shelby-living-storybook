# Verified ThreeUI baseline

All six registered source files and all 17 assets are copied byte-for-byte from ThreeUI. Canonical SHA-256: e0330548b1ac905cf1b81698163ffa29f8a3a8c39b8d39f9b71ba5b9255b6dd1. Retrieved 2026-09-25.

The unchanged configured component usage is in `src/BaselineScene.tsx`. The original catalog also imports unrelated components not included in this registered bundle; `src/threeui-entry.tsx` extracts the exact sketchbook component body without rewriting it, using its original typography recipe and frame.

Original sources: https://threeui.com/source-code/meng-to-sketchbook-landing-page.json and https://threeui.com/landing-pages/meng-to-sketchbook.html. All source comments retained. No license notice was present in the registered bundle.
