import pyglet
import time

def tts_pyglet(filename):
    pyglet.options['audio'] = ('openal','pulse','directsound','silent')
    sound = pyglet.resource.media(filename)
    sound.play()
    time.sleep(sound.duration)

if __name__ == "__main__":
    tts_pyglet("good_morning.mp3")
