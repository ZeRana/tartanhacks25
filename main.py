import pygame
import sys
from pygame.locals import *
import Events

# Snake case --> pygame builtin
# Camel case --> our functions

pygame.init()

width = 400
"""Screen width."""
height = 400
"""Screen height."""

display = pygame.display.set_mode((width, height))
handler = Events.EventHandler()


while True:
    handler.systemEvents()
    pygame.display.update()


