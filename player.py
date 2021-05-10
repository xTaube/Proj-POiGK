import pygame
import os
from conf import SCREEN_WIDTH, SCREEN_HEIGHT

#-------------------------------------------------------------
#animacje protagonisty
PLAYER_WIDTH = SCREEN_WIDTH//15
PLAYER_HEIGHT = round(PLAYER_WIDTH*1.35)

WALK_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-run-0.png")),
                   pygame.image.load(os.path.join("player animation", "pl-run-1.png")),
                   pygame.image.load(os.path.join("player animation", "pl-run-2.png")),
                   pygame.image.load(os.path.join("player animation", "pl-run-3.png")),
                   pygame.image.load(os.path.join("player animation", "pl-run-4.png")),
                   pygame.image.load(os.path.join("player animation", "pl-run-5.png"))]
WALK_RIGHT = []
for img in WALK_ANIMATIONS:
    WALK_RIGHT.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

WALK_LEFT = []
for img in WALK_RIGHT:
    WALK_LEFT.append(pygame.transform.flip(img, True, False))

STANDING_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-idle-0.png")),
                       pygame.image.load(os.path.join("player animation", "pl-idle-1.png")),
                       pygame.image.load(os.path.join("player animation", "pl-idle-2.png"))]
STANDING = []
for img in STANDING_ANIMATIONS:
    STANDING.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-jump-3.png")),
                      pygame.image.load(os.path.join("player animation", "pl-jump-2.png")),
                      pygame.image.load(os.path.join("player animation", "pl-jump-1.png")),
                      pygame.image.load(os.path.join("player animation", "pl-jump-0.png"))]
JUMPING_RIGHT = []
for img in JUMPING_ANIMATIONS:
    JUMPING_RIGHT.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

JUMPING_LEFT = []
for img in JUMPING_RIGHT:
    JUMPING_LEFT.append(pygame.transform.flip(img, True, False))

ATTACK_ANIMATIONS = [pygame.image.load(os.path.join("player animation", "pl-attack1-0.png")),
                     pygame.image.load(os.path.join("player animation", "pl-attack1-1.png")),
                     pygame.image.load(os.path.join("player animation", "pl-attack1-2.png")),
                     pygame.image.load(os.path.join("player animation", "pl-attack1-3.png")),
                     pygame.image.load(os.path.join("player animation", "pl-attack1-4.png"))]
ATTACK_RIGHT = []
for img in ATTACK_ANIMATIONS:
    ATTACK_RIGHT.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

ATTACK_LEFT = []
for img in ATTACK_RIGHT:
    ATTACK_LEFT.append(pygame.transform.flip(img, True, False))

HIT = [pygame.image.load(os.path.join("player animation", "pl-getDmg-0.png")),
       pygame.image.load(os.path.join("player animation", "pl-getDmg-1.png")),
       pygame.image.load(os.path.join("player animation", "pl-getDmg-2.png"))]

HIT_RIGHT = []
for img in HIT:
    HIT_RIGHT.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

HIT_LEFT = []
for img in HIT_RIGHT:
    HIT_LEFT.append(pygame.transform.flip(img, True, False))

DEAD = [pygame.image.load(os.path.join("player animation", "pl-die-00.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-01.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-02.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-03.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-04.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-05.png")),
        pygame.image.load(os.path.join("player animation", "pl-die-06.png")),]

DEAD_RIGHT = []
for img in DEAD:
    DEAD_RIGHT.append(pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT)))

DEAD_LEFT = []
for img in DEAD_RIGHT:
    DEAD_LEFT.append(pygame.transform.flip(img, True, False))
#--------------------------------------------------------------------

PL_VEL = PLAYER_WIDTH//18
ATTACK_CD = 30


class Health_bar():
    def __init__(self, max_health, health_bar_length):
        self.max_health = max_health
        self.current_health = self.max_health
        self.targeted_health = max_health
        self.health_bar_length = health_bar_length
        self.health_ratio = self.max_health / self.health_bar_length
        self.health_change_speed = 0.5

    def draw_health_bar(self, WIN):
        transition_width = 0
        transition_color = (255, 0, 0)
        t = 0

        if self.current_health < self.targeted_health:
            self.current_health += self.health_change_speed
            transition_width = int((self.targeted_health - self.current_health)/self.health_ratio)
            transition_color = (0, 255, 0)
        if self.current_health > self.targeted_health:
            self.current_health -= self.health_change_speed
            transition_width = int((self.current_health - self.targeted_health)/self.health_ratio)
            t = transition_width
            transition_color = (255, 255, 0)

        health_bar_rect = pygame.Rect(10, 10, self.current_health/self.health_ratio, 25)
        transition_bar_rect = pygame.Rect(health_bar_rect.right - t, 10, transition_width, 25)

        pygame.draw.rect(WIN, (70, 61, 61), (10, 10, self.health_bar_length, 25))
        pygame.draw.rect(WIN, (255, 85, 85), health_bar_rect)
        pygame.draw.rect(WIN, transition_color, transition_bar_rect)
        pygame.draw.rect(WIN, (129, 129, 129), (10, 10, self.health_bar_length, 25), 4)

    def expand_max_health(self, amount):
        self.health_bar_length += amount * self.health_bar_length / self.max_health
        self.max_health += amount
        self.health_ratio = self.max_health / self.health_bar_length


class Player():
    def __init__(self, pos):
        self.starting_pos = [pos[0], pos[1]]
        self.pos = pygame.Rect(pos[0], pos[1], PLAYER_WIDTH, PLAYER_HEIGHT)
        self.walkCount = 0
        self.jumpCount = 15
        self.idleCount = 0
        self.attackCount = 0
        self.hitCount = 0
        self.deathCount = 0
        self.ATTACK_COOLDOWN = ATTACK_CD
        self.health_bar = Health_bar(100, 400)
        self.gravitySpeed = 5
        self.DMG = 5

        #states
        self.right = False
        self.left = False
        self.isJumping = False
        self.falling = False
        self.isAttacking = False
        self.gettingDmg = False
        self.hitSide = False            #false - left // true - right
        self.isDead = False
        self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}

    def colliding_check(self, tiles, monster_list, item_list):
        hit_list = []
        collision_types = {"top": False, "bottom": False, "right": False, "left": False}
        for tile in tiles:
            if self.pos.colliderect(tile):
                hit_list.append(tile)

        for tile in hit_list:
            if abs(tile.left - self.pos.right + PLAYER_WIDTH//3) < PLAYER_WIDTH//10 and abs(tile.top - self.pos.bottom) > PLAYER_WIDTH//3:
                collision_types["right"] = True

            elif abs(tile.right - self.pos.left - PLAYER_WIDTH//3) < PLAYER_WIDTH//10 and abs(tile.top - self.pos.bottom) > PLAYER_WIDTH//3:
                collision_types["left"] = True

            if (abs(tile.bottom - self.pos.top) > PLAYER_WIDTH//4 and abs(tile.bottom - self.pos.top) < PLAYER_WIDTH//2) and (tile.left - PLAYER_WIDTH//2 < self.pos.x and tile.right - PLAYER_WIDTH//3 > self.pos.x):
                collision_types["top"] = True

            elif abs(tile.top - self.pos.bottom + PLAYER_WIDTH//3) < PLAYER_WIDTH//2 and abs(tile.right - self.pos.left - PLAYER_WIDTH/5) > PLAYER_WIDTH/5 and abs(tile.left - self.pos.right + PLAYER_WIDTH/5) > PLAYER_WIDTH/4.5:
                self.pos.bottom = tile.top + PLAYER_HEIGHT//6
                collision_types["bottom"] = True

        self.collision_types = collision_types

        hit_list.clear()
        for monster in monster_list:
            if self.pos.colliderect(monster.pos):
                hit_list.append(monster)

        for monster in hit_list:
            if self.isAttacking:
                if self.left and abs(self.pos.left - monster.pos.right) > SCREEN_WIDTH/15 and abs(self.pos.left - monster.pos.right) < SCREEN_WIDTH/7.57:
                    monster.get_hit(self.DMG)
                    if monster.health <= 0:
                        monster.isDead = True
                    else:
                        monster.hit_side = True
                elif not self.left and abs(self.pos.right - monster.pos.left) > SCREEN_WIDTH/15 and abs(self.pos.right - monster.pos.left) < SCREEN_WIDTH/7.57:
                    monster.get_hit(self.DMG)
                    if monster.health <= 0:
                        monster.isDead = True
                    else:
                        monster.hit_side = False
            elif monster.isAttacking:
                if not gettingDmg:
                    self.get_hit(monster.DMG)

        hit_list.clear()
        for item in item_list:
            if self.pos.colliderect(item.pos):
                if item.pos.left - PLAYER_WIDTH//2 < self.pos.x and item.pos.right - PLAYER_WIDTH//3 > self.pos.x:
                    if item.isPossibleToTake(self):
                        item.effect(self)
                        item_list.remove(item)

    def move(self, key_pressed):

        if key_pressed[pygame.K_RIGHT]:
            if not self.isAttacking and not self.collision_types["right"] and not self.gettingDmg and not self.isDead:
                self.pos.x += PL_VEL
                self.right = True
                self.left = False
        elif key_pressed[pygame.K_LEFT]:
            if not self.isAttacking and not self.collision_types["left"] and not self.gettingDmg and not self.isDead:
                self.pos.x -= PL_VEL
                self.right = False
                self.left = True
        else:
            self.right = False
            self.left = False

        if not(self.isJumping):
            if key_pressed[pygame.K_SPACE] and self.collision_types["bottom"] and not self.gettingDmg and not self.isDead:
                self.isJumping = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if not self.collision_types["top"]:
                if self.jumpCount >= 0:
                    self.pos.y -= (self.jumpCount ** 2) * PLAYER_HEIGHT/900
                    self.jumpCount -= 1
                else:
                    self.isJumping = False
                    self.jumpCount = 15
            else:
                self.isJumping = False
                self.jumpCount = 15

        if key_pressed[pygame.K_z] and self.ATTACK_COOLDOWN == ATTACK_CD and not self.gettingDmg and not self.isDead:
            self.isAttacking = True
        elif self.ATTACK_COOLDOWN < ATTACK_CD:
            self.ATTACK_COOLDOWN -= 1
            if self.ATTACK_COOLDOWN == 0:
                self.ATTACK_COOLDOWN = ATTACK_CD

        if self.collision_types["bottom"] or self.isJumping:
            self.falling = False
            self.gravitySpeed = PLAYER_HEIGHT/30
        else:
            self.falling = True
            self.pos.y += self.gravitySpeed
            self.gravitySpeed += PLAYER_HEIGHT/200

    def get_hit(self, dmg):
        if self.health_bar.targeted_health - dmg > 0:
            self.health_bar.targeted_health -= dmg
        else:
            self.health_bar.targeted_health = 0
            self.isDead = True
        if not self.isDead:
            self.gettingDmg = True

    def heal(self, health_amount):
        if self.health_bar.targeted_health != self.health_bar.max_health:
            self.health_bar.targeted_health += health_amount
            if self.health_bar.targeted_health > self.health_bar.max_health:
                self.health_bar.targeted_health = self.health_bar.max_health

    def dmg_up(self, dmg_value):
        self.DMG += dmg_value

    def player_animation(self, WIN, monster_list, killed_monster):
        if self.isDead:
            if self.deathCount >= 49:
                self.deathCount = 0
                self.pos.x, self.pos.y = self.starting_pos[0], self.starting_pos[1]
                self.health_bar.targeted_health = self.health_bar.max_health
                self.health_bar.current_health = self.health_bar.max_health
                monster_list += killed_monster
                killed_monster.clear()
                self.isDead = False
            else:
                if self.hitSide:
                    WIN.blit(DEAD_RIGHT[round(self.deathCount // 7)], self.pos)
                else:
                    WIN.blit(DEAD_LEFT[round(self.deathCount // 7)], self.pos)
                self.deathCount += 0.6

        elif self.gettingDmg:
            if self.hitCount >= 9:
                self.hitCount = 0
                self.gettingDmg = False

            if self.hitSide:
                WIN.blit(HIT_RIGHT[round(self.hitCount // 3)], self.pos)
            else:
                WIN.blit(HIT_LEFT[round(self.hitCount // 3)], self.pos)

            self.hitCount += 0.5
        else:
            if self.walkCount + 1 >= 36:
                self.walkCount = 0

            if self.idleCount + 1 >= 9:
                self.idleCount = 0

            if self.attackCount + 1 >= 25:
                self.attackCount = 0
                self.ATTACK_COOLDOWN -= 1
                self.isAttacking = False

            if self.isAttacking and self.left:
                WIN.blit(ATTACK_LEFT[self.attackCount // 5], self.pos)
                self.attackCount += 1

            elif self.isAttacking:
                WIN.blit(ATTACK_RIGHT[self.attackCount // 5], self.pos)
                self.attackCount += 1

            elif self.isAttacking and self.left:
                WIN.blit(ATTACK_LEFT[self.attackCount // 5], self.pos)
                self.attackCount += 1

            elif self.left and not self.isJumping and not self.falling:
                WIN.blit(WALK_LEFT[self.walkCount // 6], self.pos)
                self.walkCount += 1

            elif self.right and not self.isJumping and not self.falling:
                WIN.blit(WALK_RIGHT[self.walkCount // 6], self.pos)
                self.walkCount += 1

            elif self.isJumping and self.left:
                WIN.blit(JUMPING_LEFT[round(self.jumpCount // 4)], self.pos)

            elif self.isJumping:
                WIN.blit(JUMPING_RIGHT[round(self.jumpCount // 4)], self.pos)

            elif self.falling and self.left:
                WIN.blit(JUMPING_LEFT[1], self.pos)

            elif self.falling:
                WIN.blit(JUMPING_RIGHT[1], self.pos)
            else:
                WIN.blit(STANDING[round(self.idleCount // 3)], self.pos)
                self.idleCount += 0.2

        self.health_bar.draw_health_bar(WIN)
        # pygame.draw.rect(WIN, (0, 0, 0), self.pos)