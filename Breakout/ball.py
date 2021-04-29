import pygame
import math
import side_collisions

BALL_SIZE = 6


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.moving = False
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill('#ffffff')
        self.size = BALL_SIZE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = side_collisions.Velocity((0,0))
        self.speed = math.sqrt((self.velocity.x ** 2) + (self.velocity.y ** 2))

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        self.speed = math.sqrt((self.velocity.x ** 2) + (self.velocity.y ** 2))

    def bounce(self, collide_top, collide_bottom, collide_left, collide_right):
        if collide_top or collide_bottom:
            self.velocity.y *= -1
        if collide_left or collide_right:
            self.velocity.x *= -1
        if (collide_top and collide_left) or (collide_top and collide_right):
            self.velocity.x *= -1
        if (collide_bottom and collide_left) or (collide_bottom and collide_right):
            self.velocity.x *= -1

    def release(self):
        if self.moving == False:
            self.moving = True
            self.velocity = side_collisions.Velocity((4, -4))