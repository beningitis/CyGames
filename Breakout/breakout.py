import pygame
import math
from ball import Ball
from paddle import Paddle

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
WALL_WIDTH = 30
PADDLE_HEIGHT = 10

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = window_bg.convert()
window_bg.fill('#d3d3d3')

clock = pygame.time.Clock()

fps = 30

MAX_BOUNCE_ANGLE = (4 * math.pi) / 9

def main():
    frame_size = (SCREEN_WIDTH - 2 * WALL_WIDTH, SCREEN_HEIGHT - WALL_WIDTH)
    game_area = pygame.Surface(frame_size)
    game_area = game_area.convert()
    game_area.fill('#000000')
    window.blit(window_bg, (0, 0))
    window.blit(game_area, (WALL_WIDTH, WALL_WIDTH))

    all_sprites = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    ball = Ball((SCREEN_WIDTH - 2 * WALL_WIDTH) / 2, SCREEN_HEIGHT - WALL_WIDTH - PADDLE_HEIGHT - 50)
    paddle = Paddle((SCREEN_WIDTH - 2 * WALL_WIDTH) / 2, SCREEN_HEIGHT - PADDLE_HEIGHT)

    ball_group.add(ball)
    paddle_group.add(paddle)
    all_sprites.add(ball_group)
    all_sprites.add(paddle_group)

    pygame.mouse.set_visible(False)

    def game_loop():
        running = True
        while running:
            game_area.fill('#000000')


            ball.update()
            print(ball.rect.y)
            print(ball.y_velocity)

            # if ball collides with walls
            if ball.rect.right >= SCREEN_WIDTH - 2 * WALL_WIDTH or ball.rect.left <= 0:
                ball.x_velocity *= -1
            if ball.rect.top <= 0 :
                ball.y_velocity *= -1
            # if ball collides with paddle
            if pygame.sprite.spritecollideany(ball, paddle_group):
                collide_location = paddle.rect.centerx - ball.rect.centerx

                # normalize the collide position to be within 0 and 1
                normalized_collide_location = collide_location / (paddle.paddle_width / 2)

                # Calculate the bounce angle as a fraction of the given maximum angle,
                # based on where the ball collided with the paddle
                bounce_angle = normalized_collide_location * MAX_BOUNCE_ANGLE

                # Calculate the new velocities, using trigonometry
                ball.x_velocity = -1 * ball.speed * math.sin(bounce_angle)
                ball.y_velocity = -1 * ball.speed * math.cos(bounce_angle)

            if ball.rect.bottom > SCREEN_HEIGHT - WALL_WIDTH:
                break;

            for events in pygame.event.get():
                if events.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    paddle.rect.x = min(mouse_position[0], (SCREEN_WIDTH - 2 * WALL_WIDTH - 50))

            for sprite in all_sprites:
                game_area.blit(sprite.image, sprite.rect)
            # print(str(ball.rect.x) + " ")
            # print(str(ball.rect.y) + "\n")
            window.blit(game_area, (WALL_WIDTH, WALL_WIDTH))
            pygame.display.flip()

            clock.tick(fps)

    game_loop()


main()
