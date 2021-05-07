import pygame
import os
from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from monsters import Demon, Imp, Skeleton


WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

BACKGROUNDS = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "cloudySky.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par1_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par2_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par3_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
               ]

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
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rockpile3.png")).convert(), (SCREEN_WIDTH // 8, SCREEN_HEIGHT // 4))                                                   #14
                  ]

for tile in PLATFORM_TILES:
    tile.set_colorkey((255, 255, 255))

class GameMap:
    def __init__(self, game_level_map, monster_list):
        self.game_level_map = game_level_map
        self.monster_list = monster_list
        self.tiles_rects = []

    def draw_map(self):
        self.tiles_rects.clear()
        for col in range(len(self.game_level_map)):
            for row in range(len(self.game_level_map[0])):
                if self.game_level_map[col][row] != -1:
                    if self.game_level_map[col][row] > 8:
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

        # for tile in self.tiles_rects:
        #     pygame.draw.rect(WIN, (255, 255, 255), tile)

    def monster_animation(self, pl):
        for monster in self.monster_list:
            monster.enemy_animation(WIN, pl)



gameMap_list = []

Game_level = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, 14, -1],
              [-1,  4, -1, -1, -1, -1,  9, 10,  9, -1, -1, 11, 13, -1, -1, -1],
              [ 4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4],
              [ 8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8]]


gameMap_list.append(GameMap(Game_level, [Demon(500, 585, 1400)]))
