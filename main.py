import pygame
import sys
from asteroidfield import AsteroidField
from asteroids import Asteroids
from rendertext import TextRenderer
from shot import Shot
from constants import *
from player import Player

def main():
    pygame.init()
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0,0))
    screen_size = pygame.display.get_desktop_sizes()
    screen_width = screen_size[0][0]
    screen_height = screen_size[0][1]
    text_renderer = TextRenderer()
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(screen_width / 2 ,screen_height / 2, text_renderer)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            for shot in shots:
                if shot.isColliding(obj):
                    shot.kill()
                    obj.split()

            if obj.isColliding(player):
                print(player.lifes)
                if player.lifes >= 1: 
                    player.position = pygame.Vector2(screen_width / 2, screen_height / 2)
                    player.lifes -= 1
                    pygame.time.delay(1000)
                else:
                    print("Game Over")
                    pygame.quit()

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
