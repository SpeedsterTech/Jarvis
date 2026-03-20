import requests
import webbrowser 
from functions.online_ops import get_random_advice, get_random_joke, play_on_youtube, search_on_google, search_on_wikipedia
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import functions.os_ops as os
from random import choice
from utils import hello_text
from pprint import pprint
import functions.physics as phys
import functions.math as mth
from functions.timer import timer
import Game as gm
from random import randint
import functions.miscell as mc
from functions.weather import weather

USERNAME = "Speedster"
BOTNAME = "JARVIS"



# Text to Speech Conversion
def speak(text):
    engine = pyttsx3.init()

    # Set Rate
    engine.setProperty('rate', 190)

    # Set Volume
    engine.setProperty('volume', 1)

    # Set Voice (Female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #Used to speak whatever text is passed to it
    engine.say(str(text))
    engine.runAndWait()
    return


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 23):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query and not 'piss off'in query and not 'fuck off' in query:
            speak("")
        else:
            hour = datetime.now().hour
            if hour >= 24 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        query = 'None'
    return query

#greet_user()
def getquery(talk,que=""):
    returnMess=[]
    if talk:
        def speak(text):
            engine = pyttsx3.init()

            # Set Rate
            engine.setProperty('rate', 190)

            # Set Volume
            engine.setProperty('volume', 1)

            # Set Voice (Female)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            #Used to speak whatever text is passed to it
            engine.say(str(text))
            engine.runAndWait()
            return
        query = take_user_input().lower()
        print(query)
    else:
        def speak(text):
            return False
        query = que

    if 'hi jarvis' in query.lower() or 'hello jarvis' in query.lower() or 'hey jarvis' in query.lower():
        x = choice(hello_text)
        speak(x)
        returnMess.append(x)
    if 'open notepad' in query:
        os.open_notepad()

    if 'discord' in query:
        os.open_discord()

    if 'open command prompt' in query or 'open cmd' in query:
        os.open_cmd()
    
    if 'open calculator' in query:
        os.open_calculator()

    if 'wikipedia' in query:
        try:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen.")
            print(results)
            returnMess.append(results)
        except:
            speak("im sorry, i was unable to do you wikipedia search, please try again.")
            returnMess.append("im sorry, i was unable to do you wikipedia search, please try again.")

    if 'youtube' in query:
        speak('What do you want to play on Youtube, sir?')
        video = take_user_input().lower()
        play_on_youtube(video)

    if 'search on google' in query:
        query = mc.getGoogleInfo(query)
        search_on_google(query)

    if 'joke' in query:
        speak(f"Hope you like this one sir")
        joke = get_random_joke()
        returnMess.append(joke)
        speak(joke)
        speak("For your convenience, I am printing it on the screen sir.")
        pprint(joke)

    if "advice" in query:
        speak(f"Here's some advice for you, sir")
        advice = get_random_advice()
        speak(advice)
        speak("For your convenience, I am printing it on the screen sir.")
        pprint(advice)
    if 'open steam' in query:
        os.open_steam()
    if 'what time' in query:
        if datetime.now().hour > 12:
            message = "Its is" + str(datetime.now().hour%12) +": " + str(datetime.now().minute)
        else:
            message = "Its is" + str(datetime.now().hour) +": " + str(datetime.now().minute)
        if datetime.now().hour <12:
            message += " am"
        else:
            message += " pm"
        speak(message)
    if 'open ob' in query:
        os.open_obs()
    if "open music" in query or "drop my needle" in query:
        os.open_music()
    if "it's my birthday" in query:
        speak("happy birthday to you")
        speak("happy birthday to you")
        speak("happy birthday")
        speak("happy birthday")
        speak("happy birthday to you")
        speak("you smell like cheese")
        speak("and look like doo doo")
    if 'open fusion' in query:
        os.open_fusion()
    if 'open aud' in query:
        os.open_audacity()
    if 'open bot' in query:
        os.open_bots()
    if 'recording setup' in query:
        os.open_obs()
        os.open_audacity()
    if 'streaming setup' in query or 'stream setup' in query:
        os.open_obs()
        os.open_bots()
    if 'lb to grams' in query:
        speak("That is" + str(phys.pounds_grams(query)+ " grams"))
    if 'g to pounds' in query:
        speak("That is" + str(phys.grams_pounds(query)) + " pounds")
    if '+' in query or '-' in query or '*' in query or '/' in query:
        speak("The answer is " + mth.math(query))
    if 'play our playlist' in query:
        webbrowser.open("https://open.spotify.com/playlist/53NCsfVXtmmuPEQEVn636z")
    if 'set a timer' in query or "set timer" in query:
        hr = "0"
        min = "0"
        sec = "0"
        lastChecked = 0
        if 'hour' in query:
            for i in range (0, query.index('hour')):
                for n in range(0,10):
                    if query[i] == str(n):
                        hr+= query[i]
                lastChecked= i
        if 'minute' in query:
            for i in range (lastChecked, query.index('minute')):
                for n in range(0,10):
                    if query[i] == str(n):
                        min+= query[i]
                lastChecked= i
        if 'second' in query:
            for i in range(lastChecked, len(query)):
                for n in range(0,10):
                    if query[i] == str(n):
                        sec+= query[i]
        print(hr +":" + min + ":" + sec)
        time = ((int(hr)*60)*60)+(int(min) * 60) + int(sec)
        timer(time)
    if 'pick a game' in query:
            consoles = ["playstation","computer","switch"," "]
            info = gm.getPickInfo(query)
            players = info.properties['people']
            if players ==  " ":
                speak("Im sorry, How many people?")
                players = take_user_input().lower()
                players = mth.word_to_int(players)
            console = int(consoles[info.properties['console']])
            if console == " ":
                speak("sorry i didnt get the console, which console do you want to play on")
                console = take_user_input.lower()
                for i in range(0,len(consoles)-1):
                    if consoles[i] in console:
                        console = consoles[i]
            speak("The game is " + gm.pick(console,int(players)))
    if "heads or tails" in query or "flip a coin" in query:
        i = randint(0,10)
        if i % 2 == 0:
            speak("It is Heads")
        else:
            speak("It is Tails")
    if 'add a game' in query:
        speak("Okay, whats the name of the game?")
        name = take_user_input().lower()
        print(name)
        speak("what console do you play it on?")
        console = take_user_input().lower()
        print(console)
        speak("Nice, what the minimum amount of players?")
        min = take_user_input().lower()
        print(min)
        speak("one more thing, what is the max?")
        max = take_user_input().lower()
        print(max)
        gm.add(name,console,min,max)
        speak("The game has succesfully been added")
    if 'delete a game' in query or 'remove a game' in query:
        speak("which game do you wanna delete")
        string = take_user_input().lower()
        print(string)
        gm.remove(string)
        speak("Game removed")
    if 'magic 8 ball' in query or 'magic 8-ball' in query:
        speak(mc.magic())
    if 'entry' in query:
        speak("Start your entry")
        entry = take_user_input()
        mc.entry(entry)
    if 'calculate thrust' in query:
        info = phys.getThrustInfo()
        velocity = int(info.properties['velocity'])
        if velocity ==  " ":
            speak("Im sorry, what is the velocity?")
            velocity = take_user_input().lower()
            velocity = mth.word_to_int(velocity)
        mass = int(consoles[info.properties['mass']])
        if mass == " ":
            speak("sorry i didnt get the console, which console do you want to play on")
            mass = take_user_input().lower()
            mass = mth.word_to_int(velocity)
        speak("The game is " + phys.cal_thrust(velocity,mass))
    if 'weather' in query:
        x = weather()
        speak(x[1])
        returnMess.append(x[0])
    if talk:
        print("heres the return list:")
        print(returnMess)
    else:
        return returnMess