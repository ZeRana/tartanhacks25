import pygame
import objects.Bubble

class BubbleManager:
    def __init__(self):
        self.bubbles = []

    def moveBubbles(self):
        for bubble in self.bubbles:
            bubble.move()

    def draw(self, screen):
        for bubble in self.bubbles:
            bubble.draw(screen)


    