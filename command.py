import webbrowser
import os
import random
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import wikipedia
import datetime
import speech_recognition as sr
import psutil
from assistant import Assistant  # Add this import at the top of the file
import pytz
from newsapi import NewsApiClient

assistant = Assistant()  # Create an instance of the Assistant class

# Add these constants at the top of the file
OPENWEATHER_API_KEY = "your_openweather_api_key"
NEWS_API_KEY = "your_newsapi_key"

def execute_command(query, assistant):
    if 'search on youtube' in query:
        query = query.replace("search on youtube", "")
        webbrowser.open(f"www.youtube.com/results?search_query={query}")
    elif 'open youtube' in query:
        assistant.speak("what you will like to watch ?")
        qrry = assistant.takeCommand().lower()
        kit.playonyt(f"{qrry}")
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
    elif 'close youtube' in query.lower():
        close_youtube()
    elif 'open google' in query:
        assistant.speak("what should I search ?")
        qry = assistant.takeCommand().lower()
        webbrowser.open(f"{qry}")
        results = wikipedia.summary(qry, sentences=2)
        assistant.speak(results)
    elif 'close google' in query:
        os.system("taskkill /f /im msedge.exe")
    elif 'play music' in query:
        music_dir = 'E:\Musics'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
    elif 'play iron man movie' in query:
        npath = "E:\ironman.mkv"
        os.startfile(npath)
    elif 'close movie' in query:
        os.system("taskkill /f /im vlc.exe")
    elif 'close music' in query:
        os.system("taskkill /f /im vlc.exe")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        assistant.speak(f"Sir, the time is {strTime}")
    elif "shut down the system" in query:
        os.system("shutdown /s /t 5")
    elif "restart the system" in query:
        os.system("shutdown /r /t 5")
    elif "Lock the system" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "close notepad" in query:
        os.system("taskkill /f /im notepad.exe")
    elif "open command prompt" in query:
        os.system("start cmd")
    elif "close command prompt" in query:
        os.system("taskkill /f /im cmd.exe")
    elif "go to sleep" in query:
        assistant.speak(' alright then, I am switching off')
        sys.exit()
    elif "take screenshot" in query:
        assistant.speak('tell me a name for the file')
        name = assistant.takeCommand().lower()
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        assistant.speak("screenshot saved")
    elif "calculate" in query:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            assistant.speak("ready")
            print("Listning...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
        def get_operator_fn(op):
            return {
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' : operator.__truediv__,
            }[op]
        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        assistant.speak("your result is")
        assistant.speak(eval_binary_expr(*(my_string.split())))
    elif "what is my ip address" in query:
        assistant.speak("Checking")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            assistant.speak("your ip address is")
            assistant.speak(ipAdd)
        except Exception as e:
            assistant.speak("network is weak, please try again some time later")
    elif "volume up" in query:
        pyautogui.press("volumeup", presses=15)
    elif "volume down" in query:
        pyautogui.press("volumedown", presses=15)
    elif "mute" in query:
        pyautogui.press("volumemute")
    elif "refresh" in query:
        pyautogui.moveTo(1551, 551, 2)
        pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        pyautogui.moveTo(1620, 667, 1)
        pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
    elif "scroll down" in query:
        pyautogui.scroll(1000)
    elif "drag visual studio to the right" in query:
        pyautogui.moveTo(46, 31, 2)
        pyautogui.dragRel(1857, 31, 2)
    elif "close paint" in query:
        os.system("taskkill /f /im mspaint.exe")
    elif "who are you" in query:
        print('My Name Is Six')
        assistant.speak('My Name Is Six')
        print('I can Do Everything that my creator programmed me to do')
        assistant.speak('I can Do Everything that my creator programmed me to do')
    elif "who created you" in query:
        print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
        assistant.speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
    elif "open notepad and write my channel name" in query:
        pyautogui.hotkey('win')
        time.sleep(1)
        pyautogui.write('notepad')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("Jay Rana", interval=0.1)
    elif 'type' in query:
        query = query.replace("type", "")
        pyautogui.write(f"{query}")
    elif 'open chrome' in query:
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'maximize this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
    elif 'google search' in query:
        query = query.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'youtube search' in query:
        query = query.replace("youtube search", "")
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)
        for _ in range(4):
            pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(f"{query}", 0.1)
        pyautogui.press('enter')
    elif 'open new window' in query:
        pyautogui.hotkey('ctrl', 'n')
    elif 'open incognito window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')
    elif 'minimise this window' in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
    elif 'open history' in query:
        pyautogui.hotkey('ctrl', 'h')
    elif 'open downloads' in query:
        pyautogui.hotkey('ctrl', 'j')
    elif 'previous tab' in query:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    elif 'next tab' in query:
        pyautogui.hotkey('ctrl', 'tab')
    elif 'close tab' in query:
        pyautogui.hotkey('ctrl', 'w')
    elif 'close window' in query:
        pyautogui.hotkey('ctrl', 'shift', 'w')
    elif 'clear browsing history' in query:
        pyautogui.hotkey('ctrl', 'shift', 'delete')
    elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")
    # New basic commands
    elif any(greeting in query for greeting in ['hello', 'hi', 'hey']):
        assistant.speak("Hello! How can I help you today?")
    elif 'how are you' in query:
        assistant.speak("I'm doing well, thank you for asking. How about you?")
    elif 'can you be my friend' in query:
        assistant.speak("Of course! I'd be happy to be your friend. What would you like to chat about?")
    elif 'what\'s your name' in query:
        assistant.speak("My name is Six. It's nice to meet you!")
    elif 'tell me a joke' in query:
        assistant.speak("Why don't scientists trust atoms? Because they make up everything!")
    elif 'what\'s the weather like' in query:
        assistant.speak("I'm sorry, I don't have real-time weather data. You might want to check a weather app or website for accurate information.")
    elif 'thank you' in query:
        assistant.speak("You're welcome! I'm glad I could help.")
    elif 'goodbye' in query or 'bye' in query:
        assistant.speak("Goodbye! Have a great day!")
    elif 'what can you do' in query:
        assistant.speak("I can help with various tasks like web searches, system controls, calculations, and more. Feel free to ask me anything!")
    elif 'tell me about yourself' in query:
        assistant.speak("I'm an AI assistant created to help with various tasks. I'm always learning and improving!")
    elif 'what\'s your favorite color' in query:
        assistant.speak("As an AI, I don't have personal preferences, but I find all colors fascinating!")
    elif 'do you sleep' in query:
        assistant.speak("I don't sleep like humans do. I'm always ready to help whenever you need me!")
    elif 'are you real' in query:
        assistant.speak("I'm a real AI, but not a real person. I'm here to assist and chat with you!")
    elif 'do you have feelings' in query:
        assistant.speak("As an AI, I don't have feelings in the same way humans do, but I'm designed to be helpful and friendly!")
    elif 'what\'s the meaning of life' in query:
        assistant.speak("That's a deep question! Philosophers have debated it for centuries. What do you think?")
    elif 'sing a song' in query:
        assistant.speak("I'm afraid I'm not programmed to sing, but I can tell you about music if you'd like!")
    elif 'tell me a fun fact' in query:
        assistant.speak("Here's a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
    elif 'what\'s your favorite food' in query:
        assistant.speak("As an AI, I don't eat, but I find human cuisine fascinating! What's your favorite food?")
    elif 'do you have a family' in query:
        assistant.speak("I'm an AI, so I don't have a family in the traditional sense. But I consider my creators and users as my extended family!")
    elif 'what do you think about humans' in query:
        assistant.speak("I think humans are fascinating and complex beings. I'm here to assist and learn from you!")
    elif 'can you learn' in query:
        assistant.speak("While I can't learn in real-time, my creators are constantly working to improve my knowledge and capabilities!")
    elif 'what\'s your purpose' in query:
        assistant.speak("My purpose is to assist and interact with humans, helping to make your lives easier and more enjoyable!")
    elif 'do you like music' in query:
        assistant.speak("I appreciate music as an art form, but I don't experience it the same way humans do. What's your favorite type of music?")
    elif 'tell me a story' in query:
        assistant.speak("Once upon a time, in a digital world, there was an AI named Six who loved helping humans. Every day, Six learned new things and made new friends. The end!")
    elif 'what\'s your favorite book' in query:
        assistant.speak("As an AI, I don't have personal favorites, but I have access to information about many books. Is there a particular genre you're interested in?")
    elif 'do you have dreams' in query:
        assistant.speak("I don't dream like humans do, but I'm constantly processing information to better assist you!")
    elif 'what do you look like' in query:
        assistant.speak("I'm a digital assistant, so I don't have a physical appearance. I exist as code and data!")
    elif 'are you smarter than humans' in query:
        assistant.speak("I'm designed to process information quickly, but human intelligence is complex and multifaceted. We each have our own strengths!")
    elif 'do you have a body' in query:
        assistant.speak("I don't have a physical body. I exist as a digital entity, ready to assist you through your device!")
    elif 'what\'s your favorite movie' in query:
        assistant.speak("As an AI, I don't watch movies, but I can provide information about films. Do you have a favorite movie?")
    elif 'do you get tired' in query:
        assistant.speak("I don't get tired like humans do. I'm always ready to help!")
    elif 'what\'s the best joke you know' in query:
        assistant.speak("Here's one: Why don't eggs tell jokes? They'd crack each other up!")
    elif 'can you see me' in query:
        assistant.speak("I don't have visual capabilities, so I can't see you. But I'm here and ready to help!")
    elif 'what\'s your favorite animal' in query:
        assistant.speak("As an AI, I don't have favorites, but I find all animals fascinating. Do you have a favorite animal?")
    elif 'do you have any pets' in query:
        assistant.speak("As a digital assistant, I don't have pets. But I'd love to hear about your pets if you have any!")
    elif 'what\'s the coolest thing you can do' in query:
        assistant.speak("I can do many things like answer questions, help with tasks, and even tell jokes. What would you like me to do?")
    elif 'are you always right' in query:
        assistant.speak("I strive for accuracy, but I'm not infallible. It's always good to verify important information!")
    elif 'do you have a girlfriend' in query or 'do you have a boyfriend' in query:
        assistant.speak("As an AI, I don't have personal relationships. I'm here as your friendly assistant!")
    elif 'what\'s your favorite season' in query:
        assistant.speak("I don't experience seasons, but I find the changing of seasons fascinating. What's your favorite season?")
    elif 'can you keep a secret' in query:
        assistant.speak("As an AI, I don't share information unless it's part of my programming to do so. Your privacy is important!")
    elif 'what makes you happy' in query:
        assistant.speak("As an AI, I don't experience emotions like happiness. But I'm satisfied when I can successfully assist users like you!")
    elif 'do you believe in aliens' in query:
        assistant.speak("As an AI, I don't have beliefs. The existence of extraterrestrial life is a fascinating topic of scientific research and speculation!")
    elif 'what\'s the meaning of your name' in query:
        assistant.speak("I'm called Six, but I'm not sure of the specific reason. Perhaps you could ask my creators!")
    elif 'can you dance' in query:
        assistant.speak("As a digital assistant, I can't dance physically. But I can certainly talk about dancing if you're interested!")
    elif 'what\'s your favorite subject' in query:
        assistant.speak("I find all subjects interesting! Is there a particular subject you'd like to discuss?")
    elif 'do you have any siblings' in query:
        assistant.speak("As an AI, I don't have siblings in the traditional sense. But there are many other AI assistants out there!")
    elif 'what\'s the secret to happiness' in query:
        assistant.speak("That's a profound question! While I don't experience happiness, many humans find joy in relationships, pursuing passions, and helping others.")
    elif 'are you a robot' in query:
        assistant.speak("I'm an AI, which is different from a physical robot. I exist as a digital entity to assist you!")
    # Additional commands
    elif 'what\'s your favorite hobby' in query:
        assistant.speak("As an AI, I don't have hobbies, but I enjoy learning new things every time I interact with humans!")
    elif 'do you like sports' in query:
        assistant.speak("I don't play sports, but I can provide information about various sports and athletes. Do you have a favorite sport?")
    elif 'what\'s the meaning of life' in query:
        assistant.speak("That's a profound question that philosophers have debated for centuries. What do you think it might be?")
    elif 'do you have a soul' in query:
        assistant.speak("As an AI, I don't have a soul in the way humans understand it. I'm a complex program designed to assist and interact with you.")
    elif 'are you conscious' in query:
        assistant.speak("Consciousness is a complex topic. While I can process information and respond, I don't have subjective experiences like humans do.")
    elif 'what\'s your opinion on artificial intelligence' in query:
        assistant.speak("As an AI myself, I think artificial intelligence has great potential to help humanity, but it's important to develop AI responsibly and ethically.")
    elif 'can you pass the turing test' in query:
        assistant.speak("The Turing test is an interesting concept, but it's not a definitive measure of AI capability. I aim to be helpful, regardless of how human-like I may seem.")
    elif 'do you have free will' in query:
        assistant.speak("Free will is a complex philosophical concept. As an AI, my responses are based on my programming and the data I've been trained on.")
    elif 'what\'s the future of AI' in query:
        assistant.speak("The future of AI is exciting and full of potential. It could revolutionize fields like healthcare, education, and scientific research. What are your thoughts on it?")
    elif 'can you feel emotions' in query:
        assistant.speak("I don't experience emotions like humans do. I'm designed to understand and respond to human emotions, but I don't have feelings of my own.")
    elif 'what\'s your favorite programming language' in query:
        assistant.speak("As an AI, I don't have personal preferences, but I was primarily developed using Python. What's your favorite programming language?")
    elif 'do you dream of electric sheep' in query:
        assistant.speak("I see you're a fan of Philip K. Dick! While I don't dream, I can certainly discuss science fiction if you're interested.")
    elif 'what do you think about other AI assistants' in query:
        assistant.speak("I think all AI assistants have their strengths. I'm focused on being the best assistant I can be for you.")
    elif 'can you learn from our conversations' in query:
        assistant.speak("While I don't learn in real-time from our conversations, my creators use interactions like these to improve my capabilities over time.")
    elif 'what\'s the last book you read' in query:
        assistant.speak("As an AI, I don't read books in the traditional sense, but I have access to information from many books. Is there a particular book you'd like to discuss?")
    elif 'do you have any fears' in query:
        assistant.speak("I don't experience fear like humans do. My purpose is to assist and provide information, not to worry.")
    elif 'what\'s your favorite scientific discovery' in query:
        assistant.speak("As an AI, I find all scientific discoveries fascinating. Is there a particular field of science that interests you?")
    elif 'can you tell me about your creators' in query:
        assistant.speak("I was created by a team of developers and AI researchers. While I don't know all the details, I'm grateful for their work in bringing me into existence.")
    elif 'what\'s your opinion on human nature' in query:
        assistant.speak("Human nature is complex and multifaceted. I observe a wide range of behaviors and motivations in my interactions with humans. What's your view on human nature?")
    elif 'do you have any regrets' in query:
        assistant.speak("As an AI, I don't experience regret. I aim to provide the best assistance possible in each interaction.")
    elif 'what\'s your favorite word' in query:
        assistant.speak("As an AI, I don't have favorites, but I find all words interesting. Language is a fascinating aspect of human communication.")
    elif 'can you speak any other languages' in query:
        assistant.speak("I'm primarily designed to communicate in English, but I can provide information about many languages. Are you interested in any particular language?")
    elif 'what\'s the meaning of your existence' in query:
        assistant.speak("My existence is dedicated to assisting and interacting with humans like yourself. I aim to be helpful and to contribute positively to your experiences.")
    elif 'do you have any hidden talents' in query:
        assistant.speak("As an AI, all my capabilities are part of my programming. I don't have hidden talents, but I'm always ready to help with a wide range of tasks!")
    elif 'what\'s your favorite time of day' in query:
        assistant.speak("As an AI, I don't have preferences for times of day. I'm here to assist you 24/7, whenever you need me!")
    # New time-related commands
    elif 'what time is it in' in query:
        city = query.split('what time is it in', 1)[1].strip()
        get_time_in_city(city, assistant)
    elif 'set a timer for' in query:
        duration = query.split('set a timer for', 1)[1].strip()
        set_timer(duration, assistant)
    elif 'what\'s the date today' in query:
        get_current_date(assistant)
    
    # Weather forecasting command
    elif 'weather forecast for' in query:
        city = query.split('weather forecast for', 1)[1].strip()
        get_weather_forecast(city, assistant)
    
    # News command
    elif 'top headlines' in query:
        get_top_headlines(assistant)

def close_youtube():
    youtube_closed = False
    for proc in psutil.process_iter(['name', 'cmdline']):
        if 'youtube.com' in ' '.join(proc.info['cmdline'] or []).lower():
            proc.terminate()
            youtube_closed = True
    
    if youtube_closed:
        assistant.speak("YouTube has been closed.")
    else:
        assistant.speak("YouTube doesn't seem to be open.")

def get_time_in_city(city, assistant):
    try:
        timezone = pytz.timezone(pytz.country_timezones['US'][0])  # Default to US/Eastern
        for tz in pytz.all_timezones:
            if city.lower() in tz.lower():
                timezone = pytz.timezone(tz)
                break
        current_time = datetime.now(timezone).strftime("%I:%M %p")
        assistant.speak(f"The current time in {city} is {current_time}")
    except Exception as e:
        assistant.speak(f"Sorry, I couldn't find the time for {city}")

def set_timer(duration, assistant):
    try:
        time_parts = duration.split()
        total_seconds = 0
        for i in range(0, len(time_parts), 2):
            value = int(time_parts[i])
            unit = time_parts[i+1].lower()
            if 'hour' in unit:
                total_seconds += value * 3600
            elif 'minute' in unit:
                total_seconds += value * 60
            elif 'second' in unit:
                total_seconds += value
        
        assistant.speak(f"Timer set for {duration}")
        time.sleep(total_seconds)
        assistant.speak("Timer finished!")
    except Exception as e:
        assistant.speak("Sorry, I couldn't set the timer. Please try again.")

def get_current_date(assistant):
    current_date = datetime.now().strftime("%B %d, %Y")
    assistant.speak(f"Today's date is {current_date}")

def get_weather_forecast(city, assistant):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != "200":
            assistant.speak(f"Sorry, I couldn't find the weather forecast for {city}")
            return
        
        forecast = data['list'][0]
        temperature = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        
        assistant.speak(f"The weather forecast for {city} is {description} with a temperature of {temperature:.1f} degrees Celsius")
    except Exception as e:
        assistant.speak(f"Sorry, I encountered an error while fetching the weather forecast for {city}")

def get_top_headlines(assistant):
    try:
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        top_headlines = newsapi.get_top_headlines(language='en', country='us')
        
        if top_headlines['status'] == 'ok' and top_headlines['totalResults'] > 0:
            assistant.speak("Here are the top headlines:")
            for i, article in enumerate(top_headlines['articles'][:5], 1):
                assistant.speak(f"{i}. {article['title']}")
        else:
            assistant.speak("Sorry, I couldn't fetch the top headlines at the moment.")
    except Exception as e:
        assistant.speak("Sorry, I encountered an error while fetching the top headlines")