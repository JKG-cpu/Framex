from .imports import *
from .factories import Factory

factory = Factory()

class Text:
    def __init__(self, font_file_path: str | None = None, size: int = 20) -> None:
        self.font = pygame.font.Font(font_file_path, size)
    
    def get_text_object(
            self, 
            text: str, 
            position: tuple[int, int],
            alias: bool = True, 
            color: tuple[int, int, int] | tuple[int, int, int, int] = (0, 0, 0),
            alpha: bool = True,
            center: bool = True) -> tuple[pygame.Surface, pygame.Rect]:
        image = self.font.render(text, alias, color).convert_alpha() if alpha else self.font.render(text, alias, color).convert()
        return (
            image,
            factory.create_rect(
                image = image,
                position = position,
                center = center
            )
        )
    