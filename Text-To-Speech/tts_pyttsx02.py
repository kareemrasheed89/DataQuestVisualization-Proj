# tts_pyttsx02.py

import pyttsx3
engine = pyttsx3.init()

# English
engine.say("Hello world")
engine.setProperty('rate',160)  #160 words per minute
engine.setProperty('volume',0.9) # 90% volume
engine.runAndWait()

# Turkish
engine.setProperty('voice','turkish')
engine.say("merhaba dünya")
engine.runAndWait()
