import pygame
import player
import map
import sys
import json

def draw_window(pl, gameMap):

    for element in map.BACKGROUNDS:
        map.WIN.blit(element, (0, 0))

    gameMap.draw_map()
    gameMap.every_animation(pl, gameMap.item_list)

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

def check_map_conditions(pl, map_id, max_map_id, monster_list):
    m_id = map_id
    if pl.pos.right > map.SCREEN_WIDTH and m_id != max_map_id:
        m_id += 1
        pl.pos.x -= map.SCREEN_WIDTH - player.PLAYER_WIDTH

    elif pl.pos.left < 0 and m_id != 0:
        m_id-= 1
        pl.pos.x += map.SCREEN_WIDTH - player.PLAYER_WIDTH

    if pl.pos.right - player.PLAYER_WIDTH/4 > map.SCREEN_WIDTH and m_id == max_map_id:
        pl.collision_types["right"] = True

    elif pl.pos.left + player.PLAYER_WIDTH/4 < 0 and m_id == 0:
        pl.collision_types["left"] = True

    if pl.pos.top > map.SCREEN_HEIGHT:
        pl.get_hit(pl.health_bar.max_health, monster_list)

    return m_id

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
                map_index = game(FPS, clock, map_index, gameMap, pl)

        if resume_button.pos.collidepoint((mx, my)):
            if click and gameIsRunning:
                map_index = game(FPS, clock, map_index, gameMap, pl)

        if options_button.pos.collidepoint((mx, my)):
            if click:
                options(FPS, clock)

        if continue_button.pos.collidepoint((mx, my)):
            if click:
                with open("save_data.txt") as save_file:
                    save_data = json.load(save_file)
                    map_index = save_data["Map_index"]
                    player_data = save_data["Player"]
                    gm_data = save_data["Game_map"]
                    load_player_data(pl, player_data)
                    load_gm_data(gameMap, gm_data)

                gameIsRunning = True
                map_index = game(FPS, clock, map_index, gameMap, pl)

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
                    map_index = game(FPS, clock, map_index, gameMap, pl)

        if gameIsRunning:
            draw_menu([resume_button, new_game_button, options_button, continue_button])
        else:
            draw_menu([new_game_button, options_button, continue_button])


def game(FPS, clock, map_index, gameMap, pl):

    map_id = map_index
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
                    pl.get_hit(30,gameMap[map_id].monster_list)

                if event.key == pygame.K_c:
                    pl.heal(30)

                if event.key == pygame.K_ESCAPE:
                    game_on = False
                    return map_id

                if event.key == pygame.K_F5:
                    game_save(pl, gameMap, map_id)

        keys_pressed = pygame.key.get_pressed()
        pl.colliding_check(gameMap[map_id].tiles_rects, gameMap[map_id].monster_list, gameMap[map_id].item_list, gameMap[map_id].taken_items, )
        map_id = check_map_conditions(pl, map_id, len(gameMap)-1, gameMap[map_id].monster_list)
        pl.move(keys_pressed)
        draw_window(pl, gameMap[map_id])


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

def game_save(pl, gameMap, index):
    player_data = {"Health": pl.health_bar.current_health, "Max_health":pl.health_bar.max_health, "DMG": pl.DMG, "Position": (pl.pos.x, pl.pos.y)}
    gm_data_dict = {}
    for gm in gameMap:
        monster_id = []
        for monster in gm.killed_monsters:
            monster_id.append(monster.id)

        item_id = []
        for item in gm.taken_items:
            item_id.append(item.id)

        gm_data = {"Killed_monsters":monster_id, "Taken_items":item_id, "Cleared": gm.cleared}
        gm_data_dict[gm.id] = gm_data

    save_data = {"Map_index": index, "Player": player_data, "Game_map": gm_data_dict}

    with open("save_data.txt", "w") as save_file:
        json.dump(save_data, save_file)

def load_player_data(pl, player_data):
    pl.health_bar.expand_max_health(player_data["Max_health"] - pl.health_bar.max_health)
    pl.health_bar.current_health = player_data["Health"]
    pl.health_bar.targeted_health = player_data["Health"]
    pl.DMG = player_data["DMG"]
    pl.pos.x = player_data["Position"][0]
    pl.pos.y = player_data["Position"][1]

def load_gm_data(gmaps, gm_data):
    for gm in gmaps:
        gm_d = gm_data[str(gm.id)]
        killed_monsters = gm_d["Killed_monsters"]
        taken_items = gm_d["Taken_items"]

        for monster in gm.monster_list:
            if monster.id in killed_monsters:
                gm.killed_monsters.append(monster)

        for monster in gm.killed_monsters:
            if monster in gm.monster_list:
                gm.monster_list.remove(monster)

        for item in gm.item_list:
            if item.id in taken_items:
                gm.taken_items.append(item)

        for item in gm.taken_items:
            if item in gm.item_list:
                gm.item_list.remove(item)


        gm.cleared = gm_d["Cleared"]

if __name__ == "__main__":
    main_menu()
