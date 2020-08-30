import json
from threading import Thread

import pygame
import data

pygame.init()

class Loader(Thread):    
    
    def __init__(self):
        super(Loader, self).__init__()
        self.done = False
        self.image2load  = ''
        self.sounds2load = []
        self.frames = {}
        self.sounds = {}
        self.json_file = ''




    def load_image(self, filename, transparent=False, alpha=False, pixel=(0,0) ):
        try: image = pygame.image.load(data.imagepath(filename))
        except pygame.error, message:
            raise SystemExit, message
        if not alpha:
            image = image.convert()
        else:
            image = image.convert_alpha()
        if transparent:
            color = image.get_at(pixel)
            image.set_colorkey(color, pygame.RLEACCEL)

        return image

    def generate_frames(self, filename, json_file):
        frames = {}
        image = self.load_image(filename, True, True)
        j_file=open(json_file)
        data = json.load(j_file)
        j_file.close()

        for frame in data['frames']:
            name = frame['filename'][:-4]
            x, y = frame['frame']['x'], frame['frame']['y']
            w, h = frame['frame']['w'], frame['frame']['h']
            if frame['rotated']:
                w, h = h, w
                tmp = image.subsurface(x, y, w, h)
                frames[name] = pygame.transform.rotate(tmp, 90)
            else:
                frames[name] = image.subsurface(x, y, w, h)

        return frames

    def load_sounds(self):
        sounds = {}
        for s in self.sounds2load:
            name = s[:-4]
            s = data.filepath(s, 'sounds')
            sound = pygame.mixer.Sound(s)
            sounds[name] = sound
        return sounds

    def run(self):
        print 'start loading'
        self.frames = self.generate_frames(self.image2load, self.json_file)
        self.sounds = self.load_sounds()
        print 'done loading'
        self.done = True