import speech_recognition as sr
import pyttsx3
from config import VOICE_RATE, VOICE_INDEX

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[VOICE_INDEX].id)

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            return ""

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
