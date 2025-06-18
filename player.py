from pygame.math import Vector2
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from typing import Tuple
import pygame

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x,y, PLAYER_RADIUS)

        self.rotation: int = 0

    def triangle(self) -> list[Vector2]:
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

