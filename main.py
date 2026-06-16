import pygame
import sys
from logger import log_event
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    player_one = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    print("Starting Asteroids with pygame version: VERSION")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


    while(True):
        dt = clock.tick(60) / 1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player_one.update(dt)
        # player_one.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player_one):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        print(dt)


if __name__ == "__main__":
    main()

