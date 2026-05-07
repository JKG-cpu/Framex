# Framex

A game engine built off of pygame-ce. Created specifically to spin up quick testing worlds or to make actual games.

## Installation

```bash
pip install framex-ce

# This should auto install pygame-ce, if not, run
pip install pygame-ce
```

## Usage

#### A starting window (500x500) 
```python
from Framex import *

loop = Loop(
    caption = "My First Framex Window",
    background_color = (15, 15, 15),
    size = (500, 500),
    frame_rate = 60
)

loop.run()
```

#### A Custom quit key
```python
import pygame
from Framex import *

loop = Loop(
    caption = "My First Framex Window",
    background_color = (15, 15, 15),
    size = (500, 500),
    frame_rate = 60
)

loop.run(
    quit_key = pygame.K_q
)
```

#### A Simple player controlled Character
```python
import pygame
from Framex import *

loop = Loop(
    caption = "My First Framex Window",
    background_color = (15, 15, 15),
    size = (500, 500),
    frame_rate = 60
)

groups = Groups(
    zorder = True
)

player = DynamicEntity(
    position = (50, 50),
    group_ref = groups,
    color = (0, 255, 0),
    center = True,
    player_controlled = True
)
groups.add_dynamic(player)

def draw_func(screen: pygame.Surface, camera: None | Camera):
    groups.draw(screen = screen, camera = camera)

def update_func(dt: float):
    groups.update(dt = dt)

loop.run(
    draw_func = draw_func,
    update_func = update_func,
    quit_key = pygame.K_q
)
```

#### Some static entities with a camera
```python
import pygame

from Framex import *

l = Loop()

groups = Groups(True)

player = DynamicEntity(
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

groups.add_dynamic(player)

def draw_func(screen: pygame.Surface, camera) -> None:
    groups.draw(screen, camera)

def update_func(dt: float | int) -> None:
    groups.update(dt)

camera = Camera("lerp")
camera.set_target(player)

l.run(
    draw_func = draw_func, 
    update_func = update_func, 
    camera = camera, 
    quit_key = pygame.K_q)
```

#### More Tutorials
Some more tutorials will be added [here](https://github.com/JKG-cpu/Framex/tree/main/docs) soon!