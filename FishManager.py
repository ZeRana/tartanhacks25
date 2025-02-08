import pygame
import Fish

class FishManager:

    def __init__(self):
        self.fishList = []


    def drawFish(self):
        for fish in self.fishList:
            fish.draw()