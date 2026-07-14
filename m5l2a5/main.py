import sys
import pygame

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = 'pygame.display'.'set_display_mode'((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window caption
pygame.display.set_caption("My First Game")

# Define colors (RGB format)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Note: (0,0,0) is black, (255,255,255) is white
BLUE = (0, 0, 255)

# Set up font for displaying text
# None uses the default Pygame font, 36 is the font size
font = pygame.font.Font(None, 36)

# Create the text surface
# "Hello World" is the text, True enables antialiasing, BLUE is the text color
text_surface = font.render("Hello World", True, BLUE)

# Get the bounding box of the text to help center it
text_rect = text_surface.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main game loop
running = True
while running:
    # Handle events (like clicking the X to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color (Setting it to White)
    screen.fill(WHITE)

    # Draw the text surface onto the screen at the designated coordinates
    screen.blit(text_surface, text_rect)

    # Update the display to show the changes
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit(