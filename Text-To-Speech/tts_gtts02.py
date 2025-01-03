# tts_gtts02.py

import pyglet
import time
from gtts import gTTS #internet gerekli
filename = "hello.mp3"
print("wait Google API to responde")

tts = gTTS(text="Hello World! How are you?", lang="en")

print("Save incoming answer as an mp3 file")
tts.save(filename)

print("set pyglet options")
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

print("load mp3 file")
audio = pyglet.media.load(filename, streaming=False)

print("play the sound")
audio.play()

print("wait until playing to be completed")
time.sleep(audio.duration)

print("Completed")
