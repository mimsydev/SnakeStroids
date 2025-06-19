from pygame.math import Vector2
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from typing import Tuple
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x,y, PLAYER_RADIUS)

        self.rotation: float = 0

    def triangle(self) -> list[Vector2]:
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen: pygame.Surface)-> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: float) -> None:
        forward: pygame.Vector2 = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
