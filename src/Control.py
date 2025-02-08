from objects.GameObject import GameObject, SpriteSurface
from objects.Fish import Fish
from objects.FishManager import FishManager
from objects.Bubble import Bubble
from objects.BubbleManager import BubbleManager

class Control():
    def __init__(self, mode, gameObjectsList):
        self.mode = mode
        self.gameObjectsList = gameObjectsList

        self.bubbleImage = SpriteSurface("bubble.png", scale=1)
        self.bubbleManager = BubbleManager()
        self.fishManager = FishManager()
        for i in range(10):
            self.bubbleManager.bubbles.append(Bubble(self.bubbleImage))
        for i in range(5):
            self.fishManager.newFish()
            self.fishManager.newSeaHorse()
            self.fishManager.newTurtle()

    def load(self):
        if self.mode.currentMode == 'idle':
            self.gameObjectsList += [self.bubbleManager, 
                                     self.fishManager]

    def loop(self):
        self.fishManager.moveFish()
        self.bubbleManager.moveBubbles()

class Mode(GameObject):
    def __init__(self):
        self.modes = ('idle', 'sandbox', 'game')
        self.modeIndex = 0
        self.currentMode = self.modes[self.modeIndex]

    def interacted(self, event):
        if 'm' in event:
            self.modeIndex = (self.modeIndex + 1) % 3
            self.currentMode = self.modes[self.modeIndex]
            print(self.currentMode)

    def isClicked(self, x, y):
        pass

    def draw(self, layer):
        pass

    def __repr__(self):
        return 'mode'

