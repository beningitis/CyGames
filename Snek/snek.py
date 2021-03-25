import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
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


def main():
    # Main method

    # Initialize Pygame and set up window
    pygame.init()

    frame_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(frame_size)

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
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT:
                    start = True
                # check for quit event
            elif event.type == QUIT:
                game.game_over = True

        if pygame.sprite.spritecollideany(game.player.snake_body[0], game.apples):
            game.score += 1
            game.apple.update()
            print(game.score)

        pressed_keys = pygame.key.get_pressed()
        # update the snake object
        game.player.update(pressed_keys)
        game.move_snake()
        game.grow_snake()

        for block in range(1, len(game.player.snake_body)):
            if game.player.snake_body[0].rect == game.player.snake_body[block].rect:
                print(pressed_keys)
                game.game_over = True

        if game.player.snake_body[0].rect.x >= SCREEN_WIDTH - BLOCK_WIDTH or game.player.snake_body[0].rect.x <= 0:
            game.game_over = True
        if game.player.snake_body[0].rect.y >= SCREEN_HEIGHT - BLOCK_WIDTH or game.player.snake_body[0].rect.y <= 0:
            game.game_over = True



        # game.show_score()



        # Blit background and sprites to the screen
        screen.blit(background, (0, 0))
        game.all_sprites.draw(screen)

        pygame.display.flip()

        # Set frame rate
        clock.tick(FRAME_RATE)

main()
