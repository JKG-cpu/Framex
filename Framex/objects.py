from .imports import *
from .frame import Framex

# Be able to add Entities

def create_object(image: pygame.Surface | None, pos: tuple[int, int], center: bool = False, size: tuple[int, int] = (50, 50), srcalpha: bool = False) -> list[pygame.Surface, pygame.Rect]:
    """
    Creates a basic object

    ARGS
        image: The surface you want to render, if None then creates a blank surface
        pos: The position of your object
        center: If you want the object to be centered at that position (Defaults to False)
        size: The size you want your surface to be
        srcalpha: Makes your surface has the pygame.SRCALPHA flag
    """
    image = image if image else Framex._create_surface(size, srcalpha)
    rect = image.get_frect(topleft = pos) if not center else image.get_frect(center = pos)
    return [image, rect]

class TopDownEntity(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface | None, pos: tuple[int, int], group: pygame.sprite.Group, collision_sprites: pygame.sprite.Group | None = None, color: str | tuple[int, int, int] | tuple[int, int, int, int] = None, center: bool = False, size: tuple[int, int] = (50, 50), srcalpha: bool = False, movement_type: str = "ARRW", speed: int = 250, screen_collision: bool = False) -> None:
        """
        Ceates a basic entitiy that is NOT animated
        
        ARGS
            image: The surface you want to render, if None then creates a blank surface
            pos: The position of your object
            group: The group for your sprite
            collision_sprites: This is a pygame.sprite.Group that adds your sprite to the collision sprite group (optional)
            color: The color of the sprite, Defaults to None
            center: If you want the object to be centered at that position (Defaults to False)
            size: The size you want your surface to be
            srcalpha: Makes your surface has the pygame.SRCALPHA flag
            movement_type: This sets the key input for movement, defaults to arrow keys ("ARRW") but can be changed to WASD ("WASD")
            speed: The speed of the entitiy
        """
        if collision_sprites:
            super().__init__(group, collision_sprites)
        
        else:
            super().__init__(group)

        self.collision_sprites = collision_sprites

        self.image, self.rect = create_object(image, pos, center, size, srcalpha)
        
        if color:
            self.image.fill(color)

        self.movement_direction = vector()
        self.movement_type = movement_type
        self.speed = speed
        self.screen_collision = screen_collision
        self.screen = pygame.display.get_surface()
        
    def switch_movement_type(self, new_type: str = "ARRW") -> None:
        """
        Switch the input keys for movement

        ARGS
            new_type: The keys you want, either arrow keys ("ARRW") or WASD ("WASD"). Defaults to arrow keys
        """
        self.movement_type = new_type if new_type == "ARRW" or new_type == "WASD" else "ARRW"
    
    def input(self) -> None:
        """
        This gets user input
        """
        keys = pygame.key.get_pressed()
        temp_vector = vector()

        if self.movement_type == "ARRW":
            if keys[pygame.K_LEFT]:
                temp_vector.x -= 1
            
            if keys[pygame.K_RIGHT]:
                temp_vector.x += 1
            
            if keys[pygame.K_UP]:
                temp_vector.y -= 1
            
            if keys[pygame.K_DOWN]:
                temp_vector.y += 1

        else:
            if keys[pygame.K_a]:
                temp_vector.x -= 1
            
            if keys[pygame.K_d]:
                temp_vector.x += 1
            
            if keys[pygame.K_w]:
                temp_vector.y -= 1
            
            if keys[pygame.K_s]:
                temp_vector.y += 1

        self.movement_direction = temp_vector.normalize() if temp_vector else temp_vector
    
    def move(self, dt: float) -> None:
        """
        This moves the Entitiy

        ARGS
            dt: Delta Time
        """
        self.rect.centerx += self.movement_direction.x * self.speed * dt
        self.check_collisions('x')
    
        self.rect.centery += self.movement_direction.y * self.speed * dt
        self.check_collisions('y')
    
    def check_collisions(self, axis: str):
        """
        This checks if the sprite collides with any other objects (in collision sprites)

        ARGS
            axis: The axis to check (x, y)
        """
        if self.collision_sprites:
            for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.rect):
                    if axis == "x":
                        if self.movement_direction.x > 0:
                            self.rect.right = sprite.rect.left
                        
                        if self.movement_direction.x < 0:
                            self.rect.left = sprite.rect.right
                
                        self.rect.centerx = sprite.rect.centerx

                    else:
                        if self.movement_direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        
                        if self.movement_direction.y < 0:
                            self.rect.top = sprite.rect.bottom
                        
                        self.rect.centery = sprite.rect.centery
        
        # Screen Collision
        if self.screen_collision:
            if self.rect.left <= 0:
                self.rect.left = 0
            
            if self.rect.right >= self.screen.get_width():
                self.rect.right = self.screen.get_width()

            if self.rect.top <= 0:
                self.rect.top = 0
            
            if self.rect.bottom >= self.screen.get_height():
                self.rect.bottom = self.screen.get_height()

    def update(self, dt: float):
        """
        This updates the entity (DOES NOT DRAW)

        ARGS
            dt: Delta Time
        """
        self.input()
        self.move(dt)

