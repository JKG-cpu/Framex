from os.path import join

from ..utils import *
from ..utils.imports import *

class Window:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
            icon: pygame.Surface | None = None
        ) -> None:
        """Base class for creating a screen"""
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.screen.fill(background_color)
        pygame.display.set_caption(caption)

        if icon:
            pygame.display.set_icon(icon)
        
        else:
            pygame.display.set_icon(create_surface(image = join("src", "images", "logo.png"), alpha = True))
    
        self.background_color = background_color

    def get_screen(self) -> pygame.Surface: return self.screen
    def clear(self) -> None: self.screen.fill(self.background_color)
    def update(self) -> None: pygame.display.flip()
    def draw(self, surface: pygame.Surface, position: tuple[int, int] | pygame.Rect) -> None: self.screen.blit(surface, position)
