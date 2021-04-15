import pygame
import math

BALL_SIZE = 6


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill('#ffffff')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_velocity = 10
        self.y_velocity = -10
        self.speed = math.sqrt((self.x_velocity ** 2) + (self.y_velocity ** 2))

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity
        self.speed = math.sqrt((self.x_velocity ** 2) + (self.y_velocity ** 2))
