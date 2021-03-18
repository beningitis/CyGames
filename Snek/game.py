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

    '''
    def game_over(self):
        font = pygame.font.Font(None, 90)
        text = font.render('Game Over', True, (255, 255, 255))
        game_over_rect = text.get_rect()
        game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        screen.blit(text, game_over_rect)
        pygame.display.flip()

    #def show_score(self):
        font = pygame.font.Font(None, 25)
        text = font.render('Score : ' + str(self.score), True, (255, 255, 255))
        score_rect = text.get_rect()
        score_rect = (100, 100)
        screen.blit(text, score_rect)
    '''






