# IT Atlas (Gesture Graph)

Your vault as a 3D brain you can explore with the mouse or your hands.

## How it's organized
- **Brain view**: one glowing, labelled ball per area of IT (the lobes): Help Desk, RMM, Backup & DR, Security, Concepts, Playbooks and so on. The number is how many notes it holds.
- **Inside a lobe**: its groups (for example SaaS backup, VM backup) and their notes, with names on every dot.
- **Card**: selecting a note shows its plain-English summary and what it connects to. Click a connection to jump there.
- Navigation pages (Home, Glossary, reference sheets, vendors) are left out, so the picture stays readable.

## Controls
| | Mouse | Hands (turn on Hand control) |
|---|---|---|
| Rotate | Drag | ✋ Open palm, move |
| Zoom | Scroll | 🤏 Pinch and move up/down, or 🙌 two palms apart/together |
| Go inside / select | Click | ☝️ Point and hold |
| Open a note | Click it again, or "Open note" | ☝️ Keep holding |
| Go back | Esc or ← Back | ✊ Hold a fist |

**Find a note**: type in the search box and press Enter. **Learning lens**: pick a week from the learning path to light up its notes.

## Commands (Ctrl+P)
- **Open IT Atlas**
- **Turn hand control on or off**
- **Restore colours and clean filters in Obsidian's graph view**: puts the IT Atlas colours back in Obsidian's own graph (Ctrl+G) and hides navigation pages there too. Obsidian reloads afterwards.

## Privacy and network
- Video is processed on this computer by MediaPipe (bundled here). No frames are sent anywhere. The camera is on only while Hand control says "on".
- The first time you turn hand control on, the hand model (about 8 MB) downloads from storage.googleapis.com and is saved here as `hand_landmarker.task`. If your network blocks that, download it elsewhere from the URL in the settings and put it in this folder with that name.

## Mac: camera on but no picture
Obsidian on macOS can open the camera without receiving any video (a packaging issue in the Obsidian app that plugins can't change). When that happens the plugin offers **Use browser camera**:
1. It starts a small page on your own computer (127.0.0.1 only) and opens it in your default browser.
2. Click **Start camera** on that page and allow the camera.
3. Keep that browser window open and visible beside Obsidian. Your hand movements steer the IT Atlas.
Only the hand positions are sent to Obsidian; the video stays in the browser page. The choice is remembered (Settings > Camera source).

## Troubleshooting
- No brain icon or command: Settings > Community plugins: turn community plugins on (leave Restricted mode) and enable "IT Atlas (Gesture Graph)".
- "Camera permission denied": Windows Settings > Privacy & security > Camera > let desktop apps use the camera. Close Teams or Zoom if they're using it.
- Slow: turn off Glow and Firing particles in the plugin settings.
