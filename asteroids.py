import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random
    
class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

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
