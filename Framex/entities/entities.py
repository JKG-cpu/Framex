"""
Framex/entities.py
==================
Sprite entity classes for game objects.

ROADMAP ITEM #4 — Keymap Injection:
    Entities accept a dictionary mapping actions to pygame key
    constants (e.g., {"up": pygame.K_w}). The input() method
    checks dictionary values instead of hardcoded keys, making
    it easy to swap controls mid-game.

ROADMAP ITEM #6 — Static vs. Dynamic Distinction:
    - StaticEntity: Non-moving objects (walls, floors). Added to
      collision_group but never call update() or input(), saving CPU.
    - DynamicEntity: Moving "actors" (player, NPCs). They move and
      check collisions against the Static group.

Responsibilities:
    - Entity: Base class inheriting from pygame.sprite.Sprite
    - StaticEntity: Non-moving, no update/input, collision-only
    - TopDownEntity: Dynamic entity with WASD/Arrow movement
    - Dictionary-based keymap for input handling
    - Delta-time-based movement using loop.dt
    - Screen boundary clamping (optional)

Used by:
    - groups.py (entities add themselves to FramexGroup)
    - collisions.py (entities pass their rect for collision checks)
    - main.py (user creates entities and adds them to the scene)
"""
