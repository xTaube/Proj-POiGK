class Demon():
    IMP_WIDTH = SCREEN_WIDTH // 5
    IMP_HEIGHT = round(IMP_WIDTH * 0.8)
    #####
    WALK_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "walk_1.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_2.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_3.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_4.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_5.png")),
                       pygame.image.load(os.path.join("enemy animation\\demon", "walk_6.png"))]
    WALK_RIGHT = []
    for img in WALK_ANIMATIONS:
        WALK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
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
        SPRINT_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
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
        STANDING.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
    #####
    JUMPING_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "jump_1.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_2.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_3.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_4.png")),
                          pygame.image.load(os.path.join("enemy animation\\demon", "jump_5.png"))]
    JUMPING_RIGHT = []
    for img in JUMPING_ANIMATIONS:
        JUMPING_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
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
        LIGHT_ATTACK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
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
        HEAVY_ATTACK_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))
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
        DEAD_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

    DEAD_LEFT = []
    for img in DEAD_RIGHT:
        DEAD_LEFT.append(pygame.transform.flip(img, True, False))
    #####
    HIT_ANIMATIONS = [pygame.image.load(os.path.join("enemy animation\\demon", "hit_1.png")),
                      pygame.image.load(os.path.join("enemy animation\\demon", "hit_2.png")),
                      pygame.image.load(os.path.join("enemy animation\\demon", "hit_3.png"))]
    HIT_RIGHT = []
    for img in HIT_ANIMATIONS:
        HIT_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

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
        STANDING_RIGHT.append(pygame.transform.scale(img, (IMP_WIDTH, IMP_HEIGHT)))

    STANDING_LEFT = []
    for img in STANDING_RIGHT:
        STANDING_LEFT.append(pygame.transform.flip(img, True, False))

    #####
    def __init__(self, posX, posY, posEnd):
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
        self.health = 25
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

    def enemy_animation(self, WIN, pl, monster_list, killed_monsters):
        if self.isDead:
            if self.deathCount >= 16:
                self.health = 25
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

        if self.playerNearby and not self.playerVeryNearby:
            if self.vel > 0 and self.pos.x + self.IMP_WIDTH // 10 > pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel < 0 and self.pos.centerx + self.IMP_WIDTH // 15 < pl.pos.x:
                self.vel = self.vel * -1
                # self.sprintCount = 0
                # self.pos.x += self.vel
            if self.vel > 0 and self.pos.centerx + self.IMP_WIDTH // 15 < pl.pos.x:
                self.pos.x += 1.25 * self.vel
                # self.left = True
                # self.right = False
            if self.vel < 0 and self.pos.x + self.IMP_WIDTH // 10 > pl.pos.x:
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

        if self.playerVeryNearby:
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

        elif self.playerNearby and not self.playerVeryNearby:
            self.isAttacking = False
            if self.vel > 0:
                WIN.blit(self.SPRINT_RIGHT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5
            else:
                WIN.blit(self.SPRINT_LEFT[round(self.sprintCount // 6)], self.pos)
                self.sprintCount += 0.5







    def get_hit(self, dmg):
        if not self.gettingDMG:
            self.health -= dmg
            self.gettingDMG = True
        print(self.health)

    def player_nearby(self, pl):
        if pl.pos.x - self.IMP_WIDTH * 1.3 < self.pos.x < pl.pos.x + (self.IMP_WIDTH // 2) * 1.3 and (
                pl.pos.top*0.63 < pl.pos.top - (pl.pos.bottom - pl.pos.top)):
            self.playerNearby = True
        else:
            self.playerVeryNearby = False
            self.playerNearby = False

    def player_very_nearby(self, pl):
        if pl.pos.x - self.IMP_WIDTH * 0.65 < self.pos.x + self.IMP_WIDTH // 12 < pl.pos.x + (self.IMP_WIDTH // 2) * 0.3 and (
                pl.pos.top < self.pos.y + self.IMP_HEIGHT / 2 < pl.pos.bottom):
            self.playerVeryNearby = True
        if pl.pos.x - self.IMP_WIDTH * 0.6 < self.pos.x - self.IMP_WIDTH // 4:
            self.right = True   # monster jest na prawo od gracza
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