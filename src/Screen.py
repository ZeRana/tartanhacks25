import pygame
import pyautogui

class Screen():
    def __init__(self, gameObjectsList):
        width, height = pyautogui.size()
        self.width = round(width * 3/4)
        self.height = round(height * 3/4)

        self.scaleVal = 1
        self.xOffset = 0
        self.yOffset = 0

        self.display = pygame.display.set_mode((self.width, self.height), 
                                               pygame.RESIZABLE)
        self.updateCoords()
        self.gameObjectsList = gameObjectsList
    
    def updateCoords(self):
        self.width, self.height = self.display.get_size()
        self.scaleVal = min(self.width, self.height)
        self.xOffset = self.width/2 - self.scaleVal/2
        self.yOffset = self.height/2 - self.scaleVal/2

    def draw(self):
        layer = pygame.Surface((1000, 1000))
        for obj in self.gameObjectsList:
            obj.draw(layer)

        self.display.blit(pygame.transform.scale(layer, (self.scaleVal, self.scaleVal)),
                          (self.xOffset, self.yOffset))
