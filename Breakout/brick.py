
import pygame
import side_collisions

BRICK_SIZE = (60, 20)


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface(BRICK_SIZE)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = side_collisions.Velocity((0, 0))
