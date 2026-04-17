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
    def __init__(self) -> None:
        self.on_hit_functions = []

    def add_on_hit(self, on_hit, add_self: bool = False) -> None:
        """Set a function to run when a sprite collides with another sprite.
        **MUST BE A CALLABLE**"""
        self.on_hit_functions.append(on_hit if not add_self else lambda : on_hit(self))

    def on_hit(self) -> None:
        for func in self.on_hit_functions:
            if callable(func):
                func()

    def resolve_collision(self, sprite, static_group, axis) -> None:
        for static_sprite in static_group:
            if static_sprite.rect.colliderect(sprite.rect):
                if axis == "X":
                    if sprite.direction.x == -1:
                        # Moving Left
                        sprite.rect.left = static_sprite.rect.right

                    elif sprite.direction.x == 1:
                        # Moving Right
                        sprite.rect.right = static_sprite.rect.left

                elif axis == "Y":
                    if sprite.direction.y == -1:
                        # Moving Up
                        sprite.rect.top = static_sprite.rect.bottom
                    
                    elif sprite.direction.y == 1:
                        sprite.rect.bottom = static_sprite.rect.top

            self.on_hit()

    def resolve_collisions(self, sprite, static_group) -> None:
        self.resolve_collision(
            sprite = sprite,
            static_group = static_group,
            axis = "X"
        )
        sprite.move("X")

        self.resolve_collision(
            sprite = sprite,
            static_group = static_group,
            axis = "Y"
        )
        sprite.move("Y")
