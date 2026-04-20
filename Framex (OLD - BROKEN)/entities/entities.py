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

        self.collisionHandler = CollisionHandler(
            self.groups()
        )

        self.image, self.rect = factory.create_object(
            image = image,
            color = color,
            alpha = alpha,
            position = position,
            center = center
        )

        self.block = False
        self.direction = vector()
        self.draw_hitbox = False
    
    def add_on_hit_callback(self, on_hit, add_self: bool = False) -> None:
        self.collisionHandler.add_on_hit(on_hit, add_self)

    def toggle_draw_hitbox(self) -> None:
        self.draw_hitbox = True if not self.draw_hitbox else False

    def move(self, dt: float) -> None:
        self.rect.centerx += self.direction.x * DEFAULT_ENTITY_SPEED * dt
        self.collisionHandler.resolve_collision(self, "X")
    
        self.rect.centery += self.direction.y * DEFAULT_ENTITY_SPEED * dt
        self.collisionHandler.resolve_collision(self, "Y")

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

    def _custom_movement(self) -> None:
        """To Be Added
        Gonna work somewhat like this

        sprite.custom_movement(type: str)
        """
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