import pygame
from pygame.math import Vector2 as vector
from collections.abc import Callable
from inspect import signature

pygame.init()

__all__ = [
    "pygame",
    "vector",
    "Callable",
    "signature"
]