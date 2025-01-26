import pygame
import os
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random
    
class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.has_been_on_screen = False
        self.image_dir = os.path.join(os.path.dirname(__file__), "assets/PNG/Meteors")
        self.small1_image = pygame.image.load(os.path.join(self.image_dir, "meteorBrown_small1.png"))
        self.med1_image = pygame.image.load(os.path.join(self.image_dir, "meteorBrown_med1.png"))
        self.big1_image = pygame.image.load(os.path.join(self.image_dir, "meteorBrown_big1.png"))

    def draw(self, screen):
        if self.radius == ASTEROID_MIN_RADIUS * 1:
            screen.blit(self.small1_image, self.position)
        elif self.radius == ASTEROID_MIN_RADIUS * 2:
            screen.blit(self.med1_image, self.position)
        else:
            screen.blit(self.big1_image, self.position)

    def update(self, dt, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        self.position += self.velocity * dt

        if self.position[0] >= 0 and self.position[0] < screen_width and self.position[1] >= 0 and self.position[1] < screen_height:
            self.has_been_on_screen = True

        if self.has_been_on_screen:
            self.positionWarp(screen)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        v_a = self.velocity.rotate(angle)
        v_b = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = v_a * 1.2
        asteroid_b = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = v_b * 1.2
