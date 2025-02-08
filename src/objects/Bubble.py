import pygame
import random
from objects.GameObject import GameObject, SpriteSurface


class Bubble(GameObject):
    def __init__(self, surface):
        super().__init__(surface)

        self.y = 900
        self.x = random.randint(0, 1600)

    def move(self):
        self.y -= random.random()/10 * self.deltaTime
        if self.y <= 0:
            self.resetPos()

    def resetPos(self):
        self.y = 900
        self.x = random.randint(0, 1600)

    def interacted(self, event):
        if event == 'click':
            self.resetPos()
