# Shelby & the Cuddle Warriors — living storybook prototype

Six little moments from Chapter 1 v0.9, adapted from the exact ThreeUI Meng To sketchbook.

## Run locally

Requires Node.js 20.19+ or 22+ and npm. The generated page textures, images, fonts, and all six videos are included; Python is only needed when changing the page artwork or text.

```sh
npm ci
npm run dev
```

Open the local URL printed by Vite. For a production build, run `npm run build`; `npm run preview` serves it locally.

[Play the published storybook](https://shelby-living-storybook.shudoof.chatgpt.site)

This repository starts from the six-video version published on September 25, 2026. GitHub changes do not automatically update that Site. The original deployment identity and temporary runtime files are excluded from this copy.

## Where to edit

| File | Purpose |
| --- | --- |
| `story.json` | Spread order, text, images, videos, and playback settings |
| `public/landing-pages/shelby.html` | Page turns, navigation, zoom, and magnifier |
| `public/landing-pages/shelby-media.js` | Video playback, replay, and pause behavior |
| `public/landing-pages/shelby.css` | Shelby-specific layout and styling |
| `scripts/prepare_spreads.py` | Regenerates page textures and `story-data.js` |
| `public/landing-pages/shelby-media/` | Included images, page textures, and six MP4s |

Future ideas are recorded in [Interaction experiments](docs/interaction-experiments.md); they are not implemented in this baseline.

## Try it

The main route opens Shelby. `/?baseline` opens the original configured Singapore sketchbook. The footer includes an **Original sketchbook** link.

- Tap the right or left page, use the side arrows, or drag a page to turn it.
- Arrow keys turn pages. The contents list jumps to a spread.
- Move the pointer to tilt the book. Use the toolbar to zoom; double-click the book to return to 100%.
- On a mouse or trackpad, drag the magnifying glass across a page. The original template hides it on touch devices.
- Portrait phones have a readable text excerpt below the book; landscape gives the pictures more room.
- All six spreads have supplied video clips. Each is set to play once, muted, when its page opens; use **Replay clip** to watch again. Readers with reduced motion enabled use **Play clip** to start manually.

## Story and media

Source: [Chapter 1 — Windworks, v0.9](https://app.notion.com/p/3c21f16ba962807783d2d8ecb44e67e2), fetched 2026-09-25. Its newer scene illustrations were selected instead of the attached multi-panel journal sheets because these six illustrations form the requested coherent reveal. No art was generated.

| Spread | Illustration | Excerpt / role |
| --- | --- | --- |
| 1 | `warmth.png` — Noodles by the blanket | His warmth reached me; the room returned. |
| 2 | `room.png` — the family on the hospital bed | The arrangement follows Shelby; everybody makes room. |
| 3 | `carried.png` — leaving the Pokémon Center | Shelby is carried toward the Windworks. |
| 4 | `waiting.png` — Shelby among flowers | She waits for the footsteps to leave. |
| 5 | `blanket.png` — the picnic blanket opens | Instead—FWUMP. |
| 6 | `together-video-poster.webp` — the opening meadow frame of the supplied portrait clip | Everybody here. Good. |

Original downloaded PNGs are preserved in `media-originals/`. The website uses WebP copies and prepared page textures. Every full source frame is contained proportionally on the right page, including its original taped edge and caption; no face, image edge, or caption is cropped. The original ThreeUI fonts and a faint copy of its paper wash are used for the page layout.

## Change the sequence

Edit `story.json` to change order, image filenames, headings, or excerpt paragraphs. Put new stills in `public/landing-pages/shelby-media/`, then run:

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/prepare_spreads.py
npm install
npm run build
```

`prepare_spreads.py` composes the supplied pictures and typography into textures at the original 1760 × 1240 coordinate system used by the authored curl. It also writes `story-data.js`; do not edit that generated file. No generated art or illustration retouching takes place.

For local development: `npm run dev -- --host 0.0.0.0`. Vite prints the actual address. A phone on the same network can use that machine’s network address if its firewall allows it. The deployed site is public and can be opened by anyone with its URL; it does not depend on a local computer running.

## Moving pictures

Six supplied MP4s are integrated, one on every spread:

| Spread | Supplied clip | Published file | Duration |
| --- | --- | --- | --- |
| 1 — His warmth reached me | `his warmth reached me.mp4` | `warmth.mp4` | 6.59 s |
| 2 — Room for Shelby | `failed to aquire an edge.mp4` | `room.mp4` | 9.44 s |
| 3 — Back to the meadow | `on the day i could travel with you you put me in your arms.mp4` | `carried.mp4` | 6.59 s |
| 4 — I waited | `i waited for your footsteps to reach the road.mp4` | `waiting.mp4` | 10.14 s |
| 5 — Instead—FWUMP | `FWUMP.mp4` | `blanket.mp4` | 12.26 s |
| 6 — Everybody here | `no part of shelby had to move.mp4` | `together.mp4` | 6.59 s |

The published copies preserve each full frame, 24 fps, clip duration, and audio track. Spreads 1–5 use landscape 1152 × 768 clips; spread 6 uses the supplied portrait 768 × 1152 clip. They use H.264 (CRF 20, yuv420p) with MP4 fast-start metadata for progressive loading. No frames were cropped or deliberately trimmed. The original uploads are unchanged. Spread 6 uses its opening meadow frame at 0.1 seconds as its poster and page texture, with the full portrait image centered on the right page; the original landscape `together.webp` and downloaded PNG remain available.

To add another supplied clip, put it in `public/landing-pages/shelby-media/`, set that spread’s `video` to `shelby-media/<filename>.mp4`, set `playback` to `once` or `loop`, and rerun `prepare_spreads.py`. The poster defaults to the full still for that spread. Clips should match the poster’s composition and aspect ratio.

The adapter is set up for muted inline playback when the spread settles, pausing when it closes or the tab becomes hidden. A Play/Replay button handles user playback. Reduced-motion readers must start clips manually. Failed clips fall back to the complete still page.

**Deliberate compromise:** the original curl uses image-backed strips. Page turns and the loupe use the poster; the live video is attached to the page’s transformed surface only while the spread is open. The waiting clip begins with Shelby being placed in the flowers, while its poster shows the later waiting pose. Browser playback and the poster-to-video transition still need a playtest. GIF fallback has not been tested.

## Baseline and adaptation

- `baseline/` contains all six registered source files and all 17 original assets, unchanged.
- Every source and asset hash matches the supplied revision. See `baseline/verification.json`.
- Original canonical SHA-256: `e0330548b1ac905cf1b81698163ffa29f8a3a8c39b8d39f9b71ba5b9255b6dd1`.
- The unchanged original source is preserved in `baseline/`, so future experiments can compare against it. The original Sites history is separate from this new GitHub repository.
- `src/BaselineScene.tsx` uses the exact requested public configuration.
- The registered catalog imports unrelated components that are not included in the bundle. `src/threeui-entry.tsx` extracts the exact, unchanged sketchbook component function and uses its original frame and typography recipe. The full registered catalog remains untouched.
- `public/landing-pages/shelby.html` is the separately tracked local adaptation of the canonical HTML, not a reconstruction from a preview or a documentation embed.
- Original page-curl strips, springs, lighting, shadows, pointer tilt, zoom, loupe, and contents navigation are retained. Changes cover story data, metadata, captions, page layout, accessibility, optional media hooks, and disabling the introductory riffle to preserve the reveal.
- Small interaction fixes in the adaptation support keyboard activation of page hit targets, keep arrow-button clicks outside leaf pointer capture, cancel interrupted touch drags, clear the magnified copy when the loupe is switched off, and avoid invisible loupe hit targets.
- All original source comments are retained. No separate license notice was included in the retrieved registered bundle.

## Verification and limits

Completed for the original release: exact source and asset hash checks; JavaScript syntax checks; production build; local reference checks; visual inspection of all six composed spread textures for uncropped artwork, readable desktop-scale text, and absence of layout overflow. Its three supplied clips were inspected at their beginning, middle, and end; published MP4s were fully decoded without errors and checked for dimensions, duration, codecs, and fast-start layout. The user subsequently confirmed that playback worked. The added clips on spreads 1, 2, and 6 passed the same full-decode and media checks, including unchanged frame counts. All six video, poster, and page references resolve and have matching aspect ratios. The portrait ending is fitted without cropping.

**Automated browser interaction QA remains unavailable.** The original session could not open the preview, and the required browser-control skill is not available for this update. No alternate browser path was used. The existing playback adapter is unchanged; the three newly added clips still need a real-device playtest. Forward/back dragging, pointer tilt, zoom, loupe, keyboard behavior, narrow-screen layout, video autoplay, replay, pause-on-close, reduced-motion behavior, and actual-device performance must not be reported as automatically browser-verified.

An unused font face for other components in the unmodified shared ThreeUI stylesheet produces a build warning for `fragment-mono.woff2`. The selected sketchbook uses its verified, locally served Instrument Serif and Newsreader files.

## Suggested 35–40-second recording

Start on “Back to the meadow” and let its 6.6-second clip finish. Turn to “I waited” and leave the full 10.1 seconds for the words and face. Slowly turn to “Instead—FWUMP” and let its 12.3-second reveal finish. End on “Everybody here” and let its 6.6-second portrait clip settle. Record on desktop or a landscape tablet first, after checking playback there.

## What this version establishes

Observed in the composed textures: each complete illustration fits a right-hand page without cropping, including the portrait ending; short text on the left keeps faces and scene composition intact. Page 4 and page 5 are separate surfaces, so the blanket is placed after a deliberate reader action.

Playtest hypotheses, not observations: a pause on “I waited” may give the turn emotional weight; the final scene may need more dwell time than the earlier spreads; starting the blanket clip only after the page settles may make its movement feel like a second reveal. Timing, phone readability, live motion, and the poster-to-video transition require actual viewing before drawing conclusions.

## Credits

Story and creative direction: Keshav Prasad / Pixel Rhythms Labs. Book interaction: Meng To / ThreeUI. Moving illustrations: MiniMax H3, using Krea and Reactor in the creative workflow. Implementation assistance: ChatGPT.

This is an unofficial Pokémon fan project. Original third-party source comments and attributions are retained. No blanket open-source license is assigned by this repository to the template, fonts, artwork, characters, or media.
