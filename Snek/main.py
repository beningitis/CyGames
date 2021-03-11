import pygame
import apple
import snake

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

clock = pygame.time.Clock()

# Screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snek')

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    # Instantiate Snake object
    player = snake.Snake()
    target = apple.Apple()

    targets = pygame.sprite.Group()
    targets.add(target)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(target)

    # Text
    # font = pygame.font.Font(None, 36)
    # text = font.render("Hello There", 1, WHITE)
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos.centery = background.get_rect().centery
    #
    # text2 = font.render("General Kenobi", 1, WHITE)
    # text2pos = text2.get_rect()
    # text2pos.centerx = background.get_rect().centerx
    # text2pos.centery = textpos.centery + 20
    # background.blit(text, textpos)
    # background.blit(text2, text2pos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    running = True
    # Event loop
    while running:
        for event in pygame.event.get():
            # Check for key presses
            if event.type == KEYDOWN:
                # escape key?
                if event.key == K_ESCAPE:
                    running = False
                # check for quit event
            elif event.type == QUIT:
                running = False

        if pygame.sprite.spritecollideany(player, targets):
            target.kill()

        # Check for user keyboard input
        pressed_keys = pygame.key.get_pressed()
        print(pressed_keys[K_DOWN], pressed_keys[K_RIGHT])
        print(pygame.event.get())

        # Update the snake object
        player.update(pressed_keys)
        screen.blit(background, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        # screen.blit(player.surf, player.rect)
        target.normalize_position()
        # screen.blit(target.surf, (target.rect.x, target.rect.y))
        pygame.display.flip()

        # set frame rate
        clock.tick(15)


main()


