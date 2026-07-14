import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game")

font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Hello, Pygame!", True, (0, 0, 0))  # Black text

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    screen.blit(text_surface, (50, 50))

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 120, 60, 60))

    pygame.display.flip()

pygame.quit()
