from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random
    
class Asteroids(CircleShape):
    def __init__(self, x, y, radius, meteor):
        super().__init__(x, y, radius)
        self.meteor = meteor
        self.has_been_on_screen = False
        self.kind = None

        if ASTEROID_MIN_RADIUS * 1 == self.radius:
            self.kind = "small"
        elif ASTEROID_MIN_RADIUS * 2 == self.radius:
            self.kind = "med"
        elif ASTEROID_MIN_RADIUS * 3 == self.radius:
            self.kind = "big"

        self.index = random.randint(0, len(self.meteor[self.kind]) - 1)


    def get_random_int(self, arr):
        return random.randint(0, len(arr) - 1)

    def draw(self, screen):
        screen.blit(self.meteor[self.kind][self.index], self.position)

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

        asteroid_a = Asteroids(self.position.x, self.position.y, new_radius, self.meteor)
        asteroid_a.velocity = v_a * 1.2
        asteroid_b = Asteroids(self.position.x, self.position.y, new_radius, self.meteor)
        asteroid_b.velocity = v_b * 1.2
