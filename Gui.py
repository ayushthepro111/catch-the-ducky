import pygame
import random

pygame.init()

score = 0

sc = pygame.display.set_mode((600, 600))

player = pygame.image.load("dog.png")
icn = pygame.image.load("dog.png")

pygame.display.set_icon(icn)
pygame.display.set_caption("Catching The Egg")

playerX = 270
playerY = 500
playerX_change = 0
playerY_change = 0
player_rect = player.get_rect(topleft=(playerX, playerY))

egg = pygame.image.load("egg.png")
eggX = random.randint(10, 500)  # Limit egg spawn within x-axis boundaries
eggY = random.randint(100, 200)
eggY_change = 0.5
egg_rect = egg.get_rect(bottomleft=(eggX, eggY))

font = pygame.font.Font("fonts/Oswald-Medium.ttf", 36)


run = True
while run:
    sc.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    eggY += eggY_change

    if playerX <= 10:
        playerX = 10
    elif playerX >= 500:
        playerX = 500

    player_rect.topleft = (playerX, playerY)
    egg_rect.bottomleft = (eggX, eggY)

    sc.blit(egg, (eggX, eggY))
    sc.blit(player, (playerX, playerY))

    if player_rect.colliderect(egg_rect):
        score += 1
        eggX = random.randint(10, 500)  # Limit egg spawn within x-axis boundaries
        eggY = random.randint(100, 200)
        eggY_change += 0.020

    if eggY >= 520:
        print("Missed ")
        break
    with open("HighScore.txt", "w") as file:
        file.write(str(score))
    scr = font.render("Score: " + str(score), True, (0, 0, 0))
    sc.blit(scr, (10, 10))
    pygame.display.flip()
