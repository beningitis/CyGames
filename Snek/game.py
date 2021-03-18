import pygame

from Snek import (
    food,
    snake,
)


class Game(object):
    # Represents an instance of the Snek game

    def __init__(self):

        self.score = 0
        self.game_over = False

        # Sprite groups
        self.apple_group = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Create apple object
        self.apple = food.Food()
        self.apple_group.add(self.apple)

        # Create snake object
        self.snake = snake.Snake()
        self.player.add(self.snake)

        self.all_sprites.add(self.apple_group)
        self.all_sprites.add(self.player)

    def grow_snake(self):
        self.snake.body.insert(0, list(self.snake.position))
        if not pygame.sprite.spritecollideany(self.snake, self.apple_group):
            self.snake.body.pop()