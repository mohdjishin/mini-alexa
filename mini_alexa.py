import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", " ")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("current time is " + time)
    elif "who" in command:
        person = command.replace("who is ", " ")
        info =wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "are you single" in command:
        talk("no, you are only single in this world")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk("sorry i didn't get you.")

try:
    while True:
        run_alexa()

except UnboundLocalError:
    talk("try again")
    print("try again..")