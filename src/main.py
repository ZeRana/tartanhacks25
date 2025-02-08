import os
import sys
import pygame
from pygame.locals import *
from pygame import mixer

from Events import EventHandler
from Screen import Screen
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
 
mixer.music.load('music/fish_music_final.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)



def main():
    clock = pygame.time.Clock()
    handler = EventHandler()
    SpriteSurface.rootPath = os.path.dirname(__file__)

    background = Background(SpriteSurface("backgrounds/background.png"))
    fishImage = SpriteSurface("fish/clownfish.png", scale = 1)
    fishImage1 = SpriteSurface("fish/yellowseahorse.png", scale = 1)

    bubbleImage = SpriteSurface("bubble.png", scale=1)
    bubbleManager = BubbleManager()
    fishManager = FishManager()
    musicManager = Music()

    for i in range(10):
        bubbleManager.bubbles.append(Bubble(bubbleImage))
    for i in range(5):
        fishManager.fishList.append(Fish(fishImage))
        fishManager.fishList.append(Fish(fishImage1))

    gameObjectsList = [background, fishManager, bubbleManager, musicManager]
    screen = Screen(gameObjectsList)

    while True:
        GameObject.deltaTime = clock.tick()
        screen.updateCoords()

        # events
        handler.systemEvents(screen, gameObjectsList)

        # actions here:
        fishManager.moveFish()
        bubbleManager.moveBubbles()

        # draw to screen
        screen.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()
