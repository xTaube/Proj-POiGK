import pygame
import player
import map


def draw_window(pl, gameMap):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    gameMap.draw_map()
    gameMap.every_animation(pl)

    pl.player_animation(map.WIN)
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pl.get_hit(30)

                if event.key == pygame.K_c:
                    pl.heal(30)
        keys_pressed = pygame.key.get_pressed()
        pl.colliding_check(gameMap[map_index].tiles_rects, gameMap[map_index].monster_list, gameMap[map_index].item_list)
        pl.move(keys_pressed)
        draw_window(pl, gameMap[map_index])


if __name__ == "__main__":
    main()
