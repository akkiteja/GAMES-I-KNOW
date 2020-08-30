import random
from math import sqrt

import pygame
import util as u
from pickups import *

PICKS = [
    'ammo',
    'painkiller',
    'power',
    'none',
    'none',
    'none',
    'none',
    'none',
    'none',
]

class EnemyCtrl(object):
    def __init__(self, ctrl, game):
        self.ctrl = ctrl

        self.curr_enemies = 0
        self.max_enemies = 15
        self.player_kills = 0
        self.game = game

        self.done = False
        self.ticks = 0

    def distance(self, a, b):
        return sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2)

    def get_closer(self, player, enemies):
        dist = 9999999
        i = -1
        for e in enemies:
            d = self.distance(player.rect.center, e.rect.center)
            if d < dist:
                i = enemies.index(e)
                dist = d
        
        return i

    def update(self):
        if self.curr_enemies <= self.max_enemies:
            z = Zombie(self.ctrl, self.game)
            z.item = random.choice(PICKS)
            self.game.entities.append(z)
            self.curr_enemies += 1
            print 'new zombie created'


        target = self.game.player.rect.center
        if self.ticks > 50:
            for e in self.game.entities:
                e.target = target
            self.ticks = 0

        self.ticks +=  1




class Enemy(pygame.sprite.Sprite):
    def __init__(self, ctrl):
        super(Enemy, self).__init__()
        self.ctrl = ctrl
        self.moving = False
        self.move = [0,0]

        self.orientation = 'ltr'
        self.animate_timer = 0.0
        self.animate_fps = 5.0

        self.health = 100
        self.die = False

        

    def get_frame(self, frames):
        if self.curr_frame  < len(frames) - 1:
            self.curr_frame += 1
        else:
            self.curr_frame = 0

        return self.curr_frame

    def update(self):
            
        now = pygame.time.get_ticks()
        if now-self.animate_timer > 1000/self.animate_fps:
            if self.moving:
                if self.target[0] > self.rect.centerx:
                    self.move[0] += self.speed
                    self.orientation = 'ltr'
                    if self.move[0] > self.target[0]:
                        self.move[0] = self.target[0]

                elif self.target[0] < self.rect.centerx:
                    self.move[0] -= self.speed
                    self.orientation = 'rtl'
                    if self.move[0] < self.target[0]:
                        self.move[0] = self.target[0] 

                if self.target[1] > self.rect.centery:
                    self.move[1] += self.speed
                    if self.move[1] > self.target[1]:
                        self.move[1] = self.target[1] 
                elif self.target[1] < self.rect.centery:
                    self.move[1] -= self.speed
                    if self.move[1] < self.target[1]:
                        self.move[1] = self.target[1]

                self.rect.center = self.move


                frame = self.get_frame(self.walk_frames)
                if self.orientation == 'ltr':
                    self.image = self.walk_frames[frame]
                else:
                    self.image = pygame.transform.flip(self.walk_frames[frame],1,0)
            else:
                frame = self.normal
                if self.orientation == 'ltr':
                    self.image = frame
                else:
                    self.image = pygame.transform.flip(frame,1,0)

                
                self.target = self.game.player.rect.center
                self.moving = True

            self.animate_timer = now                


        self.d_rect.center = self.rect.center
        self.d_rect.left -= self.game.camera.left
        self.d_rect.top -= self.game.camera.top

        if self.rect.colliderect(self.game.player.rect):
            self.game.player.health -= 2

        if self.rect.center == self.target:
                self.moving = False

        if self.health <= 0:
            self.die = True

        if self.die:
            self.generete_pickup()


    def render(self, screen, camera):
        screen.blit(self.image, (self.rect.left - camera.left,
                                 self.rect.top - camera.top))


    def generete_pickup(self):
        if self.item == 'ammo':
            a = Ammo(self.rect.center)
            self.game.objects.append(a)
        elif self.item == 'painkiller':
            p = PainKiller(self.rect.center)
            self.game.objects.append(p)
        elif self.item == 'power':
            p = Power(self.rect.center)
            self.game.objects.append(p)




    


class Zombie(Enemy):
    def __init__(self, ctrl, game):
        super(Zombie, self).__init__(ctrl)

        self.normal = self.ctrl.frames['zombie/normal']
        self.image = self.normal

        self.walk_frames = [
            self.ctrl.frames['zombie/walk-0'],
            self.ctrl.frames['zombie/walk-1']
        ]

        self.curr_frame = 0

        self.game = game

        self.rect = self.image.get_rect()
        self.d_rect = self.image.get_rect()
        


        x, y = u.get_pixel_coords(random.randint(0, 100), random.randint(0, 100))
        self.rect.center = (x, y)
        self.move = list(self.rect.center)
        self.target = self.game.player.rect.center


        self.d_rect.center = self.rect.center
        self.d_rect.left -= self.game.camera.left
        self.d_rect.top -= self.game.camera.top

        self.moving = True

        self.speed = 5

        self.item = 'none'


    