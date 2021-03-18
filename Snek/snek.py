import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLOCK_WIDTH,
    FRAME_RATE,
    BLACK,
    WHITE,
    RED,
    GREEN,
    BLUE
)

from Snek.game import Game
from Snek.food import Food
from Snek.snake import Snake


def main():
    # Main method

    # Initialize Pygame and set up window
    pygame.init()

    ADD_APPLE = pygame.event.Event(pygame.USEREVENT + 1)

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Snek")

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    clock = pygame.time.Clock()

    game = Game()

    screen.blit(background, (0, 0))
    pygame.display.flip()


    # main game loop
    while not game.game_over:
        for event in pygame.event.get():
            # Check for key presses
            if event.type == KEYDOWN:
                # escape key?
                if event.key == K_ESCAPE:
                    game.game_over = True
                # check for quit event
            elif event.type == QUIT:
                game.game_over = True

        if pygame.sprite.spritecollideany(game.snake, game.apples):
            game.score += 1
            game.apple.update()

        pressed_keys = pygame.key.get_pressed()

        # update the snake object
        game.snake.update(pressed_keys)

        if game.snake.x <= 0 or game.snake.x >= SCREEN_WIDTH - BLOCK_WIDTH or game.snake.y <= 0 or game.snake.y >= SCREEN_HEIGHT - BLOCK_WIDTH:
            game.game_over = True

        # Blit background and sprites to the screen
        screen.blit(background, (0, 0))
        for sprite in game.all_sprites:
            screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()

        # Set frame rate
        clock.tick(FRAME_RATE)


main()
