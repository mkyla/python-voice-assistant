#!/usr/bin/env python3
"""
Python Voice Assistant

A simple voice assistant that listens for commands like 'time' and 'weather',
responds using text-to-speech.
"""

import speech_recognition as sr
import pyttsx3
import datetime
import requests
import spacy

# Load spaCy model for basic NLP (optional, can fallback to keywords)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
    nlp = None

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for speech and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, speech service is unavailable.")
        return ""

def get_time():
    """Get current time."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_weather(location="New York"):
    """Get weather using wttr.in (no API key needed)."""
    try:
        response = requests.get(f"https://wttr.in/{location}?format=1")
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Unable to fetch weather."
    except Exception as e:
        return f"Error: {str(e)}"

def process_command(command):
    """Process the recognized command using keywords or spaCy."""
    if nlp:
        doc = nlp(command)
        intents = [token.lemma_ for token in doc if token.pos_ in ['VERB', 'NOUN']]
    else:
        intents = command.split()

    if 'time' in intents or 'what time' in command:
        time_str = get_time()
        speak(f"The current time is {time_str}")
    elif 'weather' in intents or 'what weather' in command:
        weather_str = get_weather()
        speak(f"The weather is {weather_str}")
    else:
        speak("Sorry, I don't know that command.")

def main():
    """Main loop for the voice assistant."""
    speak("Hello, I'm your voice assistant. Say 'time' or 'weather'.")
    while True:
        command = listen()
        if command:
            process_command(command)
        if 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()