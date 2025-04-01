import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5
    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def collision(self, other):
        if pygame.math.Vector2.distance_to(self.position, other.position) < self.radius + other.radius:
            return True
        else:
            return False