import os
import pygame
from circleshape import CircleShape
from shot import Shot
from constants  import BOOST_COOLDOWN, BOOST_DURATION, BOOST_MULTIPLIER, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):    
    def __init__(self, x, y, text_renderer):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.is_boosting = False
        self.shot_timer = 0
        self.boost_timer = 0
        self.boost_cooldown = 0
        self.text_renderer = text_renderer
        self.lifes = 3
        self.original_image = pygame.image.load(os.path.join("assets/PNG", "playerShip1_blue.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        scaled_image = pygame.transform.scale(self.original_image, (32, 32))
        screen.blit(scaled_image, (10, 50))
        self.text_renderer.render(screen, f"x {self.lifes}", (55, 55))
        
        if self.is_boosting:
            self.text_renderer.render(screen, "Boosting", (10, 10))
        else:
            if self.boost_cooldown > 0:
                self.text_renderer.render(screen, "Charging Boost", (10, 10))
            else:
                self.text_renderer.render(screen, "Boost Ready!", (10, 10))

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, dt, boost_multiplier = 1.0):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * boost_multiplier
        self.rect.center = self.position

    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y) 
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def boost(self):
        if self.boost_cooldown > 0:
            return

        self.is_boosting = True
        self.boost_timer = BOOST_DURATION
        
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()

        self.positionWarp(screen)

        if self.is_boosting:
            self.boost_timer -= dt
            self.move(dt, BOOST_MULTIPLIER)
            if self.boost_timer <= 0:
                self.is_boosting = False
                self.boost_timer = 0
                self.boost_cooldown = BOOST_COOLDOWN
        else:
            if self.boost_cooldown > 0:
                self.boost_cooldown -= dt
            else: 
                self.boost_cooldown = 0
        
        if self.shot_timer > 0:
            self.shot_timer -= dt
        else:
            self.shot_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_LSHIFT]:
            self.boost()
