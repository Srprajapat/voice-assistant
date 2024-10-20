import requests
from bs4 import BeautifulSoup
from speak import speak
import phrases
import random
import pyjokes
import datetime
import shutil

def temp():
    search = "temperature in jodhpur"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current{search} is {temp}")
    phrase = random.choice(phrases.offer)
    print(phrase)
    speak(phrase)

def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M")    
    speak(f"Sir, the time is {strTime}")
    print(strTime)

def get_joke():
    j= pyjokes.get_joke()
    speak(j)
    print(j)
    phrase = random.choice(phrases.offer)
    print(phrase)
    speak(phrase)   

def get_date():
    strdate = datetime.datetime.now().strftime("%d/%m/%Y")
    speak(f"Sir, the date is {strdate}")
    print(strdate)
    phrase = random.choice(phrases.offer)
    print(phrase)
    speak(phrase)   



# temp()/