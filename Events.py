import pygame
import sys
from pygame.locals import *

class EventHandler:

    def __init__(self):
        pass
    # Anything that happens after a key is pressed should go in this function
    def handleKeyPress(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

    def systemEvents(self):
        for event in pygame.event.get():
            match event.type :
                case pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    self.handleKeyPress()

def pixels_to_coords(x, y):
    return (x/SCREEN_X * 1000, y/SCREEN_Y * 1000)
