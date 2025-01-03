import pygame
import time

def tts_pygame(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(1)

if __name__ == "__main__":
    tts_pygame("good_morning.mp3")
