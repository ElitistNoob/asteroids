import pygame
import os
from asteroidfield import AsteroidField
from asteroids import Asteroids
from rendertext import TextRenderer
from shot import Shot
from constants import *
from player import Player

def main():
    pygame.init()
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((0,0), flags)
    screen_size = pygame.display.get_desktop_sizes()
    screen_width = screen_size[0][0]
    screen_height = screen_size[0][1]
    text_renderer = TextRenderer()
    clock = pygame.time.Clock()
    assets = os.path.join(os.path.dirname(__file__), "assets")
    background_image = pygame.image.load(os.path.join(assets, "Backgrounds", "black.png"))
    bg_width = background_image.get_width()
    bg_height = background_image.get_height()

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
    bg_x = 0
    bg_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        for obj in updatable:
            obj.update(dt, screen)

        for obj in asteroids:
            for shot in shots:
                if shot.isColliding(obj):
                    shot.kill()
                    obj.split()

            if obj.isColliding(player):
                if player.lifes >= 2: 
                    player.position = pygame.Vector2(screen_width / 2, screen_height / 2)
                    player.lifes -= 1
                    pygame.time.delay(1000)
                else:
                    print("Game Over")
                    pygame.quit()

        for x in range(0, screen_width // bg_width + 2):
            for y in range(0, screen_height // bg_height + 2):
                screen.blit(background_image, (bg_x + x * bg_width, bg_y + y * bg_height))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
