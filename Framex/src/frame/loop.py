from typing import Literal

from ..utils.imports import *
from .window import Window
from .camera import Camera

class Loop:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
            icon: pygame.Surface | None = None,
            size: tuple[int, int] = (750, 500),
            frame_rate: int = 60
        ) -> None:
        self.window = Window(
            caption = caption,
            background_color = background_color,
            icon = icon,
            size = size
        )

        self.fps = frame_rate
        self.clock = pygame.time.Clock()
        self.dt = 0

    def get_window(self) -> pygame.Surface: return self.window
    def get_events(self) -> list[pygame.Event]: return pygame.event.get()
    def get_dt(self) -> float | int: return self.dt

    def quit(self) -> None:
        """Quitting pygame"""
        pygame.quit()
        exit()

    def run(self, draw_func: Callable | None = None, event_func: Callable | None = None, update_func: Callable | None = None, camera: Camera | None = None, quit_key = None) -> None:
        """Run the gameloop"""
        if draw_func:
            if (not callable(draw_func)) or not (len(signature(draw_func).parameters) == 2):
                raise TypeError("draw_func must be a function or method with a parameter for the window and camera position!")

        if event_func:
            if (not callable(event_func)) or not (len(signature(event_func).parameters) == 1):
                raise TypeError("event_func must be a function or a method with a parameter for events!")

        if update_func:
            if (not callable(update_func)) or not (len(signature(update_func).parameters) == 1):
                raise TypeError("update_func must be a function or method with a parameter for delta time!")

        while True:
            self.window.clear()

            self.dt = self.clock.tick(self.fps) / 1000 if self.fps else self.clock.tick() / 1000

            events = self.get_events()

            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == quit_key:
                        self.quit()

            if camera: camera.update(self.dt, self.window.get_screen())
            if draw_func: draw_func(self.window.get_screen(), camera)
            if update_func: update_func(self.dt)
            if event_func: event_func(events)

            self.window.update()

