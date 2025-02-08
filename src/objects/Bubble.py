import pygame
import random
from objects.GameObject import GameObject, SpriteSurface


class Bubble(GameObject):
    def __init__(self, surface):
        super().__init__(surface)

        self.y = 900
        self.x = random.randint(0, 1600)

        self.speed = random.uniform(.1, .5)

    def move(self):
        self.y -= self.speed * self.deltaTime
        self.resetPos()

    def resetPos(self):
        self.y = 900
        self.x = random.randint(0, 1600)
        self.speed = self.speed = random.uniform(.1, .8)

    def interacted(self, event):
        if event == 'click':
            self.resetPos()
