from logging.config import listen
import speech_recognition as sr
import pyttsx3
import pygame
import time

pygame.mixer.init()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                command = command.replace('hello', '')
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                time.sleep(.9)
    except:
        pass
    return(command)

act_commands = ["play", "joke", "search", "open"]

def run_alexa():
    command = take_command()
    if command not in act_commands:
        print("Error!")
        talk("error! didnt get that! try again!")
    else:
        print("sucess!")
        exit
        
run_alexa()
