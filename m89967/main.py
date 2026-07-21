import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

BG_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 255, 128)
STATIC_COLOR = (255, 87, 34)

class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player_sprite = RectSprite(PLAYER_COLOR, 50, 50, 200, 300)
static_sprite = RectSprite(STATIC_COLOR, 60, 60, 500, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite)
all_sprites.add(static_sprite)

clock = pygame.time.Clock()
player_speed = 5
running = True

while running:
    # 1. Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_sprite.rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_sprite.rect.x += player_speed
    if keys[pygame.K_UP]:
        player_sprite.rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_sprite.rect.y += player_speed

    player_sprite.rect.left = max(0, player_sprite.rect.left)
    player_sprite.rect.right = min(SCREEN_WIDTH, player_sprite.rect.right)
    player_sprite.rect.top = max(0, player_sprite.rect.top)
    player_sprite.rect.bottom = min(SCREEN_HEIGHT, player_sprite.rect.bottom)

    screen.fill(BG_COLOR)
    all_sprites.draw(screen)
    pygame.display.flip()
    # 4. Cap the frame rate at 60 FPS
    clock.tick(60)

# Clean quit
pygame.quit()
sys.exit()
