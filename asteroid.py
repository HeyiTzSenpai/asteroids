import pygame.draw
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y, radius)
        self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, (254,254,254), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid"
        else:
            random_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_vector1 * 1.2)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_vector2 * 1.2)






