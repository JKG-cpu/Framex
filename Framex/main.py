from .core import *
from .entities import *
from .physics import *
from .utils import *

class Frame:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | str = (0, 0, 0),
            icon: pygame.Surface | None = None,
            fps: int = 60,
            zorder: bool = True
        ) -> None:
        self.window = None
        self.loop = None
        self.groups = None
        self.debugOverlay = None
        self.setup(caption, background_color, icon, fps, zorder)

        self.update_fn = lambda dt: self.groups.update(dt)
        self.draw_fn = lambda screen: self.groups.draw(screen)
        self.event_fn = lambda events: 0
        self.quit_key = pygame.K_q

    def setup(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | str = (0, 0, 0),
            icon: pygame.Surface | None = None,
            fps: int = 60,
            zorder: bool = True
        ) -> None:
        self.loop = Loop(
            caption = caption,
            background_color = background_color,
            icon = icon,
            fps = fps
        )
        self.window = self.loop.get_window()

        self.groups = Groups(zorder)
        self.debugOverlay = Debugger(
            groups = self.groups, clock = self.loop.clock
        )

    def set_quit_key(self, key: pygame.key) -> None:
        if isinstance(key, pygame.key):
            self.quit_key = key
        else:
            raise TypeError(f"Must use a pygame.key object as a quit key.")

    def set_update_fn(self, func):
        if callable(func):
            self.update_fn = func
        else:
            raise TypeError("Must pass in a function for update_fn")

    def set_draw_fn(self, func):
        if callable(func):
            self.draw_fn = func
        else:
            raise TypeError("Must pass in a function for draw_fn")

    def set_event_fn(self, func):
        if callable(func):
            self.event_fn = func
        else:
            raise TypeError("Must pass in a function for event_fn")

    def run(self, debug: bool = False) -> None:
        self.loop.run(
            update_fn = self.update_fn,
            draw_fn = self.draw_fn,
            event_fn = self.event_fn,
            quit_key = self.quit_key
        )