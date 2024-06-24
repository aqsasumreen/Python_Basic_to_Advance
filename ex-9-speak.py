import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


names = ["Aqsa", "sumreen", "fatima", "ali"]

for name in names:
    speak(f"shoutput to {name}")
    # engine.say(f"shoutout to {name}")
