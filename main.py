import pygame
import player
import map
import sys


def draw_window(pl, gameMap):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    gameMap.draw_map()
    gameMap.every_animation(pl)

    pl.player_animation(map.WIN, gameMap.monster_list, gameMap.killed_monsters, gameMap.cleared)

    if not gameMap.monster_list:
        gameMap.cleared = True

    pygame.display.update()


def draw_menu(button_list):
    map.WIN.fill((0, 0, 0))

    for button in button_list:
        button.draw_button()

    pygame.display.update()


def draw_options():
    map.WIN.fill((0 ,0, 0))

    map.WIN.blit(map.Control_options, (0, 0))

    pygame.display.update()

def check_map_conditions(pl, map_id, max_map_id):
    if pl.pos.right > map.SCREEN_WIDTH and map_id != max_map_id:
        map_id += 1
        pl.pos.x -= map.SCREEN_WIDTH - player.PLAYER_WIDTH

    elif pl.pos.left < 0 and map_id != 0:
        map_id -= 1
        pl.pos.x += map.SCREEN_WIDTH - player.PLAYER_WIDTH

    if pl.pos.right - player.PLAYER_WIDTH/4 > map.SCREEN_WIDTH and map_id == max_map_id:
        pl.collision_types["right"] = True

    elif pl.pos.left + player.PLAYER_WIDTH/4 < 0 and map_id == 0:
        pl.collision_types["left"] = True

    if pl.pos.top > map.SCREEN_HEIGHT:
        pl.get_hit(pl.health_bar.max_health)

    return map_id

def main_menu():
    resume_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 100, map.BUTTONS[0])
    new_game_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 300, map.BUTTONS[1])
    options_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 700, map.BUTTONS[2])
    continue_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 500, map.BUTTONS[3])
    FPS = 60
    map_index = 0
    gameMap = map.create_game_map_list()
    pl = player.Player(gameMap[map_index].starting_point)
    clock = pygame.time.Clock()
    menu = True
    click = False
    gameIsRunning = False

    while menu:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        if new_game_button.pos.collidepoint((mx, my)):
            if click:
                gameIsRunning = True
                map_index = 0
                gameMap = map.create_game_map_list()
                pl = player.Player(gameMap[map_index].starting_point)
                game(FPS, clock, map_index, gameMap, pl)

        if resume_button.pos.collidepoint((mx, my)):
            if click and gameIsRunning:
                game(FPS, clock, map_index, gameMap, pl)

        if options_button.pos.collidepoint((mx, my)):
            if click:
                options(FPS, clock)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and gameIsRunning:
                    game(FPS, clock, map_index, gameMap, pl)

        if gameIsRunning:
            draw_menu([resume_button, new_game_button, options_button, continue_button])
        else:
            draw_menu([new_game_button, options_button, continue_button])


def game(FPS, clock, map_index, gameMap, pl):

    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pl.get_hit(30)

                if event.key == pygame.K_c:
                    pl.heal(30)

                if event.key == pygame.K_ESCAPE:
                    game_on = False

                if event.key == pygame.K_F5:
                    pass

        keys_pressed = pygame.key.get_pressed()
        pl.colliding_check(gameMap[map_index].tiles_rects, gameMap[map_index].monster_list, gameMap[map_index].item_list)
        map_index = check_map_conditions(pl, map_index, len(gameMap)-1)
        pl.move(keys_pressed)
        draw_window(pl, gameMap[map_index])


def options(FPS, clock):

    options_on = True
    while options_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                options_on = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options_on = False

        draw_options()


if __name__ == "__main__":
    main_menu()
