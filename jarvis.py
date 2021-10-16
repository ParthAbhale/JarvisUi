import keyboard
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
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
from tasks import *
from featureHI import *

state = "Listening"

def speak(voice = 3 , audio = ""):
    global state
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)
    if voice == 0:
        state = f"Friday: {audio}"
        engine.say(audio)
        print(f"Friday: {audio}")
        engine.runAndWait()
    else:
        state = f"Jarvis: {audio}"
        engine.say(audio)
        print(f"Jarvis: {audio}")
        engine.runAndWait()


try:
    import pywhatkit as kit
except:
    speak(audio="No Internet connection Sir. I Am Going Offline Bye Sir.")
    sys.exit()


def takeCommand():
    global state
    r = sr.Recognizer()
    with sr.Microphone() as source:
        state = "Listening..."
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
        try:
            state = "Recognizing...."
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"User: {command}")
        except Exception as e:
            return "none"
    return command.lower()


def takeCommandInHindi():
    global state
    r = sr.Recognizer()
    with sr.Microphone() as source:
        state = "Listening..."
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
        try:
            state = "Recognizing...."
            print("Recognizing...")
            command = r.recognize_google(audio, language='hi')
            command = Tran_EN(command)
        except Exception as e:
            return "none"
    state = "Speaking..."
    return command.lower()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().strftime("%M"))
    greet = "Good Morning Sir"

    if hour > 0 and hour < 12:
        speak(audio=greet)

    elif hour >= 12 and hour < 16:
        greet = "Good Afternoon Sir"
        speak(audio=greet)

    else:
        greet = "Good Evening Sir"
        speak(audio=greet)
    query = takeCommand()
    if "hello jarvis" in query:
        speak(audio="Hello sir")
    elif "good" in query:
        query = query.replace("jarvis", "")
        query = query.replace("yes", "")
        speak(audio=f"Yes {greet}")
    curr_date = date.today()
    speak(audio=f"Today is {calendar.day_name[curr_date.weekday()]}")
    if hour == 13 or hour > 13:
        hours = (hour) - 12
    if hour <= 12:
        if(hour > 0 and hour < 12):
            speak(audio=f"Its {hour}:{min} AM")
        else:
            speak(audio=f"Its {hour}:{min} PM")
    else:
        if(hour > 0 and hour < 12):
            speak(audio=f"Its {hours}:{min} AM")
        else:
            speak(audio=f"Its {hours}:{min} PM")


def getCurrentWeather(cityname):
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
        speak(audio=f"Current Temperature of our area is { temp_of_area } degree celcius,it looks {description} outside")
        speak(audio = f"Todays maximum temperature will be {high_temp} degree celcius and humidity outside is {humidity}")
    except:
        speak(audio="No weather data available fro today sir...")



class MainThread(QThread):

    def __init__(self):

        super(MainThread, self).__init__()

    def run(self):
        speak(audio ="Allow me to introduce myself. I am Jarvis, the virtual Artificial Intelligence, and I am here to asist you the verity of task as best I can. 24 hours a day and 7 days a week. Collecting all preferences from home interface")
        time.sleep(2)
        speak(audio ="Collected preferences from home interface and now ready and online.")
        wishMe()
        getCurrentWeather("shirdi")
        speak(audio = "How May I help you Sir")
        taskExecution(speak,takeCommand,takeCommandInHindi)

startFunctions = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)

        self.jarvis_ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./img/download.png'))
        self.setWindowTitle("Jarvis AI Asistant - Home")
        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        global state
        self.jarvis_ui.movies_2 = QtGui.QMovie(
            "./img/WebHD_720p-_1_.gif")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunctions.start()

    def showtime(self):
        self.jarvis_ui.label_2.setText(state)
        self.jarvis_ui.label_2.setAlignment(Qt.AlignCenter)


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
sys.exit(Gui_App.exec_())