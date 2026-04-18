"""
Framex/loop.py
==============
Manages the game loop, clock, delta time, and event handling.

ROADMAP ITEM #1 — Internal Delta Time Handling:
    Instead of making the user calculate and pass dt every frame,
    the loop owns the clock and stores dt as a property. Entities
    simply reference the loop instance to get the current dt.

Responsibilities:
    - Owning pygame.time.Clock() and calling tick() each frame
    - Storing self.dt (delta time in seconds) as a property
    - Polling pygame events and handling QUIT
    - Providing a run() method that drives the main loop
    - Calling hooks: update(dt), draw(), and event callbacks

Used by:
    - main.py (calls run() to start the application)
    - entities.py (reads loop.dt for movement calculations)
    - debug.py (reads loop.clock.get_fps() for FPS overlay)
"""
from ..utils.imports import *
from .window import Window

class Loop:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | str = (0, 0, 0),
            icon: pygame.Surface | None = None,
            frame_rate: int | None = 60
        ):
        self.screen = Window(
            caption = caption,
            background_color = background_color,
            icon = icon
        )

        self.clock = pygame.time.Clock()
        self.fps = frame_rate
        self.dt = 0
    
    def get_dt(self) -> float: return self.dt
    def tick(self) -> None: 
        self.dt = self.clock.tick(self.fps) / 1000
    def poll_events(self) -> list[pygame.Event]: return pygame.event.get()
    def get_window(self) -> pygame.Surface: return self.screen

    def run(self, update_fn, draw_fn, event_fn, quit_key: pygame.key = pygame.K_q) -> None:
        """
        Loop to run the game
        """
        while True:
            self.tick()
            events = self.poll_events()

            if any(e.type == quit_key for e in events) or any(e.key == quit_key for e in events):
                break

            event_fn(events)
            update_fn(self.dt)
            draw_fn(self.screen)
            self.screen.update()