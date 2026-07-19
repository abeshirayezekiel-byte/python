import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont('Arial', 30)
text = font.render('Hello, Pygame!', True, BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (100, 150, 200, 100))
    screen.blit(text,(120, 200))
    pygame.display.update()
pygame.quit()
sys.exit()