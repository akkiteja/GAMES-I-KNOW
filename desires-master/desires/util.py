import pygame
import data 

pygame.init()

sfont = pygame.font.SysFont(data.filepath('terminal.fon', 'fonts'), 12)
jfont = pygame.font.Font(data.filepath('visitor2.ttf', 'fonts'), 15)
nfont = pygame.font.Font(data.filepath('visitor2.ttf', 'fonts'), 25)
bfont = pygame.font.Font(data.filepath('visitor2.ttf', 'fonts'), 35)
tfont = pygame.font.Font(data.filepath('color-basic.ttf', 'fonts'), 35)

class Option:
    def __init__(self, text, func, x, y, args=None):
        self.normal = nfont.render(text, 1, (255,255,255))
        self.highlight = bfont.render(text, 1, (100,100,100))
        self.highlighted = False
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.dest_x = x
        self.x = -500
        self.rect.y = y
        self.func = func
        if args: self.args = args

    def update(self):
        if self.highlighted: self.image = self.highlight
        else:  self.image = self.normal


        self.x += (self.dest_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def render(self, screen):
        screen.blit(self.image, self.rect)


class NestedOption:
    def __init__(self, text, options, x , y):
        self.text = text
        self.options = []
        for text, func in options:
            txt = self.text + ' < ' + text + ' >'
            o = Option(txt, func, x, y, text)
            o.x = x # no animation
            self.options.append(o)

        self.options[0].x = -500 # animate the firts time

        self.curr_index = 0
        self.highlighted = False
        self.options_len = len(self.options)

    def handle_events(self, d):
        self.curr_index += d

        if self.curr_index >= self.options_len:
            self.curr_index = 0
        elif self.curr_index < 0:
            self.curr_index = self.options_len - 1

    def update(self):
        if self.highlighted:
            self.options[self.curr_index].highlighted = True
        else:
            self.options[self.curr_index].highlighted = False
        self.options[self.curr_index].update()

    def render(self, screen):
        self.options[self.curr_index].render(screen)

    def func(self):
        o = self.options[self.curr_index]
        o.func(o.args)


def get_pixel_coords(x, y):
    px = 16 * x
    py = 16 * y
    return px, py

def get_tile_coords((x, y)):
    tx = x / 16
    ty = y / 16
    return tx, ty