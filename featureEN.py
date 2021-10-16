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
from plyer import notification

#Features which jarvis will perform in english

def youtubeauto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Youtube Auto mode activated.Now sir I am listening in background just tell me your order.")
    while True:
        cm = takeCommandForWishing()
        if "pause" in cm:
            keyboard.send('space bar')
            speak(voice = voice,audio = "Video Paused sir")
        elif "skip" in cm:
            keyboard.send('l')
            speak(voice = voice,audio = "Video Skipped sir")
        elif "restart" in cm:
            keyboard.send('0')
            speak(voice = voice,audio = "Video Restarted sir")
        elif "mute" in cm:
            keyboard.send('m')
            speak(voice = voice,audio = "Video Muted sir")
        elif "back" in cm or "rewind" in cm:
            keyboard.send('j')
            speak(voice = voice,audio = "Video rewinded Sir")
        elif "full screen" in cm:
            keyboard.send('f')
            speak(voice = voice,audio = "full screen mode activated sir.")
        elif "cinema mode" in cm:
            keyboard.send('t')
            speak(voice = voice,audio = "Cinema mode activated sir.")

        elif "play" in cm:
            keyboard.send('space bar')
            speak(voice = voice,audio = "Video played sir")

        elif "search" in cm or "different" in cm:
            speak(voice = voice,audio = 
                "Okay sir then which video should I play tell me the name of that video.")
            search = takeCommandForWishing()
            search = search.replace("jarvis play", "")
            search = search.replace("jarvis search", "")
            search = search.replace("friday play", "")
            search = search.replace("friday search", "")
            speak(voice = voice,audio = f"Playing {search}")
            kit.playonyt(search)
            speak(voice = voice,audio = f"Started {search}")

        elif "volume up" in cm:
            send("enter")
            speak(voice = voice,audio = "Ok sir....")
            speak(voice = voice,audio = "By how much should I increase the volume sir.")
            vol = takeCommandForWishing()
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
            speak(voice = voice,audio = f"Sir system volume decreased by{vol}")
            send("enter")

        elif "volume down" in cm:
            send("enter")
            speak(voice = voice,audio = "Ok sir....")
            speak(voice = voice,audio = "By how much should I decrease the volume sir.")
            vol = takeCommandForWishing()
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
            speak(voice = voice,audio = f"Sir system volume decreased by{vol}")
            send("enter")

        elif "mute" in cm and "system" in cm:
            send("m")
            speak(voice = voice,audio = "Muted the system sir.")

        elif "unmute" in cm and "system" in cm:
            send('m')
            speak(voice = voice,audio = "Muted the system sir.")

        elif "escape" in cm or "exit" in cm:
            send('esc')
            cm = cm.replace("jarvis","")
            cm = cm.replace("friday","")
            cm = cm.replace("escape")
            speak(voice = voice,audio = f"escaped {cm}")

        elif "exit" in cm and "youtube mod" in cm:
            speak(voice = voice,audio = "Okay sir!")
            speak(voice = voice,audio = "Should I close youtube?")
            cm = takeCommandForWishing()
            if "yes" in cm:
                speak(voice = voice,audio = "Okay sir!")
                hotkey('ctrl', 'w')
            else:
                speak(voice = voice,audio = 
                    "Exiting the youtube mode you can tell me open youtube to again activate.")
                break

def topNews(speak,voice):
    #Jarvis
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1385e142fe3c42f395697e5172e3877f"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(voice = voice,audio = f"today's {day[i]} news is: {head[i]}")



def getCurrentWeather(cityname,speak,voice):
    #Jarvis
    try:
        apikey = "6648a1a243eb612b204c1e431efad6c8"
        baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
        cityname = cityname
        completeURL = baseUrl + cityname + "&units=metric" + "&appid=" + apikey
        response = requests.get(completeURL)
        data = response.json()
        temp_of_area = data["main"]["temp"]
        description = data["weather"][0]["description"]
        high_temp = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        speak(voice = voice,audio = 
            f"Current Temperature of our area is { temp_of_area } degree celcius,it looks {description} outside")
        speak(voice = voice,audio = 
            f"Todays maximum temperature will be {high_temp} degree celcius and humidity outside is {humidity}")
    except:
        speak(voice = voice,audio = "No weather data available fro today sir...")



def spotifyAuto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Spotify is now automated sir no need to touch the laptop just tell me I will do every thing for you.")
    while True:
        cm = takeCommandForWishing()
        if "next" in cm:
            speak(voice = voice,audio = "Okay sir")
            hotkey("ctrl", 'right')
            speak(voice = voice,audio = "Next song started sir.")
        elif "previous" in cm:
            speak(voice = voice,audio = "Okay sir")
            hotkey("ctrl", 'left')
            speak(voice = voice,audio = "Previou song started sir.")
        elif "pause" in cm:
            time.sleep(1)
            send("space bar")
            speak(voice = voice,audio = "song paused sir.")

        elif "play" in cm or "different" in cm:
            send('space bar')
            speak(voice = voice,audio = "Which song you have to hear sir. Tell me the name of that song.")
            song = takeCommandForWishing()
            song = song.replace("play", "")
            hotkey('ctrl', 'l')
            time.sleep(2)
            search = pyautogui.locateCenterOnScreen('./img/music_search.png')
            pyautogui.moveTo(search)
            pyautogui.click()
            time.sleep(2)
            hotkey('ctrl', 'a')
            time.sleep(1)
            send('backspace')
            pyautogui.write(song)
            time.sleep(4)
            song = pyautogui.locateCenterOnScreen('./img/spo.png')
            pyautogui.moveTo(song)
            pyautogui.click()
            time.sleep(3)
            send('enter')
            speak(voice = voice,audio = "Song changed to your favorite song")

        elif "play" in cm:
            time.sleep(1)
            send("space bar")
            speak(voice = voice,audio = "song played sir.")

        elif "close" in cm and "mode" in cm or "close" in cm and "mod" in cm:
            speak(voice = voice,audio = "Okay sir!")
            speak(voice = voice,audio = "Sir exited the auto music mod.")
            break

        elif "close spotify" in cm:
            speak(voice = voice,audio = "Yes Sir!")
            os.system("TASKKILL /F /im spotify.exe")
            break
        elif "repeat" in cm:
            speak(voice = voice,audio = "Okay sir,Repeating the song!")
            hotkey('ctrl', 'r')
            speak(voice = voice,audio = "Song Repeated sir.")

        elif "volume up" in cm:
            send("enter")
            speak(voice = voice,audio = "Ok sir....")
            speak(voice = voice,audio = "By how much should I increase the volume sir.")
            vol = takeCommandForWishing()
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
            speak(voice = voice,audio = f"Sir system volume increased by{vol}")
            send("enter")

        elif "volume down" in cm:
            send("enter")
            speak(voice = voice,audio = "Ok sir....")
            speak(voice = voice,audio = "By how much should I decrease the volume sir.")
            vol = takeCommandForWishing()
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
            speak(voice = voice,audio = f"Sir system volume decreased by{vol}")
            send("enter")

        elif "mute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak(voice = voice,audio = "Muted the system sir.")

        elif "unmute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak(voice = voice,audio = "Unmuted the system sir.")

        elif "exit" in cm and "Jarvis" or "exit" in cm and "friday" in cm:
            speak(voice = voice,audio = "exiting the auto music mode!")
            speak(voice = voice,audio = "exited the auto music mode!")
            speak(voice = voice,audio = "Anthing else sir.")
            break


def youtubeDownloader(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Okay sir,starting the process of downloading the video")
    time.sleep(2)
    hotkey('ctrl', 'l')
    time.sleep(1)
    hotkey('ctrl', 'a')
    time.sleep(1)
    hotkey('ctrl', 'c')
    value = paste()
    value = value.replace("https://", "")
    link = str(value)

    def download(url):
        tube_url = YouTube(url)

        video = tube_url.streams.filter(progressive=True, file_extension='mp4')
        video = video.get_highest_resolution()
        os.chdir("C:\\")
        path = "D:\\Video"
        if not os.path.exists(path):
            os.makedirs('Video')
        video.download("D:\\Video\\")
    try:
        download(link)
        speak(voice = voice,audio = "Video downloaded sir")
        speak(voice = voice,audio = "You should check it out sir.Should I open that video")
        cm = takeCommandForWishing()
        if "yes" in cm or "ok" in cm:
            speak(voice = voice,audio = "Okay sir!")
            speak(voice = voice,audio = "Anything else")
            os.startfile("D:\\Video\\")
        elif "no" in cm:
            speak(voice = voice,audio = 
                "Okay sir you can check it out later,The video is saved in the D drive and in Video folder.")
    except:
        speak(voice = voice,audio = "Sir you have not opened the youtube first open the youtube and play the video which you have to download.")


def notepadAuto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Okay sir notepad mode activated.")
    speak(voice = voice,audio = "Okay sir start telling")
    while True:
        cm = takeCommandForWishing()
        time.sleep(1)
        if "next line" in cm:
            send('enter')
            speak(voice = voice,audio = "sir switched to next line , continue sir.")
        elif "erase" in cm:
            hotkey('ctrl', 'backspace')
            speak(voice = voice,audio = "the word erased.")

        elif "save this" in cm:
            while True:
                speak(voice = voice,audio = "What should be the name of this file.")
                file_name = takeCommandForWishing()
                if 1:
                    file_name = file_name.replace("jarvis save", "")
                    file_name = file_name.replace("friday save", "")
                    file_name = file_name.replace("file", "")
                    file_name = file_name.replace("name", "")
                    file_name = file_name.replace("by", "")
                hotkey('ctrl', 's')
                if cm != "none":
                    pyautogui.write(file_name)
                    time.sleep(1)
                    send('enter')
                    speak(voice = voice,audio = "file saved sir")
                else:
                    speak(voice = voice,audio = 
                        "Sir you gave me the none content which can't be saved , Repeat again.")
                break
            time.sleep(1)
            speak(voice = voice,audio = "now sir what i should do")
            cm = takeCommandForWishing()
            if "close" in cm:
                speak(voice = voice,audio = "Closing notepad.")
                keyboard.send("alt+F4, space")
                break
            elif "show" in cm:
                send('win')
                time.sleep(1)
                pyautogui.write(f"{file_name}.txt")
                time.sleep(1)
                send('enter')
                speak(voice = voice,audio = "file opened sir")
                speak(voice = voice,audio = "sir now i am exiting the notepad mode")
                break
            else:
                speak(voice = voice,audio = "Sir may i exit the notepad mode")
                cm = takeCommandForWishing()
                if "yes" in cm:
                    speak(voice = voice,audio = "As you wish sir.")
                    break
                elif "no" in cm:
                    speak(voice = voice,audio = "Okay sir , I am in notepad mode you can tell me the work.")
                else:
                    speak(voice = voice,audio = "Exited the notepad mode")
                    break

            if "close notepad" in cm:
                keyboard.send("alt+F4, space")
                speak(voice = voice,audio = "Notepad closed")

        elif "exit" in cm:
            speak(voice = voice,audio = "exiting the auto notepad mode!")
            speak(voice = voice,audio = "exited the auto notepad mode!")
            break

        elif "close" in cm and "notepad" in cm:
            speak(voice = voice,audio = "Okay sir closing the notepad.")
            speak(voice = voice,audio = "Sir should i save this file.")
            while True:
                cm = takeCommandForWishing()
                if "yes" in cm:
                    speak(voice = voice,audio = "What should be the name of this file.")
                    cm = takeCommandForWishing()
                    cm = cm.replace("jarvis", "")
                    cm = cm.replace("friday", "")
                    cm = cm.replace("save", "")
                    cm = cm.replace("file", "")
                    cm = cm.replace("name", "")
                    cm = cm.replace("by", "")
                    hotkey('ctrl', 's')
                    pyautogui.write(cm)
                    time.sleep(1)
                    send('enter')
                    speak(voice = voice,audio = "file saved sir")
                    time.sleep(1)
                    keyboard.send("alt+F4, space")
                    break
                elif "no" in cm:
                    speak(voice = voice,audio = "Okay sir Closing notepad without saving the file.")
                    keyboard.send("alt+F4, space")
                    speak(voice = voice,audio = "Notepad closed sir any other work")
                    break
                else:
                    speak(voice = voice,audio = "Sir give a valid command!")

        elif cm != "none":
            pyautogui.write(cm)

    speak(voice = voice,audio = "Any more work for me sir.")


def chromeAuto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Sir now you can tell me the commands.")
    while True:
        query = takeCommandForWishing()
        if 'new tab' in query:
            press_and_release('ctrl + t')
            speak(voice = voice,audio = "New tab opened!")

        elif 'close tab' in query:
            press_and_release('ctrl + w')
            speak(voice = voice,audio = "tab closed!")

        elif 'new window' in query:
            press_and_release('ctrl + n')
            speak(voice = voice,audio = "New window opened!")

        elif 'history' in query:
            press_and_release('ctrl + h')
            speak(voice = voice,audio = "History opened!")

        elif 'download' in query:
            press_and_release('ctrl + j')
            speak(voice = voice,audio = "Downloads opened!")

        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            speak(voice = voice,audio = "Bookmarked the website sir.!")

            send('enter')

        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
            speak(voice = voice,audio = "Incognito tab opened!")

        elif 'switch' in query:
            tab = query.replace("switch ", "")
            Tab = tab.replace("to", "")
            Tab = tab.replace("number", "")
            Tab = tab.replace("go", "")
            Tab = tab.replace("the", "")
            Tab = tab.replace("jarvis", "")
            Tab = tab.replace("friday", "")
            Tab = tab.replace("tab", "")
            Tab = tab.replace("first", "1")
            Tab = tab.replace("second", "2")
            Tab = tab.replace("third", "3")
            Tab = tab.replace("fourth", "4")
            Tab = tab.replace("fifth", "5")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)
            speak(voice = voice,audio = f"Switched to {num} tab")

        elif "search" in query:
            query = query.replace("friday search", "")
            query = query.replace("jarvis search", "")
            hotkey('ctrl', 'l')
            time.sleep(1)
            pyautogui.write(query)
            time.sleep(1)
            send("enter")
            speak(voice = voice,audio = "Sir work finished!")

        elif "exit" in query and "jarvis" in query or "exit" in query and "friday" in query:
            speak(voice = voice,audio = "exiting the auto chrome mode!")
            speak(voice = voice,audio = "exited the auto chrome mode!")
            speak(voice = voice,audio = "Anthing else sir.")
            break


def My_Location(speak,voice):
    #Jarvis
    speak(voice = voice,audio = "Checking....")
    send_url = "http://api.ipstack.com/check?access_key=5837f62761d7dc6e8ef5ecb37207ee64"
    geo_req = requests.get(send_url)
    data = geo_req.json()
    district = data['city']
    country = data['country_name']
    st = data['region_name']
    speak(voice = voice,audio = 
        f"Sir , You Are Now In {st , country} and you are in {district} district.")


def NasaNews(Date,speak,voice):
    #Jarvis
    speak(voice = voice,audio = "Extracting Data From Nasa . ")
    Api_Key = "Sei23hvo3fNbQgDP89e2xzsaza8foyiTG4J7e2Wi"
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + Api_Key
    Params = {'date': str(Date)}
    r = requests.get(Url, params=Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    speak(voice = voice,audio = f"Title : {Title}")
    speak(voice = voice,audio = f"According To Nasa : {Info}")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def WindiowsAuto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Sir Auto Windows mode activated!")
    speak(voice = voice,audio = "From now you can give me commands")
    while True:
        query = takeCommandForWishing()
        if 'home screen' in query:
            press_and_release('windows + m')
            speak(voice = voice,audio = "Back to home screen!")

        elif 'minimize' in query:
            press_and_release('windows + m')
            speak(voice = voice,audio = "Screen minimized!")

        elif 'close this' in query:
            keyboard.send("alt+F4, space")
            speak(voice = voice,audio = "Sir window closed!")

        elif 'show start' in query:
            send('win')
            speak(voice = voice,audio = "Start menu displayed!")

        elif 'open setting' in query:
            press_and_release('windows + i')
            speak(voice = voice,audio = "Opned setting!")

        elif 'open search' in query:
            press_and_release('windows + s')
            speak(voice = voice,audio = "Search menu opened!")
            speak(voice = voice,audio = "Sir what you have to search tell me I will help you.")
            cm = takeCommandForWishing()
            if "yes" in cm or "okay" in cm or "Okay" in cm:
                speak(voice = voice,audio = "What you have to search.")
            elif "search" in cm or "open" in cm:
                if 1:
                    cm = cm.replace("jarvis","")
                    cm = cm.replace("friday","")
                    cm = cm.replace("search","")
                    cm = cm.replace("open","")
                if cm != "none":
                    pyautogui.write(cm)
            elif "no" in cm:
                speak(voice = voice,audio = "Okay sir!")
            else:
                speak(voice = voice,audio = "Okay sir you gave me the wrong command")

        elif 'screen shot' in query:
            speak(voice = voice,audio = 
                "Please hold the screen for a second sir i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            speak(voice = voice,audio = 
                "Sir I Took the screenshot now tell me the name for the screenshot image to save")
            name = takeCommandForWishing()
            os.chdir("C:\\")
            os.mkdir('Screenshot Images')
            img.save(f"C:\\Screenshot Images\\{name}.png")
            speak(voice = voice,audio = 
                "Sir I am done Saved the screenshot in D drive and Screenshot Images folder")

        elif 'restore windows' in query:
            press_and_release('Windows + Shift + M')
            speak(voice = voice,audio = "Window restored.")

        elif "exit" in query and "jarvis" in query or "exit" in query and "friday" in query:
            speak(voice = voice,audio = "exiting the auto chrome mode!")
            speak(voice = voice,audio = "exited the auto chrome mode!")
            speak(voice = voice,audio = "Anthing else sir.")
            break


def emailAuto(speak,takeCommandForWishing,voice):
    #Jarvis
    speak(voice = voice,audio = "Okay sir.")
    send('win')
    time.sleep(1)
    pyautogui.write("email")
    time.sleep(1)
    send('enter')
    time.sleep(3)
    hotkey('ctrl', 'n')
    while True:
        speak(voice = voice,audio = "sir just pyautogui.write the email adress to whom you want to send email.")
        while True:
            to = takeCommandForWishing()
            if "yes" in to and "wrote" in to:
                speak(voice = voice,audio = "okay sir what is the subject for this email.")
                sub = takeCommandForWishing()
                speak(voice = voice,audio = "Sir whats the message!")
                msg = takeCommandForWishing()
                speak(voice = voice,audio = "Okay sir starting the process")
                if sub != "none":
                    send('tab')
                    time.sleep(0.5)
                    send('tab')
                    time.sleep(0.5)
                    send('tab')
                    time.sleep(2)
                    pyautogui.write(sub)
                else:
                    speak(voice = voice,audio = "Subject is a none content.")
                if msg != "none":
                    send('tab')
                    time.sleep(1)
                    pyautogui.write(msg)
                    while True:
                        speak(voice = voice,audio = "Sir should I send this email!")
                        cm = takeCommandForWishing()
                        if "yes" in cm or "okay" in cm and "send" in cm:
                            speak(voice = voice,audio = "Okay sir!")
                            hotkey('alt', 's')
                            speak(voice = voice,audio = "Email sent!")
                            break
                        elif "no" in cm or "don't" in cm:
                            speak(voice = voice,audio = "Okay sir discarding the email.")
                            dis = pyautogui.locateCenterOnScreen(
                                './img/discard.png')
                            pyautogui.moveTo(dis)
                            pyautogui.click()
                            time.sleep(1)
                            send('tab')
                            time.sleep(1)
                            send('enter')
                            speak(voice = voice,audio = "email discarded succeccfully sir.")
                            break
                        else:
                            speak(voice = voice,audio = "sir give me a valid command.")
                else:
                    speak(voice = voice,audio = "message is a none content.")

            elif "exit" in to and "jarvis" in to or "exit" in to and "friday":
                break
            else:
                speak(voice = voice,audio = "Sir can you repeat")
        speak(voice = voice,audio = "Exiting the auto email mode")
        break


def computer_intelligence(speak,takeCommandForWishing,voice):
    #Jarvis
    try:
        speak(voice = voice,audio = "Okay sir.")
        speak(voice = voice,audio = "tell me your question.")
        cm = takeCommandForWishing()
        cm = cm.replace("jarvis", "")
        cm = cm.replace("friday", "")
        cm = cm.replace("my", "")
        cm = cm.replace("question", "")
        cm = cm.replace("is", "")
        cm = cm.replace("plus", "+")
        cm = cm.replace("minus", "-")
        cm = cm.replace("divide", "/")
        cm = cm.replace("multiply", "*")
        cm = cm.replace("addition", "+")
        cm = cm.replace("subtraction", "-")
        cm = cm.replace("division", "/")
        cm = cm.replace("multiplication", "*")
        cm = cm.replace("add", "+")
        cm = cm.replace("subtract", "-")
        cm = cm.replace("into", "*")
        cm = cm.replace("times", "*")
        cm = cm.replace("equals to", "=")
        cm = cm.replace("equal to", "=")
        client = wolframalpha.Client("5JGW4L-923KXWP52P")
        answer = client.query(cm)
        f = next(answer.results).text
        speak(voice = voice,audio = f"The answer of the given question is {f}")
    except:
        speak(voice = voice,audio = "No answer was found.")

def dif_solver(speak,takeCommandForWishing,voice):
    #Jarvis
    try:
        speak(voice = voice,audio = "tell me your difficulty.")
        cm = takeCommandForWishing()
        cm = cm.replace("jarvis", "")
        cm = cm.replace("friday", "")
        cm = cm.replace("my", "")
        cm = cm.replace("question", "")
        cm = cm.replace("is", "")
        cm = cm.replace("plus", "+")
        cm = cm.replace("minus", "-")
        cm = cm.replace("divide", "/")
        cm = cm.replace("multiply", "*")
        cm = cm.replace("addition", "+")
        cm = cm.replace("subtraction", "-")
        cm = cm.replace("division", "/")
        cm = cm.replace("multiplication", "*")
        cm = cm.replace("add", "+")
        cm = cm.replace("subtract", "-")
        cm = cm.replace("into", "*")
        cm = cm.replace("times", "*")
        cm = cm.replace("equals to", "=")
        cm = cm.replace("equal to", "=")
        client = wolframalpha.Client("5JGW4L-923KXWP52P")
        answer = client.query(cm)
        f = next(answer.results).text
        speak(voice = voice,audio = f"The answer of the given question is {f}")
    except:
        speak(voice = voice,audio = "No answer was found.")


def classAutoMod(link,speak,voice):
    #Jarvis
    speak(voice = voice,audio = "Starting the process of joining the class sir.")
    webbrowser.open(link)
    time.sleep(2)
    join_btn = pyautogui.locateCenterOnScreen('./img/join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(1)
    send('tab')
    time.sleep(1)
    send('tab')
    time.sleep(1)
    send('enter')
    time.sleep(25)
    send('enter')
    hotkey('alt', 'f')
    try:
        mute = pyautogui.locateCenterOnScreen('./img/unmute.png')
        pyautogui.moveTo(mute)
        pyautogui.click()
        speak(voice = voice,audio = "Sir Your class started!")
    except:
        speak(voice = voice,audio = "Sir Your class started!")

def drinkWaters(speak,takeCommandForWishing,voice):
    if datetime.datetime.now().minute % 30 == 0  or datetime.datetime.now().minute == 00:
        notification.notify(
            title = "Sir please drink water",
            message = "Sir now you should drink water from half an hour you have not drink water now you should firstly drink water",
            app_name = "Jarvis AI Asistant",
            app_icon = "./img/glass.ico",
            timeout = 10,
            ticker = "Jarvis AI Asistant",
            toast = False
        )
        speak(voice = voice,audio = "Sir please drink water, from half an hour you have not drink water now you should firstly drink water.")
        while True:
            cm = takeCommandForWishing()
            if "yes" in cm or "okay" in cm or "okay" in cm:
                speak(voice = voice,audio="Thank you sir for listening me in first attempt")
                break
            elif "no" in cm or "not" in cm:
                speak(voice = voice,audio="No sir i will not listen to you now immediately you should drink water. Other wise i will call your mother.")
            elif "drink" in cm and "water" in cm:
                speak(voice = voice,audio="Okay sir!")
                
            else:
                speak(voice = voice,audio="Sir are you drinking water or not?")


def Alarm(speak,takeCommandForWishing,voice,hour,minute):
    if datetime.datetime.now().hour == hour  or datetime.datetime.now().minute == minute:
        notification.notify(
            title = "Sir time to wake up",
            message = "Sir Now you should probably get up sir you have set the alarm for making you getting up so please wake up.",
            app_name = "Jarvis AI Asistant",
            app_icon = "./img/glass.ico",
            timeout = 10,
            ticker = "Jarvis AI Asistant",
            toast = False
        )
        speak(voice = voice,audio = "Sir please wake up, your alrm is ringing.")
        while True:
            cm = takeCommandForWishing()
            if "yes" in cm or "okay" in cm or "okay" in cm:
                speak(voice = voice,audio="Thank you sir for listening me in first attempt")
                break
            elif "no" in cm or "not" in cm:
                speak(voice = voice,audio="No sir i will not listen to you now immediately you should wake up. Other wise i will call your mother.")
            elif "drink" in cm and "water" in cm:
                speak(voice = voice,audio="Okay sir!")
                
            else:
                speak(voice = voice,audio="Sir are you waking up or not?")

