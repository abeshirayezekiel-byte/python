import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 0.5
ENEMY_SPEED_Y = 5
BULLET_SPEED_Y = 1
COLLISION_DISTANCE = 27
PLAYER_SIZE = 40
ENEMY_SIZE = 40
BULLET_WIDTH = 28
BULLET_HEIGHT = 40

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('C:\\Users\\PC\\Downloads\\space invaders_bg.jpg').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:\\Users\\PC\\Downloads\\icon_space invaders.jpg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('C:\\Users\\PC\\Downloads\\player.png')
playerImg = pygame.transform.scale(playerImg, (PLAYER_SIZE, PLAYER_SIZE))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 6
for i in range(num_of_enemies):
    img = pygame.image.load('C:\\Users\\PC\\Downloads\\enemy.png')
    img = pygame.transform.scale(img, (ENEMY_SIZE, ENEMY_SIZE))
    enemyImg.append(img)
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('C:\\Users\\PC\\Downloads\\bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (BULLET_WIDTH, BULLET_HEIGHT))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (bulletX + PLAYER_SIZE // 2 - BULLET_WIDTH // 2, bulletY))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt(
    ((enemyX + ENEMY_SIZE // 2) - (bulletX + BULLET_WIDTH // 2)) ** 2 +
    ((enemyY + ENEMY_SIZE // 2) - (bulletY + BULLET_HEIGHT // 2)) ** 2)
    return distance < COLLISION_DISTANCE

#Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -1
          if event.key == pygame.K_RIGHT:
              playerX_change = 1
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
          playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_SIZE))

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_SIZE:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()