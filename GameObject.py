import os
import pygame
from pygame.sprite import Sprite
from pygame import Surface
rootPath = os.getenv('GAMEPATH')

class GameObject(Sprite):
    def __init__(self, image):
        super().__init__();

        self.image = image
        self.x = 0
        self.y = 0

    def isClicked(self, x, y):
        pass

    def interact(self, **kwargs):
        pass

    def draw(self, screen):
        screen.blitz(self.image, (self.x, self.y))

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
class SpriteSurface(Surface):
    def __init__(self, spriteVal,
                 length = 30, width = 30, color = (255, 255, 255),
                 imgDir = None, **kwargs):
        self.length = length
        self.width = width
        self.isRect = True

        if isinstance(spriteVal, str):
            if spriteVal == 'default':
                super().__init__((self.length, self.width))
                self.fill(color)
                return

            filepath = None
            if imgDir:
                filepath = os.path.join(imgDir, spriteVal)
            elif os.path.isfile(spriteVal):
                filepath = spriteVal
            elif os.path.isfile(os.path.join(rootPath, spriteVal)):
                filepath = os.path.join(rootPath, spriteVal)

            if filePath is None or not os.path.isfile(filepath):
                raise FileNotFoundError(f'{spriteVal} file not found')

            spriteVal = pygame.image.load(filepath)
        elif not isinstance(spriteVal, Surface):
            raise Exception(f'invalid surface {spriteVal}')

        self.length, self.width = spriteVal.get_size()
        super().__init__((self.length, self.width))
        self.blit(spriteVal, (0, 0))
        self.isRect = False
