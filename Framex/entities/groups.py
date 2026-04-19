from ..utils.imports import *

class Group(pygame.sprite.Group):
    def __init__(self, zorder: bool):
        super().__init__()
        self.order = zorder
    
    def draw(self, screen: pygame.Surface) -> None:
        filtered_sprites = self.sprites().sort(key = lambda spr: spr.rect.centery)
        
        if not filtered_sprites:
            return
        
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