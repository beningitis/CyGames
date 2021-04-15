import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_WIDTH])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Snake(pygame.sprite.Sprite):
    # Represents the snake

    def __init__(self):
        super().__init__()

        self.snakeBodySpriteGroup = pygame.sprite.Group()
        self.snake_body = []
        self.x_velocity = 24
        self.y_velocity = 0

        # Snake does not move initially
        for i in range(2):
            x = SCREEN_WIDTH // 2 - BLOCK_WIDTH // 2 - BLOCK_WIDTH * i
            y = SCREEN_HEIGHT // 2 - BLOCK_WIDTH // 2
            block = Block(x, y)
            self.snake_body.append(block)
            self.snakeBodySpriteGroup.add(block)

        # loads the high score data from file
        # self.load_data()

    def update(self, pressed_keys):

        # self.rect.move_ip(self.x_velocity, self.y_velocity)
        # self.body[0][0] += self.x_velocity
        # self.body[0][1] += self.y_velocity

        # Prevent snake from going off screen

        if self.snake_body[0].rect.x < 0:
            self.snake_body[0].rect.x = 0
        if self.snake_body[0].rect.x > SCREEN_WIDTH - BLOCK_WIDTH:
            self.snake_body[0].rect.x = SCREEN_WIDTH - BLOCK_WIDTH
        if self.snake_body[0].rect.y < 0:
            self.snake_body[0].rect.y = 0
        if self.snake_body[0].rect.y > SCREEN_HEIGHT - BLOCK_WIDTH:
            self.snake_body[0].rect.y = SCREEN_HEIGHT - BLOCK_WIDTH

        if pressed_keys[K_UP]:
            if self.y_velocity <= 0:
                self.y_velocity = -1 * BLOCK_WIDTH
                self.x_velocity = 0
        if pressed_keys[K_DOWN]:
            if self.y_velocity >= 0:
                self.y_velocity = BLOCK_WIDTH
                self.x_velocity = 0
        if pressed_keys[K_LEFT]:
            if self.x_velocity <= 0:
                self.x_velocity = -1 * BLOCK_WIDTH
                self.y_velocity = 0
        if pressed_keys[K_RIGHT]:
            if self.x_velocity >= 0:
                self.x_velocity = BLOCK_WIDTH
                self.y_velocity = 0
