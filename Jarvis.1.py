import speech_recognition as sr
import webbrowser
import Jarvis_Library
import requests
import time
import win32com.client
import sys

newsapi = ""
weather_api = ""

recognizer = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = -1

def speak(text):
    print(text)  # Debug print
    speaker.Speak(text)
    time.sleep(0.5)

def get_weather(city=None):
    try:
        if not city:
            location = requests.get("https://ipapi.co/json/").json()
            city = location.get("city", "Delhi")

        city = city.strip().title()
        speak(f"Fetching weather for {city}...")

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            temp = round(data["main"]["temp"], 1)
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            speak(f"Today in {city}, it is {desc} with a temperature of {temp} degrees Celsius.")
            speak(f"Humidity is {humidity} percent and wind speed is {wind_speed} meters per second.")
        else:
            speak(f"Sorry, I could not fetch the weather for {city} right now.")
    except Exception as e:
        speak("An error occurred while fetching the weather.")
        print(f"[ERROR] Weather: {e}")


def processCommand(c):
    c = c.lower().strip()
    print(f"Processing command: {c}")

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c:
        webbrowser.open("https://whatsapp.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        link = Jarvis_Library.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I don't have that song in my library.")
    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if not articles:
                    speak("No news found right now.")
                else:
                    speak("Here are the top headlines.")
                    for article in articles[:7]:
                        speak(article['title'])
            else:
                speak("Sorry, I could not fetch the news at the moment.")
        except Exception as e:
            speak("An error occurred while fetching the news.")
            print(f"[ERROR] News: {e}")
    elif any(word in c for word in ["weather", "temperature", "climate", "forecast"]):
        city = None
        for keyword in [" in ", " at ", " for "]:
            if keyword in c:
                city = c.split(keyword, 1)[1].strip()
                break
        get_weather(city)
    elif "stop" in c or "exit" in c or "quit" in c:
        speak("Shutting down. Goodbye sir.")
        sys.exit()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("Sir?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"[ERROR] {e}")

