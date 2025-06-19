from constants import *
import pygame
from typing import Tuple
import math
from player import Player

def main() -> None:
    (passnum, failnum) = pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0

    player = Player(math.ceil(SCREEN_WIDTH / 2), math.ceil(SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1017



if __name__ == "__main__":
    main()
