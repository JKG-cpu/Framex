import pygame

from src.frame import Loop
from src.entities import *

l = Loop()

groups = Groups(True)

dynamic_sprite = DynamicEntity(
    position = (50, 50),
    group_ref = groups,
    color = (0, 255, 0),
    center = True,
    player_controlled = True
)

x = 100
for _ in range(10):
    static_sprite = StaticEntity(
        position = (x, 100),
        group_ref = groups,
        color = (255, 0, 0),
        center = True
    )
    groups.add_static(static_sprite)
    x += 140

groups.add_dynamic(dynamic_sprite)

def draw_func(screen: pygame.Surface) -> None:
    groups.draw(screen, dynamic_sprite)

def update_func(dt: float | int) -> None:
    groups.update(dt)

def event_func(events: list[pygame.Event]) -> None:
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                exit()

l.run(draw_func = draw_func, update_func = update_func, event_func = event_func, quit_key = pygame.K_q)
