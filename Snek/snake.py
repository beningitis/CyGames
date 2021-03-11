import pygame

from main import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.x_velocity = 0;
        self.y_velocity = 0;
        self.surf = pygame.Surface((24, 24))
        self.surf.fill('#ffffff')
        self.rect = self.surf.get_rect()
        self.trail = []

    def update(self, pressed_keys):
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        if pressed_keys[K_UP]:
            self.y_velocity = -24
            self.x_velocity = 0
        if pressed_keys[K_DOWN]:
            self.y_velocity = 24
            self.x_velocity = 0
        if pressed_keys[K_LEFT]:
            self.x_velocity = -24
            self.y_velocity = 0
        if pressed_keys[K_RIGHT]:
            self.x_velocity = 24
            self.y_velocity = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
