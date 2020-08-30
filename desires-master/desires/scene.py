import pygame

import camera, data, level, player, enemies
import util as u

# FRAMES = global FRAMES

class Scene(object):
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.back_scene = None
        self.hold = False
        self.bg_color = (0,0,0)

    def handle_events(self):
        raise NotImplemented("handle_events func have to be implemented")

    def update(self):
        raise NotImplemented("update func have to be implemented")

    def render(self, screen):
        raise NotImplemented("render func have to be implemented")

    def back(self):
        self.ctrl.change_scene(self.back_scene)


class TestScene():
    def handle_events(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255,255,255))
        text = u.nfont.render('hello world', 1, (0,0,0))
        screen.blit(text, (0,0))


class SplashScene(Scene):
    def __init__(self, ctrl):
        super(SplashScene, self).__init__(ctrl)
        self.image = pygame.image.load(data.imagepath('splash.png'))
        self.ticks = 0

    def handle_events(self):
        pass

    def update(self):
        if self.ctrl.loader.done and self.ticks > 120:
            self.ctrl.frames = self.ctrl.loader.frames
            self.ctrl.sounds = self.ctrl.loader.sounds

            scene = MainMenuScene(self.ctrl)
            self.ctrl.change_scene(scene)

        self.ticks += 1

    def render(self, screen):
        screen.blit(self.image, (0,0))



class MenuScene(Scene):
    def __init__(self, ctrl):
        super(MenuScene, self).__init__(ctrl)

        self.options = {}
        self.rendered_options = []
        self.curr_index = 0        
        self.hold = False
        self.first = True

    def prepare_options(self):
        x = 20
        y = 100
        line_height = 25
        for text, func in self.options:
            if type(func) == list:
                op = u.NestedOption(text, func, x, y)
            else:
                op = u.Option(text, func, x, y)

            self.rendered_options.append(op)
            y += line_height



    def handle_events(self):
        keys = self.ctrl.keys
        o = self.rendered_options[self.curr_index]
        sound = self.ctrl.sounds['menu']

        if not self.hold and not self.first:
            if keys[pygame.K_RETURN]:
                o.func()

            if keys[pygame.K_DOWN]:
                self.ctrl.sfx.play(sound)
                self.curr_index += 1
                if self.curr_index >= len(self.rendered_options):
                    self.curr_index = 0


            if keys[pygame.K_UP]:
                self.ctrl.sfx.play(sound)
                self.curr_index -= 1
                if self.curr_index < 0:
                    self.curr_index = len(self.rendered_options) - 1


            if keys[pygame.K_LEFT]:
                self.ctrl.sfx.play(sound)
                if isinstance(o, u.NestedOption):
                    o.handle_events(-1)



                self.ctrl.sfx.play(sound)
            if keys[pygame.K_RIGHT]:                
                if isinstance(o, u.NestedOption):
                    o.handle_events(1)





        keys_pressed = (keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_RETURN],
               keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
        self.hold =  any(keys_pressed)


        # wait to pass here more than once
        self.first = False 

    def update(self):
        self.rendered_options[self.curr_index].highlighted = True
        for option in self.rendered_options:
            option.update()
        self.rendered_options[self.curr_index].highlighted = False

    def render(self, screen):
        screen.fill(self.bg_color)     
        for option in self.rendered_options:
            option.render(screen)



class MainMenuScene(MenuScene):    

    def __init__(self, ctrl):
        super(MainMenuScene, self).__init__(ctrl)

        self.options = [
            ('Play', self.play),
            ('Fullscreen:', [
                    ('no', self.toggle_fullscreen),
                    ('yes', self.toggle_fullscreen),
                ]),
            ('Credits', self.credits),
            ('Quit', self.ctrl.quit)
        ]

        self.prepare_options()
        self.title = u.tfont.render('Limbo Room', 1, (255,255,255))

        self.ctrl.music.play(self.ctrl.sounds['DST-Defunkt'], -1)


    def render(self, screen):
        super(MainMenuScene, self).render(screen)
        x = screen.get_width() - self.title.get_width()
        screen.blit(self.title, (x, 20))

    def play(self):        
        scene = PlayScene(self.ctrl)
        scene.back_scene = self
        self.ctrl.change_scene(scene)

    def toggle_fullscreen(self, yesno):
        if yesno == 'yes':
            flags = pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF 
            self._screen = pygame.display.set_mode(self.ctrl.screen_size, flags)
        else:
            flags = pygame.DOUBLEBUF|pygame.HWSURFACE
            self._screen = pygame.display.set_mode(self.ctrl.screen_size, flags)


    def credits(self):
        scene = CreditsScene(self.ctrl)
        scene.back_scene = self
        self.ctrl.change_scene(scene)




class PlayScene(Scene):
    def __init__(self, ctrl):
        super(PlayScene, self).__init__(ctrl)
        self.player = player.Player(self.ctrl, self)
        self.bg_color = (100, 128, 64)
        w, h = self.ctrl.screen.get_size()
        self.camera = camera.Camera(self.player.rect, w, h)
        self.level = level.Level('data/map.tmx')

        self.entities = []
        self.objects = self.level.generate_objects(self.ctrl)
        self.enemies = enemies.EnemyCtrl(self.ctrl, self)

    def draw_info(self):
        lines = [
            'Health: {}'.format(self.player.health),
            'Ammo: {}'.format(self.player.weapon.ammo),
            'Power: {}'.format(self.player.power)
        ]
        rendered = []
        for l in lines:
            s = u.sfont.render(l, 1, (255,255,255))
            rendered.append(s)

        line_height = 14
        x = y = 1
        for r in rendered:
            self.ctrl.screen.blit(r, (x,y))
            y += line_height



    def render_entities(self):
        for e in self.entities:
            if self.camera.colliderect(e.rect):
                e.render(self.ctrl.screen, self.camera)

    def render_objects(self):
        for o in self.objects:
            if isinstance(o, pygame.sprite.Sprite):
                if self.camera.colliderect(o.rect):
                    o.render(self.ctrl.screen, self.camera)
            else:
                if self.camera.colliderect(o):
                    o.render(self.ctrl.screen, self.camera)

    def handle_events(self):
        self.player.handle_events(self.ctrl.keys)


    def update(self):        
        self.player.update(self.ctrl.keys, self.level)
        self.camera.update(self.player.rect, self.level)
        self.enemies.update()
        for e in self.entities:
            e.update()
            if e.die:
                self.entities.remove(e)
                self.enemies.curr_enemies -= 1
                self.enemies.player_kills += 1


    def render(self, screen):
        screen.fill(self.bg_color)
        # to change
        self.level.render(screen, self.camera)
        self.player.render(screen, self.camera)
        self.render_entities()
        self.render_objects()
        self.draw_info()
        pygame.display.update(self.camera)

    def won(self):
        scene = WonScene(self.ctrl)
        self.ctrl.change_scene(scene)

    def lose(self):
        scene = GameOverScene(self.ctrl)
        self.ctrl.change_scene(scene)

class WonScene(Scene):
    def __init__(self, ctrl):
        super(WonScene, self).__init__(ctrl)

        self.image = self.ctrl.frames['won']

    def handle_events(self):
        if self.ctrl.keys[pygame.K_SPACE]:
            self.ctrl.quit()

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (0,0))


class GameOverScene(Scene):
    def __init__(self, ctrl):
        super(GameOverScene, self).__init__(ctrl)

        self.image = self.ctrl.frames['gameover']

    def handle_events(self):
        if self.ctrl.keys[pygame.K_SPACE]:
            scene = MainMenuScene(self.ctrl)
            self.ctrl.change_scene(scene)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (0,0))



class CreditsScene(Scene):
    def __init__(self, ctrl):
        super(CreditsScene, self).__init__(ctrl)

        self.image = self.ctrl.frames['credits']

    def handle_events(self):
        if self.ctrl.keys[pygame.K_SPACE]:
            self.back()

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (0,0))
