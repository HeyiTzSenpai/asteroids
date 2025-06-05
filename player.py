import os

import pygame.draw

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import *


class Player(CircleShape):
    HIGH_SCORE_FILE = "highscore.txt"

    timer = 0
    score = 0
    high_score = 0



    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.score = 0


    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0.0:
                self.shoot()
                self.timer = PLAYER_SHOT_COOLDOWN




    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        velocity = pygame.Vector2(0,-1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot_obj = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)

    @classmethod
    def load_high_score(cls):
        if os.path.exists(cls.HIGH_SCORE_FILE):
            with open(cls.HIGH_SCORE_FILE, "r") as f:
                try:
                    cls.high_score = int(f.read().strip())
                except:
                    cls.high_score = 0
        else:
            cls.high_score = 0

    @classmethod
    def save_high_score(cls):
        with open(cls.HIGH_SCORE_FILE, "w") as f:
            f.write(str(cls.high_score))


    def increment_score(self):
        self.score += 1
        if self.score > Player.high_score:
            Player.high_score = self.score
            Player.save_high_score()

    def get_high_score(self):
        return f"Your high score is: {Player.high_score}"


