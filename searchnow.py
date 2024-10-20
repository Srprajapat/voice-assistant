import wikipedia
import webbrowser
import pywhatkit
from speak import speak 

def searchgoogle(command):
    if "google" in command:
        command = command.replace("google search","")
        command = command.replace("search","")
        command = command.replace("google","")
        print("this is what I found on google")
        speak("This is what I found on google")

        try:
            pywhatkit.search(command)
            result = wikipedia.summary(command,1)
            print(result)
            speak(result)
        
        except:
            print("no speakable output available")
            speak("no speakable output available")


def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("search","")
        query = query.replace("youtube","")
        query = query.replace("play","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

# searchgoogle("search google car culture song")