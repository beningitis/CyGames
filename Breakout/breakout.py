import pygame
import math
from ball import Ball
from paddle import Paddle
from brick import Brick
import side_collisions

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 480
WALL_WIDTH = 30
PADDLE_HEIGHT = 10
GAME_AREA_WIDTH = SCREEN_WIDTH - 2 * WALL_WIDTH
GAME_AREA_HEIGHT = SCREEN_HEIGHT - WALL_WIDTH

score = 0
high_score = 0
HS_FILE = "highscore.txt"

# colors = ('#ff0000', '#ff8000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff', "#ffffff")
colors = ('#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff')

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
window_bg = window_bg.convert()
window_bg.fill('#d3d3d3')

clock = pygame.time.Clock()

fps = 25

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

    ball = Ball(200,200)
    #ball = Ball((SCREEN_WIDTH - 2 * WALL_WIDTH) / 2, SCREEN_HEIGHT - WALL_WIDTH - PADDLE_HEIGHT - 50)
    paddle = Paddle((SCREEN_WIDTH - 2 * WALL_WIDTH) / 2, SCREEN_HEIGHT - PADDLE_HEIGHT)

    # Set up bricks
    brick_list = []
    brick_x = 4
    brick_y = 4
    brick_color = 0

    for row in range(7):
        for col in range(14):
            brick_row = []
            new_brick = Brick(brick_x, brick_y, colors[brick_color % len(colors)])
            brick_row.append(new_brick)
            brick_group.add(new_brick)
            brick_x += 64
            brick_color += 1
        brick_list.append(brick_row)
        brick_y += 24
        brick_x = 4

    # test_brick = Brick(450, 240, colors[brick_color])
    # brick_group.add(test_brick)
    ball_group.add(ball)
    paddle_group.add(paddle)
    all_sprites.add(brick_group)
    all_sprites.add(ball_group)
    all_sprites.add(paddle_group)

    pygame.mouse.set_visible(False)

    def is_collide_right(hit_brick):
        if hit_brick.rect.centerx <= ball.rect.centerx <= GAME_AREA_WIDTH and \
                hit_brick.rect.bottom <= ball.rect.centerx <= hit_brick.rect.top:
            return True
        else:
            return False

    def is_collide_left(hit_brick):
        if 0 >= ball.rect.centerx >= hit_brick.rect.centerx and \
                hit_brick.rect.bottom <= ball.rect.centery <= hit_brick.rect.top:
            return True
        else:
            return False

    def is_collide_top(hit_brick):
        if 0 >= ball.rect.centery >= hit_brick.rect.centery and \
                hit_brick.rect.left <= ball.rect.centerx <= hit_brick.rect.right:
            return True
        else:
            return False

    def is_collide_bottom(hit_brick):
        if hit_brick.rect.centery <= ball.rect.top <= GAME_AREA_HEIGHT and \
                hit_brick.rect.left <= ball.rect.centerx <= hit_brick.rect.right:
            return True
        else:
            return False

    def game_loop():
        running = True
        while running:
            game_area.fill('#000000')
            # if ball collides with walls
            if ball.rect.right >= SCREEN_WIDTH - 2 * WALL_WIDTH or ball.rect.left <= 0:
                ball.velocity.x *= -1
            if ball.rect.top <= 0:
                ball.velocity.y *= -1
            # if ball collides with paddle
            if pygame.sprite.spritecollideany(ball, paddle_group):
                collide_location = paddle.rect.centerx - ball.rect.centerx
                # normalize the collide position to be within 0 and 1
                normalized_collide_location = collide_location / (paddle.paddle_width / 2)
                # Calculate the bounce angle as a fraction of the given maximum angle,
                # based on where the ball collided with the paddle
                bounce_angle = normalized_collide_location * MAX_BOUNCE_ANGLE
                # Calculate the new velocities, using trigonometry
                ball.velocity.x = -1 * ball.speed * math.sin(bounce_angle)
                ball.velocity.y = -1 * ball.speed * math.cos(bounce_angle)

            # ball collides with brick
            hit_bricks = pygame.sprite.spritecollide(ball, brick_group, True)
            if hit_bricks:
                for brick in hit_bricks:
                    # print("Brick: ")
                    # print(" Top: " + str(brick.rect.top))
                    # print(" Bottom: " + str(brick.rect.bottom))
                    # print(" Right: " + str(brick.rect.right))
                    # print(" Left: " + str(brick.rect.left))
                    # print("Ball: " + str(ball.rect))
                    # print(" Top: " + str(ball.rect.top))
                    # print(" Bottom: " + str(ball.rect.bottom))
                    # print(" Right: " + str(ball.rect.right))
                    # print(" Left: " + str(ball.rect.left))
                    if side_collisions.top(brick, ball):
                        print("Hit top side of brick")
                        ball.velocity.y *= -1
                    elif side_collisions.bottom(brick, ball):
                        print("Hit bottom side of brick")
                        ball.velocity.y *= -1
                    elif side_collisions.right(brick, ball):
                        print("Hit right side of brick")
                        ball.velocity.x *= -1
                    elif side_collisions.left(brick, ball):
                        print("Hit left side of brick")
                        ball.velocity.x *= -1
                    # ball.bounce(side_collisions.top(brick, ball), side_collisions.bottom(brick, ball),
                    #            side_collisions.left(brick, ball), side_collisions.right(brick, ball))

            if ball.rect.bottom > SCREEN_HEIGHT - WALL_WIDTH:
                break;

            ball.update()

            for events in pygame.event.get():
                if events.type == pygame.MOUSEMOTION:is_collide_top(brick)
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
