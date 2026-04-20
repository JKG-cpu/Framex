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
        while True:
            self.tick()
            events = self.poll_events()

            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == quit_key:
                        exit()

            event_fn(events)
            update_fn(self.dt)
            draw_fn(self.screen)
            self.screen.update()

    