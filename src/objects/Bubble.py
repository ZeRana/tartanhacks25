import pygame
import random
from objects.GameObject import GameObject, SpriteSurface


class Bubble(GameObject):
    def __init__(self, surface):
        super().__init__(surface)

        self.y = 900
        self.x = random.randint(0, 1600)

    def move(self):
        self.y -= random.random() * self.deltaTime
        self.resetPos()

    def resetPos(self):
        if self.y <= 0:
            self.y = 900
            self.x = random.randint(0, 1600)
