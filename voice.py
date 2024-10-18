import speech_recognition as sr
import pyttsx3
import datetime
import os
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, the server is down.")
        return None

# Function to get and announce the current time
def get_time():
    now = datetime.datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    am_pm = now.strftime("%p")
    speak(f"The time is {hour}:{minute} {am_pm}")

def get_name():
    speak("My name is moon")

def main():
    speak("How can I assist you?")
    while True:
        command = listen()

        if command is None:
            continue

        if "time" in command:
            get_time()
        elif "your name" in command:
            get_name()
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can only tell the time or my name for now.")

if __name__ == "__main__":
    main()
