import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import calendar

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listennig...')
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

    #elif 'Hey Jarvis' in command:
        #hi=
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') 
        talk('Current time is ' + time)
        print(time)


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
        
    elif 'out' in command:
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
        
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'lets go for a dinner' in command:
        ab=('sorry i have a headache')
        print(ab)
        talk(ab)

    elif 'who is your father' in command:
        ab=('rajnish is my father')
        print(ab)
        talk(ab)

    elif 'who is your mother' in command:
        ab=('yuvaraj s my mother')
        print(ab)
        talk(ab)
        
        
    elif'bye jarvis' in command:
        talk("Turning OFF")
        
    
        
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
    

    
