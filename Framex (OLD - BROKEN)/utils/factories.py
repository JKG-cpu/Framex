 
from .imports import *
from .config import *

class Factory:
    def create_surface(self, image: pygame.Surface | str | None = None, color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0), alpha: bool = False) -> pygame.Surface:
        if image is not None:
            if isinstance(image, str):
                return pygame.image.load(image).convert_alpha() if alpha else pygame.image.load(image).convert_alpha()
            elif isinstance(image, pygame.Surface):
                return image.convert_alpha() if alpha else image.convert()

        surf = pygame.Surface(DEFAULT_ENTITY_SIZE, pygame.SRCALPHA if alpha else 0)
        surf.fill(color)
        return surf.convert_alpha() if alpha else surf.convert()
        
    def create_rect(self, image: pygame.Surface, position: tuple[int, int], center: bool = False) -> pygame.Rect:
        return image.get_frect(center = position) if center else image.get_frect(topleft = position)

    def create_object(
            self,
            image: pygame.Surface | None = None,
            color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
            alpha: bool = False,
            position: tuple[int, int] = (0, 0),
            center: bool = False
        ) -> tuple[pygame.Surface, pygame.Rect]:
        surface = self.create_surface(
            image = image,
            color = color,
            alpha = alpha
        )
        rect = self.create_rect(
            image = surface,
            position = position,
            center = center
        )

        return (surface, rect)
