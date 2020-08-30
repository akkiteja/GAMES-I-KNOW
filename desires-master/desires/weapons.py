import pygame

class Bullet(pygame.Rect):
    def __init__(self, (x, y), w, h, target, target_obj, damage):
        super(Bullet, self).__init__(x, y, w, h)
        self.move = list((x, y))
        self.target = target
        self.x_reach = False
        self.y_reach = False

        self.damage = damage

        self.speed = 15
        self.die = False
        self.target_obj = target_obj


    def update(self):

        if self.target[0] > self.centerx:
            self.move[0] += self.speed
            if self.move[0] > self.target[0]:
                self.move[0] = self.target[0]

        elif self.target[0] < self.centerx:
            self.move[0] -= self.speed
            if self.move[0] < self.target[0]:
                self.move[0] = self.target[0] 

        if self.target[1] > self.centery:
            self.move[1] += self.speed
            if self.move[1] > self.target[1]:
                self.move[1] = self.target[1] 
        elif self.target[1] < self.centery:
            self.move[1] -= self.speed
            if self.move[1] < self.target[1]:
                self.move[1] = self.target[1]

        self.center = self.move

        if self.colliderect(self.target_obj.d_rect):
            self.target_obj.health -= self.damage

        if self.center == self.target:
            self.die = True





    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), self)


class Weapon(pygame.sprite.Sprite):
    def __init__(self, ctrl):
        super(Weapon, self).__init__()
        self.ctrl = ctrl
        self.relative_y = None
        self.bullets = []
        self.fire_rate = 0
        self.ticks = 0
        self.ammo = 100

    def generate_bullet(self, origin, target, target_obj):
        if self.ticks > self.fire_rate and self.ammo:
            b = Bullet(origin, 2,2, target, target_obj, self.damage)
            self.bullets.append(b)
            self.ammo -= 1

    def update(self, p_rect, orientation):
        self.ticks += 1
        self.rect.top = p_rect.top + self.relative_y
        self.rect.left = p_rect.left

        if orientation == 'ltr':
            self.image = self.normal
        else:
            self.image = pygame.transform.flip(self.normal, 1, 0)
            self.rect.left -= 8 # magic numbers

        for bullet in self.bullets:
            bullet.update()
            if bullet.die:
                self.bullets.remove(bullet)

    def render(self, screen, camera):
        screen.blit(self.image, (self.rect.left - camera.left,
                                 self.rect.top - camera.top))

        if self.bullets:
            for bullet in self.bullets:
                bullet.render(screen)


class Ak47(Weapon):
    def __init__(self, ctrl, x, y):
        super(Ak47, self).__init__(ctrl)
        self.normal = self.ctrl.frames['weapons/ak47']
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.relative_y = 21
        self.rect.left = x
        self.rect.top = self.relative_y + y
        self.fire_rate = 3
        self.damage = 5
        self.ammo = 300


class Hkg36(Weapon):
    def __init__(self, ctrl, x, y):
        super(Hkg36, self).__init__(ctrl)
        self.normal = self.ctrl.frames['weapons/hkg36']
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.relative_y = 21
        self.rect.left = x
        self.rect.top = self.relative_y + y
        self.fire_rate = 1
        self.damage = 2
        self.ammo = 300


class Shotgun(Weapon):
    def __init__(self, ctrl, x, y):
        super(Shotgun, self).__init__(ctrl)
        self.normal = self.ctrl.frames['weapons/shotgun']
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.relative_y = 21
        self.rect.left = x
        self.rect.top = self.relative_y + y
        self.fire_rate = 10
        self.damage = 70
        self.ammo = 25

class Flamethrower(Weapon):
    def __init__(self, ctrl, x, y):
        super(Flamethrower, self).__init__(ctrl)
        self.normal = self.ctrl.frames['weapons/flamethrower']
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.relative_y = 13
        self.rect.left = x
        self.rect.top = self.relative_y + y
        self.fire_rate = 0
        self.damage = 50
        self.ammo = 0


class Chainsaw(Weapon):
    def __init__(self, ctrl, x, y):
        super(Chainsaw, self).__init__(ctrl)
        self.normal = self.ctrl.frames['weapons/chainsaw-0']
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.relative_y = 21
        self.rect.left = x
        self.rect.top = self.relative_y + y

        self.curr_frame = 0
        self.fire_rate = 0

        self.damage = 80
        self.ammo = 0


