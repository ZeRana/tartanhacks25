import pygame
import sys
from pygame.locals import *
from pygame import mixer

# Snake case --> pygame builtin
# Camel case --> our functions

pygame.init()

width = 400
"""Screen width."""
height = 400
"""Screen height."""

display = pygame.display.set_mode((width, height))

def quit_game():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
######AUDIO 
mixer.music.load(audio_file)
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

while True:
    pygame.display.update()
    quit_game()

pygame.quit()
sys.exit()



