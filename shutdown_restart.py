# Code Changed, Optimized And Commented By: OZX-OG
#import libraries

import pyttsx3
import speech_recognition as sr
import os
import time

def take_input_voice():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio, language="en")
            print("You say='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
          
    time.sleep(2)
    return Query

def Speak(audio):
    engine_api = pyttsx3.init("sapi5")
    engine_api.say(audio)
    engine_api.runAndWait()

Speak("Do you want to shutdown or restart your computer sir?")
while True:
    voice = take_input_voice()
    if "no" in voice:
        Speak("Thank u sir I will not shut down the computer")
        break
        
    elif "restart" in voice:
        Speak("restarting the computer")
        os.system('shutdown /r /t 0')
        break
        
    elif "shutdown" in voice:
        # Shutting down
        Speak("Shutting the computer")
        os.system("shutdown /s /t 0")
        break
        
    else:
        Speak("Say that again sir")
        continue
