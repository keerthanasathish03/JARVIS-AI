import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
       with sr.Microphone() as source:
          print('listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command = command.lower()
          if 'alexa' in command:
                command = command('replace', '')
                print(command)
    except:
     pass
     return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command .replace('play', '')
        talk(song + 'playing' )
        pywhatkit.playonyt(song)
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open whatsapp' in command:
        talk("Here you go to Whatsapp\n")
        webbrowser.open("web.whatsapp.com")
    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you")
    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'wikipedia' in command:
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, 1)
            talk("According to Wikipedia")
            print(results)
            talk(results)
    elif 'how to' in command:
        howto = command .replace('play', '')
        talk('playing' + howto)
        pywhatkit.playonyt(howto)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again...')

while True:
    run_alexa()