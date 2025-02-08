import pygame
from objects.GameObject import GameObject

class BubbleManager(GameObject):
    def __init__(self):
        self.bubbles = []

    def moveBubbles(self):
        for bubble in self.bubbles:
            bubble.move()

    def draw(self, screen):
        for bubble in self.bubbles:
            bubble.draw(screen)

    def isClicked(self, x, y):
        for bubble in self.bubbles:
            bubble.isClicked(x, y)
    
    def __repr__(self):
        return 'bubblemanager'
