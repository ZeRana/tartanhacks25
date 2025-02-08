from objects.GameObject import GameObject

class Music(GameObject):

    def __init__(self):
        mixer.music.load('music/fish_music_final.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)
        mixer.music.pause() = True

    def interacted(self, event):
        if event == 'p':
            mixer.music.pause() = not mixer.music.pause()

    # def isClicked(self, x, y):
    #     pass

    # def action(self):
    #     pass
        
    # def draw(self):
    #     pass

    # def setPosition(self, x, y):
    #     pass

    # def checkOnScreen(self)
    #     pass


