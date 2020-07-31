import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis , How may I help You")

def takeCommand():
    '''
    It takes microphone input from user and returns string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis Active.\nPlease Tell what should I do ?")
        r.adjust_for_ambient_noise(source,duration=1)
        #r.pause_threshold = 1
        #r.energy_threshold=500
        audio=r.listen(source)
    try:
        print("Jarvis Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"You said : {query}\n")
    except Exception as e:
        print(e)
        print("Please Repeat")
        return "None"
    return query

def sendEmail(to , content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your password")
    server.sendmail('youremail@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia ..')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query,sentences=2)
            speak ("According to wikipedia ")
            print(results)
            speak (results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open Instagram" in query:
            webbrowser.open("Instagram.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music " in query:
            music_dir = "C:\\Users\\Public\\Music\\Sample Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif "time" in query:
            strTime = datetime.datetime.now().starttime("%h:%m:%s")
            speak("The time is " + strTime)
        elif "open code" in query:
            codepath="F:\\program files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "send email to gunjan" in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send Email ")
        elif "quit" in query:
            exit()


    