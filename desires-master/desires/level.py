import time
import pygame
from pytmx import tmxloader
import util as u

class Level:
    def __init__(self, filename):
        self.tiledmap = tmxloader.load_pygame(filename, pixelalpha=True)

        self.tw = self.tiledmap.tilewidth
        self.th = self.tiledmap.tileheight
        self.width = self.tiledmap.width
        self.height = self.tiledmap.height
        self.get_tile_image = self.tiledmap.getTileImage
        l = self.tiledmap.getTileLayerByName('collition')
        self.collition_layer = self.tiledmap.tilelayers.index(l)

        self.layers = []
        for layer_name in ('below', 'above'):
            l = self.tiledmap.getTileLayerByName(layer_name)
            layer = self.tiledmap.tilelayers.index(l)
            self.layers.append(layer)

        


        self.left_edge = 0
        self.top_edge = 64 # height of player
        self.right_edge = self.tiledmap.width * self.tw
        self.bottom_edge = self.tiledmap.height * self.th

        self.objects =  self.tiledmap.getObjects()

        self.tile_rect = pygame.Rect(0,0, self.tw, self.th)


        """
        tiledmap.width and tiledmap.height are int numbers like 70, 80, etc.
        so in the render function i need to know which tiles collides with camera rect,
        i can looking for all the tiles "for x in range(self.width):", 
        but that have a low perfomance. For that reason i calculate a view rect
        which tell me where are the tiles, that i need.
        level.view_x1 = camera.left / level.tw
        level.view_x2 = camera.right / level.tw
        level.view_y1 = camera.top / level.tw
        level.view_y2 = camera.bottom / level.tw
        """
        self.view_x1 = 0
        self.view_x2 = 20
        self.view_y1 = 0
        self.view_y2 = 15

    def generate_objects(self, ctrl):
        objects = []
        for obj in self.objects:
            if obj.name == 'tv':
                t = Tv(obj.x, obj.y, obj.width, obj.height)
                objects.append(t)
            if obj.name == 'desk':
                d = Desk(obj.x, obj.y, obj.width, obj.height)
                objects.append(d)

            if obj.name == 'bed':
                b = Bed(obj.x, obj.y, obj.width, obj.height)
                objects.append(b)

            if obj.name == 'fire':
                f = Fire(obj.x, obj.y, obj.width, obj.height, ctrl)
                objects.append(f)

            if obj.name == 'portal':
                f = Portal(obj.x, obj.y, obj.width, obj.height, ctrl)
                objects.append(f)

        return objects

    def render(self, screen, camera):
        r = self.tile_rect
        for layer in self.layers:
            for y in xrange(self.view_y1, self.view_y2):
                for x in xrange(self.view_x1, self.view_x2):
                    r.x = x*self.tw
                    r.y =  y*self.th
                    if camera.colliderect(r):
                        t = self.get_tile_image(x, y, layer)
                        if t != 0:
                            screen.blit(t, 
                                        ((x*self.tw)- camera.left,
                                         (y*self.th)- camera.top))



class Msg(pygame.Rect):
    def __init__(self, x, y, w,h):
        super(Msg, self).__init__( x, y, w, h)
        self.activated = False

    def pickup(self, player):
        self.activated = True

    def render(self, screen, camera):
        if self.activated:
            self.lines = self.text.split('\n')
            line_height = 13
            y = 150
            for l in self.lines:
                text = u.jfont.render(l, 0, (250, 250, 250), (0,0,0))
                textpos = text.get_rect(centerx=screen.get_width()/2, centery=y+line_height)
                y=y+line_height
                screen.blit(text, textpos)
            self.activated = False


class Tv(Msg):    
    def __init__(self, x, y, w,h):
        super(Msg, self).__init__( x, y, w, h)

        self.text = """idk if being angry with you,
or thank you for saving my life Life
"""

class Bed(Msg):    
    def __init__(self, x, y, w,h):
        super(Bed, self).__init__( x, y, w, h)

        self.text = """WTf, my bed?...
this is a weird dream
"""

class Desk(Msg):    
    def __init__(self, x, y, w,h):
        super(Desk, self).__init__( x, y, w, h)

        self.text = """I think this is goodbye,
thank you for the beautiful moments together.
"""

class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, ctrl):
        super(Fire, self).__init__()

        self.frames = [
            ctrl.frames['fire/frame-0'],
            ctrl.frames['fire/frame-1'],
            ctrl.frames['fire/frame-2'],
            ctrl.frames['fire/frame-3'],
        ]
        self.curr_frame = 0

        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = x, y

    def get_frame(self, frames):
        if self.curr_frame  < len(frames) - 1:
            self.curr_frame += 1
        else:
            self.curr_frame = 0

        return self.curr_frame

    def pickup(self, player):
        player.health -= 0.02

    def render(self, screen, camera):
        frame = self.get_frame(self.frames)
        self.image = self.frames[frame]
        screen.blit(self.image, (self.rect.left - camera.left,
                                 self.rect.top - camera.top))


class Portal(Msg):    
    def __init__(self, x, y, w, h, ctrl):
        super(Portal, self).__init__(x, y, w, h,)

        self.text = """not have enough power to travel."""

    def pickup(self, player):
            if player.power >= 100:
                self.text = """the adventure is just beginning, but get here today"""
                time.sleep(2)
                player.game.won()   
            else:
                super(Portal, self).pickup(player)



