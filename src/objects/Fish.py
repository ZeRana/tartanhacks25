import pygame
import random
from objects.GameObject import GameObject, SpriteSurface

class Fish(GameObject):
    def __init__(self, surface):
        super().__init__(surface)
        self.value = 0
        self.y = random.randint(20, 880)

        self.facingRight = True
        self.speed = random.uniform(.05, .3)

    def interacted(self, event):
        print(event)

    def move(self):
        x, y = self.getPosition()
        xOffset = self.speed * (1 if self.facingRight else -1)
        self.setPosition(x + xOffset, y)
        self.turnAround()

    def turnAround(self):
        if (self.facingRight and self.x >= 1575) or (not self.facingRight and self.x <= 15):
            self.facingRight = not self.facingRight
            self.surface = SpriteSurface(pygame.transform.flip(self.surface, True, False))

    def __repr__(self):
        return 'fish'

    def __eq__(self, other):
        return "fish" == other
