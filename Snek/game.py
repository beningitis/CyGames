import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


from Snek.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

from Snek.food import Food
from Snek.snake import Snake, Block


class Game(object):
    # Represents an instance of the Snek game

    def __init__(self):

        self.player = Snake()
        self.apple = Food()
        self.score = 0
        self.high_score = 0
        self.game_over = False

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.apples = pygame.sprite.Group()

        # Create snake object
        self.player = Snake()
        self.apples.add(self.apple)
        self.all_sprites.add(self.apples)
        self.all_sprites.add(self.player.snakeBodySpriteGroup)

    def move_snake(self):
        x = self.player.snake_body[0].rect.x + self.player.x_velocity
        y = self.player.snake_body[0].rect.y + self.player.y_velocity
        new_block = Block(x, y)

        self.player.snake_body.insert(0, new_block)
        self.all_sprites.add(new_block)
        if not pygame.sprite.spritecollideany(self.player.snake_body[0], self.apples):
            old_block = self.player.snake_body.pop()
            self.all_sprites.remove(old_block)

    def game_logic(self):
        for event in pygame.event.get():
            # Check for key presses
            if event.type == KEYDOWN:
                # escape key?
                if event.key == K_ESCAPE:
                    self.game_over = True
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT:
                    start = True
                # check for quit event
            elif event.type == QUIT:
                self.game_over = True

        if pygame.sprite.spritecollideany(self.player.snake_body[0], self.apples):
            self.score += 1
            self.apple.update()

        pressed_keys = pygame.key.get_pressed()
        # update the snake object
        self.player.update(pressed_keys)
        self.move_snake()

        # Check if snake intersects any of its own blocks
        for block in range(1, len(self.player.snake_body)):
            if self.player.snake_body[0].rect == self.player.snake_body[block].rect:
                self.game_over = True

        # Check if snake collides with walls
        if self.player.snake_body[0].rect.x >= SCREEN_WIDTH or self.player.snake_body[0].rect.x < 0:
            self.game_over = True
        if self.player.snake_body[0].rect.y >= SCREEN_HEIGHT or self.player.snake_body[0].rect.y < 0:
            self.game_over = True
