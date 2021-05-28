import pygame
import os
from conf import SCREEN_WIDTH, SCREEN_HEIGHT
import time
ATTACK_CD = 50


class Demon():
    DEMON_WIDTH = SCREEN_WIDTH // 5
    DEMON_HEIGHT = round(DEMON_WIDTH * 0.8)
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
    SPRINT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "run_1.png")),
                         pygame.image.load(os.path.join("enemy animation\\demon", "run_2.png")),
                         pygame.image.load(os.path.join("enemy animation\\demon", "run_3.png")),
                         pygame.image.load(os.path.join("enemy animation\\demon", "run_4.png")),
                         pygame.image.load(os.path.join("enemy animation\\demon", "run_5.png")),
                         pygame.image.load(os.path.join("enemy animation\\demon", "run_6.png"))]
    SPRINT_RIGHT = []
    for img in SPRINT_ANIMATIONS:
        SPRINT_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))
    SPRINT_LEFT = []
    for img in SPRINT_RIGHT:
        SPRINT_LEFT.append(pygame.transform.flip(img, True, False))
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
    DEAD_RIGHT = []
    for img in DEAD_ANIMATIONS:
        DEAD_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))

    DEAD_LEFT = []
    for img in DEAD_RIGHT:
        DEAD_LEFT.append(pygame.transform.flip(img, True, False))
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

    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_3.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_4.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_5.png")),
                           pygame.image.load(os.path.join("enemy animation\\demon", "ready_6.png"))]
    STANDING_RIGHT = []
    for img in STANDING_ANIMATIONS:
        STANDING_RIGHT.append(pygame.transform.scale(img, (DEMON_WIDTH, DEMON_HEIGHT)))

    STANDING_LEFT = []
    for img in STANDING_RIGHT:
        STANDING_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd, id):
        self.pos = pygame.Rect(posX, posY, self.DEMON_WIDTH, self.DEMON_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.sprintCount = 0
        self.attackCount = 0
        self.idleCount = 0
        self.hitCount = 0
        self.deathCount = 0
        self.vel = self.DEMON_WIDTH // 120
        self.MAX_HEALTH = 30
        self.health = self.MAX_HEALTH
        self.DMG = 8
        self.hit_side = False  # False = left // True = right
        self.isDead = False
        self.isAttacking = False
        self.gettingDMG = False
        self.playerNearby = False
        self.playerVeryNearby = False
        self.left = False
        self.right = False
        self.ATTACK_COOLDOWN = ATTACK_CD
        self.bottomColission = True
        self.id = id

    def enemy_animation(self, WIN, pl, monster_list, killed_monsters):
        if self.isDead:
            if self.deathCount >= 16:
                self.health = 30
                self.deathCount = 0
                killed_monsters.append(self)
                monster_list.remove(self)
                self.isDead = False
                self.gettingDMG = False
            else:
                if self.hit_side:
                    WIN.blit(self.DEAD_RIGHT[round(self.deathCount // 4)], self.pos)
                else:
                    WIN.blit(self.DEAD_LEFT[round(self.deathCount // 4)], self.pos)
                self.deathCount += 0.5

        elif self.gettingDMG:
            if self.hit_side:
                WIN.blit(self.HIT_RIGHT[round(self.hitCount // 3)], self.pos)
            else:
                WIN.blit(self.HIT_LEFT[round(self.hitCount // 3)], self.pos)

            self.hitCount += 0.2
            if self.hitCount >= 7:
                self.hitCount = 0
                self.gettingDMG = False

        else:
            self.move(WIN, pl)
            # pygame.draw.rect(WIN, (0, 0, 0), self.pos)

    def move(self, WIN, pl):

        self.player_nearby(pl)
        self.player_very_nearby(pl)

        if pl.isDead:
            self.playerNearby = False
            self.playerVeryNearby = False

        if not self.playerNearby:
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

        if self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            if self.vel > 0 and self.pos.x + self.DEMON_WIDTH // 10 > pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel < 0 and self.pos.centerx + self.DEMON_WIDTH // 15 < pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel > 0 and self.pos.centerx + self.DEMON_WIDTH // 15 < pl.pos.x:
                self.pos.x += 1.25 * self.vel
                # self.left = True
                # self.right = False
            if self.vel < 0 and self.pos.x + self.DEMON_WIDTH // 10 > pl.pos.x:
                self.pos.x += 1.25 * self.vel
                # self.left = False
                # self.right = True

        ############
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.sprintCount + 1 >= 36:
            self.sprintCount = 0
        if self.idleCount + 1 >= 36:
            self.idleCount = 0

        if not self.playerNearby and not self.playerVeryNearby:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5
            else:
                WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5

        if self.playerVeryNearby and self.bottomColission:
            if self.attackCount + 1 >= 36:
                self.attackCount = 0
                self.ATTACK_COOLDOWN -= 1
                self.isAttacking = False
                self.playerVeryNearby = False


            elif self.isAttacking and self.left and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_RIGHT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1

            elif self.isAttacking and self.right and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_LEFT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1
            else:
                if self.left:
                    WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 6)], self.pos)
                    self.idleCount += 0.3
                elif self.right:
                    WIN.blit(self.STANDING_LEFT[round(self.idleCount // 6)], self.pos)
                    self.idleCount += 0.3

        elif self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.SPRINT_RIGHT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5
            else:
                WIN.blit(self.SPRINT_LEFT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5

        if (not self.bottomColission and self.playerNearby and not self.playerVeryNearby) or (
                not self.bottomColission and self.playerNearby and self.playerVeryNearby):
            if self.left:
                WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 6)], self.pos)
                self.idleCount += 0.3
            elif self.right:
                WIN.blit(self.STANDING_LEFT[round(self.idleCount // 6)], self.pos)
                self.idleCount += 0.3

    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

    def player_nearby(self, pl):
        if pl.pos.x - self.DEMON_WIDTH * 1.3 < self.pos.x < pl.pos.x + (self.DEMON_WIDTH // 2) * 1.3 and (self.pos.bottom * 0.95 < pl.pos.bottom < self.pos.bottom * 1.1):
            self.playerNearby = True
        else:
            self.playerVeryNearby = False
            self.playerNearby = False

    def player_very_nearby(self, pl):
        if pl.pos.x - self.DEMON_WIDTH * 0.65 < self.pos.x + self.DEMON_WIDTH // 12 < pl.pos.x + (self.DEMON_WIDTH // 2) * 0.3 and (
                pl.pos.top< self.pos.y + self.DEMON_HEIGHT / 2 < pl.pos.bottom):
            self.playerVeryNearby = True
        if pl.pos.x - self.DEMON_WIDTH * 0.6 < self.pos.x - self.DEMON_WIDTH // 4:
            self.right = True   # monster jest na prawo od gracza
            self.left = False
        elif self.pos.x < pl.pos.x + (self.DEMON_WIDTH // 2) * 0.3:
            self.right = False
            self.left = True

        if self.ATTACK_COOLDOWN == ATTACK_CD and not self.gettingDMG:
            self.isAttacking = True
        elif self.ATTACK_COOLDOWN < ATTACK_CD:
            self.ATTACK_COOLDOWN -= 1
            if self.ATTACK_COOLDOWN == 0:
                self.ATTACK_COOLDOWN = ATTACK_CD

        else:
            self.playerVeryNearby = False


class Imp():
    IMP_WIDTH = SCREEN_WIDTH // 5
    IMP_HEIGHT = round(IMP_WIDTH * 0.8)
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
    SPRINT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "run_1.png")),
                         pygame.image.load(os.path.join("enemy animation\\imp", "run_2.png")),
                         pygame.image.load(os.path.join("enemy animation\\imp", "run_3.png")),
                         pygame.image.load(os.path.join("enemy animation\\imp", "run_4.png")),
                         pygame.image.load(os.path.join("enemy animation\\imp", "run_5.png")),
                         pygame.image.load(os.path.join("enemy animation\\imp", "run_6.png"))]
    SPRINT_RIGHT = []
    for img in SPRINT_ANIMATIONS:
        SPRINT_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    SPRINT_LEFT = []
    for img in SPRINT_RIGHT:
        SPRINT_LEFT.append(pygame.transform.flip(img, True, False))
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
    DEAD_RIGHT = []
    for img in DEAD_ANIMATIONS:
        DEAD_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

    DEAD_LEFT = []
    for img in DEAD_RIGHT:
        DEAD_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\imp", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\imp", "hit_3.png"))]
    HIT_RIGHT = []
    for img in HIT_ANIMATIONS:
        HIT_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

    HIT_LEFT = []
    for img in HIT_RIGHT:
        HIT_LEFT.append(pygame.transform.flip(img, True, False))

    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\imp", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_3.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_4.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_5.png")),
                           pygame.image.load(os.path.join("enemy animation\\imp", "ready_6.png"))]
    STANDING_RIGHT = []
    for img in STANDING_ANIMATIONS:
        STANDING_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

    STANDING_LEFT = []
    for img in STANDING_RIGHT:
        STANDING_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd, id):
        self.pos = pygame.Rect(posX, posY, self.IMP_WIDTH, self.IMP_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.sprintCount = 0
        self.attackCount = 0
        self.idleCount = 0
        self.hitCount = 0
        self.deathCount = 0
        self.vel = self.IMP_WIDTH // 120
        self.MAX_HEALTH = 25
        self.health = self.MAX_HEALTH
        self.DMG = 5
        self.hit_side = False  # False = left // True = right
        self.isDead = False
        self.isAttacking = False
        self.gettingDMG = False
        self.playerNearby = False
        self.playerVeryNearby = False
        self.left = False
        self.right = False
        self.ATTACK_COOLDOWN = ATTACK_CD
        self.bottomColission = True
        self.id = id

    def enemy_animation(self, WIN, pl, monster_list, killed_monsters):
        if self.isDead:
            if self.deathCount >= 25:
                self.health = 25
                self.deathCount = 0
                killed_monsters.append(self)
                monster_list.remove(self)
                self.isDead = False
                self.gettingDMG = False
            else:
                if self.hit_side:
                    WIN.blit(self.DEAD_RIGHT[round(self.deathCount // 5)], self.pos)
                else:
                    WIN.blit(self.DEAD_LEFT[round(self.deathCount // 5)], self.pos)
                self.deathCount += 0.5

        elif self.gettingDMG:
            if self.hit_side:
                WIN.blit(self.HIT_RIGHT[round(self.hitCount // 3)], self.pos)
            else:
                WIN.blit(self.HIT_LEFT[round(self.hitCount // 3)], self.pos)

            self.hitCount += 0.2
            if self.hitCount >= 7:
                self.hitCount = 0
                self.gettingDMG = False

        else:
            self.move(WIN, pl)
           # pygame.draw.rect(WIN, (0, 0, 0), self.pos)

    def move(self, WIN, pl):

        self.player_nearby(pl)
        self.player_very_nearby(pl)

        if pl.isDead:
            self.playerNearby = False
            self.playerVeryNearby = False

        if not self.playerNearby:
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

        if self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            if self.vel > 0 and self.pos.x + self.IMP_WIDTH // 10 > pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel < 0 and self.pos.centerx + self.IMP_WIDTH // 15 < pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel > 0 and self.pos.centerx + self.IMP_WIDTH // 15 < pl.pos.x:
                self.pos.x += 1.2 * self.vel
                # self.left = True
                # self.right = False
            if self.vel < 0 and self.pos.x + self.IMP_WIDTH // 10 > pl.pos.x:
                self.pos.x += 1.2 * self.vel
                # self.left = False
                # self.right = True

        ############
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.sprintCount + 1 >= 36:
            self.sprintCount = 0
        if self.idleCount + 1 >= 36:
            self.idleCount = 0

        if not self.playerNearby and not self.playerVeryNearby:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5
            else:
                WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5

        if self.playerVeryNearby and self.bottomColission:
            if self.attackCount + 1 >= 36:
                self.attackCount = 0
                self.ATTACK_COOLDOWN -= 1
                self.isAttacking = False
                self.playerVeryNearby = False


            elif self.isAttacking and self.left and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_RIGHT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1

            elif self.isAttacking and self.right and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_LEFT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1
            else:
                if self.left:
                    WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 6)], self.pos)
                    self.idleCount += 0.3
                elif self.right:
                    WIN.blit(self.STANDING_LEFT[round(self.idleCount // 6)], self.pos)
                    self.idleCount += 0.3

        elif self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.SPRINT_RIGHT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5
            else:
                WIN.blit(self.SPRINT_LEFT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5

        if (not self.bottomColission and self.playerNearby and not self.playerVeryNearby) or (not self.bottomColission and self.playerNearby and self.playerVeryNearby):
            if self.left:
                WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 6)], self.pos)
                self.idleCount += 0.3
            elif self.right:
                WIN.blit(self.STANDING_LEFT[round(self.idleCount // 6)], self.pos)
                self.idleCount += 0.3




    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

    def player_nearby(self, pl):
        if pl.pos.x - self.IMP_WIDTH * 1.2 < self.pos.x < pl.pos.x + (self.IMP_WIDTH // 2) * 1.2 and (self.pos.bottom * 0.95 < pl.pos.bottom < self.pos.bottom * 1.1)  :
            self.playerNearby = True
        else:
            self.playerVeryNearby = False
            self.playerNearby = False

    def player_very_nearby(self, pl):
        if pl.pos.x - self.IMP_WIDTH * 0.5 < self.pos.x + self.IMP_WIDTH // 6 < pl.pos.x + (
                self.IMP_WIDTH // 2) * 0.3 and (
                pl.pos.top < self.pos.y + self.IMP_HEIGHT / 2 < pl.pos.bottom) :
            self.playerVeryNearby = True
        if pl.pos.x - self.IMP_WIDTH * 0.6 < self.pos.x - self.IMP_WIDTH // 4:
            self.right = True  # monster jest na prawo od gracza
            self.left = False
        elif self.pos.x < pl.pos.x + (self.IMP_WIDTH // 2) * 0.3:
            self.right = False
            self.left = True

        if self.ATTACK_COOLDOWN == ATTACK_CD and not self.gettingDMG:
            self.isAttacking = True
        elif self.ATTACK_COOLDOWN < ATTACK_CD:
            self.ATTACK_COOLDOWN -= 1
            if self.ATTACK_COOLDOWN == 0:
                self.ATTACK_COOLDOWN = ATTACK_CD

        else:
            self.playerVeryNearby = False


class Skeleton():
    SKELETON_WIDTH = SCREEN_WIDTH // 5
    SKELETON_HEIGHT = round(SKELETON_WIDTH * 0.8)
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
    SPRINT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "run_1.png")),
                         pygame.image.load(os.path.join("enemy animation\\skeleton", "run_2.png")),
                         pygame.image.load(os.path.join("enemy animation\\skeleton", "run_3.png")),
                         pygame.image.load(os.path.join("enemy animation\\skeleton", "run_4.png")),
                         pygame.image.load(os.path.join("enemy animation\\skeleton", "run_5.png")),
                         pygame.image.load(os.path.join("enemy animation\\skeleton", "run_6.png"))]
    SPRINT_RIGHT = []
    for img in SPRINT_ANIMATIONS:
        SPRINT_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))
    SPRINT_LEFT = []
    for img in SPRINT_RIGHT:
        SPRINT_LEFT.append(pygame.transform.flip(img, True, False))
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
    DEAD_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\skeleton", "dead_far_6.png"))]
    DEAD_RIGHT = []
    for img in DEAD_ANIMATIONS:
        DEAD_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))

    DEAD_LEFT = []
    for img in DEAD_RIGHT:
        DEAD_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\skeleton", "hit_3.png"))]
    HIT_RIGHT = []
    for img in HIT_ANIMATIONS:
        HIT_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))

    HIT_LEFT = []
    for img in HIT_RIGHT:
        HIT_LEFT.append(pygame.transform.flip(img, True, False))

    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\skeleton", "ready_3.png"))]
    STANDING_RIGHT = []
    for img in STANDING_ANIMATIONS:
        STANDING_RIGHT.append(pygame.transform.scale(img, (SKELETON_WIDTH, SKELETON_HEIGHT)))

    STANDING_LEFT = []
    for img in STANDING_RIGHT:
        STANDING_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd, id):
        self.pos = pygame.Rect(posX, posY, self.SKELETON_WIDTH, self.SKELETON_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.sprintCount = 0
        self.attackCount = 0
        self.idleCount = 0
        self.hitCount = 0
        self.deathCount = 0
        self.vel = self.SKELETON_WIDTH // 90
        self.MAX_HEALTH = 20
        self.health = self.MAX_HEALTH
        self.DMG = 10
        self.hit_side = False  # False = left // True = right
        self.isDead = False
        self.isAttacking = False
        self.gettingDMG = False
        self.playerNearby = False
        self.playerVeryNearby = False
        self.left = False
        self.right = False
        self.ATTACK_COOLDOWN = ATTACK_CD
        self.bottomColission = True
        self.id = id

    def enemy_animation(self, WIN, pl, monster_list, killed_monsters):
        if self.isDead:
            if self.deathCount >= 36:
                self.health = 20
                self.deathCount = 0
                killed_monsters.append(self)
                monster_list.remove(self)
                self.isDead = False
                self.gettingDMG = False
            else:
                if self.hit_side:
                    WIN.blit(self.DEAD_RIGHT[round(self.deathCount // 6)], self.pos)
                else:
                    WIN.blit(self.DEAD_LEFT[round(self.deathCount // 6)], self.pos)
                self.deathCount += 0.5

        elif self.gettingDMG:
            if self.hit_side:
                WIN.blit(self.HIT_RIGHT[round(self.hitCount // 3)], self.pos)
            else:
                WIN.blit(self.HIT_LEFT[round(self.hitCount // 3)], self.pos)

            self.hitCount += 0.2
            if self.hitCount >= 7:
                self.hitCount = 0
                self.gettingDMG = False

        else:
            self.move(WIN, pl)
            # pygame.draw.rect(WIN, (0, 0, 0), self.pos)

    def move(self, WIN, pl):

        self.player_nearby(pl)
        self.player_very_nearby(pl)

        if pl.isDead:
            self.playerNearby = False
            self.playerVeryNearby = False

        if not self.playerNearby:
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

        if self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            if self.vel > 0 and self.pos.x + self.SKELETON_WIDTH // 10 > pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel < 0 and self.pos.centerx + self.SKELETON_WIDTH // 15 < pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel > 0 and self.pos.centerx + self.SKELETON_WIDTH // 15 < pl.pos.x:
                self.pos.x += 1.35 * self.vel
                # self.left = True
                # self.right = False
            if self.vel < 0 and self.pos.x + self.SKELETON_WIDTH // 10 > pl.pos.x:
                self.pos.x += 1.35 * self.vel
                # self.left = False
                # self.right = True

        ############
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.sprintCount + 1 >= 36:
            self.sprintCount = 0
        if self.idleCount + 1 >= 9:
            self.idleCount = 0

        if not self.playerNearby and not self.playerVeryNearby:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5
            else:
                WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5

        if self.playerVeryNearby and self.bottomColission:
            if self.attackCount + 1 >= 36:
                self.attackCount = 0
                self.ATTACK_COOLDOWN -= 1
                self.isAttacking = False
                self.playerVeryNearby = False


            elif self.isAttacking and self.left and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_RIGHT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1

            elif self.isAttacking and self.right and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_LEFT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1
            else:
                if self.left:
                    WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 3)], self.pos)
                    self.idleCount += 0.3
                elif self.right:
                    WIN.blit(self.STANDING_LEFT[round(self.idleCount // 3)], self.pos)
                    self.idleCount += 0.3

        elif self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.SPRINT_RIGHT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5
            else:
                WIN.blit(self.SPRINT_LEFT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5

        if (not self.bottomColission and self.playerNearby and not self.playerVeryNearby) or (
                not self.bottomColission and self.playerNearby and self.playerVeryNearby):
            if self.left:
                WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 3)], self.pos)
                self.idleCount += 0.3
            elif self.right:
                WIN.blit(self.STANDING_LEFT[round(self.idleCount // 3)], self.pos)
                self.idleCount += 0.3

    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

    def player_nearby(self, pl):
        if pl.pos.x - self.SKELETON_WIDTH * 1.35 < self.pos.x < pl.pos.x + (self.SKELETON_WIDTH // 2) * 1.35 and (self.pos.bottom * 0.95 < pl.pos.bottom < self.pos.bottom * 1.1):
            print(pl.pos.top)
            print(self.pos.top)
            self.playerNearby = True
        else:
            self.playerVeryNearby = False
            self.playerNearby = False

    def player_very_nearby(self, pl):
        if pl.pos.x - self.SKELETON_WIDTH * 0.5 < self.pos.x + self.SKELETON_WIDTH // 6 < pl.pos.x + (
                self.SKELETON_WIDTH // 2) * 0.3 and (
                pl.pos.top < self.pos.y + self.SKELETON_HEIGHT / 2 < pl.pos.bottom):
            self.playerVeryNearby = True
        if pl.pos.x - self.SKELETON_WIDTH * 0.6 < self.pos.x - self.SKELETON_WIDTH // 4:
            self.right = True  # monster jest na prawo od gracza
            self.left = False
        elif self.pos.x < pl.pos.x + (self.SKELETON_WIDTH // 2) * 0.3:
            self.right = False
            self.left = True

        if self.ATTACK_COOLDOWN == ATTACK_CD and not self.gettingDMG:
            self.isAttacking = True
        elif self.ATTACK_COOLDOWN < ATTACK_CD:
            self.ATTACK_COOLDOWN -= 1
            if self.ATTACK_COOLDOWN == 0:
                self.ATTACK_COOLDOWN = ATTACK_CD

        else:
            self.playerVeryNearby = False


class Knight():
    KNIGHT_WIDTH = SCREEN_WIDTH // 5
    KNIGHT_HEIGHT = round(KNIGHT_WIDTH * 0.9)
    #####
    WALK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "walk_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "walk_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "walk_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "walk_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "walk_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "walk_6.png"))]
    WALK_RIGHT = []
    for img in WALK_ANIMATIONS:
        WALK_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))
    WALK_LEFT = []
    for img in WALK_RIGHT:
        WALK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    SPRINT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "run_1.png")),
                         pygame.image.load(os.path.join("enemy animation\\knight", "run_2.png")),
                         pygame.image.load(os.path.join("enemy animation\\knight", "run_3.png")),
                         pygame.image.load(os.path.join("enemy animation\\knight", "run_4.png")),
                         pygame.image.load(os.path.join("enemy animation\\knight", "run_5.png")),
                         pygame.image.load(os.path.join("enemy animation\\knight", "run_6.png"))]
    SPRINT_RIGHT = []
    for img in SPRINT_ANIMATIONS:
        SPRINT_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))
    SPRINT_LEFT = []
    for img in SPRINT_RIGHT:
        SPRINT_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "jump_1.png")),
                          pygame.image.load(os.path.join("enemy animation\\knight", "jump_2.png")),
                          pygame.image.load(os.path.join("enemy animation\\knight", "jump_3.png")),
                          pygame.image.load(os.path.join("enemy animation\\knight", "jump_4.png")),
                          pygame.image.load(os.path.join("enemy animation\\knight", "jump_5.png"))]
    JUMPING_RIGHT = []
    for img in JUMPING_ANIMATIONS:
        JUMPING_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))
    JUMPING_LEFT = []
    for img in JUMPING_RIGHT:
        JUMPING_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    LIGHT_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "attack1_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack1_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack1_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack1_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack1_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack1_6.png"))]
    LIGHT_ATTACK_RIGHT = []
    for img in LIGHT_ATTACK_ANIMATIONS:
        LIGHT_ATTACK_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))
    LIGHT_ATTACK_LEFT = []
    for img in LIGHT_ATTACK_RIGHT:
        LIGHT_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HEAVY_ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "attack2_1.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack2_2.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack2_3.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack2_4.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack2_5.png")),
                               pygame.image.load(os.path.join("enemy animation\\knight", "attack2_6.png"))]
    HEAVY_ATTACK_RIGHT = []
    for img in HEAVY_ATTACK_ANIMATIONS:
        HEAVY_ATTACK_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))
    HEAVY_ATTACK_LEFT = []
    for img in HEAVY_ATTACK_RIGHT:
        HEAVY_ATTACK_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    DEAD_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "fall_back_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "fall_back_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "fall_back_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "fall_back_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\knight", "fall_back_5.png"))]
    DEAD_RIGHT = []
    for img in DEAD_ANIMATIONS:
        DEAD_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))

    DEAD_LEFT = []
    for img in DEAD_RIGHT:
        DEAD_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\knight", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\knight", "hit_3.png"))]
    HIT_RIGHT = []
    for img in HIT_ANIMATIONS:
        HIT_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))

    HIT_LEFT = []
    for img in HIT_RIGHT:
        HIT_LEFT.append(pygame.transform.flip(img, True, False))

    STANDING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\knight", "ready_1.png")),
                           pygame.image.load(os.path.join("enemy animation\\knight", "ready_2.png")),
                           pygame.image.load(os.path.join("enemy animation\\knight", "ready_3.png"))]
    STANDING_RIGHT = []
    for img in STANDING_ANIMATIONS:
        STANDING_RIGHT.append(pygame.transform.scale(img, (KNIGHT_WIDTH, KNIGHT_HEIGHT)))

    STANDING_LEFT = []
    for img in STANDING_RIGHT:
        STANDING_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd, id):
        self.pos = pygame.Rect(posX, posY, self.KNIGHT_WIDTH, self.KNIGHT_HEIGHT)
        self.posEnd = posEnd
        self.path = [self.pos.x, self.posEnd]
        self.walkCount = 0
        self.sprintCount = 0
        self.attackCount = 0
        self.idleCount = 0
        self.hitCount = 0
        self.deathCount = 0
        self.vel = self.KNIGHT_WIDTH // 100
        self.MAX_HEALTH = 50
        self.health = self.MAX_HEALTH
        self.DMG = 20
        self.hit_side = False  # False = left // True = right
        self.isDead = False
        self.isAttacking = False
        self.gettingDMG = False
        self.playerNearby = False
        self.playerVeryNearby = False
        self.left = False
        self.right = False
        self.ATTACK_COOLDOWN = ATTACK_CD
        self.bottomColission = True
        self.id = id

    def enemy_animation(self, WIN, pl, monster_list, killed_monsters):
        if self.isDead:
            if self.deathCount >= 25:
                self.health = 50
                self.deathCount = 0
                killed_monsters.append(self)
                monster_list.remove(self)
                self.isDead = False
                self.gettingDMG = False
            else:
                if self.hit_side:
                    WIN.blit(self.DEAD_RIGHT[round(self.deathCount // 5)], self.pos)
                else:
                    WIN.blit(self.DEAD_LEFT[round(self.deathCount // 5)], self.pos)
                self.deathCount += 0.5

        elif self.gettingDMG:
            if self.hit_side:
                WIN.blit(self.HIT_RIGHT[round(self.hitCount // 3)], self.pos)
            else:
                WIN.blit(self.HIT_LEFT[round(self.hitCount // 3)], self.pos)

            self.hitCount += 0.2
            if self.hitCount >= 7:
                self.hitCount = 0
                self.gettingDMG = False

        else:
            self.move(WIN, pl)
            # pygame.draw.rect(WIN, (0, 0, 0), self.pos)

    def move(self, WIN, pl):

        self.player_nearby(pl)
        self.player_very_nearby(pl)

        if pl.isDead:
            self.playerNearby = False
            self.playerVeryNearby = False

        if not self.playerNearby:
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

        if self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            if self.vel > 0 and self.pos.x + self.KNIGHT_WIDTH // 10 > pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel < 0 and self.pos.centerx + self.KNIGHT_WIDTH // 15 < pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel > 0 and self.pos.centerx + self.KNIGHT_WIDTH // 15 < pl.pos.x:
                self.pos.x += 1.45 * self.vel
                # self.left = True
                # self.right = False
            if self.vel < 0 and self.pos.x + self.KNIGHT_WIDTH // 10 > pl.pos.x:
                self.pos.x += 1.45 * self.vel
                # self.left = False
                # self.right = True

        ############
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.sprintCount + 1 >= 36:
            self.sprintCount = 0
        if self.idleCount + 1 >= 9:
            self.idleCount = 0

        if not self.playerNearby and not self.playerVeryNearby:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.WALK_RIGHT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5
            else:
                WIN.blit(self.WALK_LEFT[round(self.walkCount // 6)], self.pos)
                self.walkCount += 0.5

        if self.playerVeryNearby and self.bottomColission:
            if self.attackCount + 1 >= 36:
                self.attackCount = 0
                self.ATTACK_COOLDOWN -= 1
                self.isAttacking = False
                self.playerVeryNearby = False


            elif self.isAttacking and self.left and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_RIGHT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1

            elif self.isAttacking and self.right and not pl.isDead:
                WIN.blit(self.LIGHT_ATTACK_LEFT[round(self.attackCount // 6)], self.pos)
                self.attackCount += 1
            else:
                if self.left:
                    WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 3)], self.pos)
                    self.idleCount += 0.3
                elif self.right:
                    WIN.blit(self.STANDING_LEFT[round(self.idleCount // 3)], self.pos)
                    self.idleCount += 0.3

        elif self.playerNearby and not self.playerVeryNearby and self.bottomColission:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.SPRINT_RIGHT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.6
            else:
                WIN.blit(self.SPRINT_LEFT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.6

        if (not self.bottomColission and self.playerNearby and not self.playerVeryNearby) or (
                not self.bottomColission and self.playerNearby and self.playerVeryNearby):
            if self.left:
                WIN.blit(self.STANDING_RIGHT[round(self.idleCount // 3)], self.pos)
                self.idleCount += 0.3
            elif self.right:
                WIN.blit(self.STANDING_LEFT[round(self.idleCount // 3)], self.pos)
                self.idleCount += 0.3

    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

    def player_nearby(self, pl):
        if pl.pos.x - self.KNIGHT_WIDTH * 1.4 < self.pos.x < pl.pos.x + (self.KNIGHT_WIDTH // 2) * 1.4 and (self.pos.bottom * 0.7 < pl.pos.bottom < self.pos.bottom * 1.1):
            self.playerNearby = True
        else:
            self.playerVeryNearby = False
            self.playerNearby = False

    def player_very_nearby(self, pl):
        if pl.pos.x - self.KNIGHT_WIDTH * 0.5 < self.pos.x + self.KNIGHT_WIDTH // 6 < pl.pos.x + (
                self.KNIGHT_WIDTH // 2) * 0.3 and (
                pl.pos.top < self.pos.y + self.KNIGHT_HEIGHT / 2 < pl.pos.bottom):
            self.playerVeryNearby = True
        if pl.pos.x - self.KNIGHT_WIDTH * 0.6 < self.pos.x - self.KNIGHT_WIDTH // 4:
            self.right = True  # monster jest na prawo od gracza
            self.left = False
        elif self.pos.x < pl.pos.x + (self.KNIGHT_WIDTH // 2) * 0.3:
            self.right = False
            self.left = True

        if self.ATTACK_COOLDOWN == ATTACK_CD and not self.gettingDMG:
            self.isAttacking = True
        elif self.ATTACK_COOLDOWN < ATTACK_CD:
            self.ATTACK_COOLDOWN -= 1
            if self.ATTACK_COOLDOWN == 0:
                self.ATTACK_COOLDOWN = ATTACK_CD

        else:
            self.playerVeryNearby = False