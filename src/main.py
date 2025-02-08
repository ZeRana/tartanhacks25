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

pygame.init()

def quit_game():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
######AUDIO 
#mixer.music.load(audio_file)
# mixer.music.set_volume(0.5)

def playMusic(audio_file):
    while True:
        #should be changed accordingly 
        mixer.music.play()
        user_input = input("")
        if user_input == 'o': #or if mouse clicks a button 
            mixer.music.pause()
        if user_input == 'p': #or if mouse clicks a button 
            mixer.music.play()
        if user_input == 'b': #emergency break
            break

def soundEffect(audio_file):
    sound_fx = pygame.mixer.Sound(audioFile)
    sound_fx.play()

def main():
    clock = pygame.time.Clock()
    gameObjectsList = []

    handler = EventHandler()
    mode = Mode()
    control = Control(mode, gameObjectsList)
    screen = Screen(gameObjectsList)

    SpriteSurface.rootPath = os.path.dirname(__file__)

    background = Background(SpriteSurface("backgrounds/newbackground.png"))


    while True:
        GameObject.deltaTime = clock.tick()
        screen.updateCoords()
        gameObjectsList += [background, mode]
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
