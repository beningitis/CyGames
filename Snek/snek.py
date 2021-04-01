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
    BLACK,
    WHITE,
    RED,
    GREEN,
    BLUE,
    game_over_text
)

from Snek.game import Game
WINDOW_SIZE = [640, 800]
GAME_AREA_POS = [20, 75]
SCORE_POS = [20, 20]
HISCORE_POS = [380, 20]

play_again = True

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
window_bg = pygame.Surface(WINDOW_SIZE)
window_bg = window_bg.convert()
window_bg.fill(GREEN)


def main():
    # Main method

    # Initialize Pygame and set up window

    frame_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    pygame.display.set_caption("Snek")

    # Background
    game_area = pygame.Surface(frame_size)
    game_area = game_area.convert()
    game_area.fill(BLACK)

    clock = pygame.time.Clock()

    FRAME_RATE = 15

    game = Game()
    window.blit(window_bg, (0, 0))

    game.game_over = False

    def game_over():
        game_area.fill(BLACK)
        window.blit(game_area, GAME_AREA_POS)
        font = pygame.font.Font(None, 120)
        death_message = font.render(game_over_text, True, (255, 255, 255))
        game_over_rect = death_message.get_rect()
        game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        window.blit(death_message, game_over_rect)
        pygame.display.flip()

        wait = True;
        while wait:
            clock.tick(FRAME_RATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    wait = False

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
            if game.score % 10 == 0:
                FRAME_RATE += 2

        pressed_keys = pygame.key.get_pressed()
        # update the snake object
        game.player.update(pressed_keys)
        game.move_snake()

        # Check if snake intersects any of its own blocks
        for block in range(1, len(game.player.snake_body)):
            if game.player.snake_body[0].rect == game.player.snake_body[block].rect:
                game.game_over = True

        # Check if snake collides with walls
        if game.player.snake_body[0].rect.x >= SCREEN_WIDTH or game.player.snake_body[0].rect.x < 0:
            game.game_over = True
        if game.player.snake_body[0].rect.y >= SCREEN_HEIGHT or game.player.snake_body[0].rect.y < 0:
            game.game_over = True

        # Display Score
        font = pygame.font.Font(None, 50)
        score_text = font.render('Score : ' + str(game.score), True, BLACK)
        score_rect = score_text.get_rect()
        high_score_text = font.render('High Score : ' + str(game.high_score), True, BLACK)
        high_score_rect = high_score_text.get_rect()
        score_rect = SCORE_POS
        high_score_rect = HISCORE_POS

        # Blit background and sprites to the screen
        # Put the background in the window
        window.blit(window_bg, (0, 0))
        # Fill the game screen with black
        game_area.fill(BLACK)
        # Draw the sprites on the game area
        game.all_sprites.draw(game_area)
        # Blit the game area onto the window
        window.blit(game_area, GAME_AREA_POS)

        # Blit the score and high score to the window
        window.blit(score_text, score_rect)
        window.blit(high_score_text, high_score_rect)

        if game.game_over:
            game_over()

        pygame.display.flip()


        # Set frame rate
        clock.tick(FRAME_RATE)


main()





