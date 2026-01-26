# Framex

This is a python module that utilizes pygame-ce. It will just make creating quick test windows a lot easier + you will be able to use it just like a normal pygame window!

```
pip install framex
```

## Example Uses
### Little Red Box
```python
import pygame
from Framex import *

# Create a Window
window = Framex(
    size = (500, 500),
    title = "Little Red Box",
    color = "Black"
)

# Create a little red box
image, rect = create_object(
    image = None,
    pos = (250, 250),
    center = True,
    size = (50, 50),
    srcalpha = True
)
image.fill("Red")

# Get all the items to draw
items = [(image, rect)]

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    window.update(items = items)
```

### Top Down Character
```python
import pygame
from Framex import *

# Create a window
window = Framex(
    size = (500, 500),
    title = "Top Down Character",
    color = "Black"
)

# Create a clock for dt
clock = pygame.time.Clock()

# Create a top down character
sprites = pygame.sprite.Group()

character = TopDownEntity(
    image = None,
    pos = (250, 250),
    group = sprites,
    color = "red",
    center = True,
    size = (50, 50),
    srcalpha = True,
    movement_type = "WASD",
    speed = 250
)

# Get all the items to draw
items = [(character.image, character.rect)]

# Game Loop
while True:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    sprites.draw(window.screen)
    sprites.update(dt)

    window.update(items = items)
```