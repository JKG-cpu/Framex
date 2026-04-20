 
from .imports import *
from .text import Text
from ..entities.groups import Groups

t = Text()

class Debugger:
    def __init__(self, groups: Groups, clock: pygame.time.Clock) -> None:
        self.groups = self.setup_sprites(groups)
        self.clock = clock

    def setup_sprites(self, groups: Groups) -> Groups:
        def func(instance):
            print(instance.__class__.__qualname__ + " has collided with another sprite.")

        static_sprites = groups.static_sprites
        for sprite in static_sprites:
            sprite.draw_hitbox = True
            sprite.add_on_hit_callback(
                func, True
            )

        dynamic_sprites = groups.dynamic_sprites
        for sprite in dynamic_sprites:
            sprite.draw_hitbox = True
            sprite.add_on_hit_callback(
                func, True
            )

    def toggle_sprites(self, groups: Groups) -> Groups:
        static_sprites = groups.static_sprites
        for sprite in static_sprites:
            sprite.draw_hitbox = False if sprite.draw_hitbox else True

        dynamic_sprites = groups.dynamic_sprites
        for sprite in dynamic_sprites:
            sprite.draw_hitbox = False if sprite.draw_hitbox else True

    def get_fps(self) -> int:
        return int(self.clock.get_fps())

    def draw(self, screen = pygame.Surface) -> None:
        fps = self.get_fps()
        (fps_surface, fps_rect) = t.get_text_object(
            text = fps,
            position = (25, 25),
            alias = True,
            color = (255, 255, 255),
            alpha = True,
            center = True
        )

        screen.blit(fps_surface, fps_rect)

    def update(self) -> None:
        keys = pygame.key.get_just_pressed()

        if keys[pygame.K_h]:
            self.groups = self.toggle_sprites(self.groups)
