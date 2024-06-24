# import required module
from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3("audio/notes.mp3")
print('playing sound using  pydub')
play(song)