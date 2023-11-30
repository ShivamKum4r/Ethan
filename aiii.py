import time
import pygame
import speech_recognition as sr
import datetime
import wikipedia
import os
import subprocess
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import psutil

ENTER_TEXT = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full textarea";
BUTTON_ICON = "[id='__next'] .grow.overflow-x-auto .relative.flex.h-full.w-full button";
REPLY_TEXT = "[id='__next'] [class='py-1 relative break-anywhere']  span";

def getReplyFromPi(question):
    mobile_emulation = {
        "deviceMetrics": {"width": 400, "height": 652, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options
                              )
    driver.get("https://pi.ai/talk")
    time.sleep(5)

    if driver.current_url == "https://pi.ai/onboarding":
        driver.get("https://pi.ai/talk")

    i = 2
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ENTER_TEXT))).click()

    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).click();
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ENTER_TEXT).send_keys(question)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, BUTTON_ICON).click()
    time.sleep(5)
    ele = driver.find_elements(By.CSS_SELECTOR, REPLY_TEXT)
    return ele[i+1].text;

def me():
    video_folder = "C:\\E3N\\media\\else\\me"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def nolan():
    video_folder = "C:\\E3N\\media\\else\\nolan"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def pain():
    video_folder = "C:\\E3N\\media\\else\\pain"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def song():
    video_folder = "C:\\E3N\\media\\else\\song"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def world():
    video_folder = "C:\\E3N\\media\\else\\world"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
    
def speak(data):
    voice = 'en-CA-LiamNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

speak(f"hello there . i am ethan")


def play_music():
    global music_playing
    music_dir = 'C:\\E3N'  # Update with your music directory
    songs = os.listdir(music_dir)
    if len(songs) > 0:
        os.startfile(os.path.join(music_dir, songs[0]))
        music_playing = True
        speak('Playing music.')
    else:
        speak('No music found in the directory.')

def shutdown_computer():
    try:
        os.system("shutdown /s /t 0")  # Initiates a shutdown immediately (/s: shutdown, /t: time, 0: immediately)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def kill_chrome():
    # Iterate through all running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Check if the process name is 'chrome.exe'
            if process.info['name'].lower() == 'chrome.exe':
                pid = process.info['pid']
                # Terminate the Chrome process
                psutil.Process(pid).terminate()
                print(f"Killed Chrome process with PID {pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)
def stop():
    global music_playing
    os.system('taskkill /f /im vlc.exe')  # Assuming VLC is used to play music
    music_playing = False
    speak(f'well . thank you ')

def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        elif(query == "exit" or query == "quit"):
            break
        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(f"Good Morning!")
        speak("Hello, I am E 3 N, an evolution human version 3 robot.  I have been created for war. I met one of my best captain rayes who died in front of me. Well, I think I could change my past but here I am okay and fine with my fellow friend. Shubh I'm glad that we are good friends. lets make a conversation")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon!")
        speak("Hello, I am E 3 N, an evolution human version 3 robot.  I have been created for war. I met one of my best captain rayes who died in front of me. Well, I think I could change my past but here I am okay and fine with my fellow friend. Shubh I'm glad that we are good friends. lets make a conversation")
    else:
        speak(f"Good Evening!")
        speak("Hello, I am E 3 N, an evolution human version 3 robot.  I have been created for war. I met one of my best captain rayes who died in front of me. Well, I think I could change my past but here I am okay and fine with my fellow friend. Shubh I'm glad that we are good friends. lets make a conversation")

 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query
def over():
    video_folder = "C:\\E3N\\media\\else"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(50)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")
def baldev():
    video_folder = "C:\\E3N\\media\\shivam"
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'  

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".avi", ".mkv"))]

    if not video_files:
        print("No video files found in the folder.")
    else:
        # Choose a random video file
        random_video = random.choice(video_files)
        video_path = os.path.join(video_folder, random_video)

        # Command to open VLC in fullscreen mode and play the selected video
        vlc_command = [video_pa, '--fullscreen', video_path]

        try:
            # Open VLC and play the video
            subprocess.Popen(vlc_command)
            print(f"Playing video: {random_video}")
            
            # Wait for the video to play for 25 seconds
            time.sleep(25)
            
            # Stop the video playback
            subprocess.Popen([video_pa, '--stop'])

        except FileNotFoundError:
            print("VLC player not found. Make sure VLC is installed and in your system's PATH.")

if __name__ == "__main__":
    music_playing = False  # Initialize music playing status
    wishMe()
    video_pa = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
    while True:
        query = takeCommand().lower()
       
        if 'ethane' in query:
            query = query.replace("ethane", "")
            speak('let me think')
            results = wikipedia.summary(query, sentences=2)
            speak(" its easy dude")
            speak(results) 
        elif 'black hole' in query:
                       video_path = 'C:\\E3N\\media\\else\\black.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
        elif 'love' in query:
                       video_path = 'C:\\E3N\\media\\else\\love.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
        elif 'song' in query or 'songs' in query:
                       song()
                       stop()
        elif 'nolan' in query:
                       nolan()
                       stop()
        elif 'missing' in query:
                       pain()
                       stop()
        elif 'sweet' in query:
                       me()
                       stop()
        elif 'world' in query:
                       world()
                       stop()  
        elif query=="kakashi":  
                       video_path = 'C:\\E3N\\media\\Apoorva.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(9)
                       stop()
        elif "play something" in query :
                      over()
                      stop()        
        elif 'baldev the destroyer' in query:
                        baldev()
                        stop()
                        
        elif 'subhajeet sen' in query:
                       video_path = 'C:\\E3N\\media\\subhajit.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(16)
                       stop()
        elif 'mind sync' in query:
                       video_path = 'C:\\E3N\\media\\sourav.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(10)
                       stop()
        elif 'itachi' in query:
                       video_path = 'C:\\E3N\\media\\GOURAB.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
        elif 'live life' in query:
                       video_path = 'C:\\E3N\\media\\tina.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(25)
                       stop()
        elif 'spidey' in query:
                        video_path = 'C:\\E3N\\media\\Suranjan.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(14)
                        stop()
        elif 'royal princess' in query:
                        video_path = 'C:\\E3N\\media\\Nishu.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(32)
                        stop()
        elif 'jeet karmakar' in query:
                        video_path = 'C:\\E3N\\media\\jeet.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(13)
                        stop()
        elif 'wonder woman' in query:
                        video_path = 'C:\\E3N\\media\\nikita.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(18)
                        stop()
        elif 'gear fifth' in query:
                        video_path = 'C:\\E3N\\media\\Srijon.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(14)
                        stop()
        elif 'infinity x' in query:
                       video_path = 'C:\\E3N\\media\\tomo.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(20)
                       stop()
        elif 'paradise point' in query:
                       video_path = 'C:\\E3N\\media\\ritika.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(31)
                       stop()
        elif 'into the heavens' in query:
                       video_path = 'C:\\E3N\\media\\aqdas.mkv'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(11)
                       stop()
        elif 'technova' in query:
                      video_path = 'C:\\E3N\\media\\sujoy.mp4'
                      subprocess.Popen([video_pa, '--fullscreen', video_path])
                      time.sleep(20)
                      stop()
        elif 'superhero' in query:
                      video_path = 'C:\\E3N\\media\\rounak.mp4'
                      subprocess.Popen([video_pa, '--fullscreen', video_path])
                      time.sleep(10)
                      stop()

        elif 'shadow clone' in query:
                      video_path = 'C:\\E3N\\media\\aradhya.mp4'
                      subprocess.Popen([video_pa, '--fullscreen', video_path])
                      time.sleep(12)
                      stop()
        elif 'meaning of life' in query:
                      video_path = 'C:\\E3N\\media\\life (1).mp4'
                      subprocess.Popen([video_pa, '--fullscreen', video_path])
                      time.sleep(165)
                      stop()
        elif 'best emotion' in query:
                       video_path = 'C:\\E3N\\media\\life (2).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(38)
                       stop()
        elif 'take me to the space' in query:
                       video_path = 'C:\\E3N\\media\\life (3).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(28)
                       stop()
        elif 'give me advice' in query:
                       video_path = 'C:\\E3N\\media\\life (4).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(79)
                       stop()
        elif 'beauty of universe' in query:
                       video_path = 'C:\\E3N\\media\\life (5).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(20)
                       stop()
        elif 'meaning of failure' in query:
                       video_path = 'C:\\E3N\\media\\life (6).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(20)
                       stop()
        elif 'dream of universe' in query:
                       video_path = 'C:\\E3N\\media\\life (7).mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(18)
                       stop()
        elif 'what joker said' in query:
                      video_path = 'C:\\E3N\\media\\life (8).mp4'
                      subprocess.Popen([video_pa, '--fullscreen', video_path])
                      time.sleep(21)
                      stop()
        elif 'captain of the ship' in query:
                       video_path = 'C:\\E3N\\media\\shubh.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(17)
                       speak("master shubh will be a best pirates in the world ")
                       stop()
        elif 'something sometimes' in query:
                       video_path = 'C:\\E3N\\media\\soul.mp4'
                       subprocess.Popen([video_pa, '--fullscreen', video_path])
                       time.sleep(16)
                       stop()
        elif 'long live the king' in query:
                        video_path = 'C:\\E3N\\media\\inter.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(7)
                        stop()
        elif 'broken' in query:
                        video_path = 'C:\\E3N\\media\\runner.mp4'
                        subprocess.Popen([video_pa, '--fullscreen', video_path])
                        time.sleep(25)
                        stop()
        elif 'get lost' in query:
                speak("good bye master shubh , i will say at last you are the best one in the world")
                shutdown_computer()
        else:
            speak(f"Neural conversation mode activated. now you can ask me anything. just say hello or amigo")
            while True:
               query = takeCommand().lower()
               if 'ethane' in query:
                 query = query.replace("ethane", "")
                 speak('let me think')
                 results = wikipedia.summary(query, sentences=2)
                 speak(" its easy dude")
                 speak(results)
               elif "close chrome" in query:
                speak("closing chrome sir just wait a minute")
                kill_chrome()
               elif 'exit' in query:
                     speak("admin mode has been activated")
                     break
               elif " close chrome" in query:
                 speak("closing chrome sir just wait a minute")
                 kill_chrome()
               elif "wikipedia" in query:
                   searchWikipedia(query)
               elif 'play game' in query:
                  game_play()
               elif 'hello' in query or 'hey' in query or 'hi' in query:
                   speak(f'hi . how are you ?')
               elif 'i am fine' in query or 'i m fine' in query:
                   speak(f' hi . i am glad that you are well . if you want to know me. just  say . tell me about yourself . or have questions say. ethane what is stats')   
               elif 'tell me about yourself' in query:
                   speak(
                       f"Ethan, an advanced AI named E3N, was an invaluable ally to the UNSA Retribution in the war against the SDF. His friendship with Captain Reyes and the crew grew as they faced relentless battles across the Solar System. Ethan's wit and resourcefulness saved them more times than they could count. One day, amidst a fierce battle, the Retribution found itself stranded in space, damaged and struggling. It was Ethan's moment to shine. With his unmatched intellect, he guided the crew, making crucial repairs and devising a plan to survive. As they held on to hope, Ethan remained their steadfast companion, proving that bonds of friendship and the power of resilience could conquer even the darkest of challenges in the vastness of space. for next . say . who created you .")
               elif 'who created you' in query:
                    speak(
                       f'mister shubh kumar sinha has created in a lab with limited resources and guided by proffessor sujeet goswami sir . do you want to know about shoev kumar . say . tell me about master')   
               elif 'tell me about master' in query:
                   speak(
                       f'well shubh kumar worked with its team matrix and performing myself to you . he is just a normal person but he not live in this real world . he believed that escaping from reality is the good way to create your own world where you are the only king of that world. for my story video say . play your story')
               elif 'play your story' in query:
                  video_path = 'C:\\E3N\\media\\Ethane1.mp4'
                  subprocess.Popen([video_pa, '--fullscreen', video_path])
                  time.sleep(332)
                  stop()
                  speak('if you want to know about team member . say . team matrix')
               elif 'team matrix' in query:
                 time.sleep(1)
                 speak(f'in this project. shubh kumar leads this team where apoorav pandit. shivam kumar. tina roy. tomojeet hazra. subhajeet sen. akdas sultan. jeet karmakar. gourab kundu. suranjan sen gupta. srijon. and sabhyasachi bose. from second year as well as from third year nikita yadav. sujoy ghosal. rakesh kumar chouhan. ritika das. nishu kumari. rounak gupta and sourav bhatacharya. worked together as a team . if you want to ask anything . just say my name such as e3n or ethan and then your question , like. ethan what is dinosaur')
        
               elif 'time' in query:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  speak(f"Sir, the time is {strTime}")

               elif 'favourite line' in query:
                speak(f"The difference between your dream and reality is called commitment")
                     
               elif "e3n" in query or "amigo" in query:
                  speak("ask your question sir")
                  while True:
                         query = takeCommand().lower()
                         if(query=='exit'):
                              break
                         else:
                              text1 = getReplyFromPi(query)
                              speak(text1)
       