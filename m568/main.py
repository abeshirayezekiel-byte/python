import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Clock to manage frame rate
clock = pygame.time.Clock()

# --- SPRITE CLASSES ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a blue square representing the player
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        # Start player in the center of the screen
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        # Handle movement controls (Arrow keys or WASD)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player within screen bounds
        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a red square representing an enemy
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Randomize spawn position within screen limits
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def reset_position(self):
        # Reposition enemy somewhere else if collected/hit
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


# --- INITIALIZATION ---

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

# Create 1 player
player = Player()
all_sprites.add(player)

# Create 7 random enemies
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)

# --- MAIN GAME LOOP ---
running = True
while running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update States
    all_sprites.update()

    # Check collisions between player and enemy group
    # The 'False' argument means the enemy won't be deleted automatically
    collided_enemies = pygame.sprite.spritecollide(player, enemy_sprites, False)
    
    for enemy in collided_enemies:
        score += 1             # Increment score by 1 per hit
        enemy.reset_position() # Move the hit enemy to a new random location

    # 3. Draw / Render
    screen.fill(WHITE) # Clear background
    all_sprites.draw(screen) # Draw all game characters

    # Render text displaying the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Refresh screen display
    pygame.display.flip()

    # Cap game performance at 60 FPS
    clock.tick(60)

pygame.quit()
