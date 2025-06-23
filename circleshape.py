import pygame
from typing import Self

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int):
        # we will use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def is_coliding(self, colidingShape: Self) -> bool:
        distance = self.position.distance_to(colidingShape.position)
        return distance < self.radius + colidingShape.radius

    def draw(self, screen: pygame.Surface) -> None:
        # subclasses must override
        pass

    def update(self, dt: float) -> None:
        # subclass must override
        pass




