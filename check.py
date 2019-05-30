import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import smtplib

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 5 and hour < 12:
        speak('Good morning boss')

    elif hour >= 12 and hour < 16:
        speak('Good afternoon boss...')

    elif hour >= 16 and hour < 20:
        speak('Good evening boss')

    elif hour >= 20 and hour < 24:
        speak('ready')

    elif hour >= 0 and hour < 5:
        speak('its late night boss...')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening:")
        # r.energy_threshold = 300
        r.pause_threshold = 1
        # r.operation_timeout = 3
        audio = r.listen(source)

    try:
        # print("You said " + r.recognize_google(audio))
        print('in try block')
        text = r.recognize_google(audio)
        print('you said:',text)
        # speak(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return 'none'
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return
    return text

def smallcommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.energy_threshold = 300
        r.pause_threshold = 0.8
        # r.operation_timeout = 3
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return 'none'
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return
    return text

if __name__ == '__main__':
    wish()
    count = 1
    while True:
        if count == 1:
            speak('tell me what to do..')
            count += 1
        else:
            speak('anything else boss??')
        query = takecommand().lower()
        print(query)
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace('wikipedia','')
            print(query)
            # result = wikipedia.search(query,results=5,suggestion=True)
            result = wikipedia.summary(query,sentences=2,auto_suggest=True)
            # print(result)
            print(result)
            speak('i printed it in terminal.. may i read?')
            reply = smallcommands().lower()
            if 'yes' in reply or 'read' in reply:
                speak(result)
                speak('      its all boss!!')
            else:
                speak('see the terminal')

        elif 'open youtube' in query:
            # webbrowser.open('youtube.com')
            speak('what should i search on youtube ?')
            reply = smallcommands().lower()
            print('you searched for '+reply)
            tosearch = reply.replace(' ', '+')
            speak('serching'+reply)
            webbrowser.open('https://www.youtube.com/results?search_query='+tosearch)
            speak('done.. ')

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            # webbrowser.open('https://stackoverflow.com/')
            speak('what should i search in stack overflow?')
            reply = smallcommands().lower()
            tosearch = reply.replace(' ', '+')
            speak('serching'+reply)
            webbrowser.open('https://stackoverflow.com/search?q='+tosearch)
            speak('done.. ')

        elif 'play music' in query or 'music' in query:
            mdir = 'F:\\music'
            songs = os.listdir(mdir)
            print(songs)
            os.startfile(os.path.join(mdir, songs[0]))
            speak('playing music')

        elif 'open ultra search' in query or 'ultra search' in query or 'ultra' in query:
            file = "C:\\Program Files\\JAM Software\\UltraSearch\\UltraSearch.exe"
            os.startfile(file)

        elif 'search' in query:
            query = query.replace('search','')
            webbrowser.open_new(query)
            speak('done.. ')


        elif 'quit' in query or 'shut' in query or 'down' in query or 'fuck' in query or 'close' in query:
            speak('i am shutting down')
            break


        else:
            speak('sorry!! ')
            continue

