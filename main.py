import pygame
import player
import map
import monsters


def draw_window(pl, demon, imp, skeleton, gameMap):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    gameMap.draw_map()
    pl.player_animation()
    # demon.enemy_animation()
    # imp.enemy_animation()
    # skeleton.enemy_animation()
    pygame.display.update()


def main():

    FPS = 60
    map_index = 0
    clock = pygame.time.Clock()
    game_on = True
    pl = player.Player(map.SCREEN_WIDTH//2, 450)
    demon = monsters.Demon(500, 450,920)
    imp = monsters.Imp(500, 750, 920)
    skeleton = monsters.Skeleton(500, 250, 920)
    gameMap = map.gameMap_list

    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                quit()

        keys_pressed = pygame.key.get_pressed()
        pl.colliding_check(gameMap[map_index].tiles_rects)
        pl.move(keys_pressed)
        draw_window(pl, demon, imp, skeleton, gameMap[map_index])


if __name__ == "__main__":
    main()
