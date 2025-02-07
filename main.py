import pygame
import sys
from pygame.locals import *

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

while True:
    pygame.display.update()
    quit_game()

pygame.quit()
sys.exit()

