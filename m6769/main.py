import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Custom Event - Sprite Lab")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = self.get_random_color()
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_random_color(self):
        """Generates a random RGB color."""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def change_color(self):
        """Updates the sprite with a new random color."""
        self.color = self.get_random_color()
        self.image.fill(self.color)

sprite1 = CustomSprite(200, 250, 100, 100)
sprite2 = CustomSprite(500, 250, 100, 100)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    screen.fill((30, 30, 30))
    
    all_sprites.draw(screen)
    
    # Refresh display
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
