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
from ..utils.imports import *
from ..utils.factories import Factory
from ..utils.config import *
from ..physics import *

factory = Factory()

class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        image: str | pygame.Surface,
        position: tuple[int, int],
        center: bool = True,
        alpha: bool = True,
        color: tuple[int, int, int] | tuple[int, int, int, int] | None = None
    ) -> None:
        super().__init__()

        self.collisionHandler = CollisionHandler()

        self.image, self.rect = factory.create_object(
            image = image,
            color = color,
            alpha = alpha,
            position = position,
            center = center
        )

        self.block = False
        self.direction = vector()

    def move(self, dt: float) -> None:
        self.rect.centerx += self.direction.x * DEFAULT_ENTITY_SPEED * dt
        self.collisionHandler.resolve_collision("X")
    
        self.rect.centery += self.direction.y * DEFAULT_ENTITY_SPEED * dt
        self.collisionHandler.resolve_collision("Y")

    def update(self, dt: float) -> None:
        self.move(dt)

class StaticEntity(Entity):
    def __init__(
            self,
            image: str | pygame.Surface, 
            position: tuple[int, int], 
            center: bool = True, 
            alpha: bool = True, 
            color: tuple[int, int, int] | tuple[int, int, int, int] = None
        ) -> None:
        super().__init__(image, position, center, alpha, color)

class DynamicEntity(Entity):
    def __init__(
            self,
            image: str | pygame.Surface, 
            position: tuple[int, int],
            player_controlled: bool = False,
            center: bool = True, 
            alpha: bool = True, 
            color: tuple[int, int, int] | tuple[int, int, int, int] = None
        ) -> None:
        super().__init__(image, position, center, alpha, color)
        self.player_controlled = player_controlled

    def custom_movement(self) -> None:
        pass
    
    def input(self) -> None:
        if not self.player_controlled:
            return
        
        keys = pygame.key.get_just_pressed()
        temp_direction = vector()

        for key in KEY_MAP:
            if keys[KEY_MAP[key]]:
                temp_direction += VALUES[KEY_MAP[key]]

        self.direction = temp_direction.normalize() if temp_direction else temp_direction

    def update(self, dt: float) -> None:
        self.input()
        self.move(dt)