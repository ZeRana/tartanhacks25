import pygame
import sys
from pygame.locals import *

class EventHandler:
    def handleKeyPress(self, gameObjectsList):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        keysList = getKeysPressed(keys)
        for obj in gameObjectsList:
            obj.interacted(keysList)

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

def getKeysPressed(keys):
    keysList = set()
    if keys[pygame.K_w]: keysList.add('w')
    if keys[pygame.K_e]: keysList.add('e')
    if keys[pygame.K_r]: keysList.add('r')
    if keys[pygame.K_t]: keysList.add('t')
    if keys[pygame.K_y]: keysList.add('y')
    return keysList

def pixelsToCoords(screen, x, y):
    return ((x - screen.xOffset)/screen.scaleVal, 
            (y - screen.yOffset)/screen.scaleVal)
