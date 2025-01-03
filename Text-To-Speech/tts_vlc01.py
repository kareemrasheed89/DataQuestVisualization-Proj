import vlc
import time

def tts_vlc(filename):
    p = vlc.MediaPlayer(filename)
    p.play()
    time.sleep(1)

if __name__ == "__main__":
    tts_vlc("good_morning.mp3")
