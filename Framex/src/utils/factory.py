from .imports import *

__all__ = [
    "create_surface",
    "create_rect",
    "create_object"
]

def create_surface(
        size: tuple[int, int] = (50, 50),
        image: None | str = None,
        background_color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
        alpha: bool = True
    ) -> pygame.Surface:
    """
    Create a simple pygame.Surface

    ARGS
        size: Surface size (only matters if image = None)
        image: Image you would like to load (PATH)
        background_color: Image background color
        alpha: Whether or not to use pygame.SRCALPHA + .convert_alpha()
    """
    if image:
        surface = pygame.image.load(image)
    else:
        surface = pygame.Surface(size) if not alpha else pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
        surface.fill(background_color)

    return surface

def create_rect(
        surface: pygame.Surface,
        position: tuple[int, int],
        center: bool = True
    ) -> pygame.Rect:
    """
    Creates a pygame.Rect object based off of a pygame.Surface

    ARGS
        surface: The surface to use
        position: The position of the rect
        center: Whether or not to center the rect
    """
    return surface.get_frect(center = position) if center else surface.get_frect(topleft = position)

def create_object(
        position: tuple[int, int],
        center: bool = True,
        size: tuple[int, int] = (50, 50),
        image: None | str = None,
        background_color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
        alpha: bool = True
    ) -> tuple[pygame.Surface, pygame.Rect]:
    """
    This creates a pygame.Surface + pygame.Rect for you

    Uses create_surface() + create_rect()
    """
    surface = create_surface(
        size = size,
        image = image,
        background_color = background_color,
        alpha = alpha
    )
    rect = create_rect(
        surface = surface,
        position = position,
        center = center
    )

    return (surface, rect)