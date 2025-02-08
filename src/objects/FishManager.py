import pygame
import random
from objects.GameObject import GameObject, SpriteSurface
from objects.Fish import Fish

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

    def newFish(self):
        self.fishList.append(Fish(SpriteSurface("fish/clownfish.png", scale = random.uniform(.9, 1.5))))
        print(self.fishList)
    

    def newSeaHorse(self):
        self.fishList.append(Fish(SpriteSurface(random.choice(["fish/blueseahorse.png", "fish/yellowseahorse.png"]),
                                                 scale = random.uniform(.9, 1.5))))
    
    def newTurtle(self):
        self.fishList.append(Fish(SpriteSurface("fish/turtle.png", scale= random.uniform(1, 2))))

    def __repr__(self):
        return 'bubblemanager'
