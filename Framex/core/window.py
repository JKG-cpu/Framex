"""
Framex/window.py
================
Handles all pygame display and surface operations.

This module wraps pygame.display in a clean interface so users
don't need to call pygame directly for basic window operations.

Responsibilities:
    - Creating the display surface (pygame.display.set_mode)
    - Setting window title and icon
    - Creating surfaces with proper convert_alpha() handling
    - Managing background color and screen clearing
    - Exposing the screen surface for external drawing

Used by:
    - FramexLoop (clears screen each frame, draws to surface)
    - entities.py (gets screen dimensions for boundary clamping)
    - debug.py (renders overlay onto the screen surface)
"""
from ..utils.imports import *
from ..utils.config import *

class Window:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | str = (0, 0, 0),
            icon: pygame.Surface | None = None
        ):
        self.screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
        self.screen.fill(background_color)

        pygame.display.set_caption(caption)
        if icon:
            pygame.display.set_icon(icon)

        self.background_color = background_color

    # Basic Methods
    def clear(self) -> None: self.screen.fill(self.background_color)
    def update(self) -> None: pygame.display.update()
    def fill(self, color: tuple[int, int, int] | str) -> None: self.screen.fill(color)
    def draw(self, surface: pygame.Surface, position: tuple[int, int]) -> None: self.screen.blit(surface, position)
    def get_screen(self) -> pygame.Surface: return self.screen

    # Creating Surfaces
    def create_surface(
        self,
        size: tuple[int, int],
        color: tuple[int, int, int, int] | tuple[int, int, int] | None = None,
        alpha: bool = True
    ) -> None:
        if alpha:
            surface = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()

        else:
            surface = pygame.Surface(size).convert()
        
        if color is not None:
            surface.fill(color)
        
        return surface

