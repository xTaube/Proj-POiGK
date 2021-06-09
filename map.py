import pygame
import os
from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from monsters import Demon, Imp, Skeleton, Knight, Wizard


pygame.init()
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

BACKGROUNDS = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "cloudySky.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par1_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par2_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par3_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))]


for background in BACKGROUNDS:
    background.set_colorkey((255, 255, 255))

PLATFORM_TILES = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "long_platform.png")).convert(), (SCREEN_WIDTH // 8, SCREEN_HEIGHT // 18)),                                             #0
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                             #1
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), True, False), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),             #2
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "mossyTile.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                 #3
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "path_tile.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                 #4
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "single_platform.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 18)),                                          #5
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                 #6
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall.png")).convert(), True, False), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),             #7
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "black_wall.png")).convert(), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),                                                    #8
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "fence1.png")).convert(), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),                                                        #9
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "fence2.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                    #10
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "tree1.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                     #11
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "tree2.png")).convert(), (SCREEN_WIDTH // 8, SCREEN_HEIGHT // 4)),                                                      #12
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rockpile2.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                                 #13
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rockpile3.png")).convert(), (SCREEN_WIDTH // 8, SCREEN_HEIGHT // 4)),                                                  #14
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall_2.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                               #15
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall_2.png")).convert(), True, False), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),               #16
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "path_tile_2.png")).convert(), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9)),                                               #17
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "path_tile.png")).convert(), False, True), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),             #18sufit
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall_2.png")).convert(), False, True), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),           #19
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall_2.png")).convert(), True, True), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),            #20
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), False, True), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),         #21
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), True, True), (SCREEN_WIDTH//16, SCREEN_HEIGHT//9)),          #22
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "path_tile.png")).convert(), True, True), (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9))  ]        #23


for tile in PLATFORM_TILES:
    tile.set_colorkey((255, 255, 255))

BUTTONS_WIDTH = SCREEN_WIDTH // 5
BUTTONS_HEIGHT = SCREEN_WIDTH // 15
BUTTONS = [pygame.transform.scale(pygame.image.load(os.path.join("menu", "Resume Button.png")).convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT)),
           pygame.transform.scale(pygame.image.load(os.path.join("menu", "New game Button.png")).convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT)),
           pygame.transform.scale(pygame.image.load(os.path.join("menu", "Options Button.png")).convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT)),
           pygame.transform.scale(pygame.image.load(os.path.join("menu", "Continue Button.png")).convert(), (BUTTONS_WIDTH, BUTTONS_HEIGHT))]

Control_options = pygame.transform.scale(pygame.image.load(os.path.join("menu", "Control_options.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

class Button:
    '''
    defining button
    '''
    def __init__(self, posX, posY, img):
        self.pos = pygame.Rect(posX, posY, BUTTONS_WIDTH, BUTTONS_HEIGHT)
        self.img = img

    def draw_button(self):
        '''
        drawing button
        '''
        WIN.blit(self.img, self.pos)


class GameMap:
    '''
    this class defines a single panel of whole map
    '''
    def __init__(self, game_level_map, starting_point, monster_list, item_list, id):
        self.id = id
        self.game_level_map = game_level_map
        self.starting_point = starting_point
        self.monster_list = monster_list
        self.item_list = item_list
        self.taken_items = []
        self.killed_monsters = []
        self.tiles_rects = []
        self.cleared = False

    def draw_map(self):
        '''
        displaying current map panel
        '''
        self.tiles_rects.clear()
        for col in range(len(self.game_level_map)):
            for row in range(len(self.game_level_map[0])):
                if self.game_level_map[col][row] != -1:
                    if self.game_level_map[col][row] > 8 and self.game_level_map[col][row] < 15:  # dla 15,16 kolizja
                        if self.game_level_map[col][row] == 12 or self.game_level_map[col][row] == 14:
                            WIN.blit(PLATFORM_TILES[self.game_level_map[col][row]], (row * SCREEN_WIDTH // 16, col * SCREEN_WIDTH // 16 - SCREEN_HEIGHT // 100))
                        else:
                            WIN.blit(PLATFORM_TILES[self.game_level_map[col][row]], (row * SCREEN_WIDTH // 16, col * SCREEN_WIDTH // 16 + SCREEN_HEIGHT // 100))
                    else:
                        WIN.blit(PLATFORM_TILES[self.game_level_map[col][row]], (row * SCREEN_WIDTH // 16, col * SCREEN_HEIGHT // 9))
                        if self.game_level_map[col][row] != 8:
                            if self.game_level_map[col][row] == 0:
                                self.tiles_rects.append(pygame.Rect(row * SCREEN_WIDTH // 16, col * SCREEN_HEIGHT // 9, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 18))
                            elif self.game_level_map[col][row] == 5:
                                self.tiles_rects.append(pygame.Rect(row * SCREEN_WIDTH // 16, col * SCREEN_HEIGHT // 9, SCREEN_WIDTH // 16, SCREEN_HEIGHT // 18))
                            else:
                                self.tiles_rects.append(pygame.Rect(row * SCREEN_WIDTH // 16, col * SCREEN_HEIGHT // 9, SCREEN_WIDTH // 16, SCREEN_HEIGHT // 9))

    def every_animation(self, pl, item_list):
        '''
        displaying monsters and items sprites
        '''
        for monster in self.monster_list:
            monster.enemy_animation(WIN, pl, self.monster_list, self.killed_monsters)

        for items in self.item_list:
            items.animation()


class Life_up:
    '''
    defines item which extends hero health bar
    '''
    ANIMATION = [pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-0.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-1.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-2.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-3.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-4.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\life_up", "Life_up-5.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 ]

    for animation in ANIMATION:
        animation.set_colorkey((0, 0, 0))

    def __init__(self, health_amount, posX, posY, id):
        self.id = id
        self.pos = pygame.Rect(posX, posY, SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)
        self.health_amount = health_amount
        self.animation_count = 0

    def animation(self):
        '''
        item displaying logic
        '''
        WIN.blit(self.ANIMATION[self.animation_count // 6], (self.pos.x, self.pos.y))
        self.animation_count += 1
        if self.animation_count >= 36:
            self.animation_count = 0

    def effect(self, pl):
        '''
        item effect logic
        '''
        pl.health_bar.expand_max_health(self.health_amount)
        pl.heal(self.health_amount)

    def isPossibleToTake(self, pl):
        '''
        checking if hero can take the item
        '''
        if pl.health_bar.max_health == 300:
            return False
        else:
            return True


class Heal:
    '''
    defines item which heals hero
    '''
    ANIMATION = [pygame.transform.scale(pygame.image.load(os.path.join("items\\heal", "Heart-0.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\heal", "Heart-1.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\heal", "Heart-2.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\heal", "Heart-3.png")).convert(), (SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)),
                 ]

    for animation in ANIMATION:
        animation.set_colorkey((0, 0, 0))

    def __init__(self, health_amount, posX, posY, id):
        self.id = id
        self.pos = pygame.Rect(posX, posY, SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)
        self.health_amount = health_amount
        self.animation_count = 0

    def animation(self):
        '''
        item displaying logic
        '''
        WIN.blit(self.ANIMATION[round(self.animation_count // 4)], (self.pos.x, self.pos.y))
        self.animation_count += 0.5
        if self.animation_count >= 16:
            self.animation_count = 0

    def effect(self, pl):
        '''
        item effect logic
        '''
        pl.heal(self.health_amount)

    def isPossibleToTake(self, pl):
        '''
        checking if hero can take the item
        '''
        if pl.health_bar.current_health == pl.health_bar.max_health:
            return False
        else:
            return True


class Dmg_up:
    '''
    defines item which boosts hero damage
    '''
    ANIMATION = [pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_1.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_2.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_3.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_4.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_5.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_6.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_7.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_8.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_9.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_10.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_11.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15)),
                 pygame.transform.scale(pygame.image.load(os.path.join("items\\dmg_up", "Espada_12.png")).convert(), (SCREEN_WIDTH // 22, SCREEN_HEIGHT // 15))]

    for animation in ANIMATION:
        animation.set_colorkey((0, 0, 0))

    def __init__(self, dmg_value, posX, posY, id):
        self.id = id
        self.pos = pygame.Rect(posX, posY, SCREEN_WIDTH // 18, SCREEN_HEIGHT // 11)
        self.dmg_value = dmg_value
        self.animation_count = 0

    def animation(self):
        '''
        item displaying logic
        '''
        WIN.blit(self.ANIMATION[self.animation_count // 12], (self.pos.x, self.pos.y))
        self.animation_count += 1
        if self.animation_count >= 144:
            self.animation_count = 0

    def effect(self, pl):
        '''
        item effect logic
        '''
        pl.dmg_up(self.dmg_value)

    def isPossibleToTake(self, pl):
        '''
        checking if hero can take the item
        '''
        if pl.DMG == 50:
            return False
        else:
            return True


def create_game_map_list():
    '''
    in this function we create map from single panels
    '''
    gameMap_list = []

    Game_level = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1],
                  [9, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [6, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, 12, 14, -1],
                  [6, 9, 9, -1, 10, -1, 10, -1, 10, -1, 10, 10, 13, -1, -1, -1],
                  [15, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4],
                  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]

    gameMap_list.append(
        GameMap(
            Game_level, (200, 700),
            [Imp(220, 350, 590, 0), Imp(950, 350, 1350, 1), Demon(550, -10, 1300, 2), Skeleton(750, 580, 1350, 3)],
            [Life_up(25, 1450, 150, 0), Heal(10, 246, 280, 1)],
            0)
    )
#Heal(20, 246, 280, 0) Knight(650, 550, 1250, 2)
    Game_level = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, 20],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22],
                  [-1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, 9],
                  [-1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, 2, 3, 3, 4],
                  [-1, -1, -1, 14, -1, -1, -1, -1, -1, -1, 5, -1, 7, 8, 8, 8],
                  [10, -1, -1, -1, -1, 9, -1, -1, 10, -1, -1, -1, 7, 8, 8, 8],
                  [4, 4, 3, 4, 4, 1, -1, -1, 2, 4, 4, 4, 16, 8, 8, 8],
                  [8, 8, 8, 8, 8, 6, -1, -1, 7, 8, 8, 8, 8, 8, 8, 8]]

    gameMap_list.append(
        GameMap(
            Game_level, (50, 700),
            [Knight(350, 184, 700, 0), Skeleton(1400, 225, 1600, 1)],
            [Life_up(25, 247, 160, 0)],
            1)
    )

    Game_level = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                  [23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 20, 8, 8],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, 20, 8],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, 20],
                  [1, -1, -1, -1, -1, 5, -1, 5, -1, 5, -1, 5, -1, -1, -1, 22],
                  [15, 1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [8, 15, 1, 9, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, 13, 9],
                  [8, 8, 15, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3],
                  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]

    gameMap_list.append(
        GameMap(
            Game_level, (50, 400),
            [Demon(300, 580, 900, 0), Demon(1000, 580, 1600, 1)],
            [Heal(50, 240, 640, 0), Life_up(25, 1327, 385, 1)],
            2)
    )

    Game_level = [[8, 8, 8, 19, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [8, 8, 19, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [8, 19, 21, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, 2],
                  [19, 21, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, 7],
                  [21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, 7],
                  [-1, -1, -1, 5, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, 7],
                  [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7],
                  [1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, 7],
                  [6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, 7]]

    gameMap_list.append(
        GameMap(
            Game_level, (30, 700),
            [],
            [Dmg_up(25, 1570, 865, 0)],
            3)
    )

    Game_level = [[-1, -1, -1, -1, -1, 22, 23, 20, 19, 23, 21, -1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1, -1, -1, 22, 21, -1, -1, -1, -1, -1, -1, -1],
                  [ 4,  4,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2,  4,  4],
                  [19, 23, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, 23, 20],
                  [ 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  7],
                  [ 6, -1, 12, 12, -1, -1, -1, -1, -1, -1, -1, 12, 12, -1, -1,  7],
                  [ 6, 10, -1, 10, -1, 10, -1, -1, -1, -1, 10, -1, 10, -1, 10,  7],
                  [15,  4,  3,  3,  3,  4,  3,  4,  4,  3,  4,  3,  3,  3,  4, 16],
                  [ 8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8]]

    gameMap_list.append(
        GameMap(
            Game_level, (30, 100),
            [Wizard(100, 422, 1350, 0)],
            [Heal(50, 250, 160, 0)],
            4)
    )
    return gameMap_list
