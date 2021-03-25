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

    snakeBodySpriteGroup = pygame.sprite.Group()
    snake_body = []
    x_velocity = 24
    y_velocity = 0

    def __init__(self):
        super().__init__()
        # Snake does not move initially
        for i in range(2):
            x = SCREEN_WIDTH // 2 - BLOCK_WIDTH // 2 - BLOCK_WIDTH * i
            y = SCREEN_HEIGHT // 2 - BLOCK_WIDTH // 2
            block = Block(x, y)
            self.snake_body.append(block)
            self.snakeBodySpriteGroup.add(block)

        """
        self.x_velocity = 0
        self.y_velocity = 0

        self.x = SCREEN_WIDTH // 2 - BLOCK_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2 - BLOCK_WIDTH // 2

        self.position = [self.x, self.y]
        self.body_pos = [[self.x, self.y], [self.x - BLOCK_WIDTH, self.y], [self.x - 2 * BLOCK_WIDTH, self.y]]

        self.body = []
        self.body_surf = []
        # surf is a 24x24 px surface, filled with white

        # Create rects for each position in the body
        for i in range(len(self.body_pos)):
            self.rect = pygame.Rect(self.body_pos[i][0], self.body_pos[i][1], BLOCK_WIDTH, BLOCK_WIDTH)
            self.body.append(self.rect)

        print(self.body)

        for j in range(len(self.body_pos)):
            surf = pygame.Surface((BLOCK_WIDTH, BLOCK_WIDTH))
            self.body_pos.append(surf)

        #self.surf = pygame.Surface((BLOCK_WIDTH, BLOCK_WIDTH))

        #self.surf.fill('#ff00ff')

        #self.rect = self.surf.get_rect()
        ## Center of rect object is at position[]
        #self.rect.x = self.position[0]
        #self.rect.y = self.position[1]

        # loads the high score data from file
        # self.load_data()
        """

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

        """
        if self.rect.left < 0:
            self.rect.left = 0
        # Make sure snake stays within window
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        """
