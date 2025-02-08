import pygame
import random
from objects.GameObject import GameObject, SpriteSurface

class Fish(GameObject):

    def __init__(self, surface):
        super().__init__(surface)
        self.value = 0
        self.y = random.randint(500, 900)

        self.facingRight = True

    def interacted(self, event):
        print(event)

    def isClicked(self, x, y):
        super().isClicked(x, y)

    def move(self):
        self.x += (random.random() * self.deltaX)
        self.turnAround()

    def turnAround(self):
        if (self.facingRight and self.x >= 975) or (not self.facingRight and self.x <= 15):
            self.facingRight = not self.facingRight
            self.deltaX *= -1
            self.surface = SpriteSurface(pygame.transform.flip(self.surface, True, False))

    def __repr__(self):
        return 'fish'

    def __eq__(self, other):
        return "fish" == other
