from ..utils.imports import *
from ..utils import *

__all__ = [
    "Entity",
    "StaticEntity",
    "DynamicEntity"
]

class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        image: str | pygame.Surface | None = None,
        center: bool = True,
        alpha: bool = True,
        color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
        speed: int = 250
    ) -> None:
        super().__init__()

        self.image, self.rect = create_object(
            position = position,
            center = center,
            image = image,
            background_color = color,
            alpha = alpha
        )

        self.block = False
        self.draw_hitbox = False
        self.direction = vector()
        self.speed = speed

    def toggle_drawhitbox(self) -> None: self.draw_hitbox = False if self.draw_hitbox else True
    def update(self, dt: float | int) -> None: self.move(dt)

    def move(self, dt: float | int):
        # X
        self.rect.centerx += self.speed * dt * self.direction.x

        # Y
        self.rect.centery += self.speed * dt * self.direction.y

class StaticEntity(Entity):
    def __init__(
            self,
            position: tuple[int, int],
            image: str | pygame.Surface | None = None,
            center: bool = True,
            alpha: bool = True,
            color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
            speed: int = 250
        ):
        super().__init__(position, image, center, alpha, color, speed)

class DynamicEntity(Entity):
    def __init__(
            self,
            position: tuple[int, int],
            image: str | pygame.Surface | None = None,
            center: bool = True,
            alpha: bool = True,
            player_controlled: bool = False,
            color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
            speed: int = 250
        ):
        super().__init__(position, image, center, alpha, color, speed)
        self.player_controlled = player_controlled
    
    def input(self):
        if not self.player_controlled:
            return

        keys = pygame.key.get_pressed()

        temp = vector()

        if keys[pygame.K_w]:
            temp.y -= 1
        
        if keys[pygame.K_s]:
            temp.y += 1
        
        if keys[pygame.K_a]:
            temp.x -= 1
        
        if keys[pygame.K_d]:
            temp.x += 1
    
        self.direction = temp.normalize() if temp else temp
    
    def update(self, dt: float | int) -> None:
        self.input()
        self.move(dt)