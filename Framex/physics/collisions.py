"""
Framex/collisions.py
====================
Collision detection and resolution utilities.

ROADMAP ITEM #5 — Collision Correction:
    The old logic "centered" the sprite on the object it hit,
    causing it to get stuck or teleport. The new implementation:
    - Uses edge snapping: player's right snaps to obstacle's left
      (if moving right), or vice versa.
    - Two-phase movement: Move X -> Check X -> Move Y -> Check Y.
      This prevents the "diagonal clipping" bug entirely.

Responsibilities:
    - resolve_collision(): Axis-separated collision resolution
    - Edge snapping (no center-snapping bug)
    - Two-phase movement (X then Y) to prevent diagonal clipping
    - Collision callback hooks (on_hit) for custom logic

Used by:
    - entities.py (calls resolve_collision during move())
    - groups.py (passes static_group for collision targets)
    - debug.py (logs collision events for visualization)
"""
from ..utils.imports import *

class CollisionHandler:
    def resolve_collision(self, sprite, static_group, axis) -> None:
        pass

    def resolve_collisions(self, sprite, static_group) -> None:
        self.resolve_collision(
            sprite = sprite,
            static_group = static_group,
            axis = "X"
        )

        self.resolve_collision(
            sprite = sprite,
            static_group = static_group,
            axis = "Y"
        )
