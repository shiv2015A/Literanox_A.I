import os
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pyjokes
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import webbrowser


import winshell

import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import pywhatkit
import os
os.system('color 01')




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Must Access this to continue.
def main():
    while True:
        speak("Enter Username: ")
        UserName = input ("Enter Username: ")
        speak('Enter Password: ')
        PassWord = input ("Enter Password: ")

        if UserName == 'Computer' and PassWord == 'I.t':
            time.sleep(1)
            speak("Login successful!")
        
            logged()

        else:
            speak("Password did not match!")
def logged():
    time.sleep(1)
    speak("Welcome to Literanox")


    filePath = "E:\\Jarvis A.I\\bg literanox.py"
    os.startfile(filePath)
    exit()


main()

