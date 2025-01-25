import os
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        self.original_image = pygame.image.load(os.path.join("assets/PNG/Lasers", "laserBlue01.png"))
        self.image = self.original_image
        self.angle = angle

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, -self.angle)
        screen.blit(rotated_image, self.position)

    def update(self, dt, screen):
        self.position += self.velocity * dt
