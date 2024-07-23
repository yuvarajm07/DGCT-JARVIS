import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import calendar
import os
import webbrowser
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


webbrowser.open("file:///C:/Users/thama/OneDrive/Desktop/robot.html")

def take_command():
    try:
        with sr.Microphone() as source:
            
            
            
            print('listening...')
            talk("say your command")
            
           
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
                
    except:
       pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "hi" in command or "hey" in command or "wassup" in command or "hello" in command or "hey there" in command or "hello there" in command or "hey jarvis" in command or "hi jarvis" in command or "hello jarvis" in command:
        y = ("Hello, how can I help you")
        print(y)
        talk(y)

    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') 
        talk('Current time is ' + time)
        print(time)

    elif "what is your favourite food" in command:
        ab=("Good internet connection is what i like the most")
        print(ab)
        talk(ab)


    elif "who is most beautiful person" in command:
        ab=("Rajnish is the most beautiful person")
        print(ab)
        talk(ab)

    elif "your favourite colour" in command:
        ab=("My favourite colour is grey")
        print(ab)
        talk(ab)

    elif "who is the secretary of dhirajlal gandhi college of technology" in command:
        ab=("dhirajlal gandhi college of technology secretary is smt. Archana ManojKumar")
        print(ab)
        talk(ab)

    elif "who is the principal of dhirajlal gandhi college of technology" in command:
        ab=("dhirajlal gandhi college of technology principal is doctor A Selvaraj")
        print(ab)
        talk(ab)

    elif "who is the chair man of dhirajlal gandhi college of technology" in command:
        ab=("dhirajlal gandhi college of technology chairman is doctor Manoj Kumar")
        print(ab)
        talk(ab)

    elif "who is the chair man of dgct" in command:
        ab=("dhirajlal gandhi college of technology chairman is doctor Manoj Kumar")
        print(ab)
        talk(ab)
    elif 'who is your developer' in command:
        ab=('Those who are standing in front of you have created me')
        print(ab)
        talk(ab)
        
    elif 'who is your favourite person' in command:
        ab=('my developers Dinesh vikash Rajnish kumar and Yuvaraj are my favourite persons')
        print(ab)
        talk(ab)

    elif 'date' in command:
        now=datetime.datetime.now()
        date_now=datetime.datetime.today()
        week_now=calendar.day_name[date_now.weekday()]
        month_now=now.month
        day_now=now.day

        months= [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
            ]

        ordinals=[
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "13th",
            "14th",
            "15th",
            "16th",
            "17th",
            "18th",
            "19th",
            "20th",
            "21th",
            "22th",
            "23th",
            "24th",
            "25th",
            "26th",
            "27th",
            "28th",
            "29th",
            "30th",
            "31th",
            ]
        i="Today is"
        print("Today is", week_now , months[month_now-1], ordinals[day_now-1])
        talk(i)
        talk(week_now)
        talk(months[month_now-1])
        talk(ordinals[day_now-1])
        
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'what is' in command:
        obj = command.replace('what is', '')
        info = wikipedia.summary(obj, 1)
        print(info)
        talk(info)
        
    elif "let's go out" in command:
        po=("sorry to say but I don't have legs")
        print(po)
        talk(po)
        
    elif 'are you single' in command:
        ab=('sorry, I am having a relationship with wifi')
        print(ab)
        talk(ab)

    elif 'who are you' in command:
        ab=('i am jarvis,your personal voice assistant')
        print(ab)
        talk(ab)

    elif "Do you love me" in command:
        ab=('Everyone loves you')
        print(ab)
        talk(ab)

        
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "let's go for dinner" in command:
        ab=('sorry i have headache')
        print(ab)
        talk(ab)

    

    elif 'open' in command:
        if "chrome" in command:
            ab= ("Opening google chrome")
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        
            print(ab)
            talk(ab)
        
        elif 'word' in command :
            q = ( "Opening microsoft word")
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            print(q)
            talk(q)

        elif 'excel' in command :
            c =("Opening microsoft excel")
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
            print(c)
            talk(c)

        elif 'powerpoint' in command or 'ppt' in command:
            e = ("Opening microsoft powerpoint")
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
            print(e)
            talk(e)

        elif "gmail" in command:
            n = ("Opening gmail")
            webbrowser.open("https://gmail.com/")
            print(n)
            talk(n)

        elif "google map" in command:
            t=("Opening google maps")
            webbrowser.open("https://www.google.com/maps/")
            print(t)
            talk(t)

        elif "youtube" in command:
            r = ("Opening youtube")
            webbrowser.open("https://youtube.com/")
            print(r)
            talk(r)

        elif "amazon" in command:
            r=("Opening amazon")
            webbrowser.open("https://www.amazon.com/")
            print(r)
            talk(r)

        
        elif "flipkart" in command:
            r=("Opening flipkart")
            webbrowser.open("https://www.flipkart.com/")
            print(r)
            talk(r)

        elif "meesho" in command:
            r=("Opening meesho")
            webbrowser.open("https://www.meesho.com/")
            print(r)
            talk(r)

        elif "facebook" in command:
            r=("Opening facebook")
            webbrowser.open("https://www.facebook.com/")
            print(r)
            talk(r)

        elif "instagram" in command:
            r=("Opening instagram")
            webbrowser.open("https://www.instagram.com/")
            print(r)
            talk(r)

        elif "twitter" in command:
            r=("Opening twitter")
            webbrowser.open("https://www.twitter.com/")
            print(r)
            talk(r)

        elif "linkedin" in command:
            r=("Opening linkedin")
            webbrowser.open("https://www.linkedin.com/")
            print(r)
            talk(r)

        elif "camera" in command:
            o=("Opening camera")
            cap = cv2.VideoCapture(0)

            while True:
                success,frame=cap.read()
                print("success",success)
                print("frame", frame)
                if success:
                    cv2.imshow("My video",frame)

                if cv2.waitKey(1) & 0xFF==ord('e'):
                    break

            cap.release()
            cv2.destroyAllWindows()
                
            

    elif "ok bye" in command or "bye" in command:
        talk("Turning OFF")
        exit()
                
    
        
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
    
 
    
    
    
