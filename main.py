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


def draw_window(pl, map_index, gameMap):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    gameMap[map_index].draw_map()
    player_animation(pl)
    pygame.display.update()


def main():
    FPS = 60
    map_index = 0
    clock = pygame.time.Clock()
    game_on = True
    pl = player.Player(map.SCREEN_WIDTH//2, 450)
    gameMap = map.gameMap_list

    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                quit()

        keys_pressed = pygame.key.get_pressed()
        pl.move(keys_pressed)
        draw_window(pl, map_index, gameMap)


if __name__ == "__main__":
    main()
