
import pygame

BRICK_SIZE = (20, 60)


class Brick(pygame.sprite.Sprite):
    def __init(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface(BRICK_SIZE)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
