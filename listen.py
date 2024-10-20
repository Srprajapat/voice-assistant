from speak import speak
import speech_recognition as sr
import os
import pyaudio
from vosk import Model, KaldiRecognizer
import time
import json
import requests

vosk_model_path = "vosk"  
if not os.path.exists(vosk_model_path):
    print(f"Model not found at {vosk_model_path}, please download and unzip it.")
    exit(1)
model = Model(vosk_model_path)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

recognizer = KaldiRecognizer(model, 16000)

r = sr.Recognizer()

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def listen_vosk():
    print("Using offline recognition (Vosk)...")
    speak("Listening...")
    time.sleep(1)
    print("Listening...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print(text)
            speak(text)
            return text.lower()

def listen_google():
    print("Using online recognition (Google)...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        speak("Listening...")
        audio = r.listen(source,timeout=3,phrase_time_limit=3)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            speak(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def take_command():
    if check_internet():
        return listen_google() 
    else:
        return listen_vosk()    

# take_command()
