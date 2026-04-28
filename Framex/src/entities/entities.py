from ..utils.imports import *
from ..utils import *
from .groups import Groups

__all__ = [
    "Entity",
    "StaticEntity",
    "DynamicEntity"
]

class Entity(pygame.sprite.Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        group_ref: Groups | None = None,
        image: str | pygame.Surface | None = None,
        center: bool = True,
        alpha: bool = True,
        color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
        speed: int = 250
    ) -> None:
        super().__init__()

        self.group_ref = group_ref

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
    
    def check_collisions(self, axis: str) -> None:
        if self.group_ref is None:
            return

        for sprite in self.group_ref.static_sprites.sprites() + self.group_ref.dynamic_sprites.sprites():
            if sprite is self:
                continue

            if self.rect.colliderect(sprite.rect):
                if axis == "x":
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

                    elif self.direction.x > 0:
                        self.rect.right = sprite.rect.left

                elif axis == "y":
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    
                    elif self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top

    def move(self, dt: float | int):
        # X
        self.rect.centerx += self.speed * dt * self.direction.x
        self.check_collisions("x")

        # Y
        self.rect.centery += self.speed * dt * self.direction.y
        self.check_collisions("y")

class StaticEntity(Entity):
    def __init__(
            self,
            position: tuple[int, int],
            group_ref: pygame.sprite.Group | None = None,
            image: str | pygame.Surface | None = None,
            center: bool = True,
            alpha: bool = True,
            color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
            speed: int = 250
        ):
        super().__init__(position, group_ref, image, center, alpha, color, speed)

class DynamicEntity(Entity):
    def __init__(
            self,
            position: tuple[int, int],
            group_ref: pygame.sprite.Group | None = None,
            image: str | pygame.Surface | None = None,
            center: bool = True,
            alpha: bool = True,
            player_controlled: bool = False,
            color: tuple[int, int, int] | tuple[int, int, int, int] | None = None,
            speed: int = 250
        ):
        super().__init__(position, group_ref, image, center, alpha, color, speed)
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