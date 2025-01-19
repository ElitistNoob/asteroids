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


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius +     right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
        for life in range(self.lifes):
            print(life)
            self.text_renderer.render(screen, "<3", (10 + (life * 40), 50))
        
        if self.is_boosting:
            self.text_renderer.render(screen, "Boosting", ( 10, 10 ))
        else:
            if self.boost_cooldown > 0:
                self.text_renderer.render(screen, "Charging Boost", ( 10, 10 ))
            else:
                self.text_renderer.render(screen, "Boost Ready!", ( 10, 10 ))

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, boost_multiplier = 1.0):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * boost_multiplier

    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y) 
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def boost(self):
        if self.boost_cooldown > 0:
            return

        self.is_boosting = True
        self.boost_timer = BOOST_DURATION
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

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
