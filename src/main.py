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
    handler = EventHandler()

    background = Background(SpriteSurface("src/backgrounds/background.png"))
    fishImage = SpriteSurface("src/fish/clownfish.png", scale = 1)
    fishImage1 = SpriteSurface("src/fish/yellowseahorse.png", scale = 1)
    fishManager = FishManager()

    for i in range(5):
        fishManager.fishList.append(Fish(fishImage))
        fishManager.fishList.append(Fish(fishImage1))
    fishManager.setFishDeltaX(5)

    gameObjectsList = [background, fishManager]
    screen = Screen(gameObjectsList)
    while True:
        screen.updateCoords()

        # events
        handler.systemEvents(screen, gameObjectsList)

        # actions here:
        fishManager.moveFish()

        # draw to screen
        screen.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()
