from constants import *
import pygame
from typing import Tuple

def main() -> None:
    (passnum, failnum) = pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
