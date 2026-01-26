from .imports import *

class Framex:
    """Lightweight pygame-ce window wrapper"""

    def __init__(self, size: tuple[int, int], title: str = "pygame window", color: str | tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0)):
        """
        Create a Framex window wrapper.

        ARGS
            size: Window size as ```(width, height)```.
            color: Set the window color
            title: Window Caption
        """
        self.screen = self._create_display(size = size)
        self.screen.fill(color)
        pygame.display.set_caption(title)

        self.color = color

    # Surfaces
    def _create_display(self, size: tuple[int, int]) -> pygame.Surface:
        """
        Creates a Display

        ARGS
            size: Window size as ```(width, height)```
        """
        return pygame.display.set_mode(size)

    @staticmethod
    def _create_surface(size: tuple[int, int], srcalpha: bool = False) -> pygame.Surface:
        """
        Creates a Surface that automatically uses .convert_alpha()

        ARGS
            size: Surface size as ```(width, height)```
            srcalpha: Passes the flag SRCALPHA to the Surface
        """
        return pygame.Surface(size).convert_alpha() if not srcalpha else pygame.Surface(size, pygame.SRCALPHA).convert_alpha()

    def create_surface(self, size: tuple[int, int], srcalpha: bool = False) -> pygame.Surface:
        """
        Creates a Surface that automatically uses .convert_alpha()

        ARGS
            size: Surface size as ```(width, height)```
            srcalpha: Passes the flag SRCALPHA to the Surface
        """
        return self._create_surface(size, srcalpha)

    # Update
    def update(self, items: list[pygame.Surface, pygame.Rect] | list[pygame.Surface, tuple[int, int]]) -> None:
        """
        Draw items to the screen

        ARGS
            items: A list of items you want to blit. Used as ```[surface, rect object or (x, y)] | [surface, rect object or (x, y)]```
        """
        self.screen.fill(self.color)

        for item in items:
            if not isinstance(item[0], pygame.Surface):
                raise TypeError(f"First element must be pygame.Surface, got {type(item[0])}")
            
            if not isinstance(item[1], (pygame.Rect, pygame.FRect, tuple)):
                raise TypeError(f"Second element must be pygame.Rect or tuple[int,int], got {type(item[1])}")

            surface = item[0]
            pos = item[1]
            
            # Get Blit position
            blit_pos = pos.topleft if isinstance(pos, pygame.Rect) else pos
            
            self.screen.blit(surface, blit_pos)
        
        pygame.display.update()