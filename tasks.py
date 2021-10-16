import speech_recognition as sr
import pyttsx3
import keyboard
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import os
import requests
import json
import random
import pyjokes
import pyautogui
import time
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from pyautogui import click, hotkey, sleep
from keyboard import send, release, press_and_release
from datetime import date
import calendar
import psutil
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from googletrans import Translator, client
from newJarvisUI import Ui_MainWindow
import urllib.request
import wikipedia as googleScrap
from pyautogui import click
from PyDictionary import PyDictionary
from pytube import YouTube
from pyperclip import paste
from datetime import date
import math
import wolframalpha
from PyQt5.QtWidgets import QMainWindow
import pywhatkit as kit
from featureEN import *
from featureHI import *



voice = 3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
kk = engine.setProperty('voice', voices[1].id)

#Task which jarvis can perform in english

def taskExecution(speak,takeCommand,takeCommandInHindi):
        global voice
        voice = 3
        speak(voice = voice,audio = "Jarvis At your servis.")
        
        while True:
            if datetime.datetime.now().minute % 30 == 0 or datetime.datetime.now().minute == 00:
                drinkWaters(speak,takeCommand,voice)
            query = takeCommand()

            if query != "none":

                if "wikipedia" in query:
                    if 1:
                        query = query.replace("jarvis", "")
                        query = query.replace("friday", "")
                    try:
                        speak(voice = voice,audio = "Searching in Wikipedia...")
                        query = query.replace("wikipedia", "")
                        result = wikipedia.summary(query, sentences=2)
                        print(result)
                        speak(voice = voice,audio = "According to Wikipedia")
                        speak(voice = voice,audio = result)
                        speak(voice = voice,audio = "Anymore Work Sir!")
                    except:
                        speak(voice = voice,audio = "No results found")
                        speak(voice = voice,audio = "Anymore Work Sir!")

                elif "start friday" in query or "activate friday" in query or "change to friday" in query or "switch to friday" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    voice = 0
                    speak(voice = voice,audio = "Activated Friday")

                elif "start jarvis" in query or "activate jarvis" in query or "change to jarvis" in query or "switch to jarvis" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    voice = 3
                    speak(voice = voice,audio = "Activated Jarvis")

                elif "download" in query and "this video" in query:
                    youtubeDownloader(speak,takeCommand,voice)

                elif "what is your name" in query:
                    if voice == 0:
                        speak(voice = voice,audio = "My name is Friday!")
                        speak(voice = voice,audio = "Any work sir")
                    else:
                        speak(voice = voice,audio = "My name is Jarvis!")
                        speak(voice = voice,audio = "Any work sir")

                elif "who are you" in query or "introduce yourself" in query:
                    if voice == 0:
                        intro = ["Allow me to introduce myself. I am Friday the virtual Artificial Intelligence, and I am here to asist you the verity of task as best I can. 24 hours a day and 7 days a week",
                                 "I am Friday, made by parth, I am a computer program which is made by parth, I am very inteligent you can ask me anything."]
                        sp = random.choice(intro)
                        speak(voice = voice,audio = sp)
                        speak(voice = voice,audio = "Want to test my inteligence")
                    else:
                        intro = ["Allow me to introduce myself. I am Jarvis, the virtual Artificial Intelligence, and I am here to asist you the verity of task as best I can. 24 hours a day and 7 days a week",
                                 "I am Jarvis,made by parth,I am a computer program which is made by parth,i am very inteligent you can ask me anything."]
                        sp = random.choice(intro)
                        speak(voice = voice,audio = sp)
                        speak(voice = voice,audio = "Want to test my inteligence")

                elif "system" in query and "status" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    cpu_stats = str(psutil.cpu_percent())
                    battery_percent = psutil.sensors_battery().percent
                    memory_in_use = convert_size(psutil.virtual_memory().used)
                    total_memory = convert_size(psutil.virtual_memory().total)
                    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
                    speak(voice = voice,audio = final_res)

                elif "today" in query and "space news" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    Date = date.today()
                    NasaNews(Date,speak,voice)

                elif "start notepad mod" in query or "activate notepad mod" in query:
                    notepadAuto(speak,takeCommand,voice)

                elif "start chrome mod" in query or "activate chrome mod" in query:
                    speak(voice = voice,audio = "Yeah sir auto chrome mod activated!")
                    chromeAuto(speak,takeCommand,voice)

                elif "read this" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    hotkey('ctrl', 'c')
                    time.sleep(1)
                    p = pyperclip.paste()
                    speak(voice = voice,audio = p)

                elif "turn" in query and "on" in query and "bluetooth" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/bluetooth.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak(voice = voice,audio = "Bluetooth turn on!")
                    speak(voice = voice,audio = "Anything else sir")

                elif "turn" in query and "on" in query and "wi-fi" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/wifi.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak(voice = voice,audio = "Wifi turn on!")
                    speak(voice = voice,audio = "Anything else sir")

                elif "turn" in query and "on" in query and "battery saver" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/saver.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak(voice = voice,audio = "Battery Saver turn on!")
                    speak(voice = voice,audio = "Anything else sir")

                elif "turn" in query and "on" in query and "focus" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/yellow.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak(voice = voice,audio = "Battery Saver turn on!")
                    speak(voice = voice,audio = "Anything else sir")

                elif "temperature" in query and "outside" in query:
                    wether = "weather of shirdi"
                    url = f"https://www.google.com/search?q={wether}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(voice = voice,audio = f"current shirdi is {temp}")

                elif "weather" in query and "outside" in query:
                    getCurrentWeather('shirdi',speak,voice)

                elif "start music mod" in query or "activate music mod" in query:
                    speak(voice = voice,audio = "Okay sir.")
                    spotifyAuto(speak,takeCommand,voice)

                elif "open youtube" in query or "youtube" in query:
                    while True:
                        speak(voice = voice,audio = "Sir what should play on YouTube")
                        cm = takeCommand()
                        if 1:
                            cm = cm.replace("jarvis play", "")
                            cm = cm.replace("friday play", "")
                        if "let" in cm and "think" in cm and cm != "play":
                            speak(voice = voice,audio ="Okay sir.")

                        elif cm != "none":
                            speak(voice = voice,audio = f"Playing {cm}")
                            kit.playonyt(cm)
                            speak(voice = voice,audio = f"I played {cm} on youtube! Enjoy it.")
                            youtubeauto(speak,takeCommand,voice)
                        else:
                            speak(voice = voice,audio = 
                                "Sir you gaved me a none content which can't be played on youtube")

                elif "you are" in query and "intelligent" in query:
                    speak(voice = voice,audio = "thank you sir for prasing me.")
                    speak(voice = voice,audio = "Sir you can give me more works to test my intelligence.")

                elif "start youtube mod" in query or "activate youtube mod" in query:
                    youtubeauto(speak,takeCommand,voice)

                elif "play music" in query or "hit some music" in query or "play song" in query or "play songs" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    os.system("TASKKILL /im Spotify.exe")
                    send("win")
                    time.sleep(3)
                    pyautogui.write("spotify")
                    time.sleep(1)
                    send("enter")
                    time.sleep(6)
                    send("space")
                    speak(voice = voice,audio = "Playing music sir, Enjoy it..")
                    spotifyAuto(speak,takeCommand,voice)

                elif "start" in query and "video recording" in query:
                    speak(voice= voice,audio="Okay sir.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("obs")
                    time.sleep(1)
                    send('enter')
                    time.sleep(4)
                    hotkey('ctrl', '3')
                    speak(voice = voice,audio = "Sir video recording started.")

                elif "stop" in query and "video recording" in query:
                    speak(voice= voice,audio="Okay sir.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("obs")
                    time.sleep(1)
                    send('enter')
                    time.sleep(4)
                    hotkey('ctrl', '4')
                    speak(voice = voice,audio = "Sir video recording stopped.")


                elif "close this" in query:
                    speak(voice = voice,audio = "Okay sir..")
                    keyboard.send("alt+F4, space")
                    speak(voice = voice,audio = "Sir i finished your work now you can tell me anything else.")

                elif "are you there" in query:
                    mg = ["Yes sir I am there", "Yes sir Any work for me!", "Sir you called me.", "Sir always there for you.",
                          "Yeah! I am there sir.", "Yes Sir,I am there 24 hours a day and 7 day a week for your work!"]
                    msg = random.choice(mg)
                    speak(voice = voice,audio = msg)

                elif "hey jarvis" in query or "hi jarvis" in query or "hello jarvis" in query:
                    greet = ['hello sir!', 'Yes boss', 'yes sir i am there', "hello sir how are you", 'now you can tell me work sir', "Nice to see you sir!", "It’s nice to see you again sir!",
                             "Good to see you sir!", "Hey! How’s it going sir?", "What’s up sir", "How’s your day going sir?", "Hello sir! What a pleasant surprise!", "Jarvis at your service"]
                    greetings = random.choice(greet)
                    speak(voice = voice,audio = greetings)

                elif "hey friday" in query or "hi friday" in query or "hello friday" in query:
                    greet = ['hello sir!', 'Yes boss', 'yes sir i am there', "hello sir how are you", 'now you can tell me work sir', "Nice to see you sir!", "It’s nice to see you again sir!",
                             "Good to see you sir!", "Hey! How’s it going sir?", "What’s up sir", "How’s your day going sir?", "Hello sir! What a pleasant surprise!"]
                    greetings = random.choice(greet)
                    speak(voice = voice,audio = greetings)

                elif "i want to code" in query or "open vs code" in query:
                    speak(voice = voice,audio = "Okay sir!")
                    time.sleep(1)
                    send('win')
                    time.sleep(1)
                    pyautogui.write("vs code")
                    time.sleep(1)
                    send("enter")
                    speak(voice = voice,audio = "opening Visual Studio Code sir..")
                    speak(voice = voice,audio = "Anything else sir")
                    if "no" in query:
                        while True:
                            query = takeCommand()
                            if "wake up" in query:
                                speak(voice = voice,audio = "Yes Sir Ready and Online")
                                break

                elif "open google" in query or "search on google" in query:
                    if 1:
                        query = query.replace("jarvis search", "")
                        query = query.replace("friday search", "")
                        query = query.replace("", "")
                    if "open google" in query:
                        speak(voice = voice,audio = "What should I search on google?")
                        cm = takeCommand()
                        cm = cm.replace("jarvis search", "")
                        cm = cm.replace("friday search", "")
                        cm = cm.replace("", "")
                        webbrowser.open(
                            f"https://www.google.com/search?q={cm}")
                        speak(voice = voice,audio = "Searching for results...")
                        speak(voice = voice,audio = "Okay now Any order for me sir")
                    else:
                        webbrowser.open(
                            f"https://www.google.com/search?q={query}")
                        speak(voice = voice,audio = "Searching for results...")
                        speak(voice = voice,audio = "Okay now Any order for me sir")

                elif "how are you" in query:
                    chat = ["I am fine sir , How are you", "All good sir,What about you",
                            "Everything fine sir,What your side."]
                    bot = random.choice(chat)
                    speak(voice = voice,audio = bot)
                    while True:
                        cm = takeCommand()
                        if "i am" in cm and "fine" in cm:
                            speak(voice = voice,audio = "Its my pleasure to here this from you!")
                            speak(voice = voice,audio = "So Sir then we shall do Some Work now")
                            break
                        elif "good" in cm:
                            speak(voice = voice,audio = "Ohh! thats good to hear from you")
                            break
                        else:
                            speak(voice = voice,audio = "Okay sir let know me if you need any help.")
                            break
                        speak(voice = voice,audio = "Sir you don't tell me how are you?")
 
                elif "search" in query:
                    if 1:
                        query = query.replace("jarvis search", "")
                        query = query.replace("friday search", "")
                    speak(voice = voice,audio = "Searching for results")
                    if "what" in query or "who" in query:
                        query = query.replace("who", "")
                        query = query.replace("what", "")
                        query = query.replace("is the", "")
                        try:
                            results = googleScrap.summary(query, 3)
                            speak(voice = voice,audio = f"According to google {results}")
                        except:
                            speak(voice = voice,audio = "No speakable data found")
                    elif "how to":
                        max_result = 1
                        how_to_func = search_wikihow(
                            query=query, max_results=max_result)
                        assert len(how_to_func) == 1
                        how_to_func[0].print()
                        speak(voice = voice,audio = how_to_func[0].summary)
                    else:
                        kit.search(query)
                        speak(voice = voice,audio = "Here's the result sir.")

                elif "send" in query and "whatsapp" in query and "message" in query:
                    speak(voice = voice,audio = "Tell the phone number sir")
                    cm = takeCommand()
                    while True:
                        cm = takeCommand()
                        speak(voice = voice,audio = "Sir is this phone number correct {}".format(cm))
                        if "yes" in query or "yup" in query or "yeah" in query:
                            speak(voice = voice,audio="Okay sir")
                            break
                        elif len(cm) < 10:
                            speak(voice = voice,audio="Sir you didn't tell me the correct phone number repeat again.")
                            break
                        elif "no" in query or "nope" in query or "don't" in query:
                            speak(voice = voice,audio="Okay sir again tell me the correct phone number.")
                            while True:
                                speak(voice = voice,audio = "Okay sir,Then what message should I send sir,")
                                cm1 = takeCommand()
                                if 1:
                                    cm1 = cm1.replace("jarvis send", "")
                                    cm1 = cm1.replace("friday send", "")
                                if cm1 != "none":
                                    kit.sendwhatmsg_instantly(
                                        f"+91{cm}", cm1, wait_time=25)
                                    btn = pyautogui.locateCenterOnScreen('./img/whatsapp.png')
                                    pyautogui.moveTo(btn)
                                    pyautogui.click()
                                    speak(voice = voice,audio = "Message sent!")
                                    speak(voice = voice,audio = "Anything else sir")
                                else:
                                    speak(voice = voice,audio = "Sir please repeat again.")
                                break

                elif "the time" in query:
                    hour = int(datetime.datetime.now().hour)
                    min = datetime.datetime.now().strftime("%M")
                    if hour > 0 and hour < 12:
                        result = f"the time is {hour}:{min} AM"
                    elif hour > 12:
                        try:
                            hour = (hour) - 12
                            result = f"the time is {hour}:{min} PM"
                        except:
                            hour = 12
                            result = f"the time is {hour}:{min}"

                    speak(voice = voice,audio = result)
                    speak(voice = voice,audio = "Sir we should now do some work")

                elif "the day" in query:
                    curr_date = date.today()
                    speak(voice = voice,audio = f"Today is {calendar.day_name[curr_date.weekday()]}")

                elif "having" in query and "difficulty" in query:
                    speak(voice = voice,audio = "Okay sir I will help you.")
                    dif_solver(speak,takeCommand,voice)

                elif "stop" in query and "alarm" in query or "shut" in query and "alarm" in query or "close" in query and "alarm" in query:
                    speak(voice = voice,audio = "Offcouse sir.")
                    dismiss = pyautogui.locateCenterOnScreen(
                        './img/alarm_dis.png')
                    pyautogui.moveTo(dismiss)
                    pyautogui.click()
                    speak(voice = voice,audio = "Alarm turned off sir")

                elif "phone" in query and "call" in query:
                    speak(voice = voice,audio = "okay sir.")
                    speak(voice = voice,audio = "tell me the phone number.")
                    cm = takeCommand()
                    speak(voice = voice,audio = "Okay sir wait a second.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("your phone")
                    time.sleep(1)
                    send("enter")
                    time.sleep(6)
                    pyautogui.write(cm)
                    time.sleep(1)
                    call = pyautogui.locateCenterOnScreen('./img/call.png')
                    pyautogui.moveTo(call)
                    pyautogui.click()
                    speak(voice = voice,audio = "Sir phone called made succeccfully.")

                elif "send" in query and "message" in query:
                    speak(voice = voice,audio = "Okay sir")
                    speak(voice = voice,audio = "Tell me the phone number.")
                    no = takeCommand()
                    speak(voice = voice,audio = "Now tell me the message what you want to send.")
                    msg = takeCommand()
                    speak(voice = voice,audio = "okay sir wait a second.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("your phone")
                    time.sleep(1)
                    send('enter')
                    time.sleep(6)
                    make_msg = pyautogui.locateCenterOnScreen('./img/msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    time.sleep(2)
                    make_msg = pyautogui.locateCenterOnScreen(
                        './img/make_msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.write(no)
                    time.sleep(0.5)
                    send('enter')
                    time.sleep(1)
                    make_msg = pyautogui.locateCenterOnScreen(
                        './img/click_msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    pyautogui.write(msg)
                    time.sleep(1)
                    send('enter')
                    time.sleep(1)
                    keyboard.send("alt+F4, space")
                    speak(voice = voice,audio = "The message is send successfully sir.")

                elif "don't" in query or "properly" in query:
                    speak(voice = voice,audio = 
                        "Okay sir I will try my best to diliver you,For Now tell me anthing else")

                elif "what are you doing" in query:
                    speak(voice = voice,audio = "I am in your work boss")

                elif "mute" in query and "system" in query:
                    pyautogui.press('volumemute')
                    speak(voice = voice,audio = "Muted the system sir.")

                elif "unmute" in query and "system" in query:
                    pyautogui.press('volumemute')
                    speak(voice = voice,audio = "Unmuted the system sir.")

                elif "volume up" in query:
                    speak(voice = voice,audio = "Ok sir....")
                    speak(voice = voice,audio = "By how much should I increase the volume sir.")
                    vol = takeCommand()
                    vol = vol.replace("Jarvis", "")
                    vol = vol.replace("jarvis", "")
                    vol = vol.replace("JARVIS", "")
                    vol = vol.replace("by", "")
                    vol = vol.replace("increase", "")
                    vol = vol.replace("volume up", "")
                    vol = vol.replace("volume", "")
                    vol = vol.replace("the", "")
                    vol = str(vol)
                    volume = int(vol)
                    for i in range(volume):
                        pyautogui.keyDown('volumeup')
                        time.sleep(0.1)
                        pyautogui.keyUp('volumeup')
                        time.sleep(0.2)
                    speak(voice = voice,audio = f"Sir system volume increased by {vol}")

                elif "volume down" in query:
                    speak(voice = voice,audio = "Ok sir....")
                    speak(voice = voice,audio = "By how much should I decrease the volume sir.")
                    vol = takeCommand()
                    vol = vol.replace("Jarvis", "")
                    vol = vol.replace("jarvis", "")
                    vol = vol.replace("JARVIS", "")
                    vol = vol.replace("by", "")
                    vol = vol.replace("decrease", "")
                    vol = vol.replace("volume down", "")
                    vol = vol.replace("volume", "")
                    vol = vol.replace("the", "")
                    vol = str(vol)
                    volume = int(vol)
                    for i in range(volume):
                        pyautogui.keyDown('volumedown')
                        time.sleep(0.1)
                        pyautogui.keyUp('volumedown')
                        time.sleep(0.2)
                    speak(voice = voice,audio = f"Sir system volume decreased by{vol}")

                elif"tell me the battery" in query or "what is the battery" in query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(voice = voice,audio = 
                        f"Sir our system has {percentage} percent of battery")
                    if percentage > 70:
                        speak(voice = voice,audio = "Sir we have enough energy to work")
                    elif percentage > 50 and percentage < 70:
                        speak(voice = voice,audio = 
                            "Sir we have enough energy to work but now you should connect to charger.")
                    elif percentage > 30 and percentage < 50:
                        speak(voice = voice,audio = 
                            "Sir we are not having enough energy to work and now you should connect to charger.")
                    elif percentage > 10 and percentage < 30:
                        speak(voice = voice,audio = "Sir we are not having energy at all now you should firstly connect charger.Please sir now you should connect charger or our system will be shutdown.")
                    else:
                        speak(voice = voice,audio = 
                            "Sir no energy to work our system will shutdown at anytime please connect to the charger.")

                elif "tell me joke" in query or "tell me jokes" in query:
                    jokes = pyjokes.get_jokes()
                    speak(voice = voice,audio = "Finding a Good Joke For You")
                    speak(voice = voice,audio = "Got a Joke")
                    speak(voice = voice,audio = jokes)

                elif "tell" in query and "story" in query:
                    class Person:
                        def __init__(self, name, description, moral):
                            self.name = name
                            self.description = description
                            self.moral = moral
                    story1 = Person("The Boy Who Cried Wolf", "The protagonist of this story is a young shepherd boy living in a village. Every day, the boy would take his flock of sheep to graze on a nearby hill. One day, while the sheep were grazing, the boy felt bored and decided to play a prank on the people of his village. Wolf...Wolf he cried out as loud as he could.Listening to his cries for help, the villagers rushed to help. And, when they came close, he began laughing. When the villagers understood that the boy had fooled them, they were very angry. Warning him not to play the prank again, they returned.However, the boy indulged in the mischief again a few days later. This time too, the villagers warned the boy before returning to the village.A few days later, the villagers heard the boy's cries for help once again. And, this time, it was for real. However, the villagers were tired of being laughed at and didn't think that the boy was really in trouble. So, they ignored his cries for help. And, the wolf killed and ate all his sheep.", "People do not believe liars even when they tell the truth. Do not laugh at the  kindness and helpfulness of people, they might not always offer it.")
                    story2 = Person("The Midas Touch", "There was once a king named Midas who loved gold. One day, God appeared before him and asked him to wish for anything.Being greedy about gold, Midas said, Everything I touch should turn to gold. God granted his wish and told him that, from the nextday, everything he touched would turn to gold.Midas was very happy. He woke up early the next morning and went around touching everything and turning them to gold.After a while, Midas felt hungry. He picked up a piece of bread to eat, but it turned to gold. When hpicked up a glass of water to quench his thirst, it turned to gold as well. As Midas was thinking abouwhat to do, his daughter rushed to him. And, when Midas touched her, she turned into a golden statue.Miserable and teary-eyed, Midas no longer wanted the boon. He prayed to God and atoned for his greed.Pleased by Midas' prayer, God asked him to wash hishands in the nearby river to get rid of the goldentouch.Midas returned after washing his hands and found that everything he had changed to gold had turned back to normal.", "People do not believe liars even when they tell the truth. Do not laugh at the  kindness and helpfulness of people, they might not always offer it.")

                    story3 = Person("The Camel and the Baby", "One day, a baby camel was chatting with her mother. She asked, Mother, why do we have humps, round feet, and long eyelashes Drawing a deep breath, the mother explained, Our humps store water. This helps us survive long journeys in a desert where water is scarce. Our round feet allow us to walk comfortably on sand. And, our long eyelashes protect our eyes from dust and sand, especially during sandstorms.The baby camel remained silent for some time and then asked, Mother, why do we stay in a zoo even when we are blessed with so many qualities?", " Your skills and strengths are of no use if you are not in the right place")

                    story4 = Person("The Elephant and Friends", "There was once a lonely elephant. One day, he set out to find friends for himself in the jungle. He found a monkey and asked him if he would be a friend. The monkey refused saying, You can't swing from trees like me. The elephant next met a rabbit and asked him to be his friend. The rabbit refused as well saying, You are too big to enter my burrow. The elephant then met a frog, who also refused, saying, You can't leap like me. The elephant ventured deeper into the jungle where he met a fox. The fox also refused the elephant's friendship saying, You are too big.Disheartened, the elephant returned. However, the next day he decided to go to the jungle again. As he entered the jungle, the elephant found all the animals running to save their lives. He stopped the bear to enquire what had happened.The bear said, The tiger wants to eat us and so we are all running to save ourselves.As the elephant was thinking about what he could do to help the animals, the tiger walked up to him.Mr Tiger, please spare these animals. Do not kill and eat them, the elephant implored.Run or I'll kill and eat you as well, growled the tiger.This angered the elephant and he kicked the tiger. The frightened tiger ran away.All the animals now wanted to be friends with the elephant.", "You can even be friends with those who are different from you.")

                    story5 = Person("The Lion and the Mouse", "Once, a mouse accidentally wakes up a lion. This angers the lion and the mouse begs for his life and promises to pay him back in kind. The lion laughs at this but lets the mouse go. A few days later, the mouse finds the lion trapped in a net and sets the lion free by gnawing on the ropes.",
                                    "No one is too small to help you; everyone has something to offer. And mercy is not a wasted act.")

                    story6 = Person("The Wolf and the Shepherd", "A hungry wolf came across a farm and tried to eat a sheep. However, the farmers chase him away. The wolf came back after a while and saw some of the farmers enjoying roasted lamb. He thought to himself about how if he had done the same, the farmers would have chased him away and even killed him for having killed an innocent lamb.",
                                    "We judge other people for actions that we don't judge ourselves for doing.")

                    all_stories = [story1, story2,
                                   story3, story4, story5, story6]
                    story = random.choice(all_stories)
                    speak(voice = voice,audio = f"The name of the story is {story.name}")
                    speak(voice = voice,audio = story.description)
                    speak(voice = voice,audio = f"The moral of the story is {story.moral}")

                elif "change" in query and "screen" in query:
                    speak(voice = voice,audio = "Switching to the next window sir")
                    pyautogui.keyDown("alt")
                    pyautogui.keyDown("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")
                    speak(voice = voice,audio = "Changed the window sir!Anything more for me")

                elif "set alarm" in query:
                    speak(voice = voice,audio = 
                        "Tell me the time accordingly I ask you sir and yes please tell the time in 24 hours format.")
                    speak(voice = voice,audio = "Okay sir first tell me the hour")
                    hour = takeCommand()
                    speak(voice = voice,audio = "Okay sir now tell me the minute")
                    min = takeCommand()
                    speak(voice = voice,audio = "Okay sir starting the process")
                    send('win')
                    time.sleep(2)
                    pyautogui.write("alarm")
                    time.sleep(1)
                    send("enter")
                    time.sleep(2)
                    alarm = pyautogui.locateCenterOnScreen('./img/alarm.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    time.sleep(2)
                    alarm = pyautogui.locateCenterOnScreen(
                        './img/alarm_add.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.write(hour)
                    time.sleep(1)
                    send("tab")
                    time.sleep(1)
                    pyautogui.write(min)
                    time.sleep(1)
                    alarm = pyautogui.locateCenterOnScreen(
                        './img/alarm_save.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    speak(voice = voice,audio = "Okay sir your alarm is sheduled")

                elif "remember that" in query:
                    query = query.replace("remember that", "")
                    query = query.replace("jarvis", "")
                    query = query.replace("Jarvis", "")
                    query = query.replace("JARVIS", "")
                    speak(voice = voice,audio = 
                        f"Sir you telled me to remember that you will {query}")
                    remember = open('data.txt', 'w')
                    remember.pyautogui.write(query)
                    remember.close()

                elif "do you" in query and "reminder" in query:
                    remember = open('data.txt', 'r')
                    if len(remember.read()) != 0:
                        speak(voice = voice,audio = "Yes sir")
                        file = open('data.txt', 'r')
                        speak(voice = voice,audio = "You tell me to remember" + file.read())
                    else:
                        speak(voice = voice,audio = "No reminders for you sir.You are all up to date")

                elif "open" in query and "website" in query:
                    speak(voice = voice,audio = "tell me the domain of that website.")
                    cm = takeCommand()
                    if "jarvis" in cm or "Jarvis" in cm or "JARVIS" in cm or "website" in cm or "search" in cm or "open" in cm:
                        cm = cm.replace(" ", "")
                        cm = cm.replace("jarvis open", "")
                        cm = cm.replace("jarvis search", "")
                        cm = cm.replace("friday open", "")
                        cm = cm.replace("friday search", "")
                        cm = cm.replace("website", "")
                        cm = cm.replace(".", "")
                        cm = cm.replace(" ", "")
                    url = cm
                    speak(voice = voice,audio = f"Opening {cm} sir")
                    webbrowser.open(url)

                elif "tell" in query and "location" in query:
                    My_Location(speak,voice)

                elif "tell" in query and "news" in query:
                    speak(voice = voice,audio = "Fetching todays news for you sir")
                    topNews(speak,voice)
                    speak(voice = voice,audio = "I am ready sir you can tell work to me now")

                elif "take" in query and "screenshot" in query:
                    speak(voice = voice,audio = 
                        "Please hold the screen for a second sir i am taking screenshot")
                    time.sleep(1)
                    img = pyautogui.screenshot()
                    speak(voice = voice,audio = 
                        "Sir I Took the screenshot now tell me the name for the screenshot image to save")
                    name = takeCommand()
                    path = "C:\\Screenshot Images"
                    if not os.path.exists(path):
                        os.chdir("C:\\")
                        os.mkdir('Screenshot Images')

                    img.save(f"C:\\Screenshot Images\\{name}.png")
                    img.show()
                    speak(voice = voice,audio = 
                        "Sir I am done Saved the screenshot in D drive and Screenshot Images folder")
                    speak(voice = voice,audio = "Anything else sir")

                elif "do" in query and "calculations" in query or "calculation" in query or "calculate" in query:
                    computer_intelligence(speak,takeCommand,voice)
                    speak(voice = voice,audio = "Sir any other work for me")

                elif "weather" in query and "forecast" in query:
                    speak(voice = voice,audio = "Which city's weather forecast you want sir")
                    search = takeCommand()
                    wether = f"weather of {search}"
                    url = f"https://www.google.com/search?q={wether}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(voice = voice,audio = f"current {search} is {temp}")

                elif "i am getting bor" in query or "i am getting bored" in query or "i am bored" in query:
                    speak(voice = voice,audio = "Sir should I play music")
                    cm = takeCommand()
                    if "yes" in cm:
                        speak(voice = voice,audio = "Okay sir")
                        send("win")
                        time.sleep(2)
                        pyautogui.write("spotify")
                        time.sleep(1)
                        send("enter")
                        time.sleep(4)
                        speak(voice = voice,audio = "Would you like to hear this.")
                        send('enter')
                        spotifyAuto(speak,takeCommand,voice)

                    if "no" in cm:
                        speak(voice = voice,audio = "Then what should I do for you sir")

                elif "send mail" in query or "send email" in query or "send gmail" in query:
                    emailAuto(speak,takeCommand,voice)

                elif "join" in query and "science" in query and "class" in query:
                    classAutoMod(
                        "https://us04web.zoom.us/j/73477700587?pwd=Qm1FaFh2T3J6NVB1TzRjTFpTRUhKUT09#success",speak,voice)

                elif "join" in query and "maths" in query and "class" in query:
                    classAutoMod(
                        "https://us04web.zoom.us/j/73477700587?pwd=Qm1FaFh2T3J6NVB1TzRjTFpTRUhKUT09#success",speak,voice)

                elif "what" in query or "who" in query:
                    query = query.replace("jarvis who is", "")
                    query = query.replace("jarvis what is", "")
                    query = query.replace("meant by", "")
                    query = query.replace("mean by", "")
                    speak(voice = voice,audio = "Searching for results...")
                    try:
                        results = googleScrap.summary(query, sentences=3)
                        speak(voice = voice,audio = f"According to google {results}")
                    except:
                        speak(voice = voice,audio = "No speakable data found")

                elif "turn" in query and "language" in query and "hindi":
                    speak(voice = voice,audio = "Okay sir!")
                    taskExecutionInHindi(speak,takeCommand,takeCommandInHindi)

                elif "open" in query:
                    if 1:
                        query = query.replace("jarvis open", "")
                        query = query.replace("friday open", "")
                    send('win')

                    if query != "none":
                        time.sleep(0.5)
                        pyautogui.write(query)
                        time.sleep(0.5)
                        send("enter")
                        speak(voice = voice,audio = f"opening {query} sir..")
                        speak(voice = voice,audio = "Anything else sir")

                elif "how to" in query:
                    max_result = 1
                    how_to_func = search_wikihow(
                        query=query, max_results=max_result)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    speak(voice = voice,audio = how_to_func[0].summary)

                elif "stop" in query or "no thanks" in query or "sleep" in query or "take a break" in query:
                    bye = ["Goodbye sir", "Bye sir", "Bye Bye sir", "See you later sir", "I’m off sir", "See you on soon sir", "Until next time sir",
                           "I gotta go sir", "Catch you later", "Okay,I am happy that you used me now I am going offline,have great day"]
                    bye_r = random.choice(bye)
                    speak(voice = voice,audio = bye_r)
                    while True:
                        drinkWaters(speak,takeCommand,voice)
                        query = takeCommand()
                        if "wake up" in query:
                            speak(voice = voice,audio = "Yes Sir Ready and Online")
                            break

                elif "thanks" in query or "thank you" in query:
                    speak(voice = voice,audio = "No Problem Sir")
                    query = query.replace("thanks", "")
                    speak(voice = voice,audio = "You have any work for me sir")

                elif "ok" in query or "yeah" in query or "yes" in query or "Yeah" in query or "yup" in query:
                    ok = ["Okay sir,Anything else", "Yeah sir,any work for me.",
                          "Yeah!,Sir any order for me.", "Okay fine then tell me sir what should i do for you"]
                    chat = random.choice(ok)
                    speak(voice = voice,audio = chat)

                elif "jarvis" in query or "friday" in query:
                    speak(voice = voice,audio = "Sir did you called me?")
                    if "yes" in query:
                        speak(voice = voice,audio = "Okay sir then for which work did you called me?")

                else:
                    speak(voice = voice,audio = "What do you mean sir.")

#Task which jarvis can perform in hindi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
kk = engine.setProperty('voice', voices[1].id)

def speak(audio):
    global state
    if kk == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM":
        state = f"Friday: {audio}"
        audio = audio.replace(".", ". ")
        engine.say(audio)
        print(f"Friday: {audio}")
        engine.runAndWait()
    else:
        state = f"Jarvis: {audio}"
        engine.say(audio)
        print(f"Jarvis: {audio}")
        engine.runAndWait()

def taskExecutionInHindi(Speak,Takecommand,takeCommandInHindi):
    global kk
    kk = engine.setProperty('voice', voices[1].id)
    speak("हलो सर में आपका हिंदी जार्विस हूँ")
    while True:
        if datetime.datetime.now().minute % 30 == 0 or datetime.datetime.now().minute == 00:
            drinkWaters_hi(speak,takeCommandInHindi)
        query = takeCommandInHindi()
        if query != "none":
            if "wikipedia" in query:
                query = query.replace("jarvis", "")
                query = query.replace("friday", "")
                try:
                        speak("विकिपीडिया में खोजा जा रहा है...")
                        query = query.replace("wikipedia", "")
                        result = wikipedia.summary(query, sentences=2)
                        speak("विकिपीडिया के अनुसार")
                        speak(Tran(result))
                        speak("अब और काम सर!")
                except:
                        speak("No results found")
                        speak("अब और काम सर!")
            
            elif "download" in query and "this video" in query:
                youtubeDownloader_hi(speak,taskExecutionInHindi)
            
            elif "what is your name" in query:
                    if kk == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM":
                        speak("मेरा नाम फ्राइडे है!")
                        speak("कोई काम सर")
                    else:
                        speak("मेरा नाम जार्विस है!")
                        speak("कोई काम सर")

            elif "who are you" in query or "introduce yourself" in query:
                    if kk == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM":
                        intro = ["Allow me to introduce myself I am Friday the virtual Artificial Intelligence and I am here to asist you the verity of task as best I can 24 hours a day and 7 days a week",
                                 "I am Friday made by parth I am a computer program which is made by parth I am very inteligent you can ask me anything"]

                        sp = random.choice(intro)
                        speak(Tran(sp))
                        speak("मेरी बुद्धि का परीक्षण करना चाहते हो")
                    else:
                        intro = ["Allow me to introduce myself I am Jarvis, the virtual Artificial Intelligence and I am here to asist you the verity of task as best I can 24 hours a day and 7 days a week",
                                 "I am Jarvis,made by parth I am a computer program which is made by parth i am very inteligent you can ask me anything"]
                        sp = random.choice(intro)
                        speak(Tran(sp))
                        speak("मेरी बुद्धि का परीक्षण करना चाहते हो")

            elif "system" in query and "status" in query:
                    speak("ठीक है सर ")
                    cpu_stats = str(psutil.cpu_percent())
                    battery_percent = psutil.sensors_battery().percent
                    memory_in_use = convert_size_hi(psutil.virtual_memory().used)
                    total_memory = convert_size_hi(psutil.virtual_memory().total)
                    final_res = f"अभी {cpu_stats} प्रतिशत सीपीयू, {total_memory} कुल में से RAM का {memory_in_use}  उपयोग किया जा रहा है और बैटरी का स्तर {battery_percent} प्रतिशत है"
                    speak(final_res)

            elif "today" in query and "space news" in query:
                    speak("ठीक है सर ")
                    Date = date.today()
                    NasaNews_hi(Date)

            elif "start notepad mode" in query or "activate notepad mode" in query:
                    notepadAuto_hi(speak,takeCommandInHindi,Takecommand)

            elif "start chrome mode" in query or "activate chrome mode" in query:
                    speak("ठीक है सर ऑटो क्रोम मोड  स्टार्ट कर दिया है ")
                    chromeAuto_hi(speak,Takecommand)

            elif "read it" in query or "read this" in query:
                    speak("ठीक है सर!")
                    hotkey('ctrl', 'c')
                    time.sleep(1)
                    p = pyperclip.paste()
                    speak(p)

            elif "temperature" in query and "outside" in query:
                    wether = "weather of shirdi"
                    url = f"https://www.google.com/search?q={wether}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"सर अभी शिरडी मै {temp} डिग्री सेल्सियस टेम्परेचर है ")

            elif "weather" in query and "outside" in query:
                    getCurrentWeather_hi('shirdi',speak)

            elif "start music mode" in query or "activate music mode" in query:
                    speak("Okay sir.")
                    spotifyAuto_hi(speak,takeCommandInHindi,Takecommand)
     
            elif "you are" in query and "intelligent" in query:
                    speak("थैंक यू सर मुझे इंटेलीजेंट बोलने के लिए.")

            elif "start youtube mode" in query or "activate youtube mode" in query:
                    youtubeauto_hi(speak,takeCommandInHindi)

            elif "open youtube" in query or "youtube" in query:
                    while True:
                        speak("सर मे यूट्यूब पे आपके लिए कोनसी वीडियो लगाऊ")
                        cm = takeCommandInHindi()
                        if 1:
                            cm = cm.replace("jarvis play", "")
                            cm = cm.replace("friday play", "")
                        if "let" in cm and "think" in cm and cm != "play":
                            speak("ठीक है सर.")

                        elif cm != "none":
                            speak(f"Playing {cm}")
                            kit.playonyt(cm)
                            speak(f"सर मैंने {cm} लगा दिया है यूट्यूब पे!")
                            youtubeauto_hi(speak,takeCommandInHindi)
                        else:
                            speak("सर अपने मुझे एक नन कमांड दिया है जो यूट्यूब पाई नहीं लगाया जा सकता")

            elif "play" in query and "music" in query or "play" in query or "songs" in query:
                    speak("ठीक है सर!")
                    os.system("TASKKILL /im Spotify.exe")
                    send("win")
                    time.sleep(3)
                    pyautogui.write("spotify")
                    time.sleep(1)
                    send("enter")
                    time.sleep(6)
                    send("space")
                    speak("Playing music sir, Enjoy it..")
                    spotifyAuto_hi(speak,takeCommandInHindi,Takecommand)

            elif "start" in query and "video" in query and "recording" in query:
                    speak("ठीक है सर.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("obs")
                    time.sleep(1)
                    send('enter')
                    time.sleep(4)
                    hotkey('ctrl', '3')
                    speak("सर वीडियो रिकॉर्डिंग चालू करदी है.")

            elif "stop" in query and "video" in query and "recording" in query:
                    speak("ठीक है सर.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("obs")
                    time.sleep(1)
                    send('enter')
                    time.sleep(4)
                    hotkey('ctrl', '4')
                    speak("सर वीडियो रिकॉर्डिंग बंद करदी है.")

            elif "close this" in query:
                    speak("ठीक है सर..")
                    keyboard.send("alt+F4, space")
                    speak("सर मैंने आपका काम पूरा कर लिया है अब आप मुझे कुछ और बता सकते हैं।")

            elif "i want to code" in query or "open vs code" in query:
                    speak("ठीक है सर!")
                    time.sleep(1)
                    send('win')
                    time.sleep(1)
                    pyautogui.write("vs code")
                    time.sleep(1)
                    send("enter")
                    speak("Visual Studio Code ओपन रहा है..")
                    speak("को और काम सर")
                    if "no" in query:
                        while True:
                            query = takeCommandInHindi()
                            if "wake up" in query:
                                speak("हाँ सर तैयार और ऑनलाइन")
                                break

            elif "open google" in query or "search on google" in query:
                    if 1:
                        query = query.replace("jarvis search", "")
                        query = query.replace("friday search", "")
                        query = query.replace("on google", "")
                        query = query.replace("on google", "")
                        query = query.replace("", "")
                    if "open google" in query:
                        speak("सर मै गूगल पे क्या सर्च करू?")
                        cm = takeCommandInHindi()
                        cm = cm.replace("jarvis search", "")
                        cm = cm.replace("friday search", "")
                        cm = cm.replace("", "")
                        webbrowser.open(
                            f"https://www.google.com/search?q={cm}")
                        speak("सर रिजल्ट के लिए सर्चिंग चालू है...")
                        speak("ठीक है सर और कोई आदेश मेरे लिए")
                    else:
                        webbrowser.open(
                            f"https://www.google.com/search?q={query}")
                        speak("सर रिजल्ट के लिए सर्चिंग चालू है..")
                        speak("ठीक है सर और कोई आदेश मेरे लिए")

            elif "search" in query:
                    if 1:
                        query = query.replace("jarvis search", "")
                        query = query.replace("friday search", "")
                    speak("सर रिजल्ट के लिए सर्चिंग चालू है...")
                    if "what" in query or "who" in query:
                        query = query.replace("who", "")
                        query = query.replace("what", "")
                        query = query.replace("is the", "")
                        try:
                            results = googleScrap.summary(query, 3)
                            speak(f"गूगल के अनुसार {results}")
                        except:
                            speak("सर कोई बोला जा सके ऐसा रिजल्ट नहीं मिला")
                    elif "how to":
                        max_result = 1
                        how_to_func = search_wikihow(
                            query=query, max_results=max_result)
                        assert len(how_to_func) == 1
                        how_to_func[0].print()
                        speak(Tran(how_to_func[0].summary))
                    else:
                        kit.search(query)
                        speak("सर हे रहा रिजल्ट.")

            elif "send" in query and "whatsapp" in query and "message" in query:
                    speak("फ़ोन नंबर बताओ सर")
                    cm = takeCommandInHindi()
                    while True:
                        cm = takeCommandInHindi()
                        speak("सर क्या यह फ़ोन नंबर सही है {}".format(cm))
                        if "yes" in query or "yup" in query or "yeah" in query:
                            speak("ठीक है सर")
                            break
                        elif len(cm) < 10:
                            speak("सर आपने मुझे गलत फ़ोन नंबर बताया फिर से सही फ़ोन नंबर बताइये")
                            break
                        elif "no" in query or "nope" in query or "don't" in query:
                            speak("ठीक है सर फिर से सही फोन नंबर बताओ.")
                            while True:
                                speak("ओके सर, तो क्या मेसेज भेजूं")
                                cm1 = takeCommandInHindi()
                                if 1:
                                    cm1 = cm1.replace("jarvis send", "")
                                    cm1 = cm1.replace("friday send", "")
                                if cm1 != "none":
                                    kit.sendwhatmsg_instantly(
                                        f"+91{cm}", cm1, wait_time=25)
                                    btn = pyautogui.locateCenterOnScreen('./img/whatsapp.png')
                                    pyautogui.moveTo(btn)
                                    pyautogui.click()
                                    speak("मैसेज भेज दिया सर!")
                                    speak("और कुछ सर")
                                else:
                                    speak("सर फिरसे बताइये तो जरा.")
                                break

            elif "the time" in query:
                    hour = int(datetime.datetime.now().hour)
                    min = datetime.datetime.now().strftime("%M")
                    if hour > 0 and hour < 12:
                        result = f"सर अभी {hour} भज के {min} minute हो गए"
                    elif hour > 12:
                        try:
                            hour = (hour) - 12
                            result = f"सर अभी {hour} भज के {min} minute हो गए"
                        except:
                            hour = 12
                            result = f"सर अभी {hour} भज के {min} minute हो गए"

                    speak(result)
                    speak("सर अब हमें कुछ काम करना चाहिए")

            elif "the day" in query:
                curr_date = date.today()
                speak(f"आज है {Tran(calendar.day_name[curr_date.weekday()])}")

            elif "having" in query and "difficulty" in query:
                    speak("ठीक है सर में आपकी मदद करता हूँ.")
                    dif_solver_hi(speak,takeCommandInHindi)

            elif "stop" in query and "alarm" in query or "shut" in query and "alarm" in query or "close" in query and "alarm" in query:
                    speak("जरूर सर.")
                    dismiss = pyautogui.locateCenterOnScreen(
                        './img/alarm_dis.png')
                    pyautogui.moveTo(dismiss)
                    pyautogui.click()
                    speak("अलार्म बंद कर दिया है")

            elif "phone" in query and "call" in query:
                    speak("ठीक है सर.")
                    speak("सर मुझे फोन नंबर बताइये.")
                    cm = takeCommandInHindi()
                    speak("ठीके है सर एक मिनट रुकिए.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("your phone")
                    time.sleep(1)
                    send("enter")
                    time.sleep(6)
                    pyautogui.write(cm)
                    time.sleep(1)
                    call = pyautogui.locateCenterOnScreen('./img/call.png')
                    pyautogui.moveTo(call)
                    pyautogui.click()
                    speak("सर फोन कॉल सक्सेस्स्फुल्ली लगा दिया है.")

            elif "send" in query and "message" in query:
                    speak("ठीक है सर")
                    speak("सर मुझे फ़ोन नंबर बताइये.")
                    no = takeCommandInHindi()
                    speak("सर अब मुझे बताइये की आपको क्या मैसेज सेंड करना है.")
                    msg = takeCommandInHindi()
                    speak("सर एक सेकंड.")
                    send('win')
                    time.sleep(1)
                    pyautogui.write("your phone")
                    time.sleep(1)
                    send('enter')
                    time.sleep(6)
                    make_msg = pyautogui.locateCenterOnScreen('./img/msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    time.sleep(2)
                    make_msg = pyautogui.locateCenterOnScreen(
                        './img/make_msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.write(no)
                    time.sleep(0.5)
                    send('enter')
                    time.sleep(1)
                    make_msg = pyautogui.locateCenterOnScreen(
                        './img/click_msg.png')
                    pyautogui.moveTo(make_msg)
                    pyautogui.click()
                    pyautogui.write(msg)
                    time.sleep(1)
                    send('enter')
                    time.sleep(1)
                    keyboard.send("alt+F4, space")
                    speak("सर मैसेज सक्सेसफुली सेंड कर दिया है")

            elif "volume" in query and "increase" in query or "volume" in query and "up" in query:
                send("space")
                speak("ठीक है सर....")
                speak("सर कितना वॉल्यूम बढ़ाऊ.")
                vol = takeCommandInHindi()
                vol = vol.replace("jarvis", "")
                vol = vol.replace("friday", "")
                vol = vol.replace("by", "")
                vol = vol.replace("increase", "")
                vol = vol.replace("volume down", "")
                vol = vol.replace("volume", "")
                vol = vol.replace("the", "")
                vol = str(vol)
                volume = int(vol)
                for i in range(volume):
                    pyautogui.keyDown('volumeup')
                    time.sleep(0.1)
                    pyautogui.keyUp('volumeup')
                    time.sleep(0.2)
                speak(f"सर सिस्टम का वॉल्यूम {vol} बढ़ा दिया.")
                send("space")

            elif "volume" in query and "increase" in query or "volume" in query and "up" in query:
                send("space")
                speak("ठीक है सर....")
                speak("सर कितना वॉल्यूम कम करू.")
                vol = takeCommandInHindi()
                vol = vol.replace("jarvis", "")
                vol = vol.replace("friday", "")
                vol = vol.replace("by", "")
                vol = vol.replace("decrease", "")
                vol = vol.replace("volume down", "")
                vol = vol.replace("volume", "")
                vol = vol.replace("the", "")
                vol = str(vol)
                volume = int(vol)
                for i in range(volume):
                    pyautogui.keyDown('volumedown')
                    time.sleep(0.1)
                    pyautogui.keyUp('volumedown')
                    time.sleep(0.2)
                speak(f"सर सिस्टम का वॉल्यूम {vol} काम कर दिया.")
                send("space")

            elif "mute" in query and "system" in query:
                pyautogui.press('volumemute')
                speak("सिस्टम वॉल्यूम म्यूट कर दिया.")

            elif "unmute" in query and "system" in query:
                pyautogui.press('volumemute')
                speak("सिस्टम वॉल्यूम उन्मुते कर दिया.")

            elif"tell" in query and "battery" in query or "what" in query and "battery" in query:
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(voice = voice,audio = 
                        f"सर अपने सिस्टम की बैटरी {percentage} परसेंट हे")
                    if percentage > 70:
                        speak("सर हमारे पास काम करने के लिए पावर नहीं है")
                    elif percentage > 50 and percentage < 70:
                        speak("सर हमारे पास काम करने के लिए पर्याप्त पावर नहीं है और अब आपको अपने सिस्टम को पहले चार्जर से कनेक्ट करना चाहिए.")
                    elif percentage > 30 and percentage < 50:
                        speak("सर हमारे पास काम करने के लिए पावर नहीं है और आपको अभी अपने लैपटॉप को चार्जर से कनेक्ट करना चाहिए.")
                    elif percentage > 10 and percentage < 30:
                        speak("सर अभी तो हमारे पास बिलकुल भी पावर नहीं है काम करने के लिए अब तो आपको आपने लॅपटॉप को चार्जर से कनेक्ट करना होगा नहीं तो आपका लैपटॉप स्विच ऑफ होजायेगा.")
                    else:
                        speak("सर पावर पूरी तरह से ख़तम हो चुकी है अब आप कुछ मत सोचो और पहले लैपटॉप को चार्जर से कनेक्ट करो नहीं तो लैपटॉप कभीभी स्विच ऑफ हो सक्ता है.")

            elif "tell" in query or "jokes" in query or "tell" in query and "joke" in query:
                    jokes = pyjokes.get_jokes()
                    speak("आपके लिए अच्छा जोक ढूंढ रहा हूँ")
                    speak("मिल गया जोक सर")
                    speak(Tran(jokes))

            elif "change" in query and "screen" in query:
                    speak("सर स्क्रीन स्विच कर रहा हु")
                    pyautogui.keyDown("alt")
                    pyautogui.keyDown("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")
                    speak("सर विंडो स्विच कर दी कोई और काम")

            elif "set" in query and "alarm" in query:
                    speak("सर में अब आपको जैसे जैसे टाइम पूछूंगा आप वैसे मुझे बताओ और हा सर २४ हॉर्स के फॉर्मेट में बताइये.")
                    speak("ठीक है सर अब आप मुझे पहले आर बताइये")
                    hour = takeCommandInHindi()
                    speak("ठीक है सर अब आप मुझे पहले आर मिनट")
                    min = takeCommandInHindi()
                    speak("ठीक है सर अब में अलार्म शेड्यूल करने की प्रोसेस शुरू कर रहा हूँ")
                    send('win')
                    time.sleep(2)
                    pyautogui.write("alarm")
                    time.sleep(1)
                    send("enter")
                    time.sleep(2)
                    alarm = pyautogui.locateCenterOnScreen('./img/alarm.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    time.sleep(2)
                    alarm = pyautogui.locateCenterOnScreen(
                        './img/alarm_add.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.write(hour)
                    time.sleep(1)
                    send("tab")
                    time.sleep(1)
                    pyautogui.write(min)
                    time.sleep(1)
                    alarm = pyautogui.locateCenterOnScreen(
                        './img/alarm_save.png')
                    pyautogui.moveTo(alarm)
                    pyautogui.click()
                    speak("सर अलार्म शेड्यूल कर दिया")

            elif "tell" in query and "location" in query:
                    My_Location_hi(speak)

            elif "open" in query and "website" in query:
                    speak("सर मुझे उस वेबसाइट का डोमेन बताइए.")
                    cm = takeCommandInHindi()
                    if "jarvis" in cm or "Jarvis" in cm or "JARVIS" in cm or "website" in cm or "search" in cm or "open" in cm:
                        cm = cm.replace(" ", "")
                        cm = cm.replace("jarvis open", "")
                        cm = cm.replace("jarvis search", "")
                        cm = cm.replace("friday open", "")
                        cm = cm.replace("friday search", "")
                        cm = cm.replace("website", "")
                        cm = cm.replace(".", "")
                        cm = cm.replace(" ", "")
                    url = cm
                    speak(f"सर {cm} खोल रहा")
                    webbrowser.open(url)

            elif "tell" in query and "news" in query:
                    speak("सर आजके न्यूज़ फेच कर रहा हूँ")
                    topNews(speak)
                    speak("सर अब में रेडी हूँ अब आप मुझे और कुछ काम बता सकते है")

            elif "take" in query and "screenshot" in query:
                    speak("सर स्क्रीन एक सेकंड होल्ड करो में स्क्रीनशॉट ले रहा हूँ")
                    time.sleep(1)
                    img = pyautogui.screenshot()
                    speak("सर मेने स्क्रीनशॉट ले लिया है अब मुझे आप बताइये की में उस फोटो को क्या नाम से सेव करू")
                    name = takeCommandInHindi()
                    path = "D:\\Screenshot Images"
                    if not os.path.exists(path):
                        os.chdir("C:\\")
                        os.mkdir('Screenshot Images')

                    img.save(f"D:\\Screenshot Images\\{name}.png")
                    img.show()
                    speak("सर मेने वो फोटो सेव कर दिया है डी ड्राइव मे और स्क्रीशॉट इमेज नाम के फोल्डर में")
                    speak("और कुछ काम सर")

            elif "do" in query and "calculations" in query or "calculation" in query or "calculate" in query:
                    computer_intelligence_hi(speak,takeCommandInHindi)
                    speak("सर मेरे लिए कुछ और काम")

            elif "weather" in query and "forecast" in query:
                    speak("सर आपको कोनसे सिटी का वेदर फोरकास्ट चाहिए")
                    search = takeCommandInHindi()
                    wether = f"weather of {search}"
                    url = f"https://www.google.com/search?q={wether}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"सर करंट {search} है {temp}")

            elif "i" in query and "bored" in query or "i" in query and "bored" in query:
                    speak("सर में आप के लिए कोई गाना लगाऊ")
                    cm = takeCommandInHindi()
                    if "yes" in cm:
                        speak("ठीक है सर")
                        send("win")
                        time.sleep(2)
                        pyautogui.write("spotify")
                        time.sleep(1)
                        send("enter")
                        time.sleep(4)
                        speak("सर आप ये सुन्ना पसंद करेंगे.")
                        send('enter')
                        spotifyAuto_hi(speak,takeCommandInHindi,Takecommand)

            elif "send mail" in query or "send email" in query or "send gmail" in query:
                    emailAuto_hi(speak,takeCommandInHindi,Takecommand)  

            elif "join" in query and "science" in query and "class" in query:
                    classAutoMod(
                        "https://us04web.zoom.us/j/73477700587?pwd=Qm1FaFh2T3J6NVB1TzRjTFpTRUhKUT09#success",speak)

            elif "join" in query and "maths" in query and "class" in query:
                    classAutoMod(
                        "https://us04web.zoom.us/j/73477700587?pwd=Qm1FaFh2T3J6NVB1TzRjTFpTRUhKUT09#success",speak)

            elif "turn" in query and "on" in query and "bluetooth" in query:
                    speak("ठीक है सर!")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/bluetooth.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak("सर ब्लूटूत चालू कर दिया!")
                    speak("और कुछ काम सर")

            elif "turn" in query and "on" in query and "battery saver" in query:
                    speak("ठीक है सर!")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/saver.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak("सर battery saver चालू कर दिया!")
                    speak("और कुछ काम सर")

            elif "turn" in query and "on" in query and "wi-fi" in query:
                    speak("ठीक है सर!")
                    hotkey("win", "a")
                    time.sleep(2)
                    btn = pyautogui.locateCenterOnScreen('./img/wifi.png')
                    pyautogui.moveTo(btn)
                    pyautogui.click()
                    hotkey("win", "a")
                    speak("सर Wi-Fi चालू कर दिया!")
                    speak("और कुछ काम सर")

            elif "english" in query and "language" in query:
                speak("ठीक है सर!")
                taskExecution(Speak,Takecommand,takeCommandInHindi)

            elif "what" in query or "who" in query:
                    query = query.replace("who", "")
                    query = query.replace("what", "")
                    query = query.replace("is the", "")
                    speak("सर रिजल्ट के लिए सर्चिंग चालू है...")
                    try:
                        results = googleScrap.summary(query, 3)
                        speak(f"गूगल के अनुसार {results}")
                    except:
                        speak("सर कोई बोला जा सके ऐसा रिजल्ट नहीं मिला")

            elif "open" in query:
                    if 1:
                        query = query.replace("jarvis open", "")
                        query = query.replace("friday open", "")
                    send('win')

                    if query != "none":
                        time.sleep(0.5)
                        pyautogui.write(query)
                        time.sleep(0.5)
                        send("enter")
                        speak(f"सर {query} खोल रहा हूँ..")
                        speak("कोई और काम सर ")

            elif "how to" in query:
                    max_result = 1
                    how_to_func = search_wikihow(
                        query=query, max_results=max_result)
                    assert len(how_to_func) == 1
                    how_to_func[0].print()
                    speak(Tran(how_to_func[0].summary))

            elif "stop" in query or "no thanks" in query or "sleep" in query or "take a break" in query:
                    bye = ["Goodbye sir", "Bye sir", "Bye Bye sir", "See you later sir", "I’m off sir", "See you on soon sir", "Until next time sir",
                           "I gotta go sir", "Catch you later", "Okay,I am happy that you used me now I am going offline,have great day"]
                    bye_r = random.choice(bye)
                    speak(Tran(bye_r))
                    while True:
                        if datetime.datetime.now().minute % 30 == 0 or datetime.datetime.now().minute == 00:
                            drinkWaters_hi(speak,takeCommandInHindi)
                        query = takeCommandInHindi()
                        if "wake up" in query:
                            speak("यस सर आप के लिए हाज़िर हूँ")
                            break

            elif "thanks" in query or "thank you" in query:
                    speak("कोई बात नहीं सर")
                    speak("आप के पास मेरे लिए कुछ काम है सर")

            elif "start friday" in query or "activate friday" in query or "change to friday" in query or "switch to friday" in query:
                    speak("ठीक है सर !")
                    kk = engine.setProperty('voice', voices[2].id)
                    speak("हलो बॉस मैं फ्राइडे हूँ")
                    
            elif "start jarvis" in query or "activate jarvis" in query or "change to jarvis" in query or "switch to jarvis" in query:
                    speak("ठीक है सर !")
                    kk = engine.setProperty('voice', voices[1].id)
                    speak("हलो बॉस मैं जार्विस हूँ")

            elif "ok" in query or "yeah" in query or "yes" in query or "Yeah" in query or "yup" in query:
                    ok = ["Okay sir,Anything else", "Yeah sir,any work for me.",
                          "Yeah!,Sir any order for me.", "Okay fine then tell me sir what should i do for you"]
                    chat = random.choice(ok)
                    speak(Tran(chat))

            else:
                speak("आपका क्या मतलब है सर ।")

