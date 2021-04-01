import pygame

from Snek.food import Food
from Snek.snake import Snake, Block


class Game(object):
    # Represents an instance of the Snek game
    player = Snake()
    apple = Food()
    score = 0
    high_score = 0
    game_over = False

    def __init__(self):

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.apples = pygame.sprite.Group()

        # Create snake object
        self.player = Snake()
        self.apples.add(self.apple)
        self.all_sprites.add(self.apples)
        self.all_sprites.add(Snake.snakeBodySpriteGroup)

    def move_snake(self):
        x = self.player.snake_body[0].rect.x + self.player.x_velocity
        y = self.player.snake_body[0].rect.y + self.player.y_velocity
        new_block = Block(x, y)

        self.player.snake_body.insert(0, new_block)
        self.all_sprites.add(new_block)
        if not pygame.sprite.spritecollideany(self.player.snake_body[0], self.apples):
            old_block = self.player.snake_body.pop()
            print(old_block)
            self.all_sprites.remove(old_block)