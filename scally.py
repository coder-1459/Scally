import pyttsx3
import speech_recognition as sr
import datetime
import time
import winsound
import random
import os
import cv2
import pyautogui
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit 
import smtplib
import sys
import instaloader
import pyjokes
import naruto
import requests 
from geopy.geocoders import Nominatim
import psutil


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1 ].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login("rijuranjan087@gmail", "RijuRanjan2006")
    server.sendmail("rijuranjan087@gmail.com", to, content)
    server.close()



def get_location():
    response = requests.get('https://api.ipify.org?format=json') 
    ip = response.json()['ip'] 
    response = requests.get(f'https://ipinfo.io/{ip}/json') 
    data = response.json() 
    # Extract location details 
    loc = data['loc'].split(',') 
    latitude = loc[0] 
    longitude = loc[1] 
    # Use geopy to get address information 
    geolocator = Nominatim(user_agent="geoapiExercises") 
    location = geolocator.reverse((latitude, longitude), language='en') 
    return location.address
 

def message():
    speak("Checking for messages....")
    userID = "rijuranjan087@gmail.com"
    psd = 'RijuRanjan2006'
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"


def download_instagram_stories():
    L = instaloader.Instaloader()
    try:
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")
        L.login(username, password)
    except Exception as e:
        print(f"Error logging in: {e}")
        return

    profile_username = input("Enter the username of the profile whose stories you want to download: ")

    try:
        profile = instaloader.Profile.from_username(L.context, profile_username)

        for story in L.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                L.download_storyitem(item, target=profile_username)

        print(f"Stories from {profile_username} have been downloaded.")

    except Exception as e:
        print(f"Error downloading stories: {e}")


def takecommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, I didn't get that")
        return "none"
    return query


# def take_multiple_inputs():
#     user_inputs = []
#     print("Enter your inputs (type 'stop' to end):")
    
#     while True:
#         user_input = input("Enter value: ")
#         if user_input.lower() == 'stop':
#             break
#         user_inputs.append(user_input)
    
#     return user_inputs

# Example usage
# user_values = take_multiple_inputs()
# print("You entered:", user_values)




def get_greeting():
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        period = "morning"
    elif 12 <= current_hour < 18:
        period = "afternoon"
    else:
        period = "evening"
    # speak("I Am  Your Assistant, How Can I Help You Today " + period + " Sir")

    greetings = {
        "morning": [
            "Good morning! Have a great day!",
            "Rise and shine! It's a brand-new day.",
            "Morning! Hope your day is filled with joy."
        ],
        "afternoon": [
            "Good afternoon! Keep up the good work!",
            "Hello! Hope your afternoon is going well.",
            "Good afternoon! Enjoy the rest of your day."
        ],
        "evening": [
            "Good evening! Relax and unwind.",
            "Evening! Hope you had a productive day.",
            "Good evening! Have a peaceful night."
        ]
    }
    
    return random.choice(greetings[period])


if __name__ == "__main__":
    # speak(get_greeting())
    # introduction = "I Am  GENCO, How Can I Help You Today Sir"
    # speak(introduction)
    # while True:
    if 1:

        query = takecommand().lower()
        if "open notepad " in query:
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("Opening  Notepad")

        elif "open Chrome " in query:
            npath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
            speak("Opening  Google Chrome")

        elif "open command prompt " in query:
            os.system("start cmd")
            # subprocess.run("start cmd", shell=True)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip =get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "thank you " in query:
            speak("You're Welcome, Have a Nice Day")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%d %B, %Y")
            speak(f"Sir, the date is {strDate}")

        elif "who are you" in query:
            speak("I am your virtual assistant, here to help you with any task you want to perform")

        elif "what is your name" in query:
            speak("My name is Genica, I am your virtual assistant")

        elif "tell me something about myself" in query:
            speak("I don't know much about you, but I can tell you that you are deeply interested in various fields, ranging from technology to personal growth. You are likely a front-end web developer with a strong grasp of CSS and JavaScript, and you have some serious skills in Python. And One More Thing . you never date a single girl")
        
        elif "one side love" in query:
            speak("One-sided love can be an emotionally intense and challenging experience. It involves having deep feelings for someone who may not reciprocate those emotions in the same way , one more thing , how is parul..")
        
        # elif "no jarvis " in query:
        #     speak(" yes , i knew it , you will never get her")


        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram")

        elif "open github" in query:
            webbrowser.open("www.github.com")
            speak("Opening github")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("Opening facebook")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("Opening youtube")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif "play song on youtube" in query:
            speak("sir,what song do you want to listen to")
            cm = takecommand().lower()
            pywhatkit.playonyt(f"{cm}")

        # elif "send email"  in query:
        #     try:
        #         speak("sir,what should i write in the email")
        #         content = takecommand().lower()
        #         to = "rrsnikumbh@gmail.com"
        #         sendEmail(to, content)
        #         speak(f"Email has been sent {to}")
            
        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir email is not sent")

        
        elif "no thanks" in query:
            speak("okay sir,have a good day")
            sys.exit()

        elif "close notepad" in query:
            speak("okay sir,closing....")
            os.system("taskkill /f /im notepad.exe")

        elif "love you" in query:
            speak("love you 3000")

        # speak("sir , do you have any other work to do")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        # elif " tell me news " in query:
        #     speak("sir,what news do you want to hear")
        #     cm = takecommand().lower()
        #     news = getNews(cm)
        #     speak(news)

        elif "take screenshot" in query:
            speak("sir, taking screenshot")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png") 
            speak("Screenshot taken and saved as screenshot.png")


        
        elif "instagram profile " in query:
            speak("sir, which profile do you want to see")
            name =input("enter the username")
            webbrowser.open(f"https://www.instagram.com/ {name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile photo ot this account.")
            condition =  takecommand().lower()
            if "download" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("profile photo downloaded")
            else:
                speak("sorry sir can repat again")

        elif "download story" in query:
                speak("sir, which story do you want to download")
                download_instagram_stories()

        elif "send message on whatsapp" in query:
            speak("sir, which account do you want to send message")
            import pywhatkit as pwk  
            num = int(input("Enter The Number: "))
            speak("What is the message four your love one...")
            msg = takecommand().lower()
            speak("Which Hour You Want to Text..")
            cn = int(input("Enter The Hour: "))
            speak("Whic Minute You Want to Text..")
            mn =int(input("Enter The Minute: "))
            pwk.sendwhatmsg("+91" + str(num), msg, cn, mn,)


        # elif "send message on instagram" in query:
        #     speak("sir, which account do you want to send message")
        #     from instadm import InstaDM
        #     user = input("Enter The Username: ")
        #     speak("What is the message four your love one...")
        #     msg = takecommand().lower()
        #     insta = InstaDM(username='ankush_singh__22', password='RijuRanjan087', headless=True)
        #     insta.sendMessage(user, msg)

        elif "to do list " in query:
            while True:
                speak("Sir, what do you want to add to the list?")
                task = takecommand().lower()
                if task == "stop" or task == "done":
                    speak("Okay, I will stop adding tasks.")
                    break
                speak("Yes, sir adding this in the list")
                with open("todo.txt", "a") as f:
                    f.write(task + "\n")
                    speak("Sir, the item has been added to the list")
                    speak("sir if you want to check your list say check the list")
                    ans = takecommand().lower()
                    if "check the list" in ans:
                        speak("Sir, here is your list")
                        with open("todo.txt", "r") as f:
                            speak(f.read())
                    else:
                        speak("Sorry sir I'm not able to access todo list file ")

        elif "delete my todo list" in query:
            speak("Sir, are you sure you want to delete your todo list?")
            ans = takecommand().lower()
            if "yes" in ans:
                speak("Okay, sir deleting your todo list")
                os.remove("todo.txt")
                speak("Sir, your todo list has been deleted")
            else:
                speak("Sir, your todo list is safe")   


        elif "can you check my music player" in query:
            speak("Sir, checking your music player")
            webbrowser.open("https://music-player-pluto.vercel.app/")
            speak("opening sir.......")

        elif 'close current window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            speak('Current window is closed.')
        
        elif "how much battery " in query:
            speak("Sir, checking your battery percentage")
            battery = psutil.sensors_battery()
            speak(f"Battery is at {battery}")
            speak(battery.percent)
            print("battery is at:" + str(battery.percent))

        elif "create a reminder" in query:
                speak("What is the reminder?")
                data = takecommand().lower()
                speak("You said to remember that" + data)
                reminder_file = open("data.txt", 'a')
                reminder_file.write('\n')
                reminder_file.write(data)
                reminder_file.close()
                
        elif 'open location' in query:
                speak('tell me the location you are looking for')
                location = takecommand().lower()
                url2 = 'https://google.nl/maps/place/' + location +'/&amp;'
                webbrowser.open(url2)
                speak('location on your screen boss')

        elif " set alarm" in query:
            speak("Sir, setting an alarm for you")
            naruto()