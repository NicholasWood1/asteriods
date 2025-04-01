from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def collision(self, other):
        if pygame.math.Vector2.distance_to(self.position, other.position) < self.radius + other.radius:
            return True
        else:
            return False

    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        else:
             angle = random.uniform(20, 50)
             
             first_vel = self.velocity.rotate(angle)
             second_vel = self.velocity.rotate(-angle)

             new_radii = self.radius - ASTEROID_MIN_RADIUS

             first = Asteroid(self.position.x, self.position.y, new_radii)
             second = Asteroid(self.position.x, self.position.y, new_radii)

             first.velocity = 1.2*first_vel
             second.velocity = 1.2*second_vel

