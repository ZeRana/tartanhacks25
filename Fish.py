import pygame
import random
from GameObject import GameObject, SpriteSurface

class Fish(GameObject):

    def __init__(self, surface):
        super().__init__(surface)
        self.value = 0

        self.y = random.randint(500, 900)

    def move(self):
        self.x += 1