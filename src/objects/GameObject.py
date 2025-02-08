import os
import pygame
from pygame.sprite import Sprite
from pygame import Surface

class GameObject(Sprite):
    def __init__(self, surface):
        super().__init__();

        self.surface = surface
        self.x = 0
        self.y = 0
        self.deltaX = 1

        self.onScreen = False

    def isClicked(self, x, y):
        if self.surface.isRect: 
            if (self.x <= x <= self.x + self.surface.width and
                self.y <= y <= self.y + self.surface.height):
                self.interacted('click')
                return

        obj_mask = pygame.mask.from_surface(self.surface)
        self_mask = pygame.mask.from_surface(Surface((1, 1)))
        if obj_mask.overlap(self_mask, (self.x - x, self.y - y)):
           self.interacted('click')
           print('click')
           return
               
    def interacted(self, event):
        pass

    def action(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
class SpriteSurface(Surface):
    def __init__(self, spriteVal, scale = 1,
                 width = 30, height = 30, color = (255, 255, 255),
                 imgDir = None, **kwargs):
        self.width = width
        self.height = height
        self.isRect = True

        if isinstance(spriteVal, str):
            if spriteVal == 'default':
                super().__init__((self.width, self.height))
                self.fill(color)
                return

            filepath = None
            if imgDir:
                filepath = os.path.join(imgDir, spriteVal)
            elif os.path.isfile(spriteVal):
                filepath = spriteVal

            if filepath is None or not os.path.isfile(filepath):
                raise FileNotFoundError(f'{spriteVal} file not found')

            spriteVal = pygame.image.load(filepath)

        elif not isinstance(spriteVal, Surface):
            raise Exception(f'invalid surface {spriteVal}')

        width, height = spriteVal.get_size()
        spriteVal = pygame.transform.scale(spriteVal, (width * scale, height * scale))
        self.width, self.height = spriteVal.get_size()

        super().__init__((self.width, self.height), pygame.SRCALPHA)
        self.blit(spriteVal, (0, 0))
#        self.isRect = False

    def __repr__(self):
        return 'SpriteSurface'
