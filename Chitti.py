import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said: ",query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Chitti Sir. Please tell me how may I help you") 


if __name__ == "__main__":
    wish()
    while True:
        #query = takeCommand().lower()
        query = "the date"

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            if 'search for' in query:
                query = query.replace("search for","")
            if 'wikipedia' in query:
                query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            print(results)
            speak(results)

        elif 'the date' in query:
            date = datetime.date.today().strftime("%d:%m:%Y")
            speak("Sir,Todays date is "+date)
            
        elif 'search for' in query:
            speak("Searching in google")
            if 'search for' in query:
                query = query.replace("search for","")
            if 'in google' in query:
                query = query.replace("in google","")
            url = "https://www.google.com/search?q={}".format(query)
            webbrowser.open(url)

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("https://www.google.com",new = 1)

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com",new = 1)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir , The time is "+time)

        elif 'who are you' in query:
            speak("Sir , I am a virtual assistant named Chitti , I am developed using python")

        elif 'quit' in query:
            speak("Shutting down! Have a nice day Sir")
            quit()

        elif 'stop' in query:
            speak("Shutting down! Have a nice day Sir")
            quit()

        elif 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("https://www.spotify.com",new = 1)

        elif 'play music' in query:
            speak("Playing music in spotify")
            webbrowser.open("https://www.spotify.com",new = 1)
            

        elif query == "Null":
            speak("Say that again please")

        elif 'Hello' in query:
            speak("Hello Sir")

        else:
            speak("Sorry Sir , Its out of my limits")
