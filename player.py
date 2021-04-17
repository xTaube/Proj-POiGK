import pygame
import os
#-------------------------------------------------------------
#animacje protagonisty
WALK_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-run-0.png")), pygame.image.load(os.path.join("player animation", "pl-run-1.png")), pygame.image.load(os.path.join("player animation", "pl-run-2.png")), pygame.image.load(os.path.join("player animation", "pl-run-3.png")), pygame.image.load(os.path.join("player animation", "pl-run-4.png")), pygame.image.load(os.path.join("player animation", "pl-run-5.png"))]
WALK_RIGHT = []
for img in WALK_ANIMATIONS:
    WALK_RIGHT.append(pygame.transform.scale(img, (140, 200)))

WALK_LEFT = []
for img in WALK_RIGHT:
    WALK_LEFT.append(pygame.transform.flip(img, True, False))

STANDING_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-idle-0.png")), pygame.image.load(os.path.join("player animation", "pl-idle-1.png")), pygame.image.load(os.path.join("player animation", "pl-idle-2.png"))]
STANDING = []
for img in STANDING_ANIMATIONS:
    STANDING.append(pygame.transform.scale(img, (140, 200)))

JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-jump-0.png")), pygame.image.load(os.path.join("player animation", "pl-jump-1.png")), pygame.image.load(os.path.join("player animation", "pl-jump-2.png")), pygame.image.load(os.path.join("player animation", "pl-jump-3.png"))]
JUMPING_RIGHT = []
for img in JUMPING_ANIMATIONS:
    JUMPING_RIGHT.append(pygame.transform.scale(img, (140, 200)))

JUMPING_LEFT = []
for img in JUMPING_RIGHT:
    JUMPING_LEFT.append(pygame.transform.flip(img, True, False))

ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-attack1-0.png")), pygame.image.load(os.path.join("player animation", "pl-attack1-1.png")), pygame.image.load(os.path.join("player animation", "pl-attack1-2.png")), pygame.image.load(os.path.join("player animation", "pl-attack1-3.png")), pygame.image.load(os.path.join("player animation", "pl-attack1-4.png"))]
ATTACK_RIGHT = []
for img in ATTACK_ANIMATIONS:
    ATTACK_RIGHT.append(pygame.transform.scale(img, (140, 200)))

ATTACK_LEFT = []
for img in ATTACK_RIGHT:
    ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
#--------------------------------------------------------------------
PL_VEL = 5

class Player():
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.walkCount = 0
        self.jumpCount = 10
        self.idleCount = 0
        self.attackCount = 0
        self.right = False
        self.left = False
        self.isJumping = False
        self.isAttacking = False

    def move(self, key_pressed):
        if key_pressed[pygame.K_RIGHT]:
            if not self.isAttacking: self.posX += PL_VEL
            self.right = True
            self.left = False
        elif key_pressed[pygame.K_LEFT]:
            if not self.isAttacking: self.posX -= PL_VEL
            self.right = False
            self.left = True
        else:
            self.right = False
            self.left = False

        if not(self.isJumping):
            if key_pressed[pygame.K_SPACE]:
                self.isJumping = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -neg
                self.posY -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 0.5
            else:
                self.isJumping = False
                self.jumpCount = 10

        if key_pressed[pygame.K_z] and not self.isAttacking:
            self.isAttacking = True
