import pygame
import os
import player

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1200
FPS = 60
WIN = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# majkel
list = []

def draw_window(pl):
    WIN.fill(color=[255, 255, 255])

    #animacje protagonisty
    if pl.walkCount + 1 >= 36:
        pl.walkCount = 0

    if pl.idleCount + 1 >= 9:
        pl.idleCount = 0

    if pl.attackCount + 1 >= 25:
        pl.attackCount = 0
        pl.isAttacking = False

    if pl.isAttacking and pl.left:
        WIN.blit(player.ATTACK_LEFT[pl.attackCount//5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.isAttacking:
        WIN.blit(player.ATTACK_RIGHT[pl.attackCount//5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.isAttacking and pl.left:
        WIN.blit(player.ATTACK_LEFT[pl.attackCount//5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.left and not pl.isJumping:
        WIN.blit(player.WALK_LEFT[pl.walkCount//6], (pl.posX, pl.posY))
        pl.walkCount += 1

    elif pl.right and not pl.isJumping:
        WIN.blit(player.WALK_RIGHT[pl.walkCount//6], (pl.posX, pl.posY))
        pl.walkCount += 1

    elif pl.isJumping and pl.left:
        WIN.blit(player.JUMPING_LEFT[round(pl.jumpCount//4)], (pl.posX, pl.posY))

    elif pl.isJumping:
        WIN.blit(player.JUMPING_RIGHT[round(pl.jumpCount//4)], (pl.posX, pl.posY))

    else:
        WIN.blit(player.STANDING[round(pl.idleCount//3)], (pl.posX, pl.posY))
        pl.idleCount += 0.2

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    game_on = True
    pl = player.Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        pl.move(keys_pressed)
        draw_window(pl)

if __name__ == "__main__":
    main()
