import pygame
import random
from typing import Self
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x,y,radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        departure_angle = random.uniform(20, 50)
        departure_vel_1 = self.velocity.rotate(departure_angle)
        departure_vel_2 = self.velocity.rotate(departure_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = departure_vel_1 * 1.2
        asteroid2.velocity = departure_vel_2 * 1.2
