import pygame
import random
from Snek.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLOCK_WIDTH,
    RED,
    GREEN,
    BLUE,
    WHITE,
    BLACK
)


class Food(pygame.sprite.Sprite):
    # Represents the block of food

    def __init__(self):
        # Constructor.  Creates the food block that the snake eats
        super().__init__()
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_WIDTH))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        # Called when the food is eaten
        self.rect.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_WIDTH, BLOCK_WIDTH)
        self.rect.x = random.randrange(0, SCREEN_WIDTH - BLOCK_WIDTH, BLOCK_WIDTH)

