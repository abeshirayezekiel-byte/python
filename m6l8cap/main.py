import pygame
import sys

# 1. INITIALIZE PYGAME Safely
pygame.init()

# Setup screen properties
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Football Duel")
clock = pygame.time.Clock()

# Colors (RGB)
BG_COLOR = (18, 24, 38)
CARD_BG = (28, 36, 56)
GOLD = (212, 175, 55)
TEXT_WHITE = (240, 240, 240)
TEXT_GRAY = (150, 160, 175)

# FIXED: Passing 'None' tells Pygame to use its internal safe fallback font
FONT_TITLE = pygame.font.Font(None, 46)
FONT_SUBTITLE = pygame.font.Font(None, 24)
FONT_BODY = pygame.font.Font(None, 18)

# Player Data
OG_PLAYERS = [
    {"name": "Ronaldo", "rating": 126},
    {"name": "Maradona", "rating": 125},
    {"name": "Neymar", "rating": 124},
    {"name": "Zidane", "rating": 122},
    {"name": "Messi", "rating": 120},
    {"name": "Ronaldinho", "rating": 120},
    {"name": "Kaka", "rating": 118},
    {"name": "Beckham", "rating": 115}
]

# State Variables
user_coins = 1500
notification_text = "Welcome to Football Duel! Click options below."

# Simple Button Structure
class ClickButton:
    def __init__(self, text, x, y, w, h, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action

    def draw(self):
        # Draw button box
        pygame.draw.rect(screen, CARD_BG, self.rect, border_radius=5)
        pygame.draw.rect(screen, GOLD, self.rect, width=1, border_radius=5)
        # Render text
        txt_surf = FONT_BODY.render(self.text, True, TEXT_WHITE)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        screen.blit(txt_surf, txt_rect)

    def handle_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Create buttons
buttons = [
    ClickButton("Standard Pack (500c)", 50, 480, 220, 45, "PACK"),
    ClickButton("Invite Online Friend", 300, 480, 220, 45, "INVITE")
]

# Main Application Loop
running = True
while running:
    # Fill background color
    screen.fill(BG_COLOR)
    
    # 2. DRAW HEADER
    title = FONT_TITLE.render("FOOTBALL DUEL", True, GOLD)
    screen.blit(title, (50, 30))
    
    stats = FONT_SUBTITLE.render(f"Coins: {user_coins}c  |  Collection: 0/13 Owned", True, TEXT_WHITE)
    screen.blit(stats, (50, 80))
    
    pygame.draw.line(screen, GOLD, (50, 120), (SCREEN_WIDTH - 50, 120), 2)
    
    # 3. DRAW PLAYER CARDS (Grid Layout)
    start_x, start_y = 50, 150
    card_w, card_h = 90, 130
    
    for i, player in enumerate(OG_PLAYERS):
        row = i // 4
        col = i % 4
        x = start_x + (col * 105)
        y = start_y + (row * 145)
        
        card_rect = pygame.Rect(x, y, card_w, card_h)
        pygame.draw.rect(screen, CARD_BG, card_rect, border_radius=8)
        pygame.draw.rect(screen, GOLD, card_rect, width=2, border_radius=8)
        
        # Draw rating text
        rate_surf = FONT_BODY.render(str(player["rating"]), True, GOLD)
        screen.blit(rate_surf, (x + 10, y + 10))
        
        # Draw name text
        name_surf = FONT_BODY.render(player["name"], True, TEXT_WHITE)
        screen.blit(name_surf, (x + 10, y + 90))

    # 4. DRAW SYSTEM STATUS TICKER
    status_box = pygame.Rect(50, 550, 800, 45)
    pygame.draw.rect(screen, CARD_BG, status_box, border_radius=5)
    msg_surf = FONT_BODY.render(notification_text, True, TEXT_GRAY)
    screen.blit(msg_surf, (status_box.x + 15, status_box.y + 15))

    # 5. DRAW BUTTONS
    for btn in buttons:
        btn.draw()

    # 6. EVENT LISTENER
    for event in pygame.get_event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            m_pos = event.pos
            for btn in buttons:
                if btn.handle_click(m_pos):
                    if btn.action == "PACK":
                        if user_coins >= 500:
                            user_coins -= 500
                            notification_text = "Pack opened successfully! Check your command line console."
                            print(" -> Pack rolled! Player added to background database structure.")
                        else:
                            notification_text = "Not enough coins! You need 500c to pull a standard pack."
                    elif btn.action == "INVITE":
                        notification_text = "Multiplayer: Sent active lobby invite packet through WebSocket port."

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
