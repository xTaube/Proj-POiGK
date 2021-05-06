import pygame
import os
from conf import SCREEN_WIDTH, SCREEN_HEIGHT


class Demon():
    DEMON_WIDTH = SCREEN_WIDTH // 5
    DEMON_HEIGHT = round(DEMON_WIDTH*0.8)
    #####
    WALK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "walk_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_6.png"))]
    WALK_RIGHT = []
    for img in WALK_ANIMATIONS:
        WALK_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    WALK_LEFT = []
    for img in WALK_RIGHT:
        WALK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_3.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_4.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_5.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_6.png"))]
    STANDING = []
    for img in STANDING_ANIMATIONS:
        STANDING.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    #####
    JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "jump_1.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_2.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_3.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_4.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_5.png"))]
    JUMPING_RIGHT = []
    for img in JUMPING_ANIMATIONS:
        JUMPING_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    JUMPING_LEFT = []
    for img in JUMPING_RIGHT:
        JUMPING_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    LIGHT_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "attack1_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack1_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack1_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack1_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack1_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack1_6.png"))]
    LIGHT_ATTACK_RIGHT = []
    for img in LIGHT_ATTACK_ANIMATIONS:
        LIGHT_ATTACK_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    LIGHT_ATTACK_LEFT = []
    for img in LIGHT_ATTACK_RIGHT:
        LIGHT_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HEAVY_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "attack2_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack2_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack2_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack2_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack2_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\demon", "attack2_6.png"))]
    HEAVY_ATTACK_RIGHT = []
    for img in HEAVY_ATTACK_ANIMATIONS:
        HEAVY_ATTACK_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    HEAVY_ATTACK_LEFT = []
    for img in HEAVY_ATTACK_RIGHT:
        HEAVY_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    DEAD_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "dead_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "dead_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "dead_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "dead_4.png"))]
    DEAD = []
    for img in DEAD_ANIMATIONS:
        DEAD.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\demon", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\demon", "hit_3.png"))]
    HIT_RIGHT = []
    for img in HIT_ANIMATIONS:
        HIT_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))

    HIT_LEFT = []
    for img in HIT_RIGHT:
        HIT_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd):
        self.pos = pygame.Rect(posX, posY, self.DEMON_WIDTH, self.DEMON_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.hitCount = 0
        self.vel = self.DEMON_WIDTH//120
        self.health = 25
        self.DMG = 5
        self.hit_side = False     # False = left // True = right
        self.isDead = False
        self.isAttacking = False
        self.gettingDMG = False

    def enemy_animation(self, WIN, pl):
        if self.gettingDMG:
            if self.hit_side:
                WIN.blit(self.HIT_RIGHT[round(self.hitCount // 3)], (self.pos.x, self.pos.y))
            else:
                WIN.blit(self.HIT_LEFT[round(self.hitCount // 3)], (self.pos.x, self.pos.y))

            self.hitCount += 0.2
            if self.hitCount >= 7:
                self.hitCount = 0
                self.gettingDMG = False
        else:
            self.move()
            if self.walkCount + 1 >= 36:
                self.walkCount = 0

            if self.vel > 0:
                WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
                self.walkCount += 0.5
            else:
                WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
                self.walkCount += 0.5

            # pygame.draw.rect(WIN, (0, 0, 0), self.pos)

    def move(self):
        if self.vel > 0:
            if self.pos.x + self.vel < self.path[1]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.pos.x - self.vel > self.path[0]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

class Imp():
    IMP_WIDTH = SCREEN_WIDTH // 12
    IMP_HEIGHT = round(IMP_WIDTH*1.35)
    #####
    WALK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "walk_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "walk_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "walk_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "walk_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "walk_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "walk_6.png"))]
    WALK_RIGHT = []
    for img in WALK_ANIMATIONS:
        WALK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    WALK_LEFT = []
    for img in WALK_RIGHT:
        WALK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_3.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_4.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_5.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_6.png"))]
    STANDING = []
    for img in STANDING_ANIMATIONS:
        STANDING.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    #####
    JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "jump_1.png")),
                          pygame.image.load(os.path.join("enemy animation\\imp", "jump_2.png")),
                          pygame.image.load(os.path.join("enemy animation\\imp", "jump_3.png")),
                          pygame.image.load(os.path.join("enemy animation\\imp", "jump_4.png")),
                          pygame.image.load(os.path.join("enemy animation\\imp", "jump_5.png"))]
    JUMPING_RIGHT = []
    for img in JUMPING_ANIMATIONS:
        JUMPING_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    JUMPING_LEFT = []
    for img in JUMPING_RIGHT:
        JUMPING_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    LIGHT_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "attack1_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack1_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack1_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack1_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack1_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack1_6.png"))]
    LIGHT_ATTACK_RIGHT = []
    for img in LIGHT_ATTACK_ANIMATIONS:
        LIGHT_ATTACK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    LIGHT_ATTACK_LEFT = []
    for img in LIGHT_ATTACK_RIGHT:
        LIGHT_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HEAVY_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "attack2_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack2_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack2_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack2_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack2_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\imp", "attack2_6.png"))]
    HEAVY_ATTACK_RIGHT = []
    for img in HEAVY_ATTACK_ANIMATIONS:
        HEAVY_ATTACK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    HEAVY_ATTACK_LEFT = []
    for img in HEAVY_ATTACK_RIGHT:
        HEAVY_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    DEAD_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "fall_back_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "fall_back_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "fall_back_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "fall_back_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\imp", "fall_back_5.png"))]
    DEAD = []
    for img in DEAD_ANIMATIONS:
        DEAD.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\imp", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\imp", "hit_3.png"))]
    HIT = []
    for img in HIT_ANIMATIONS:
        HIT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    #####
    def __init__(self, posX, posY, posEnd):
        self.pos = pygame.Rect(posX, posY, self.IMP_WIDTH, self.IMP_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.vel = 1
        self.health = 25
        self.DMG = 5
        self.isDead = False
        self.isAttacking = False

    def enemy_animation(self, WIN, pl):
        self.move(pl)
        if self.walkCount + 1 >= 36:
            self.walkCount = 0

        if self.vel > 0:
            WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
            self.walkCount += 0.5
        else:
            WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
            self.walkCount += 0.5

    def move(self, pl):
        if self.vel > 0:
            if self.pos.x + self.vel < self.path[1]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.pos.x - self.vel > self.path[0]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0


class Skeleton():
    SKELETON_WIDTH = SCREEN_WIDTH // 13
    SKELETON_HEIGHT = round(SKELETON_WIDTH * 1.35)
    #####
    WALK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "walk_6.png"))]
    WALK_RIGHT = []
    for img in WALK_ANIMATIONS:
        WALK_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    WALK_LEFT = []
    for img in WALK_RIGHT:
        WALK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_3.png"))]
    STANDING = []
    for img in STANDING_ANIMATIONS:
        STANDING.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    #####
    JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "jump_1.png")),
                          pygame.image.load(os.path.join("enemy animation\\skeleton", "jump_2.png")),
                          pygame.image.load(os.path.join("enemy animation\\skeleton", "jump_3.png")),
                          pygame.image.load(os.path.join("enemy animation\\skeleton", "jump_4.png")),
                          pygame.image.load(os.path.join("enemy animation\\skeleton", "jump_5.png"))]
    JUMPING_RIGHT = []
    for img in JUMPING_ANIMATIONS:
        JUMPING_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    JUMPING_LEFT = []
    for img in JUMPING_RIGHT:
        JUMPING_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    LIGHT_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack1_6.png"))]
    LIGHT_ATTACK_RIGHT = []
    for img in LIGHT_ATTACK_ANIMATIONS:
        LIGHT_ATTACK_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    LIGHT_ATTACK_LEFT = []
    for img in LIGHT_ATTACK_RIGHT:
        LIGHT_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HEAVY_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\skeleton", "attack2_6.png"))]
    HEAVY_ATTACK_RIGHT = []
    for img in HEAVY_ATTACK_ANIMATIONS:
        HEAVY_ATTACK_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    HEAVY_ATTACK_LEFT = []
    for img in HEAVY_ATTACK_RIGHT:
        HEAVY_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    DEAD_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_near_6.png"))]
    DEAD = []
    for img in DEAD_ANIMATIONS:
        DEAD.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_3.png"))]
    HIT = []
    for img in HIT_ANIMATIONS:
        HIT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))

    #####
    def __init__(self, posX, posY, posEnd):
        self.pos = pygame.Rect(posX, posY, self.SKELETON_WIDTH, self.SKELETON_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.vel = 1
        self.health = 25
        self.DMG = 5
        self.isDead = False
        self.isAttacking = False

    def enemy_animation(self, WIN, pl):
        self.move()
        if self.walkCount + 1 >= 36:
            self.walkCount = 0

        if self.vel > 0:
            WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
            self.walkCount += 0.5
        else:
            WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], (self.pos.x, self.pos.y))
            self.walkCount += 0.5

    def move(self):
        if self.vel > 0:
            if self.pos.x + self.vel < self.path[1]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.pos.x - self.vel > self.path[0]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
