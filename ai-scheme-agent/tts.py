import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 130)
engine.setProperty("volume", 1.0)

def speak(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("namaste! yeh hindi voice test hai.")
