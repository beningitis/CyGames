import pygame

from Snek.food import Food
from Snek.snake import Snake, Block


class Game(object):
    # Represents an instance of the Snek game
    player = Snake()
    apple = Food()
    score = 0
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

    def move_snake(self):
        x = self.player.snake_body[0].rect.x + self.player.x_velocity
        y = self.player.snake_body[0].rect.y + self.player.y_velocity
        new_block = Block(x, y)

        self.player.snake_body.insert(0, new_block)
        self.all_sprites.add(new_block)

    def grow_snake(self):
        if not pygame.sprite.spritecollideany(self.player.snake_body[0], self.apples):
            old_block = self.player.snake_body.pop()
            self.all_sprites.remove(old_block)
