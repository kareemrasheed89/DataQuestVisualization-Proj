# tts_pyttsx01.py

import pyttsx3

def get_voice_list():
    voices = engine.getProperty('voices')
    no=1
    for voice in voices:
        print(f"\nVoice # {no}")
        print(f"Voice.ID: {voice.id}")
        print(f"Voice.Name: {voice.name}")
        print(f"Voice.Languages: {voice.languages}")
        print(f"Voice.Gender: {voice.gender}")
        print(f"Voice.Age: {voice.age}")
        no+=1

def speak_now():
    engine.setProperty('rate',180)  # words per minute
    engine.setProperty('volume',0.85)  # volume
    engine.say('Good morning! How are you?')
    engine.runAndWait()

if __name__ == "__main__":
    engine = pyttsx3.init()
    get_voice_list()
    speak_now()