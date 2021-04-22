import pygame
import player
import map
import monsters

def player_animation(pl):
    if pl.walkCount + 1 >= 36:
        pl.walkCount = 0

    if pl.idleCount + 1 >= 9:
        pl.idleCount = 0

    if pl.attackCount + 1 >= 25:
        pl.attackCount = 0
        pl.isAttacking = False

    if pl.isAttacking and pl.left:
        map.WIN.blit(player.ATTACK_LEFT[pl.attackCount // 5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.isAttacking:
        map.WIN.blit(player.ATTACK_RIGHT[pl.attackCount // 5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.isAttacking and pl.left:
        map.WIN.blit(player.ATTACK_LEFT[pl.attackCount // 5], (pl.posX, pl.posY))
        pl.attackCount += 1

    elif pl.left and not pl.isJumping:
        map.WIN.blit(player.WALK_LEFT[pl.walkCount // 6], (pl.posX, pl.posY))
        pl.walkCount += 1

    elif pl.right and not pl.isJumping:
        map.WIN.blit(player.WALK_RIGHT[pl.walkCount // 6], (pl.posX, pl.posY))
        pl.walkCount += 1

    elif pl.isJumping and pl.left:
        map.WIN.blit(player.JUMPING_LEFT[round(pl.jumpCount // 4)], (pl.posX, pl.posY))

    elif pl.isJumping:
        map.WIN.blit(player.JUMPING_RIGHT[round(pl.jumpCount // 4)], (pl.posX, pl.posY))

    else:
        map.WIN.blit(player.STANDING[round(pl.idleCount // 3)], (pl.posX, pl.posY))
        pl.idleCount += 0.2


def draw_window(pl, mon_list):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    x = 0
    for col in range(len(map.Game_level)):
        for row in range(len(map.Game_level[0])):
            if map.Game_level[col][row] != -1:
                if map.Game_level[col][row] > 8:
                    if map.Game_level[col][row] == 12 or map.Game_level[col][row] == 14:
                        map.WIN.blit(map.PLATFORM_TILES[map.Game_level[col][row]], (row * map.SCREEN_WIDTH // 16, col * map.SCREEN_WIDTH // 16 - map.SCREEN_HEIGHT // 100))
                    else:
                        map.WIN.blit(map.PLATFORM_TILES[map.Game_level[col][row]], (row * map.SCREEN_WIDTH // 16, col * map.SCREEN_WIDTH // 16 + map.SCREEN_HEIGHT//100))
                else:
                    map.WIN.blit(map.PLATFORM_TILES[map.Game_level[col][row]], (row*map.SCREEN_WIDTH//16, col*map.SCREEN_HEIGHT//9))

    player_animation(pl)
    pygame.display.update()


def main():
    FPS = 60
    clock = pygame.time.Clock()
    game_on = True
    pl = player.Player(map.SCREEN_WIDTH//2, 450)

    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                quit()

        keys_pressed = pygame.key.get_pressed()
        pl.move(keys_pressed)
        draw_window(pl, monster_list)


if __name__ == "__main__":
    main()
