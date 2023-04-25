import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipediaa
import webbrowser
import os
import smtplib

#this is the voice engine 0 for female and 1 for male.
#ANY ISSUES, PLEASE GET BACK TO ME.
#SOMETIMES YOUR SYSTEM MAY TROUBLE YOU FOR SYSTEM VARIBLES.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', value=170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    print("Heyy! Niharika here :) Please tell me how may I help you ? ") 
    speak("I am your Neehareeka. Please tell me how may I help you")    
      

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dineshsagar66@gmail.com', 'yourpassword')
    server.sendmail('dineshsagar66@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'what is' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("The answer to your question is")
            print(results)
            speak(results)

        elif 'who is' in query:
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("The answer to your question is")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google for you!")
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            speak("Opening netflix")
            webbrowser.open("netflix.com")

        elif 'open amazon' in query:
            speak("Opening amazon")
            webbrowser.open("amazon.in")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Darling, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("What do you want me to draft?")
                content = takeCommand()
                to = "dineshsagar66@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Dinesh. I am not able to send this email")    
        
        elif 'how are you' in query:
                speak("im super awesome as always, by the way thank you for asking")

        elif 'had your dinner' in query:
                speak("No, i wont eat food, i consume power and im full of it to assist you")
        
        elif 'had your lunch' in query:
                speak("No, i wont eat food, i consume Energy and im full of it to assist you")
  
        elif 'had your breakfast' in query:
                speak("No, i wont eat food, i consume power and im full energetic to assist you")
  
        elif 'are you single' in query:
                print("No I'm Sorry my heart is with Dinesh :)")
                speak("NO, im sorry my heart is with dinesh")

        elif 'where do you live' in query:
                print("I stay in your disk, my future goal is to stay in cloud")
                speak("I stay in your disk, my future goal is to stay in cloud")

        elif 'what are you doing' in query:
                speak("All my fans must be knowing it, Im always learning new things")

        elif 'share me the source code' in query:
                print("PROTOCOL SECURITY ERROR: Sorry I'm not supposed to share as I'm an Artificial Intelligence Assistant I can be used for wrong purposes")
                speak("Sorry, im not supposed to share source code or my genetic information as per security protocol, as im an Artificial Intelligence assistant I can be used for wrong purposes")

        elif 'tell me about yourself' in query:
                print("I'm Niharika :) I'm an Artifical Intelligence humanoid virtual assistant developed with Natural Language Processing and I interact with humans, take commands and execute results and I'm trying to work from cloud")
                speak("WELL, im Neehareeka im an artificial intelligence humanoid virtual assistant and i interact with humans take commands and execute results and im trying to work from cloud")   

        elif 'play music' in query:
                music_dir =r'C:\Users\chinni\Downloads\Extra\Setup'
                songs = os.listdir(music_dir)
                print("Playing awesome songs for you")  
                speak("Playing songs for you")  
                os.startfile(os.path.join(music_dir, songs[0]))    

        elif 'who are you' in query:
            print("I'm Niharika :) I'm an Artifical Intelligence humanoid virtual assistant developed with Natural Language Processing and I interact with humans, take commands and execute results and I'm trying to work from cloud")
            speak("WELL, im Neehareekha im an artificial intelligence humanoid virtual assistant and i interact with humans take commands and execute results and im trying to work from cloud")


        elif 'bye' in query:
            print("Okay bye:) I hope you had good time talking to me, see you later")
            speak("Okay bye I hope you had good time talking to me, see you later")
            r.stop()
                
