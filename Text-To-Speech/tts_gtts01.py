# tts_gtts01.py

from gtts import gTTS
import os
import pyglet
import time
filename = "good_morning.mp3"
# convert text to speech and save it
tts = gTTS(text="Good morning!", lang='en')
tts.save(filename)

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
audio = pyglet.media.load(filename, streaming=False)
audio.play()
# wait playing to be completed
time.sleep(audio.duration)
