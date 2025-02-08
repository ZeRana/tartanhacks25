import pygame
import pyautogui

class Screen():
    canvasDimensions = (1600, 900)

    def __init__(self, gameObjectsList):
        width, height = pyautogui.size()
        self.windowWidth = round(width * 3/4)
        self.windowHeight = round(height * 3/4)

        self.scaleVal = 1
        self.width, self.height = 0, 0
        self.xOffset, self.yOffset = 0, 0

        self.display = pygame.display.set_mode((self.windowWidth, self.windowHeight), 
                                               pygame.RESIZABLE)
        self.updateCoords()
        self.gameObjectsList = gameObjectsList
    
    def updateCoords(self):
        self.windowWidth, self.windowHeight = self.display.get_size()
        
        xScale = self.windowWidth/self.canvasDimensions[0]
        yScale = self.windowHeight/self.canvasDimensions[1]
        self.scaleVal = min(xScale, yScale)

        self.width = self.canvasDimensions[0] * self.scaleVal
        self.height = self.canvasDimensions[1] * self.scaleVal

        self.xOffset = self.windowWidth/2 - self.width/2
        self.yOffset = self.windowHeight/2 - self.height/2

    def draw(self):
        layer = pygame.Surface(self.canvasDimensions)
        for obj in self.gameObjectsList:
            obj.draw(layer)
       
        self.display.blit(pygame.transform.scale(layer, (self.width, self.height)),
                          (self.xOffset, self.yOffset))
