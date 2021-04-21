import pygame
import os
from main import SCREEN_WIDTH, SCREEN_HEIGHT

BACKGROUNDS = [pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "cloudySky.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par1_tileable.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par2_tileable.png")), (SCREEN_WIDTH, SCREEN_HEIGHT)),
               pygame.transform.scale(pygame.image.load(os.path.join("map assets\\Ruin", "par3_tileable.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
               ]

class Tile_object:
    def __init__(self, posX, posY, img, canCollide):
        self.posX = posX
        self.posY = posY
        self.img = img
        self.canColide = canCollide


Game_level = []
for background in BACKGROUNDS:
    Game_level.append(Tile_object(0, 0, background, false))

