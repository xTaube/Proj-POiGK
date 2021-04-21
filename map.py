import pygame
import os

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

BACKGROUNDS = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "cloudySky.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par1_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par2_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par3_tileable.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
               ]

for background in BACKGROUNDS:
    background.set_colorkey((255, 255, 255))

PLATFORM_TILES = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "long_platform.png")).convert(), (SCREEN_WIDTH//8, SCREEN_WIDTH//32)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "end_path_tile.png")).convert(), True, False), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "mossyTile.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "path_tile.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "single_platform.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//32)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "black_wall.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall.png")).convert(), (SCREEN_WIDTH//16, SCREEN_WIDTH//16)),
                  pygame.transform.scale(pygame.transform.flip(pygame.image.load(os.path.join("map assets\\Ruin", "rock_wall.png")).convert(), True, False), (SCREEN_WIDTH//16, SCREEN_WIDTH//16))
                  ]


for tile in PLATFORM_TILES:
    tile.set_colorkey((255, 255, 255))


Game_level = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [ 4,  4,  1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1],
              [ 6,  6,  7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
              [ 6,  6,  7, -1, -1,  2,  3,  4, 1,  -1, -1, -1,  2,  4,  4,  4],
              [ 6,  6,  7, -1, -1,  8,  6,  6, 7,  -1, -1, -1,  8,  6,  6,  6]
              ]

