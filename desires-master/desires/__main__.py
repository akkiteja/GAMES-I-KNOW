import sys
import pygame

import data
from .scene import TestScene, SplashScene
from loader import Loader

# global FRAMES = {}

class Control():
    def __init__(self):
        self.screen_size = (640,480)
        self.flags = pygame.DOUBLEBUF|pygame.HWSURFACE
        self._screen = pygame.display.set_mode(self.screen_size, self.flags)
        self.screen = self._screen.convert().subsurface(0,0,320,240)
        self.screen_rect = self.screen.get_rect()
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.td = 0 # time delta
        self.keys = pygame.key.get_pressed()

        self.scene = None

        self.frames = {}
        self.sounds = {}

        self.loader = Loader()
        self.loader.image2load = 'sprite_sheet.png'
        self.loader.json_file = data.filepath('sprites.json')
        self.loader.sounds2load = [
            'DST-Defunkt.ogg',
            'menu.wav',
        ]


        self.loader.start()
        self.music = pygame.mixer.Channel(3)
        self.sfx = pygame.mixer.Channel(4)

    def change_scene(self, scene):
        self.scene = scene


    def quit(self):
        pygame.quit()
        sys.exit()


    def handle_events(self):
        for event in pygame.event.get():
                self.keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                    self.quit()

        self.scene.handle_events()

    def update(self):
        self.td = self.clock.tick(self.fps)/1000.0
        self.scene.update()
        

    def render(self):
        self.scene.render(self.screen)
        tmp = pygame.transform.scale(self.screen, self.screen_size)
        self._screen.blit(tmp, (0,0))


    def loop(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            
            caption = "{} - FPS: {:.2f}".format('Desires', self.clock.get_fps())
            pygame.display.set_caption(caption)            

            pygame.display.update()
            self.clock.tick(self.fps)

            

    


def main():
    ctrl = Control()
    scene = SplashScene(ctrl)
    ctrl.change_scene(scene)
    ctrl.loop()
