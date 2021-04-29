from paddle import Paddle
from brick import Brick
from ball import Ball
import pygame
import math
import side_collisions


class Settings():
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 480
    WALL_WIDTH = 30
    PADDLE_HEIGHT = 10
    GAME_AREA_WIDTH = SCREEN_WIDTH - 2 * WALL_WIDTH
    GAME_AREA_HEIGHT = SCREEN_HEIGHT - WALL_WIDTH
    # colors = ('#ff0000', '#ff8000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff', "#ffffff")
    colors = ('#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff')


class Game(object):
    # Represents an instance of the Breakout game

    def __init(self):
        self.ball = Ball((Settings.SCREEN_WIDTH - 2 * Settings.WALL_WIDTH) / 2, Settings.SCREEN_HEIGHT - \
                         Settings.WALL_WIDTH - Settings.PADDLE_HEIGHT - 50)
        self.paddle = Paddle((Settings.SCREEN_WIDTH - 2 * Settings.WALL_WIDTH) / 2, Settings.SCREEN_HEIGHT \
                             - Settings.PADDLE_HEIGHT)
        self.brick_list = []

        self.lives = 3

        self.out_of_bounds = pygame.USEREVENT + 1

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.brick_group = pygame.sprite.Group()
        self.paddle_group = pygame.sprite.Group()

    def setup_bricks(self, rows, cols):
        brick_x = 4
        brick_y = 4
        brick_color = 0
        for row in range(rows):
            for col in range(cols):
                brick_row = []
                new_brick = Brick(brick_x, brick_y,
                                  Settings.colors[brick_color % len(Settings.colors)])
                brick_row.append(new_brick)
                self.brick_group.add(new_brick)
                brick_x += 64
                brick_color += 1
                self.brick_list.append(brick_row)
                brick_y += 24
            brick_x = 4

        def game_loop():


