import os
import sys
import pygame
from pygame.locals import *
from pygame import mixer

from Events import EventHandler
from Screen import Screen
from Control import Control, Mode
from objects.GameObject import GameObject, SpriteSurface
from objects.Background import Background

from objects.Fish import Fish
from objects.FishManager import FishManager
from objects.Bubble import Bubble
from objects.BubbleManager import BubbleManager
from objects.MusicAndSfx import Music

pygame.init()

def quit_game():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
 
def main():
    clock = pygame.time.Clock()
    gameObjectsList = []
    SpriteSurface.rootPath = os.path.dirname(__file__)

    handler = EventHandler()
    mode = Mode()
    control = Control(mode, gameObjectsList)
    screen = Screen(gameObjectsList)
    


    background = Background(SpriteSurface("backgrounds/newbackground.png"))
    music = Music()


    while True:
        print('root', SpriteSurface.rootPath)
        GameObject.deltaTime = clock.tick()
        screen.updateCoords()
        gameObjectsList += [background, mode, music]
        control.load()

        # events
        handler.systemEvents(screen, gameObjectsList)

        # actions here:
        control.loop()
        
        # draw to screen
        screen.draw()
        pygame.display.update()

        gameObjectsList.clear()

if __name__ == "__main__":
    main()
