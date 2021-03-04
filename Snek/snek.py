import pygame
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


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.surf = pygame.Surface((24, 24))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -24)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 24)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-24, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(24, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


def main():
    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snek')

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    # Instantiate Snake object
    snake = Snake()

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

        # Check for user keyboard input
        pressed_keys = pygame.key.get_pressed()
        print(pressed_keys[K_DOWN], pressed_keys[K_RIGHT])
        print(pygame.event.get())

        # Update the snake object
        snake.update(pressed_keys)
        screen.blit(background, (0, 0))
        screen.blit(snake.surf, snake.rect)
        pygame.display.flip()

        # set frame rate
        clock.tick(2)


main()


