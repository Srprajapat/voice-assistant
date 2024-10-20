import os 
import webbrowser
import time
import pyautogui
from speak import speak

app = {"command prompt":"cmd","cmd":"cmd","commandprompt":"cmd",
       "paint":"mspaint","word":"winword","excel":"excel",
       "chrome":"chrome","vscode":"code","vs code":"code",
       "powerpoint":"powerpnt","power point":"powerpnt",
       "edge": "msedge","notepad":"notepad","python":"idle"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    
    elif "instagram" in query:
        webbrowser.open("www.instagram.com")

    elif "facebook" in query:
        webbrowser.open("www.facebook.com")

    elif "spotify" in query:
        webbrowser.open("https://open.spotify.com/")

    elif "open" in query:  
        query = query.replace("open","")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(2)
        pyautogui.press("enter")  

    else:
        keys = list(app.keys())
        for app in keys:
            if app in query:
                os.system(f"start {app[app]}")


def closeappweb(query):
    speak("Closing,sir")
    
    if "all tabs" in query:
        pyautogui.hotkey("ctrl", "shift", "w")
        speak("All tabs closed")
    
    elif "tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")

    else:
        keys = list(app.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {app[app]}.exe")
