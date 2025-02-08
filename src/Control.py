from objects.GameObject import GameObject, SpriteSurface
from objects.Fish import Fish
from objects.FishManager import FishManager
from objects.Bubble import Bubble
from objects.BubbleManager import BubbleManager
from objects.MusicAndSfx import Sfx

class Control():
    def __init__(self, mode, gameObjectsList):
        self.mode = mode
        self.gameObjectsList = gameObjectsList
        self.sfx = Sfx()
        self.idle = dict()
        self.current = None

        self.idle = loadIdle()
        self.sandbox = loadSandbox()
        self.current = self.sandbox

    def load(self):
        if self.mode.currentMode == 'idle':
            self.gameObjectsList += [self.idle[key] for key in self.idle]
            self.current = self.idle
        elif self.mode.currentMode == 'sandbox':
            self.gameObjectsList += [self.sandbox[key] for key in self.sandbox]
            self.current = self.sandbox

    def loop(self):
        for action in GameObject.shared:
            if action == 'bubble':
                self.sfx.playAudio('bubble')

        self.current['fishes'].moveFish()
        self.current['bubbles'].moveBubbles()

def loadIdle():
    bubbleImage = SpriteSurface("bubble.png", scale=1)
    idle = dict()
    idle['bubbles'] = BubbleManager()
    idle['fishes'] = FishManager()
    for i in range(10):
        idle['bubbles'].bubbles.append(Bubble(bubbleImage))
    for i in range(5):
        idle['fishes'].newFish()
        idle['fishes'].newSeaHorse()
        idle['fishes'].newTurtle()
    return idle

def loadSandbox():
    bubbleImage = SpriteSurface("bubble.png", scale=1)
    sandbox = dict()
    sandbox['bubbles'] = BubbleManager()
    sandbox['fishes'] = FishManager()
    for i in range(10):
        sandbox['bubbles'].bubbles.append(Bubble(bubbleImage))
    for i in range(15):
        sandbox['fishes'].newTurtle()
    return sandbox



class Mode(GameObject):
    def __init__(self):
        self.modes = ('idle', 'sandbox', 'game')
        self.modeIndex = 0
        self.currentMode = self.modes[self.modeIndex]

    def interacted(self, event):
        if 'm' in event:
            self.modeIndex = (self.modeIndex + 1) % 3
            self.currentMode = self.modes[self.modeIndex]


    def isClicked(self, x, y):
        pass

    def draw(self, layer):
        pass

    def __repr__(self):
        return 'mode'

