
import datetime
import os
import smtplib
import sys
import webbrowser
from cv2 import clipLine
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from requests import get
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
from pywikihow import search_wikihow
#///////////////////////////importing lib/////////////////////////////////////////#

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[0].id)
engine.setProperty('voices', voices[0].id)


#this function speaks
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#tts recognizer

#///////////////////////////settinngs for speech/////////////////////////////////////////#






#wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning,sir")
        print("Good Morning sir")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir")
        print("Good Afternoon sir")
    else:
        speak("Good Evening,sir")
        print("Good Evening sir")
#///////////////////////////wish function/////////////////////////////////////////#

def Time():
     strTime = datetime.datetime.now().strftime("%H:%M:%S")
     print(strTime)
     speak(f" it's {strTime}\n")
#///////////////////////////time function/////////////////////////////////////////#


def sendEmail(to,content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dvtharun53@gmail.com' ,'tharun1428dv')
    server.sendmail("dvtharun53@gmail.com",to,content)
    server.close()

#///////////////////////////////sending email function/////////////////////////////////////#

#news
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513"

    
    main_page = requests.get(main_url).json()
    
    articles = main_page["articles"]

    head = []

    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")
            print(f"today's {day[i]} news is: {head[i]}")
#///////////////////////////news function/////////////////////////////////////////#

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...  ")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
 #///////////////////////////takes comments  from user/////////////////////////////////////////#
   

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:  {query}")
#///////////////////////////prints comments from user/////////////////////////////////////////#


    except Exception as e:
        return "none"
    return query

if __name__ == "__main__":
 wish()
 
 Time()

 speak(" hello,sir,how can i ,help you")


 while True:
            
            query = takecommand().lower()
            
            #logic of jarvis
            if 'open teams' in query.lower():
             teams = "C:\\Users\\Premnath\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams.lnk"
             os.startfile(teams)
 #///////////////////////////opens teams/////////////////////////////////////////#

            if 'open notepad' in query.lower():
             notepad = "C:\\Users\\Premnath\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
             os.startfile(notepad) 
#///////////////////////////opens notepad/////////////////////////////////////////#

            if 'open google' in query.lower():
              speak("sir,what should i search in google")
              cm = takecommand().lower()
              webbrowser.open(f"{cm}")
#///////////////////////////opens google/////////////////////////////////////////#
            
            if 'open youtube' in query.lower():
               speak("sir,what should i search in youtube")
               cm = takecommand().lower()
               webbrowser.open(f"{cm}")
#///////////////////////////opens youtube /////////////////////////////////////////#
           
            if 'open amazon' in query.lower():
                webbrowser.open("www.amazon.in")
#///////////////////////////opens amazon/////////////////////////////////////////#
            
            if 'open new document' in query.lower():
                webbrowser.open("https://docs.google.com/document/d/17aWAyCfYbOdCPAIP9ySQ-oWnF5zgFYUrTRKQWH0Po9U/edit")
#///////////////////////////opens  new documents/////////////////////////////////////////#
            
            if 'open new spreadsheet' in query.lower():
                webbrowser.open("https://docs.google.com/spreadsheets/u/0/create?usp=dot_new")
#///////////////////////////opens new spread sheet/////////////////////////////////////////#
            
            if 'open spotify' in query.lower():
                webbrowser.open("www.spotify.com")
#///////////////////////////opens amazon/////////////////////////////////////////#

            if 'play song' in query.lower():
                cm = takecommand().lower()
                webbrowser.open(f"https://open.spotify.com/search/{cm}")
#///////////////////////////searches specific songs on spotify/////////////////////////////////////////#

            if 'open new forms' in query.lower():
                webbrowser.open("https://docs.google.com/forms/d/1M9CTCKFGpEGDu2YEEQ2Hj9qshBBlANWpkTBZ0Lh_gpc/edit")
#///////////////////////////opens new google forms/////////////////////////////////////////#

            if 'open instagram' in query.lower():
                webbrowser.open('www.instagram.com')
           
            if 'open reddit' in query.lower():
                webbrowser.open('www.reddit.com')

            if 'open twitter' in query.lower():
                webbrowser.open('twitter.com')
            if 'open face book' in query.lower():
                webbrowser.open('www.facebook.com')                
#///////////////////////////opens various social mediea apps/////////////////////////////////////////#
            
            if 'temperature' in query.lower():
                search = "temerature in chennai"
                url = f"https://www.google.com/serach?q={search}"
                r =requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe")
                speak(f"current {search} is {temp}")

#///////////////////////////checks temperature/////////////////////////////////////////#

            
            if 'in japanese'in query.lower():
                speak("Minasan, kon'nichiwa. Watashi vaaa jarvisai,ashisutantodesu.")
                print("みなさん、こんにちは。私はjarvisaiアシスタントです。")
#///////////////////////////speaks in japanese/////////////////////////////////////////#

            if 'ip address' in query.lower():
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
                print("your IP address is :" + ip)

#///////////////////////////finds my ip/////////////////////////////////////////#

            #about friends
            if 'sher ko' in query.lower():
              speak("the panda of 11a")
              print("the panda of 11a")
            if 'gerald' in query.lower():
              speak("smallest boy of 11 a")
              print("smallest boy of 11 a")
            if 'who created you' in query.lower():
              speak("tharun,pranav,chorko,muthu vishal and jerold")
              print("tharun, pranav  ,  chorko  ,  muthu vishal and jerold")
            
            if 'who is frooti' in query.lower():
              speak("he is classmate  of tharun,advaith, and a true friend to tharun")
              print("he is classmate  of tharun,advaith, and a true friend to tharun")
            if 'what is your name' in query.lower():
               speak("my name is jarvis")
               print("my name is jarvis")
#///////////////////////////common interaction/////////////////////////////////////////#

            if 'what is the time' in query.lower():
              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              speak(f" the time is {strTime}\n")
              print(strTime)
#///////////////////////////tells the correct time/////////////////////////////////////////#
           
            if 'send mail to box' in query.lower():
                
                try:
                    speak("what should i send")
                    content = takecommand()
                    to = "durgadeviprem14@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent successfully")
                
                except Exception as e:
                            speak("error")
#///////////////////////////sends mail/////////////////////////////////////////#
            
            if 'thank you jarvis' in query.lower():
               speak("ok sir, have a good day")
               sys.exit()

            if 'ok jarvis thank you' in query.lower():
               speak("ok sir, have a good day")
               sys.exit()
            
#///////////////////////////exiting function/////////////////////////////////////////#
       
            #close function
            if "close notepad" in query.lower():
                speak("ok sir,closing notepad")
                os.system("taskkill /f /im notepad.exe") 

            if "close teams" in query.lower():
                speak("ok sir, closing teams")
                os.system("taskkill /f /im teams.exe")
#///////////////////////////terminates app window/////////////////////////////////////////#

            #alarm
            if "set alarm" in query.lower():
                nn = int(datetime.datetime.now().hour)
                if nn ==22:
                    music_dir ='C:\\Users\\Premnath\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))
#///////////////////////////sets alarm/////////////////////////////////////////#
           
            #joke
           
            if "tell me a joke" in query.lower():
                joke = pyjokes.get_joke(language='en')
                speak(joke)
                print(joke)
           
#///////////////////////////joke/////////////////////////////////////////#
         
            #system function
            if 'shutdown the system' in query.lower():
                os.system("shutdown /r /t 5")

            if 'restart the system ' in query.lower():
                os.system("shutdown /r /t 5")
            
            if 'sleep the system' in query.lower():
                os.system("run1132.exe powrprof.dll,SetSuspendState 0,1,0")
#///////////////////////////system controll/////////////////////////////////////////#

            
            if 'very good jarvis' in query.lower():
                speak("thank you sir")
            
            if 'hi jarvis' in query.lower():
                speak(" hello sir,how are you")

            if 'go to sleep' in query.lower():
                speak("ok,sir")
                sys.exit()
            
            if 'great' in query.lower():
                speak('ok,sir,thank you')
            
            if 'i am fine' in query.lower():
                speak("great to hear that sir")

#//////////////////////////interaction with people/////////////////////////////////////////#


            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
#///////////////////////////searches in wikipedia/////////////////////////////////////////#
       
            if "news" in query.lower():
                speak("wait a minute sir,feteching the latetest news for you")
                news()
#///////////////////////////reads the latest news/////////////////////////////////////////#

            if "where i am" in query or  "what is my current location" in query or "location" in query:
                 speak("one minute sir,let me check")  
                 try:
                     ipAdd = requests.get('https://api.ipify.org').text
                     print(ipAdd)
                     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                     geo_requests = requests.get(url)
                     geo_data = geo_requests.json()   
                     city = geo_data['city']
                     country = geo_data['country']
                     speak(f"sir i am not sure,but i think we are in {city},city of,{country} country")
                     print(f"sir i am not sure,but i think we are in {city},city of,{country} country")
                 except Exception as e:
                     speak("sorry sir,due to poor internet i cant find where we are.")
                     pass   
#/////////////////////////// finds my location/////////////////////////////////////////#
            
            if "instagram profile" in query or "profile on instagram" in query.lower():
                speak("sir please enter the user name")
                name = input("enter user name : ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir,here is the profile,of the user {name}")
#///////////////////////////checks instagram profiles/////////////////////////////////////////#
            
            
            def weather(city):
                city = city.replace(" ", "+")
                res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                print("Searching...\n")
                soup = BeautifulSoup(res.text,'html.parser')
                location = soup.select('#wob_loc')[0].getText().strip()
                time = soup.select('#wob_dts')[0].getText().strip()
                info = soup.select('#wob_dc')[0].getText().strip()
                weather = soup.select('#wob_tm')[0].getText().strip()
                speak("sir,you are in..."+location)
                speak("time is..."+time)
                speak(info)
                speak(weather+"celcius")     
                print(location)
                print(time)
                print(info)
                print(weather+"°C")
            if "weather" in query.lower():
             headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
             city = input("Enter the Name of City ->  ")
             city = city+" weather"
             weather(city)    
#///////////////////////////checks weather/////////////////////////////////////////#
            
            if 'activate how to do mod' in query.lower():
               speak("sir mode activated sucessfully!") 
               how =takecommand().lower()
               max_results = 1
               how_to = search_wikihow(how,max_results)
               assert len(how_to) == 1
               how_to[0].print()
               speak(how_to[0].summary)
#///////////////////////////tells ou cooking recipies/////////////////////////////////////////#
               
            if "check battery" in query.lower():
               import psutil
               battery = psutil.sensors_battery()
               plugged = battery.power_plugged
               percent = str(battery.percent)
               plugged = "Plugged In" if plugged else "Not Plugged In"
               speak('sir ,we are left with,'+percent+"percentage, of charge, | sir ,charger is"+plugged)
               print(percent+'% | '+plugged)
#///////////////////////////checks battery/////////////////////////////////////////#
           
            if 'open camera' in query.lower():
                import cv2
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k == 27:
                       break;
                cap.release()
                cv2.destroyAllWindows
#///////////////////////////opens camera/////////////////////////////////////////#

            