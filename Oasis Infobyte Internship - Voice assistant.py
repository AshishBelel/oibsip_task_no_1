import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
        return ""
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service: {e}")
        return ""

def main():
    speak("Hello, I am your voice assistant. How can I help you today?")
    
    while True:
        query = listen()
        if "hello" in query:
            speak("Hello! How are you?")
        elif "time" in query:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
        elif "date" in query:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {date}")
        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            if search_query:
                url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
                webbrowser.open(url)
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

main()
