import pygame
import random
import math

# Initializing Pygame
pygame.init()

# Preparing the screen
screen = pygame.display.set_mode((800, 600))

# Making the title
pygame.display.set_caption("Reddit vs Tik Tok by Rif")

# Score variables
score = 0
escore = 0

# Setting Logo
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player image
player_img = pygame.image.load("reddit.png")
# Player Co-ordinate variables
playerX = 370
playerY = 480
changeX = 0

# List of enemies and their co-ordinates
enemy_img = []
enemyX = []
enemyY = []
enemy_changeX = []
enemy_changeY = []

# Total enemies
no_of_enemies = 4

for i in range(no_of_enemies):
    # Enemy image
    enemy_img.append(pygame.image.load("tiktok.png"))
    # Enemy Co-ordinate variables
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(55, 150))
    enemy_changeX.append(3)
    enemy_changeY.append(30)

# Background image
background = pygame.image.load("vs image.png")

# Bullet image
bullet = pygame.image.load("bullet.png")
# Bullet Co-ordinate variables
bulletX = 0
bulletY = 480
bullet_changeX = 0
bullet_changeY = 6
bullet_state = "ready"

# Making the font for the score board
font = pygame.font.Font("freesansbold.ttf", 25)
textX = 10
textY = 10


# Rendering and printing the score board to the window
def score_board(x, y):
    global score
    scoreprint = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scoreprint, (x, y))


# Making the game over text
game_over = pygame.font.Font("freesansbold.ttf", 64)


# Printing the game over text
def game_over_text():
    texxt = game_over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(texxt, (200, 250))


# Making Watermark
mark = pygame.font.Font("freesansbold.ttf", 12)


# Printing the watermark
def water_mark():
    watermark = mark.render("Rif'sCodingShit", True, (255, 255, 255))
    screen.blit(watermark, (660, 580))


# Printing the enemy image to the screen
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# Printing the player image to the screen
def player(x, y):
    screen.blit(player_img, (x, y))


# Printing bullet to the screen
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 17))


# Detecting collisions
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((pow(bulletX - enemyX, 2) + pow(bulletY - enemyY, 2)))
    if distance <= 27:
        return True
    else:
        return False


running = True
while running:

    # Setting Window color
    screen.fill((35, 20, 70))
    screen.blit(background, (0, 0))

    # Fixing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -2
            if event.key == pygame.K_RIGHT:
                changeX = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0

    # Making player movements
    playerX += changeX

    # Making the bullet to take multiple shots
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Making the bullet move
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bullet_changeY

    # Checking if the player hits the boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(no_of_enemies):

        # Checking if the has ended
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # Making enemy movements
        enemyX[i] += enemy_changeX[i]
        # Checking if the enemy hits the boundaries
        if enemyX[i] <= 0:
            enemy_changeX[i] = 3
            enemyY[i] += enemy_changeY[i]
        elif enemyX[i] >= 736:
            enemy_changeX[i] = -3
            enemyY[i] += enemy_changeY[i]
        # Checking if there is a collision and maintaining scores
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(55, 150)
            score += 1
        # Calling the enemy function
        enemy(enemyX[i], enemyY[i], i)

    # Calling the watermark function
    water_mark()
    # Calling the player function
    player(playerX, playerY)
    # Calling the score function
    score_board(textX, textY)
    # Updating the window
    pygame.display.update()
