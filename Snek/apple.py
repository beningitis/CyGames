import pygame
import random

import main


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        self.surf = pygame.Surface((24, 24))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.x_pos = 0
        self.y_pos = 0
        self.new_position()
        self.normalize_position()

    # Rounds the position coordinates to the nearest 24 to make it in line with the Snake

    def normalize_position(self):
        if self.x_pos % 24 != 0:
            self.x_pos += (24 - self.x_pos)

        if self.y_pos % 24 != 0:
            self.y_pos += (24 - self.y_pos)

    def new_position(self):
        self.x_pos = random.randint(0, main.SCREEN_WIDTH - 24)
        self.y_pos = random.randint(0, main.SCREEN_HEIGHT - 24)

