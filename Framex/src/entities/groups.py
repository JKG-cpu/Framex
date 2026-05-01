from ..utils.imports import *
from ..utils import *
from .camera import Camera

__all__ = [
    "Group",
    "Groups"
]

class Group(pygame.sprite.Group):
    def __init__(self, zorder: bool):
        super().__init__()
        self.order = zorder
    
    def get_offset(self, screen: pygame.Surface, camera_position: tuple[int, int] | pygame.Rect) -> vector:
        offset = vector()

        screen_width, screen_height = screen.get_size()
        screen_width, screen_height = screen_width / 2, screen_height / 2

        if isinstance(camera_position, tuple):
            offset.x = tuple[0] - screen_width
            offset.y = tuple[1] - screen_height

        else:
            offset.x = camera_position.centerx - screen_width
            offset.y = camera_position.centery - screen_height

        return offset

    def draw(
            self, 
            screen: pygame.Surface, 
            camera_position: tuple[int, int] | pygame.Rect | None
        ) -> None:
        if self.order:
            filtered_sprites = sorted(self.sprites(), key=lambda spr: spr.rect.centery)
            
            if not filtered_sprites:
                return
            
            if camera_position:
                offset = self.get_offset(
                    screen = screen,
                    camera_position = camera_position.rect
                )
            
            else:
                offset = vector(0, 0)

            for sprite in filtered_sprites:
                screen.blit(sprite.image, sprite.rect.topleft - offset)
                if sprite.draw_hitbox:
                    pygame.draw.rect(screen, "Red", sprite.rect.topleft - offset, 2)

        else:
            if camera_position:
                offset = self.get_offset(
                    screen = screen,
                    camera_position = camera_position.rect
                )
            
            else:
                offset = vector(0, 0)

            for sprite in self.sprites():
                screen.blit(sprite.image, sprite.rect.topleft - offset)
                if sprite.draw_hitbox:
                    pygame.draw.rect(screen, "Red", sprite.rect.topleft - offset, 2)

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

    def draw(self, screen: pygame.Surface, camera_position: tuple[int, int] | pygame.Rect | None = None) -> None:
        self.static_sprites.draw(screen, camera_position)
        self.dynamic_sprites.draw(screen, camera_position)
    
    def update(self, dt: float) -> None:
        self.dynamic_sprites.update(dt)