import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing....")
            data= recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("not understand")
            return ''           
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)  # 0 for the male voice
    
    rate = engine.getProperty('rate')     
    engine.setProperty('rate',150)              #control the speed     
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':
    
    
    if "hello" in sptext().lower()  :  
       speechtx(" hello, I am urmila c1.0  model 2024 how may i help you?") 
       while True:
           data1= sptext().lower()
           if "your name" in data1:
               name="my name is urmila1.o modelc2024"
               speechtx(name)
           elif "old are you" in data1:
               age=" i am 1 year old"
               speechtx(age)  
           elif "time" in data1:
               time=datetime.datetime.now().steftime("%I%M%p")
               speechtx(time)
           elif "youtube" in data1:
               webbrowser.open("www.youtube.com")  
           elif "facebook" in data1:
               webbrowser.open("www.facebook.com")  
           elif "gmail" in data1:
               webbrowser.open("www.gmail.com")  
           elif "youtube" in data1:
               webbrowser.open("www.googlechrome.com")  
               
           elif "joke " in data1:
                joke_1 = pyjokes.get_joke(language="en",category="natural")  
                print(joke_1)
                speechtx(joke_1) 
                  
           elif "play song" in data1:
               add = "D:\songs" 
               listsong = os.listdir(add)
               print(listsong)
               os.startfile(os.path.join(add,listsong[0]))   
               
           elif "exit " in data1:
               speechtx("thankyou have a nice day ahead")
               break
           time.sleep(5)   
                  
    else:
        
      print("thanks")