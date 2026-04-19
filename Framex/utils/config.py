from .imports import *

DEFAULT_WINDOW_SIZE = (750, 500)
DEFAULT_ENTITY_SIZE = (50, 50)
DEFAULT_ENTITY_SPEED = 150

KEYS = {
    "WASD": {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "jump": pygame.K_SPACE
    },
    "ARROW": {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "jump": pygame.K_SPACE
    }
}
VALUES = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

KEY_MODE = "WASD"
KEY_MAP = dict(KEYS[KEY_MODE])

def get_keys() -> list[str]:
     
    return list(KEY_MAP.keys())

def custom_keys(new_keys: dict) -> None:
     
    for key in new_keys.keys():
        if key in KEY_MAP.keys():
            KEY_MAP[key] = new_keys[key]

def set_key_mode(mode: str) -> None:
     
    if mode not in KEYS:
        raise ValueError(f"Unknown key mode '{mode}'. Available: {list(KEYS.keys())}")
    
    KEY_MAP.update(KEYS[mode])
    
    global KEY_MODE
    KEY_MODE = mode

def set_default_window_size(new_size: tuple[int, int]) -> None:
     
    global DEFAULT_WINDOW_SIZE

    if not (
        isinstance(new_size, tuple)
        and len(new_size) == 2
        and all(isinstance(x, int) for x in new_size)
    ):
        raise ValueError(f"Default window size must be tuple[int, int]")
    
    DEFAULT_WINDOW_SIZE = new_size
    
def set_default_entity_size(new_size: tuple[int, int]) -> None:
     
    global DEFAULT_ENTITY_SIZE

    if not (
        isinstance(new_size, tuple)
        and len(new_size) == 2
        and all(isinstance(x, int) for x in new_size)
    ):
        raise ValueError("Default entity size must be tuple[int, int]")

    DEFAULT_ENTITY_SIZE = new_size

def set_default_entity_speed(new_speed: int) -> None:
    if not isinstance(new_speed, int):
        raise ValueError("Default entity speed value must be an int")

    global DEFAULT_ENTITY_SPEED

    DEFAULT_ENTITY_SPEED = new_speed
