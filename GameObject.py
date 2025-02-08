import os
import pygame
from pygame.sprite import Sprite
from pygame import Surface
rootPath = os.getenv('GAMEPATH')

class GameObject(Sprite):
    def __init__(self, surface):
        super().__init__();

        self.surface = surface
        self.x = 0
        self.y = 0

    def isClicked(self, x, y):
        if self.surface.isRect: 
            return (self.x <= x <= self.x + self.surface.width and
                    self.y <= y <= self.y + self.surface.height)
        else:
           obj_mask = pygame.mask.from_surface(self.surface)
           return obj_mask.get_at((x - self.x, y - self.y)) == 1
               
    def interact(self, **kwargs):
        pass

    def draw(self, screen):
        screen.blitz(self.surface, (self.x, self.y))

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
class SpriteSurface(Surface):
    def __init__(self, spriteVal,
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
            elif os.path.isfile(os.path.join(rootPath, spriteVal)):
                filepath = os.path.join(rootPath, spriteVal)

            if filepath is None or not os.path.isfile(filepath):
                raise FileNotFoundError(f'{spriteVal} file not found')

            spriteVal = pygame.image.load(filepath)
        elif not isinstance(spriteVal, Surface):
            raise Exception(f'invalid surface {spriteVal}')

        self.width, self.height = spriteVal.get_size()
        super().__init__((self.width, self.height))
        self.blit(spriteVal, (0, 0))
        self.isRect = False
