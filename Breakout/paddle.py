import pygame

PADDLE_SIZE = (80, 10)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.paddle_width = PADDLE_SIZE[0]
        self.image = pygame.Surface(PADDLE_SIZE)
        self.image.fill('#00f00f')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 435
