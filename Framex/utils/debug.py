"""
Framex/debug.py
===============
Debug tools and visual overlays for testing.

ROADMAP ITEM #3 — Debug Tools & Callbacks:
    A test window needs to show what's happening behind the scenes.

Responsibilities:
    - Visual Hitboxes: Toggle that draws rect outlines on all sprites
      to verify image matches physical boundaries
    - Performance Overlay: Renders clock.get_fps() in the corner
      using pygame's system font
    - Collision Callbacks: Hook system — when a collision is detected,
      the sprite can trigger a function (e.g., on_hit()) for custom
      logic like taking damage or bouncing

Usage:
    - Opt-in via Framex(debug=True) flag
    - Toggle hitboxes with a key press during runtime
    - FPS overlay always available when debug mode is enabled

Used by:
    - loop.py (calls debug.draw() at end of each frame)
    - collisions.py (fires collision callbacks through debug hooks)
    - main.py (enables/disables debug mode on Framex creation)
"""
