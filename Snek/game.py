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
        self.apples = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Create apple object
        self.apple = food.Food()
        self.apples.add(self.apple)

        # Create snake object
        self.snake = snake.Snake()
        self.player.add(self.snake)

        self.all_sprites.add(self.apples)
        self.all_sprites.add(self.player)


