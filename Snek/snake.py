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


class Snake(pygame.sprite.Sprite):
    # Represents the snake

    def __init__(self):
        super().__init__()
        # Snake does not move initially
        self.x_velocity = 0
        self.y_velocity = 0

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

        self.position = [self.x, self.y]
        self.body = [[self.x, self.y], [self.x - BLOCK_WIDTH, self.y], [self.x - 2 * BLOCK_WIDTH, self.y]]

        # surf is a 24x24 px surface, filled with white
        self.surf = pygame.Surface((BLOCK_WIDTH, BLOCK_WIDTH))
        self.surf.fill('#ffffff')

        self.rect = self.surf.get_rect()
        # Center of rect object is at position[]
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]

        # loads the high score data from file
        # self.load_data()

    def update(self, pressed_keys):
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        if pressed_keys[K_UP or event.key == ord('w')]:
            self.y_velocity = -24
            self.x_velocity = 0
        if pressed_keys[K_DOWN or event.key == ord('s')]:
            self.y_velocity = 24
            self.x_velocity = 0
        if pressed_keys[K_LEFT or event.key == ord('a')]:
            self.x_velocity = -24
            self.y_velocity = 0
        if pressed_keys[K_RIGHT or event.key == ord('d')]:
            self.x_velocity = 24
            self.y_velocity = 0
        if self.rect.left < 0:
            self.rect.left = 0
        # Make sure snake stays within window
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def grow(self):
        self.body.insert(0, list(self.position))


