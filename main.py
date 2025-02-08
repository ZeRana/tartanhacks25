import os
import sys
import pygame
from pygame.locals import *
from pygame import mixer

import Events
from Screen import Screen
from GameObject import GameObject, SpriteSurface
import Fish
import FishManager

os.environ['GAMEPATH'] = os.path.dirname(__file__)

# Snake case --> pygame builtin
# Camel case --> our functions

pygame.init()


def quit_game():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
######AUDIO 
#mixer.music.load(audio_file)
mixer.music.set_volume(0.5)

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

handler = Events.EventHandler()
background = GameObject(SpriteSurface("background.png"))
fishImage = SpriteSurface("fish/clownfish.png")
fish = Fish.Fish(fishImage)
fish1 = Fish.Fish(fishImage)
fishManager = FishManager.FishManager()
fishManager.fishList.append(fish)
fishManager.fishList.append(fish1)
fishManager.setFishDeltaX(90)

def main():
    gameObjectList = [background, fishManager]
    screen = Screen(gameObjectList)
    while True:
        fishManager.moveFish()
        handler.systemEvents()
        screen.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
