import pygame

class Pickup(pygame.sprite.Sprite):
    def __init__(self, (x, y)):
        super(Pickup, self).__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill((56,45,26))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def render(self, screen, camera):
        screen.blit(self.image, (self.rect.left - camera.left,
                                 self.rect.top - camera.top))




class Ammo(Pickup):
    def __init__(self, (x, y)):
        super(Ammo, self).__init__((x,y))
        self.image.fill((0,0,0))

    def pickup(self, player):
        player.weapon.ammo += 25

class PainKiller(Pickup):
    def __init__(self, (x, y)):
        super(PainKiller, self).__init__((x,y))
        self.image.fill((213,20,20))

    def pickup(self, player):
        self.image.fill((0,0,0))
        player.health += 20

class Power(Pickup):
    def __init__(self, (x, y)):
        super(Power, self).__init__((x,y))
        self.image.fill((20,20,250))

    def pickup(self, player):
        self.image.fill((0,0,0))
        player.power += 25




