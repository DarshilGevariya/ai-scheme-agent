from agent import Agent
from memory import Memory
from stt import listen
from tts import speak

memory = Memory()
agent = Agent(memory)

def main():
    speak("namaste! main sarkari yojana sahayak hoon")
    speak("kripya apni age batayein")

    while True:
        user_text = listen()

        if not user_text.strip():
            continue   # 👈 ignore noise/silence

        response = agent.execute(user_text)

        if response:
            speak(response)

        if memory.is_complete():
            speak("aapki jankari poori ho gayi hai")
            break



if __name__ == "__main__":
    main()
