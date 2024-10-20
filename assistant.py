import wolframalpha
import pyautogui
import speedtest
import wikipedia
import os
from speak import speak
from listen import take_command
from greet import greetMe
from general import temp, get_joke, get_time,get_date
import phrases
import random
from appweb import openappweb, closeappweb
from searchnow import searchgoogle, searchYoutube


while True:
    command = take_command()
    if command == "" or command == None:
        continue 
    
    if ("wake up" in command or
        "get up" in command or
        "hello assistant" in command or
        "listen up" in command or
        "hey assistant" in command or
        "are you there" in command or
        "activate" in command):
        greetMe()
        get_time()
        phrase = random.choice(phrases.hello)
        print(phrase)
        speak(phrase)

    elif "hello" in command or "hi" in command:
        phrase = random.choice(phrases.hello)
        print(phrase)
        speak(phrase)

    elif "how are you" in command or "how r u" in command:
        print("perfect, boss")
        speak("perfect, boss")

    elif "thank you" in command:
        print("you are welcome")
        speak("you are welcome")
    
    elif "i am fine" in command:
        print("that's great, boss")
        speak("that's great, boss")

    elif "who i am" in command:
        print("If you talk then definitely your human.")
        speak("If you talk then definitely your human.")
 
    elif "who made you" in command or "who created you" in command: 
        print("I have been created by Seetaram.")
        speak("I have been created by Seetaram.")

    elif "why you came to world" in command:
        print("Thanks to Seetaram. further It's a secret")
        speak("Thanks to Seetaram. further It's a secret")

    elif 'is love' in command:
        print("It is 7th sense that destroy all other senses")
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in command:
        print("I am your voice assistant created by Seetaram")
        speak("I am your voice assistant created by Seetaram")

    elif 'reason for you' in command:
        print("I was created as a Minor project by Mister Seetaram.")
        speak("I was created as a Minor project by Mister Seetaram.")

    elif "will you be my gf" in command or "will you be my bf" in command:   
        print("I'm not sure about, may be you should give me some time")
        speak("I'm not sure about, may be you should give me some time")

    elif "i love you" in command or "i love u" in command:
        print("It's hard to understand")
        speak("It's hard to understand")

    elif "the time" in command or "time" in command :
        get_time()
        phrase = random.choice(phrases.offer)
        print(phrase)
        speak(phrase)

    elif ("guess number" in command 
          or "make a guess" in command 
          or "guess a number" in command):
        num = random.randint(1,10)
        print(num)
        speak(f"{num}")


    elif "temperature" in command:
        temp()

    elif "weather" in command:
        temp()

    elif "date" in command:
        get_date()

    elif "joke" in command :
        get_joke()

    elif "google" in command:
        searchgoogle(command)
        phrase = random.choice(phrases.offer)
        print(phrase)
        speak(phrase)        

    elif "youtube" in command:
        searchYoutube(command)
        phrase = random.choice(phrases.offer)
        print(phrase)
        speak(phrase)

    elif "open" in command:
        openappweb(command)
        phrase = random.choice(phrases.offer)
        print(phrase)
        speak(phrase)

    elif "close" in command:
        closeappweb(command)
        phrase = random.choice(phrases.offer)
        print(phrase)
        speak(phrase)
    
    elif "pause" in command:
        pyautogui.press("k")
        print("video paused")
        speak("video paused")

    elif "play" in command:
        pyautogui.press("k")
        print("video played")
        speak("video played")

    elif "mute" in command:
        pyautogui.press("m")
        print("video muted")
        speak("video muted")

    elif "screenshot" in command:
        im = pyautogui.screenshot()
        im.save("ss.jpg")

    elif "click my photo" in command:
        pyautogui.press("super")
        pyautogui.typewrite("camera")
        pyautogui.press("enter")
        pyautogui.sleep(2)
        speak("SMILE")
        pyautogui.press("enter")

    elif "calculate" in command: 
        app_id = "UY86H3-J7EVT2AU8R"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate') 
        command = command.split()[indx + 1:] 
        res = client.query(' '.join(command)) 
        try:
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 
        except:
            print("some error occured")
            speak("some error occured")

    elif "what is" in command :    
        app_id = "UY86H3-J7EVT2AU8R"

        try:
            client = wolframalpha.Client(app_id)
            res = client.query(command)
        
            print (next(res.results).text)
            speak (next(res.results).text)
        except :
            print ("No results")
            speak("no results")

    elif "who is" in command:
        command = command.replace("hey","")
        command = command.replace("who is","")
        command = command.replace("assistant","")
        result = wikipedia.summary(command,3)
        print(result)
        speak(result)

    elif ("internet speed" in command 
          or "net speed" in command 
          or "network speed" in command):
        print("initiating speed test")
        speak("initiating speed test")
        wifi = speedtest.Speedtest()
        wifi.get_best_server()
        print("running speed test")
        speak("running speed test")
        upload =round( wifi.upload()/1048576)
        download = round(wifi.download()/1048576)
        print(f"download speed is {download}")
        speak(f"download speed is {download}")
        print(f"upload speed is {upload}")
        speak(f"upload speed is {upload}")

    elif "shutdown" in command or "shut down" in command:
        print("Are you sure you want to shutdown")
        speak("are you sure you want to shutdown")
        print("yes or no")
        speak("yes or no")
        shutdown = take_command()
        if "yes" in shutdown:
            os.system("shutdown /s /t 3")
            exit()
        
    elif ("exit" in command or "stop" in command or
          "bye" in command or "good bye" in command):
        phrase = random.choice(phrases.bye)
        print(phrase)
        speak(phrase)
        exit()
    
    else:
        phrase = random.choice(phrases.error)
        print(phrase)
        speak(phrase)
        print()