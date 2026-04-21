import pygame

from src.frame import Loop
from src.entities import *

l = Loop()

groups = Groups(True)

dynamic_sprite = DynamicEntity(
    position = (50, 50),
    color = (0, 255, 0),
    center = True,
    player_controlled = True
)

static_sprite = StaticEntity(
    position = (100, 100),
    color = (255, 0, 0),
    center = True
)

groups.add_dynamic(dynamic_sprite)
groups.add_static(static_sprite)

def draw_func(screen: pygame.Surface) -> None:
    groups.draw(screen)

def update_func(dt: float | int) -> None:
    groups.update(dt)

l.run(draw_func = draw_func, update_func = update_func, quit_key = pygame.K_q)