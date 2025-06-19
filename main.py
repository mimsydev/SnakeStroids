import pygame
import math
import asteroidfield
from constants import *
from typing import Tuple
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main() -> None:
    (passnum, failnum) = pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0
    # Setup Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(math.ceil(SCREEN_WIDTH / 2), math.ceil(SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1017



if __name__ == "__main__":
    main()
