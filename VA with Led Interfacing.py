import pyttsx3  # pip install pyttsx3
import pyaudio
import speech_recognition as sr  # pip install speechRecognition
import pyfirmata
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import cv2
import pywhatkit
import random
from requests import get
import smtplib
from pyfirmata import Arduino,util
from pyfirmata import OUTPUT
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

board = Arduino('COM8')
board.digital[13].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[2].mode = OUTPUT
board.digital[3].mode = OUTPUT
board.digital[4].mode = OUTPUT
board.digital[5].mode = OUTPUT


def whiteled():
    board.digital[2].write(1)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(0)

def greenled():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)

def blueled():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)

def multipleled():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)




board.digital[13].write(0)
board.digital[12].write(0)

# text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, I am Supo. Please tell me how can I help you")


# to convert voice into text
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        whiteled()
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        greenled()
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    x
        speak("Say that again please...")
        blueled()
        time.sleep(3)
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avhcloud722@gmail.com', 'vashwin1999')      #send email from login id
    server.sendmail('avhcloud722@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:

        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            multipleled()
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open notepad' in query:
            multipleled()
            npath = 'C:\\windows\\system32\\notepad.exe'
            os.startfile(npath)
            time.sleep(3)

        elif 'open command prompt' in query:
            multipleled()
            os.system('start cmd')
            time.sleep(3)

        elif 'open camera' in query:
            multipleled()
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
            cap.release()
            cv2.destroyAllWindows()
            time.sleep(3)

        elif 'open youtube' in query:
            multipleled()
            webbrowser.open("youtube.com")
            time.sleep(3)

        elif 'open stackoverflow' in query:
            multipleled()
            webbrowser.open("stackoverflow.com")
            time.sleep(3)

        elif 'open google' in query:
            multipleled()
            speak("sir, what should I search on google")
            print("sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            time.sleep(3)

        elif 'send message' in query:
            multipleled()
            pywhatkit.sendwhatmsg("+7470985249", "this is testing protocol", 3,33)  # write the time after 2mins by looking at a current time
            time.sleep(3)

        elif 'play music' in query:
            multipleled()
            music_dir = 'O:\\Songs\\All songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))
            time.sleep(3)

        elif 'ip address' in query:
            multipleled()
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")
            print(f"your IP Address is {ip}")
            time.sleep(3)

        elif 'the current time' in query:
            multipleled()
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {strTime}")
            time.sleep(3)

        elif 'tell me about yourself' in query:
            multipleled()
            speak(f"Sir,I am supo your voice assistance, the current version is 1.0")
            time.sleep(3)


        elif 'play songs on youtube' in query:
            multipleled()
            pywhatkit.playonyt("ncs songs")
            time.sleep(3)

        elif 'when was built you' in query:
            multipleled()
            speak(f"I was build in latest dangerious situation covid 19 in year 2020")
            time.sleep(3)


        elif 'what is your name' in query:
            multipleled()
            speak(f"I am supo your voice assistance.")
            time.sleep(3)



        elif 'how are you' in query:
            multipleled()
            speak(f"Sir, I am fine, and,,   you")
            time.sleep(3)


        elif 'open code' in query:
            multipleled()
            codePath = "C:\\Users\\ashwin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            time.sleep(3)

        elif 'email to ashwin' in query:
            multipleled()
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "vrgajendra2@gmail.com"           #person whom to send email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")
                time.sleep(3)

        elif 'turn on blue led' in query:
            multipleled()
            board.digital[13].write(1)
            time.sleep(3)
        elif 'turn off blue led' in query:
            multipleled()
            board.digital[13].write(0)
            time.sleep(3)

        elif 'turn on red led' in query:
            multipleled()
            board.digital[12].write(1)
            time.sleep(3)
        elif 'turn off red led' in query:
            multipleled()
            board.digital[12].write(0)
            time.sleep(3)