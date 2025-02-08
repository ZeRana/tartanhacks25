import pygame
import Fish

class FishManager:

    def __init__(self):
        self.fishList = []


    def moveFish(self):
        for fish in self.fishList:
            fish.move()


    def drawFish(self, screen):
        for fish in self.fishList:
            fish.draw(screen)