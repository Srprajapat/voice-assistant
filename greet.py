import datetime
from speak import speak

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        print("good morning")
        speak("good morning")
    elif hour >=12 and hour < 16:
        print("good afternoon")
        speak("good afternoon")
    elif hour >=16 and hour <20:
        print("good evening")
        speak("good evening")
    else:
        print("good night")
        speak("good night")

        