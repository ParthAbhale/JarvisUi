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

# Features which jarvis will perform in hindi

def Tran(line):
        print("Tell Me The Line!")
        traslate = Translator()
        result = traslate.translate(line,dest='hi')
        Text = result.text
        print(Text)
        return Text

def Tran_EN(line):
        print("Tell Me The Line!")
        traslate = Translator()
        result = traslate.translate(line,dest='en')
        Text = result.text
        print(Text)
        return Text

def youtubeauto_hi(speak,takeCommandInHindi):
    speak("Youtube Auto मोड सक्रिय हो गया है। अब सर , मैं बैकग्राउंड में सुन रहा हूं, बस मुझे अपना ऑर्डर बताओ।")
    while True:
        cm = takeCommandInHindi()
        if "pause" in cm:
            keyboard.send('space bar')
            speak("वीडियो पॉज कर दिया सर")
        elif "skip" in cm:
            keyboard.send('l')
            speak("वीडियो स्किप कर दिया सर")
        elif "restart" in cm:
            keyboard.send('0')
            speak("वीडियो रीस्टार्ट कर दिया सर")
        elif "mute" in cm:
            keyboard.send('m')
            speak("वीडियो म्यूट कर दिया सर")
        elif "back" in cm or "rewind" in cm:
            keyboard.send('j')
            speak("वीडियो रिवाइंड कर दिया सर")
        elif "full screen" in cm:
            keyboard.send('f')
            speak("फुल स्क्रीन मोड एक्टिवटे कर दिया सर.")
        elif "cinema mode" in cm:
            keyboard.send('t')
            speak("सिनेमा मोड एक्टिवटे कर दिया सर.")

        elif "play" in cm:
            keyboard.send('space bar')
            speak("वीडियो प्ले कर दिया सर")

        elif "search" in cm or "different" in cm:
            speak(
                "ठीक है सर! तो मै कौन सा वीडियो प्ले करू उस का नाम बताओ।")
            search = takeCommandInHindi()
            if 1:
                search = search.replace("jarvis play", "")
                search = search.replace("jarvis search", "")
                search = search.replace("friday play", "")
                search = search.replace("friday search", "")
            speak(f"Playing {search}")
            kit.playonyt(Tran(search))
            speak(f"चालू कर दिया {search}")

        elif "volume up" in cm:
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

        elif "volume down" in cm:
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

        elif "mute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak("सिस्टम वॉल्यूम म्यूट कर दिया.")

        elif "unmute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak("सिस्टम वॉल्यूम उन्मुते कर दिया.")

        elif "escape" in cm or "exit" in cm:
            send('esc')
            cm = cm.replace("jarvis","")
            cm = cm.replace("friday","")
            cm = cm.replace("escape")
            speak(f"{cm} escape कर दिया सर ")

        elif "close" in cm and "youtube" in cm:
            speak("ठीक है सर!")
            speak("कुछ aur kam सर")
            break

        elif "exit" in cm and "youtube mode" in cm:
            speak("ठीक है सर!!")
            speak("सर मै यूट्यूब बंद करू ")
            cm = takeCommandInHindi()
            if "yes" in cm:
                speak("ठीक है सर!!")
                hotkey('ctrl', 'w')
            else:
                speak("अभी मै यूट्यूब मोड बंद कर रहा हूँ आप मुझे फिर यूट्यूब मोड स्टार्ट करो कहकर यूट्यूब मोड फिरसे स्टार्ट कर सकते है")
                break

def getCurrentWeather_hi(cityname,speak):
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
        speak(
            f"सर अपनी सिटी का करंट टेंपरेचर है { temp_of_area } डिग्री सेल्सियस,और बहार {Tran(description)}")
        speak(
            f"आजका अधिक तापमान रहेगा {high_temp} degree celcius और humidity बाहर है {humidity}")
    except:
        speak("सर आजका वेअथेर डाटा नहीं मिला.....")

def topNews_hi(speak):
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1385e142fe3c42f395697e5172e3877f"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"आजकी {Tran(day[i])} news आजकी की: {Tran(head[i])}")

def spotifyAuto_hi(speak,takeCommandInHindi,takeCommand):
    speak("सर स्पॉटीफी अब ऑटोमेटिक कर दिया गया है अब आपको लैपटॉप को हाट लगाने की जरूरत नहीं है.")
    while True:
        cm = takeCommandInHindi()
        if "next" in cm:
            speak("ठीक है सर!")
            hotkey("ctrl", 'right')
            speak("नेक्स्ट गाना लगा दिया है सर.")
        elif "previous" in cm:
            speak("ठीक है सर!")
            hotkey("ctrl", 'left')
            speak("प्रीवियस गाना लगा दिया है सर.")
        elif "pause" in cm:
            time.sleep(1)
            send("space bar")
            speak("सर सॉंग पॉज की दिया है.")

        elif "play" in cm and "different" in cm:
            send('space bar')
            speak("सर आपको कोनसा गाना सुन्ना है उस सॉंग का नाम बताइये.")
            song = takeCommand()
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
            speak("सर अपने बताया हुआ सॉंग लगा दिया हैं.")

        elif "play" in cm:
            time.sleep(1)
            send("space bar")
            speak("सर सॉंग लगा दिया है.")

        elif "close" in cm and "mode" in cm or "close" in cm and "mode" in cm:
            speak("ठीक है सर!!")
            speak("सर ऑटो म्यूजिक मोड बंद कर दिया है.")
            break
        
        elif "close spotify" in cm:
            speak("ठीक है सर!")
            os.system("TASKKILL /F /im spotify.exe")
            break
        elif "repeat" in cm:
            speak("ठीक है सर!,सॉंग रिपीट कर दिया!")
            hotkey('ctrl', 'r')

        elif "volume up" in cm:
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

        elif "volume down" in cm:
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

        elif "mute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak("सिस्टम वॉल्यूम म्यूट कर दिया.")

        elif "unmute" in cm and "system" in cm:
            pyautogui.press('volumemute')
            speak("सिस्टम वॉल्यूम उन्मुते कर दिया.")

        elif "exit" in cm and "Jarvis" or "exit" in cm and "friday" in cm:
            speak("सर ऑटो म्यूजिक मोड एग्जिट कर रहा हूँ!")
            speak("एयर ऑटो म्यूजिक मोड एग्जिट कर दिया है!")
            speak("कोई और काम सर.")
            break

def youtubeDownloader_hi(speak,takeCommandInHindi):
    speak("ठीक है सर, वीडियो डाउनलोड करने की प्रक्रिया शुरू कर रहे हैं")
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
        speak("वीडियो डाउनलोड किया सर")
        speak("आपको इसे देखना चाहिए सर क्या मुझे वह वीडियो खोलना चाहिए")
        cm = takeCommandInHindi()
        if "yes" in cm or "ok" in cm:
            speak("ठीक है सर !")
            speak("और कुछ सर")
            os.startfile("D:\\Video\\")
        elif "no" in cm:
            speak(
                "ठीक है सर आप इसे बाद में देख सकते हैं, वीडियो डी ड्राइव और वीडियो फ़ोल्डर में सहेजा गया है।")
    except:
        speak("सर आपने youtube नहीं खोला है सबसे पहले youtube खोलिये और विडियो को प्ले कीजिये जो आपको डाउनलोड करना है.")

def notepadAuto_hi(speak,takeCommandInHindi,takeCommand):
    speak("ठीक है सर नोटपैड मोड सक्रिय कर दिया गया है")
    speak("ठीक है सर बताना शुरू करो")
    while True:
        cm = takeCommand()
        time.sleep(1)
        if "next line" in cm:
            send('enter')
            speak("सर नेक्स्ट लाइन पर स्विच किया, जारी रखें सर।")
        elif "erase" in cm:
            hotkey('ctrl', 'backspace')
            speak("शब्द मिटा दिया गया है")

        elif "save it" in cm or "save this" in cm:
            while True:
                speak("इस फाइल का नाम क्या होना चाहिए।")
                file_name = takeCommand()
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
                    speak("फाइल सेव करदी सर ")
                else:
                    speak(
                        "सर अपने मुझे खली कंटेंट दिया जो सेव नहीं हो सकता फिरसे मुझे फाइल का नाम बताइये ")
                break

        elif "exit" in cm:
            speak("सर ऑटो नोटपैड मोड़ एग्जिट किया जा रहा है")
            speak("सर ऑटो नोटपैड मोड बंद कर दिया है ")
            break

        elif "close" in cm and "notepad" in cm:
            speak("ठीक है  सर नोटपैड बंद कर रहा हूँ ")
            speak("ठीक है  सर नोटपैड बंद कर रहा हूँ ")
            while True:
                cm = takeCommandInHindi()
                if "yes" in cm:
                    speak("सर मुझे फाइल को किस नाम से सेव करना है वो नाम बताईये")
                    cm = takeCommand()
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
                    speak("सर फाइल सेव कर दी")
                    time.sleep(1)
                    keyboard.send("alt+F4, space")
                    break
                elif "no" in cm:
                    speak("ठीक है  सर नोटपैड बंद कर रहा हूँ बिना फाइल को सेव किये ")
                    keyboard.send("alt+F4, space")
                    speak("सर नोटपैड बंद कर दिया कुछ और काम सर ")
                    break
                else:
                    speak("सर मुझे वैलिड कमांड दो ")

        elif cm != "none":
            pyautogui.write(cm)

    speak("और कुछ काम है मेरे लिए सर")

def chromeAuto_hi(speak,takeCommand):
    speak("सर अब आप मुझे कमांडस देना शुरू कर सकते है")
    while True:
        query = takeCommand()
        if 'new tab' in query:
            press_and_release('ctrl + t')
            speak("न्यू  टॅब खोल दी गयी है!")

        elif 'close tab' in query:
            press_and_release('ctrl + w')
            speak("न्यू टॅब बंद करदी गयी है !")

        elif 'new window' in query:
            press_and_release('ctrl + n')
            speak("सर नई विंडो खोल दी !")

        elif 'history' in query:
            press_and_release('ctrl + h')
            speak("सर हिस्ट्रोरी चालू करदी!")

        elif 'download' in query:
            press_and_release('ctrl + j')
            speak("सर डौन्लोडस चालू करदिए है !")

        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            speak("सर बुकमार्क कर दिया!")

            send('enter')

        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
            speak("इन्कॉग्निटो टॅब चालू कर दी!")

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
            speak(f"स्विच कर दिया {num} टॅब पर")

        elif "search" in query:
            query = query.replace("friday search", "")
            query = query.replace("jarvis search", "")
            hotkey('ctrl','l')
            time.sleep(1)
            pyautogui.write(query)
            time.sleep(1)
            send("enter")
            speak("सर ये लो रिजल्ट्स!")

        elif "exit" in query and "jarvis" in query or "exit" in query and "friday" in query:
            speak("सर ऑटो क्रोम मोड़ एग्जिट किया जा रहा है")
            speak("सर ऑटो क्रोम मोड बंद कर दिया है ")
            speak("कुछ और सर.")
            break

def My_Location_hi(speak):
    speak("Checking....")
    send_url = "http://api.ipstack.com/check?access_key=5837f62761d7dc6e8ef5ecb37207ee64"
    geo_req = requests.get(send_url)
    data = geo_req.json()
    district = data['city']
    country = data['country_name']
    st = data['region_name']
    speak(
        f"सर, आप अभी {st , country} और {district} district मैं है.")

def NasaNews_hi(Date,speak):
    speak("नासा से डेटा निकाला जा रहा है")
    Api_Key = "Sei23hvo3fNbQgDP89e2xzsaza8foyiTG4J7e2Wi"
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + Api_Key
    Params = {'date': str(Date)}
    r = requests.get(Url, params=Params)
    Data = r.json()
    Info = Data['explanation']
    info_hindi = Tran(Info)
    Title = Data['title']
    title_hindi = Tran(Title)
    speak(f"Title है: {title_hindi}")
    speak(f"नासा के अनुसार: {info_hindi}")

def convert_size_hi(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def WindiowsAuto_hi(speak,takeCommandInHindi):
    speak("सर Auto Windows mode activated!")
    speak("From now you can give me commands")
    while True:
        query = takeCommandInHindi()
        if 'home screen' in query:
            press_and_release('windows + m')
            speak("सर आगये होम स्क्रीन पर!")

        elif 'minimize' in query:
            press_and_release('windows + m')
            speak("सर स्क्रीन मिनिमाइज कर दी!")

        elif 'close this' in query:
            keyboard.send("alt+F4, space")
            speak("सर विंडो क्लोज करदी!")

        elif 'show start' in query:
            send('win')
            speak("सर स्टार्ट मेनू स्टार्ट कर दिया!")

        elif 'open setting' in query:
            press_and_release('windows + i')
            speak("सर सिस्टम की सेटिंग खोल दी!")

        elif 'open search' in query:
            press_and_release('windows + s')
            speak("सर सर्च मेनू खोल दिया!")
            speak("सर आपको जो सर्च करना है मुझे बताओ में आपकी मदद कर देता हूँ.")
            cm = takeCommandInHindi()
            if "yes" in cm or "okay" in cm or "Okay" in cm:
                speak("सर आपको क्या सर्च करना है.")
            elif "search" in cm or "open" in cm:
                if 1:
                    cm = cm.replace("jarvis","")
                    cm = cm.replace("friday","")
                    cm = cm.replace("search","")
                    cm = cm.replace("open","")
                if cm != "none":
                    pyautogui.write(cm)
            elif "no" in cm:
                speak("ठीक है सर!!")
            else:
                speak("ठीक है सर! सर आपको क्या सर्च करना है")

        elif 'screen shot' in query:
            speak(
                "सर प्लीज अपनी स्क्रीन को होल्ड करे में स्क्रीनशॉट ले रहा हूँ ")
            time.sleep(3)
            img = pyautogui.screenshot()
            speak(
                "सर मेने स्क्रीनशॉट लेलिया अब आप मुझे बताओ की इस इमेज को में क्या नाम से सेव करू")
            name = takeCommandInHindi()
            os.chdir("C:\\")
            os.mkdir('Screenshot Images')
            img.save(f"C:\\Screenshot Images\\{name}.png")
            speak(
                "सर मेने स्क्रीनशॉट सेव करदिया डी दिवे में और स्क्रीनशॉट इमेज नाम के फोल्डर में")

        elif 'restore windows' in query:
            press_and_release('Windows + Shift + M')
            speak("सर विंडो रिस्टोर कर दी.")

        elif "exit" in query and "jarvis" in query or "exit" in query and "friday" in query:
            speak("सर ऑटो क्रोम मोड एग्जिट कर रहा हूँ!")
            speak("सर ऑटो क्रोम मोड एग्जिट करदिया!")
            speak("कुछ और सर.")
            break

def emailAuto_hi(speak,takeCommandInHindi,takeCommand):
    speak("ठीक है सर!")
    send('win')
    time.sleep(1)
    pyautogui.write("email")
    time.sleep(1)
    send('enter')
    time.sleep(3)
    hotkey('ctrl', 'n')
    while True:
        speak("सर आपको जिसे ईमेल भेजना है उनका ईमेल write किजीए.")
        while True:
            to = takeCommandInHindi()
            if "yes" in to and "wrote" in to:
                speak("ठीक है सर इस ईमेल के लिए सब्जेक्ट बताइये.")
                sub = takeCommand()
                speak("सर मैसेज क्या क्या भेजना है!")
                msg = takeCommand()
                speak("ठीके है सर ईमेल भेजने की प्रक्रिया शुरू कर रहा हु")
                if sub != "none":
                    send('tab')
                    time.sleep(0.5)
                    send('tab')
                    time.sleep(0.5)
                    send('tab')
                    time.sleep(2)
                    pyautogui.write(sub)
                else:
                    speak("सर ईमेल का सब्जेक्ट नन कॉन्टेंट है वो सेंड नहीं किया जा सकता.")
                if msg != "none":
                    send('tab')
                    time.sleep(1)
                    pyautogui.write(msg)
                    while True:
                        speak("सर मे इस ईमेल को भेज दू!")
                        cm = takeCommandInHindi()
                        if "yes" in cm or "okay" in cm and "send" in cm:
                            speak("ठीक है सर!")
                            hotkey('alt', 's')
                            speak("सर ईमेल भेज दिया!")
                            break
                        elif "no" in cm or "don't" in cm:
                            speak("ठीक है सर! ईमेल डिस्कार्ड कर रहा हूँ.")
                            dis = pyautogui.locateCenterOnScreen('./img/discard.png')
                            pyautogui.moveTo(dis)
                            pyautogui.click()
                            time.sleep(1)
                            send('tab')
                            time.sleep(1)
                            send('enter')
                            speak("सर ईमेल सक्सेस्स्फुल्ली डिस्कार्ड कर दिया है.")
                            break
                        else:
                            speak("सर मुझे एक वैलिड कमांड दो .")
                else:
                    speak("सर मैसेज का जो कंटेंट है वो नन है.")

            elif "exit" in to and "jarvis" in to or "exit" in to and "friday":
                break
        speak("ऑटो ईमेल मोड एग्जिट किया जा रहा है")
        break

def computer_intelligence_hi(speak,takeCommandInHindi):
    try:
        speak("ठीक है सर!")
        speak("मुझे आपका क्वेश्चन बताइये")
        cm = takeCommandInHindi()
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
        speak(f"आपने दिए हुए प्रष्ण का उत्तर है {f}")
    except:
        speak("इस प्रष्न का उत्तर नहीं मिला")

def dif_solver_hi(speak,takeCommandInHindi):
    #Jarvis
    try:
        speak("सर मुझे आपकी डिफीकल्टी बताइये.")
        cm = takeCommandInHindi()
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
        speak(f"दिए गए प्रश्न का उत्तर है {f}")
    except:
        speak("आंसर नहीं मिला सर .")


def classAutomode_hi(link,speak):
    speak("सर क्लास ज्वाइन करने की प्रोसेस शुरू कर रहा हूँ")
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
        speak("सर आपकी क्लास शुरू हो गया!")
    except:
        speak("सर आपकी क्लास शुरू हो गया!")


def drinkWaters_hi(speak,takeCommandInHindi):
    if datetime.datetime.now().minute % 30 == 0 or datetime.datetime.now().minute == 00:
        notification.notify(
            title = "sir please drink water",
            message = "sir now you should drink water from half an hour you have not drink water now you should firstly drink water",
            app_icon = "./img/glass.ico",
            timeout = 10
        )
        while True:
            speak("सर आप अब पानी पी लीजिये , आप आधे घंटे से पानी नहीं पिए है अब आप सरे काम छोड़ के पहले पानी पी लीजिये।")
            cm = takeCommandInHindi()
            if "yes" in cm or "okay" in cm or "okay" in cm:
                speak("पहले प्रयास में मुझे सुनने के लिए धन्यवाद सर")
                break
            elif "no" in cm or "not" in cm:
                speak("नहीं सर आपको पानी पीना पड़ेगा।")
            elif "drink" in cm and "water" in cm:
                speak("ठीक है सर!")
                
            else:
                speak("सर आप जल्दी से पानी पी लीजिये नहीं तो मई आपके मम्मी को फ़ोन कर  दूंगा.")


