import pygame
import random
from objects.GameObject import GameObject, SpriteSurface


class Background(GameObject):
    def __repr__(self):
        return "background"

class Title(GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.hasStarted = False
        self.x = 800 - 480
        self.y = 450 - 360

    def interacted(self, event):
        if 'click' in event:  
            self.hasStarted = True
     
    def draw(self, screen):
        if self.hasStarted:
            return
        super().draw(screen)




