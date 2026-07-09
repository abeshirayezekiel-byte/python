import pygame

# 1. ALWAYS initialize Pygame before doing anything else
pygame.init()

# 2. Set up screen dimensions and surface
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# 3. Load, convert, and scale images after display initialization
background_image = pygame.transform.scale(
    pygame.image.load('C:\\Users\\PC\\Downloads\\bg.jpg').convert(), 
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load('C:\\Users\\PC\\Downloads\\codingal logo.png').convert_alpha(), 
    (200, 200)
)
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

# 4. Initialize font and render text
text = pygame.font.Font(None, 36).render('Hello World ', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Drawing operations
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()

if __name__ == '__main__':
    game_loop()