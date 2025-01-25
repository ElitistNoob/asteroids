import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius=0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius =  radius

    def draw(self, screen):
        pass

    def update(self, dt, screen):
        pass

    def positionWarp(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        if self.position[0] >= screen_width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = screen_width

        if self.position[1] >= screen_height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = screen_height

    def isColliding(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        if distance <= self.radius + CircleShape.radius:
            return True
        else:
            return False
