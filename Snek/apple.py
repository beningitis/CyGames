import pygame
import random

import main


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        self.surf = pygame.Surface((24, 24))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.new_position()
        self.normalize_position()

    # Rounds the position coordinates to the nearest 24 to make it in line with the Snake

    def normalize_position(self):
        if self.rect.x % 24 != 0:
            self.rect.x += (24 - self.rect.x)

        if self.rect.y % 24 != 0:
            self.rect.y += (24 - self.rect.y)

    def new_position(self):
        self.rect.x = random.randint(0, main.SCREEN_WIDTH - 24)
        self.rect.y = random.randint(0, main.SCREEN_HEIGHT - 24)
        self.normalize_position()


