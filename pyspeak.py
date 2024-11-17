from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
import os

def speak(text):
    speak = gTTS(f'{text}', lang='en')
    speak.save("voice.mp3")
    pwd = os.getcwd()
    pwd = (pwd + '/voice.mp3')
    nee = AudioSegment.from_mp3(pwd)
    nee.speedup(playback_speed=1.25)
    play(nee)
    os.system("rm voice.mp3")
