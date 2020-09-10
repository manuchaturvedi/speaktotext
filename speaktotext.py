import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("listening")

        r.pause_threshold = 1 
        audio=r.listen(source)

    try:
        print("Recognizing... ")
        speak("Recognizing ...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query

takeCommand()