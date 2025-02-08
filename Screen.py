import pygame
import pyautogui

class Screen():
    def __init__(self, gameObjectsList):
        width, height = pyautogui.size()
        self.width = round(width * 3/4)
        self.height = round(height * 3/4)
        self.display = pygame.display.set_mode((self.width, self.height), 
                                               pygame.RESIZABLE)
        self.gameObjectsList = gameObjectsList
    
    def draw(self):
        layer = pygame.Surface((1000, 1000))
        for obj in self.gameObjectsList:
            obj.draw(layer)

        self.width, self.height = self.display.get_size()
        scaleVal = min(self.width, self.height)
        self.display.blit(pygame.transform.scale(layer, (scaleVal, scaleVal)), 
                          (self.width/2 - scaleVal/2, 
                           self.height/2 - scaleVal/2))
