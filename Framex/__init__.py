"""
Framex/__init__.py
==================
Public API entry point for the Framex package.

Defines what users can import via `from Framex import ...`.
Re-exports the main classes and functions from internal modules
so users don't need to know the internal file structure.

Expected exports:
    - Framex          : Main class (composes window, loop, groups, debug)
    - create_object   : Factory for quick (surface, rect) pairs
    - TopDownEntity   : Pre-built dynamic entity with movement
    - Entity          : Base sprite class
    - StaticEntity    : Non-moving collision entity (walls, floors)
    - FramexGroup     : Sprite group with static/dynamic separation
    - DebugOverlay    : Hitbox + FPS debug rendering
    - KEYMAPS         : Default keymap presets (WASD, ARROW)
"""
from .core import *
from .entities import *
from .physics import *
from .utils import *
from .main import Frame
