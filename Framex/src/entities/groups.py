from ..utils.imports import *
from ..utils import *
from ..frame.camera import Camera

__all__ = [
    "Group",
    "Groups"
]

class Group(pygame.sprite.Group):
    def __init__(self, zorder: bool):
        super().__init__()
        self.order = zorder

    def draw(
            self, 
            screen: pygame.Surface, 
            camera: Camera | None = None
        ) -> None:
        offset = camera.get_offset(screen) if camera else vector(0, 0)

        sprites = (
            sorted(self.sprites(), key = lambda s: s.rect.centery)
            if self.order else self.sprites()
        )

        for sprite in sprites:
            screen.blit(sprite.image, sprite.rect.topleft - offset)
            if sprite.draw_hitbox:
                pygame.draw.rect(screen, "Red", (*(sprite.rect.topleft - offset), *sprite.rect.size), 2)

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

    def draw(self, screen: pygame.Surface, camera: Camera | None = None) -> None:
        self.static_sprites.draw(screen, camera)
        self.dynamic_sprites.draw(screen, camera)
    
    def update(self, dt: float) -> None:
        self.dynamic_sprites.update(dt)