import pygame
import player
import map
import sys
import json


pygame.init()
pygame.font.init()


class Game():
    def __init__(self):
        self.FPS = 60
        self.map_index = 0
        self.gameMap = map.create_game_map_list()
        self.pl = player.Player(self.gameMap[self.map_index].starting_point)
        self.gameEnd = False

    def draw_window(self, gameMap):
        for element in map.BACKGROUNDS:
            map.WIN.blit(element, (0, 0))

        gameMap.draw_map()
        gameMap.every_animation(self.pl, gameMap.item_list)

        self.pl.player_animation(map.WIN, gameMap.monster_list, gameMap.killed_monsters)

        pygame.display.update()


    def draw_menu(self, button_list):
        map.WIN.fill((0, 0, 0))

        for button in button_list:
            button.draw_button()

        pygame.display.update()


    def draw_options(self):
        map.WIN.fill((0 ,0, 0))

        map.WIN.blit(map.Control_options, (0, 0))

        pygame.display.update()

    def check_map_conditions(self, max_map_id, killed_monsters, game_level_map):
        '''
        function is checking if we can change to another map panel
        '''
        if self.pl.pos.right > map.SCREEN_WIDTH and self.map_index != max_map_id:
            self.map_index += 1
            self.pl.pos.x -= map.SCREEN_WIDTH - player.PLAYER_WIDTH

        elif self.pl.pos.left < 0 and self.map_index != 0:
            self.map_index -= 1
            self.pl.pos.x += map.SCREEN_WIDTH - player.PLAYER_WIDTH

        if self.pl.pos.right - player.PLAYER_WIDTH/4 > map.SCREEN_WIDTH and self.map_index == max_map_id:
            self.gameEnd = True

        elif self.pl.pos.left + player.PLAYER_WIDTH/4 < 0 and self.map_index == 0:
            self.pl.collision_types["left"] = True

        if self.pl.pos.top > map.SCREEN_HEIGHT:
            self.pl.get_hit(self.pl.health_bar.max_health)

        for monster in killed_monsters:
            if monster.isBoss:
                if monster.isDead:
                    game_level_map[4][10] = 5
                    game_level_map[6][7] = 5

    def main_menu(self):
        '''
        main menu view
        '''
        resume_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 100, map.BUTTONS[0])
        new_game_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 300, map.BUTTONS[1])
        options_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 700, map.BUTTONS[2])
        continue_button = map.Button(map.SCREEN_WIDTH//2 - map.BUTTONS_WIDTH//2, 500, map.BUTTONS[3])
        clock = pygame.time.Clock()
        menu = True
        click = False
        gameIsRunning = False

        while menu:
            clock.tick(self.FPS)
            mx, my = pygame.mouse.get_pos()

            if new_game_button.pos.collidepoint((mx, my)):
                if click:
                    gameIsRunning = True
                    self.map_index = 0
                    self.gameMap = map.create_game_map_list()
                    self.pl = player.Player(self.gameMap[self.map_index].starting_point)
                    self.game_save()
                    self.game(clock)

            if resume_button.pos.collidepoint((mx, my)):
                if click and gameIsRunning:
                    self.game(clock)

            if options_button.pos.collidepoint((mx, my)):
                if click:
                    self.options(clock)

            if continue_button.pos.collidepoint((mx, my)):
                if click:
                    with open("save_data.txt") as save_file:
                        save_data = json.load(save_file)
                        self.map_index = save_data["Map_index"]
                        player_data = save_data["Player"]
                        gm_data = save_data["Game_map"]
                        self.gameMap = map.create_game_map_list()
                        self.pl = player.Player(self.gameMap[self.map_index].starting_point)
                        self.load_player_data(player_data)
                        self.load_gm_data(gm_data)

                    gameIsRunning = True
                    self.pl.gameOver = False
                    self.game(clock)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and gameIsRunning and not self.pl.gameOver:
                        self.game(clock)

            if gameIsRunning and not self.pl.gameOver:
                self.draw_menu([resume_button, new_game_button, options_button, continue_button])
            else:
                self.draw_menu([new_game_button, options_button, continue_button])


    def game(self, clock):

        game_on = True
        while game_on:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.pl.get_hit(30)

                    if event.key == pygame.K_c:
                        self.pl.heal(30)

                    if event.key == pygame.K_ESCAPE:
                        game_on = False

                    if event.key == pygame.K_F5:
                        self.game_save()

            keys_pressed = pygame.key.get_pressed()
            gm = self.gameMap[self.map_index]
            self.pl.colliding_check(gm.tiles_rects, gm.monster_list, gm.item_list, gm.taken_items)
            self.check_map_conditions(len(self.gameMap)-1, gm.killed_monsters, gm.game_level_map)
            self.pl.move(keys_pressed)
            self.draw_window(gm)


            if self.pl.gameOver:
                self.game_over_screen(clock)
                game_on = False
            if self.gameEnd:
                self.ending_screen(clock)
                game_on = False
                self.pl.gameOver = True

    def game_over_screen(self, clock):
        game_over_font = pygame.font.SysFont('Comic Sans MS', 70)
        text = game_over_font.render('Game Over', False, (255, 255, 255))
        game_over_scr_on = True
        while game_over_scr_on:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over_scr_on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_over_scr_on = False

            map.WIN.fill((0, 0, 0))
            map.WIN.blit(text, (map.SCREEN_WIDTH//2 - text.get_width()//2, map.SCREEN_HEIGHT//2 - text.get_height()//2))
            pygame.display.update()

    def ending_screen(self, clock):
        ending_text_font = pygame.font.SysFont('Comic Sans MS', 70)
        text = ending_text_font.render('Congratulations!', False, (255, 255, 255))
        developers_text_font = pygame.font.SysFont('ComicSans MS', 32)
        text2 = developers_text_font.render('Developers: Jakub Koniuszewski, Michał Meyer', False, (255, 255, 255))
        ending_scr_on = True
        while ending_scr_on:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over_scr_on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ending_scr_on = False
                    self.gameEnd = False

            map.WIN.fill((0, 0, 0))
            map.WIN.blit(text, (map.SCREEN_WIDTH//2 - text.get_width()//2, map.SCREEN_HEIGHT//2 - text.get_height()))
            map.WIN.blit(text2, (map.SCREEN_WIDTH// 2 - text2.get_width()// 2, map.SCREEN_HEIGHT*0.9))
            pygame.display.update()

    def options(self, clock):

        options_on = True
        while options_on:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    options_on = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        options_on = False

            self.draw_options()

    def game_save(self):
        player_data = {"Health": self.pl.health_bar.current_health, "Max_health":self.pl.health_bar.max_health, "DMG": self.pl.DMG, "Position": (self.pl.pos.x, self.pl.pos.y)}
        gm_data_dict = {}
        for gm in self.gameMap:
            monster_id = []
            for monster in gm.killed_monsters:
                monster_id.append(monster.id)

            item_id = []
            for item in gm.taken_items:
                item_id.append(item.id)

            gm_data = {"Killed_monsters":monster_id, "Taken_items":item_id}
            gm_data_dict[gm.id] = gm_data

        save_data = {"Map_index": self.map_index, "Player": player_data, "Game_map": gm_data_dict}

        with open("save_data.txt", "w") as save_file:
            json.dump(save_data, save_file)

    def load_player_data(self, player_data):
        '''
        load player params from save_data.txt
        '''
        self.pl.health_bar.expand_max_health(player_data["Max_health"] - self.pl.health_bar.max_health)
        self.pl.health_bar.current_health = player_data["Health"]
        self.pl.health_bar.targeted_health = player_data["Health"]
        self.pl.DMG = player_data["DMG"]
        self.pl.pos.x = player_data["Position"][0]
        self.pl.pos.y = player_data["Position"][1]

    def load_gm_data(self, gm_data):
        '''
        load game map params from save_data.txt
        '''
        for gm in self.gameMap:
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


def main():
    ActionGame = Game()
    ActionGame.main_menu()


if __name__ == "__main__":
    main()
