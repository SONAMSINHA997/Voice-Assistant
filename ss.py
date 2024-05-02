import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import random

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing....")
            data= recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not understand")
            return ''           
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)  # 0 for the male voice
    
    rate = engine.getProperty('rate')     
    engine.setProperty('rate',130)              #control the speed     
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':
    
    
    if "activate" in sptext().lower()  :  
       hour=int(datetime.datetime.now().hour)
       if hour>=0 and hour<=12:
           speechtx("good morning!")
       elif hour>12 and hour<18 :
            speechtx("good afternoon!")
       else:
           speechtx("good evening!")       
       speechtx(" hello, What can I do for you?") 
       while True:
           data1= sptext().lower()
           if "your name" or"tell me about yourself" or "who are you" in data1:
               name="my name is S.S, "
               name1="i am your voice assistant"
               speechtx(name)
               speechtx(name1)
           elif "old are you" or "age" in data1:
               age=" i am 1 year old"
               speechtx(age)  
           elif "thankyou" or "thanks" in data1:
               thanks=" you are welcome"
               speechtx(thanks)  
           elif "what are you doing" in data1:
               doing=" i am making your task easy"
               speechtx(doing)          
           elif "time" in data1:
               time=datetime.datetime.now().strftime("%I%M%p")
               speechtx(time)
           elif "youtube" in data1:
               speechtx("command excepted")
               webbrowser.open("www.youtube.com")  
           elif "facebook" in data1:
               speechtx("command excepted")
               webbrowser.open("www.facebook.com")  
           elif "gmail" in data1:
               webbrowser.open("www.gmail.com")  
           elif "youtube" in data1:
               webbrowser.open("www.googlechrome.com")  
           elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")  
                print(joke_1)
                speechtx(joke_1)   
           elif "song" in data1:
               add = "D:\songs" 
               listsong = os.listdir(add)
               print(listsong)
               randomsong=random.randrange(0,2)
               os.startfile(os.path.join(add,listsong[randomsong]))   
               
           elif "stop" or "go to sleep" in data1:
               speechtx("thankyou, have a nice day ahead")
               break
           #Stime.sleep(5)   
                  
    else:
      speechtx("to activate me, please say activate")  
      print("thanks")