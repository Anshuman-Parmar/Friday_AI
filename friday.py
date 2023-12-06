import pyttsx3  #We have to install it using, pip in install pyttsx3.
import speech_recognition as sr
import datetime   #It is already installed.It will wish according to time that's why we need it.
import wikipedia
import webbrowser  #For "YouTube". 
import os    #For music.
import smtplib   #For sending email.



engine = pyttsx3.init('sapi5')   #"sapi5" is basically an API used by windows to take voices.
voices = engine.getProperty('voices')
#print(voices)   #After "Run" we will see there are two voices one of male and another of female. 
#print(voices[1].id)   #After "print(voices[0].id" and running it we will see it is voice of "David" a male, while "print(voices[1].id" and running it we will see it is voice of "Zira" a female.
engine.setProperty('voice', voices[0].id) 

def speak(audio):  #It is function we will use so that our AI can speak.
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)  #We are using "datetime" that AI will wish us according to time and we typed cast by ".hour".
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am FRIDAY sir, please tell me how can I help you")


def takeCommand():
    #It takes microphone input fron user and returns string outputs.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Computing...")
        r.pause_threshold = 1  #We change this value as if I take gap of 1 sec it doesn't stop.We can change many more options too,by clicking on "pause_threshold" + Ctrl.
        audio = r.listen(source)


    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')  #Here we can use bing,google-cloud,google,etc.And "en-in" is english-india.
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)  #We are commenting it as in console this will show error that we will get and it will not look good.
        print("Say that again please...")
        return "None"
        
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("Sender's email address", "Sender's email password")
    server.sendmail("Sender's email address", to, content)
    server.close()


if __name__ == "__main__":
    #speak("Hello sir!")  Just to check.
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        #Logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "Path to music folder" #Here, we make a music folder that have all music and we git path of it here.
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  
            #Here instead of index[0] we can use "random fun".[0] will play first song while random will play any song in list.

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif "open code" in query:
            codePath = "VS Code path" #Here, we give path of VS Code, so it open on our command.
            os.startfile(codePath)

        elif "email to" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver's email address"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email at the moment")


