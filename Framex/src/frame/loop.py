from ..utils.imports import *
from .window import Window

class Loop:
    def __init__(
            self,
            caption: str = "Framex Window",
            background_color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
            icon: pygame.Surface | None = None,
            frame_rate: int = 60
        ) -> None:
        self.window = Window(
            caption = caption,
            background_color = background_color,
            icon = icon
        )

        self.fps = frame_rate
        self.clock = pygame.time.Clock()

    def get_window(self) -> pygame.Surface: return self.window
    def get_events(self) -> list[pygame.Event]: return pygame.event.get()

    def quit(self) -> None:
        """Quitting pygame"""
        pygame.quit()
        exit()

    def run(self, quit_key = None) -> None:
        """Run the gameloop"""
        while True:
            self.window.clear()

            events = self.get_events()

            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == quit_key:
                        self.quit()

            self.window.update()
