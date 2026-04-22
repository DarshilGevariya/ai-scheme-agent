import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("small", compute_type="int8")

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("🎤 boliye...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=6, phrase_time_limit=6)

    try:
        text = r.recognize_google(audio, language="hi-IN")
        print("👤:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("⚠️ samajh nahi aaya")
        return ""   # 👈 DO NOT crash

    except sr.RequestError as e:
        print("STT error:", e)
        return ""


if __name__ == "__main__":
    try:
        text = listen()
        print("Recognized text:", text)
    except Exception as e:
        print("Error:", e)
