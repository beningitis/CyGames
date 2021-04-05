import pygame
from ball import Ball
from paddle import Paddle

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = window_bg.convert()
window_bg.fill('#d3d3d3')

clock = pygame.time.Clock()

fps = 25

def main():
    frame_size = (900, 450)
    game_area = pygame.Surface(frame_size)
    game_area = game_area.convert()
    game_area.fill('#000000')
    window.blit(window_bg, (0, 0))
    window.blit(game_area, (30, 30))

    all_sprites = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    ball = Ball(475, 430)
    paddle = Paddle(475, 440)

    ball_group.add(ball)
    paddle_group.add(paddle)
    all_sprites.add(ball_group)
    all_sprites.add(paddle_group)

    def game_loop():
        running = True
        while running:
            game_area.fill('#000000')


            ball.update()

            if ball.rect.right > 900 or ball.rect.left < 0:
                ball.x_velocity *= -1
            if ball.rect.top < 0 or pygame.sprite.spritecollideany(ball, paddle_group):
                ball.y_velocity *= -1
            if ball.rect.bottom > 450:
                break;

            for events in pygame.event.get():
                if events.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    paddle.rect.x = min(mouse_position[0], 850)

            for sprite in all_sprites:
                game_area.blit(sprite.image, sprite.rect)
            # print(str(ball.rect.x) + " ")
            # print(str(ball.rect.y) + "\n")
            window.blit(game_area, (30, 30))
            pygame.display.flip()

            clock.tick(fps)

    game_loop()

main()
