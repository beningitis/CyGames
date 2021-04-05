import pygame
import random

# import Snek.score

import Snek.game

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLOCK_WIDTH,
    BLACK,
    WHITE,
    RED,
    GREEN,
    BLUE,
    game_over_text,
    play_again_text,
    FRAME_RATE
)

# from game import Game
WINDOW_SIZE = [640, 700]
GAME_AREA_POS = [20, 75]
SCORE_POS = [20, 20]
HISCORE_POS = [380, 20]


pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snek")
window_bg = pygame.Surface(WINDOW_SIZE)
window_bg = window_bg.convert()
window_bg.fill(GREEN)

frame_size = [SCREEN_WIDTH, SCREEN_HEIGHT]

clock = pygame.time.Clock()


def main():
    # Main method

    game_area = pygame.Surface(frame_size)
    game_area = game_area.convert()

    def game_over():
        game_area.fill(BLACK)
        window.blit(game_area, GAME_AREA_POS)
        go_font = pygame.font.SysFont("comicsansms", 80)
        pa_font = pygame.font.SysFont("comicsansms", 40)
        death_message = go_font.render(game_over_text, True, WHITE)
        play_again_message = pa_font.render(play_again_text, True, WHITE)
        game_over_rect = death_message.get_rect()
        play_again_rect = play_again_message.get_rect()
        game_over_rect.center = (SCREEN_WIDTH / 2 + BLOCK_WIDTH, SCREEN_HEIGHT / 2)
        play_again_rect.center = (SCREEN_WIDTH / 2 + BLOCK_WIDTH, SCREEN_HEIGHT / 2 + 60)
        window.blit(death_message, game_over_rect)
        pygame.display.flip()
        clock.tick(2)
        window.blit(play_again_message, play_again_rect)
        pygame.display.flip()

    def game_loop():

        def countdown():
            countdown_font = pygame.font.Font(None, 200)
            for i in reversed(range(1, 4)):
                countdown_text = countdown_font.render(str(i), True, WHITE)
                countdown_rect = countdown_text.get_rect()
                countdown_rect.center = (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
                game_area.fill(BLACK)
                game_area.blit(countdown_text, countdown_rect)
                window.blit(game_area, GAME_AREA_POS)
                pygame.display.flip()
                clock.tick(1)

        def update_screen():

            def display_score():
                # Display Score
                font = pygame.font.Font(None, 50)
                score_text = font.render('Score : ' + str(game.score), True, BLACK)
                score_rect = score_text.get_rect()
                high_score_text = font.render('High Score : ' + str(game.high_score), True, BLACK)
                high_score_rect = high_score_text.get_rect()
                score_rect = SCORE_POS
                high_score_rect = HISCORE_POS
                # Blit the score and high score to the window
                window.blit(score_text, score_rect)
                window.blit(high_score_text, high_score_rect)

            # Blit background and sprites to the screen
            # Put the background in the window
            window.blit(window_bg, (0, 0))
            # Fill the game screen with black
            game_area.fill(BLACK)

            # Display the score
            display_score()

            # Draw the sprites on the game area
            game.all_sprites.draw(game_area)
            # Blit the game area onto the window
            window.blit(game_area, GAME_AREA_POS)

            pygame.display.flip()

        game = Snek.game.Game()

        window.blit(window_bg, (0, 0))
        game_area.fill(BLACK)

        fps = FRAME_RATE

        running = True

        countdown()
        # main game loop
        while running:

            game.game_logic()
            update_screen()

            # Set frame rate
            clock.tick(fps)

            print(game.game_over)
            if game.game_over:
                game_over()
                running = False

    play_again = True

    game_loop()

    while play_again:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_again = False
            if event.type == pygame.KEYUP:
                game_loop()


main()







