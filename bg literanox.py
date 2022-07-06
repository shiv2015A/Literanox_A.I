import speech_recognition as sr
import os
os.system('color 01')







def takeCommand():  
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
    assname =("literanox")
    speak("I am your Assistant")
    speak(assname)








while True:
    wake_Up = takeCommand()

    if 'wake up' in wake_Up:
      os.startfile("E:\\Jarvis A.I\\literanox_code.py")

    else:
        print("nothing...")
