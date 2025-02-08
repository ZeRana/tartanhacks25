import pygame
from objects.GameObject import GameObject
import objects.Fish

class FishManager(GameObject):
    def __init__(self):
        self.fishList = []
    
    def isClicked(self, x, y):
        for fish in self.fishList:
            fish.isClicked(x, y)

    def interacted(self, keys):
        print(keys)

    def moveFish(self):
        for fish in self.fishList:
            fish.move()

    def draw(self, screen):
        for fish in self.fishList:
            fish.draw(screen)
