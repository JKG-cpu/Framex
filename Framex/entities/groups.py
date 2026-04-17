"""
Framex/groups.py
================
Sprite group management with static/dynamic entity separation.

ROADMAP ITEM #2 — Rebuild Sprite Grouping:
    Shift from manual list-checking to Pygame's built-in Sprite
    and Group system. Supports LayeredUpdates for Z-order drawing.

ROADMAP ITEM #6 — Static vs. Dynamic Distinction:
    Separating objects into static (walls, floors) and dynamic
    (players, NPCs) categories optimizes collision checks.
    Static entities never move and skip update() calls, saving CPU.
    Dynamic entities check collisions only against the static group,
    preventing "everything-against-everything" checks.

Responsibilities:
    - FramexGroup: Combined group managing static + dynamic sprites
    - Batch drawing via group.draw(surface)
    - LayeredUpdates support for Z-order rendering
    - Efficient collision pair filtering (dynamic vs static only)

May also include:
    - Custom group subclasses for specific use cases
    - Render-order groups (front-to-back, back-to-front)
    - Visibility culling groups

Used by:
    - entities.py (adds self to appropriate group on creation)
    - collisions.py (iterates static_group for collision checks)
    - main.py (creates groups and passes them to Framex)
"""
from ..utils.imports import *

class Group(pygame.sprite.Group):
    def __init__(self, zorder: bool):
        super().__init__()
        self.order = zorder
    
    def draw(self, screen: pygame.Surface) -> None:
        filtered_sprites = self.sprites().sort(key = lambda spr: spr.rect.centery)
        for sprite in filtered_sprites:
            screen.blit(sprite.image, sprite.rect)
            if sprite.draw_hitbox:
                pygame.draw.rect(screen, "Red", sprite.rect, 2)

    def update(self, dt: float) -> None:
        for sprite in self:
            sprite.update(dt)

class Groups:
    def __init__(self, zorder: bool = True):
        self.static_sprites = Group(zorder)
        self.dynamic_sprites = Group(zorder)
    
    def add_static(self, *sprite: pygame.sprite.Sprite) -> None: self.static_sprites.add(sprite)
    def add_dynamic(self, *sprite: pygame.sprite.Sprite) -> None: self.dynamic_sprites.add(sprite)
    def remove_static_sprite(self, *sprite: pygame.sprite.Sprite) -> None: self.static_sprites.remove(sprite)
    def remove_dynamic_sprite(self, *sprite: pygame.sprite.Sprite) -> None: self.dynamic_sprites.remove(sprite)

    def draw(self, screen: pygame.Surface) -> None:
        self.static_sprites.draw(screen)
        self.dynamic_sprites.draw(screen)
    
    def update(self, dt: float) -> None:
        self.dynamic_sprites.update(dt)