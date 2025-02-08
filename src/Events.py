import pygame
import sys
from pygame.locals import *

class EventHandler:

    def __init__(self):
        pass
    # Anything that happens after a key is pressed should go in this function
    def handleKeyPress(self, gameObjectsList):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
        print(keys)
        for obj in gameObjectsList:
            obj.interact(keys)

    def systemEvents(self, screen, gameObjectsList):
        for event in pygame.event.get():
            match event.type:
                case pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    for obj in gameObjectsList:
                        x, y = pixelsToCoords(screen, mouseX, mouseY)
                        obj.isClicked(x, y)
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    self.handleKeyPress(gameObjectsList)



def pixelsToCoords(screen, x, y):
    return ((x - screen.xOffset)/screen.scaleVal * 1000, 
            (y - screen.yOffset)/screen.scaleVal * 1000)
