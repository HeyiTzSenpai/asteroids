import sys

import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *


def main():
    # initialize all imported pygame modules
    pygame.init()

    # initialize a pygame.time.Clock object to limit framerate
    fps = pygame.time.Clock()

    # represent the amount of time that has passed since the last frame was drawn.
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group

    x = SCREEN_WIDTH / 2
    y = SCREEN_WIDTH / 2
    player = Player(x, y)

    asteroid = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        # This will check if the user has closed the window and exit the game loop if they do.
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        updatable_group.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit(0)

        for drawable in drawable_group:
            drawable.draw(screen)

        # method to refresh the screen.
        pygame.display.flip()
        dt = fps.tick(60) / 1000


# This line ensures the main() function is only called when this file is run directly;
# it won't run if it's imported as a module.

if __name__ == "__main__":
    main()
