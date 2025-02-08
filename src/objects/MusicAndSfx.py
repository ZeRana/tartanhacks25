from objects.GameObject import GameObject
import pygame.mixer as mixer


class Music(GameObject):

    def __init__(self):
        mixer.music.load('music/fish_music_final.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

        self.isPlay = True

    def interacted(self, event):
        if 'p' in event:
            self.isPlay = not self.isPlay
            if self.isPlay:
               mixer.music.unpause()
            else:
                mixer.music.pause()

    def draw(self, surface):
        pass

class Sfx(GameObject):
    def __init__(self):
        mixer.music.set_volume(0.7)

        self.soundDict = dict()
        self.soundDict['bubble'] = 'music/bubble-sound-43207.mp3' 

    def playAudio(self, sfxName):
        sfx = self.soundDict.get(sfxName)
        mixer.music.load(sfx)
        mixer.music.play(sfx)

    
        
#####
###'bubble' = 'music/bubble-sound-43207.mp3' 

############


