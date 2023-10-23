import pywhatkit
import datetime
import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
        print(f"user said: {query}")
        
    except Exception as e:
        print("some thing went worng..")
        return "none"
    return query


def whatsap():
            speak("Ok sir, tell me the number")
            
            spoken_number = takeCommand().lower()
            
            print(spoken_number)
            length = len(spoken_number)
            if length != 0:
                speak("what should i message")
                code = "+91"
                number_nospace = spoken_number.replace(" ","")
                numb = code + number_nospace
                print(numb)
                message = takeCommand().lower()     
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                time_what = min + 1
                pywhatkit.sendwhatmsg(numb, message, hour , time_what)
                time.sleep(120)
            else:
                speak("oh there was some problem pls try again late")

if __name__ == "__main__":
   while True:
        
        query = takeCommand().lower()
        
        if "whatsapp" in query:
             whatsap()


