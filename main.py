import speech_recognition as sr
import webbrowser
import pyttsx3
import audioFile
import wikipedia
import pyautogui
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Selecting the  voice 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate' , 210)



#Speak Function....

def speak(text):
    engine.say(text)
    engine.runAndWait()

#For Processing Commands....


def processCommand(c):

    #Open and Close Apps...
    if 'open' in c.lower() or 'close' in c.lower():
        c=c.lower()
        print(c)
        def open_app(app):
            pyautogui.moveTo(27,743,duration=1)
            pyautogui.click()
            pyautogui.sleep(0.3)
            app = app.replace('open', "")
            pyautogui.typewrite(app)

            pyautogui.sleep(1)
            pyautogui.press('enter')

        def close_app(app):
            pyautogui.moveTo(27,743,duration=1)
            pyautogui.click()
            pyautogui.sleep(0.3)
            app = app.replace('close','')
            pyautogui.typewrite(app)
            pyautogui.sleep(1)
            pyautogui.press('enter')


            pyautogui.sleep(1)


            pyautogui.moveTo(1344,9,duration=1)
            pyautogui.click()
            

            
    
        if "open" in c:
            open_app(c)

        elif "close"     in c:
            close_app(c)
        
          
        
#Speech to Text..


    elif "type" in c.lower():
        c=c.replace("type","")
        pyautogui.typewrite(c)

#For deleting a element in typing
    elif "remove" in c.lower():
        pyautogui.press('backspace')
#For deleting all  
    elif "delete all" in c.lower():
        pyautogui.hotkey('ctrl','a')
        pyautogui.sleep(0.5)
        pyautogui.press('backspace')

#For searching and opening a chat in Whatsapp
    elif "search" in c.lower():
        c=c.replace('search',"")
        pyautogui.typewrite(c)
        pyautogui.moveTo(207,181,duration= 0.5)
        pyautogui.sleep(0.5)
        pyautogui.click()
#For closing window
    elif "cancel window" in c.lower():
        pyautogui.moveTo(1344,9,duration=1)
        pyautogui.click()

#For a single click
    elif "click" in c.lower():
        pyautogui.click()
#For Enter button
    elif "press enter" in c.lower():
        pyautogui.press('enter')
#Open websites with the help of Webbrowser module..
    elif "google" in c.lower():
        webbrowser.open('https://google.com')
    elif "youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "instagram" in c.lower():
        webbrowser.open('https://instagram.com')
    elif "emails" in c.lower():
        webbrowser.open('https://gmail.com')
    
# plays youtube video songs if you have a file named "audioFile" and
#  contains a list of song with their respective urls 
#  in form of key and value in dictionary named music  
    
    
    elif c.lower().startswith('play'):
        song = c.lower().split(' ')[1]
        link = audioFile.music[song]
        webbrowser.open(link)


    
#Using wikipedia module
    elif 'wikipedia' in c.lower():
            speak('Searching Wikipedia...')
            c = c.replace("wikipedia", "")
            results = wikipedia.summary(c, sentences=2)
            speak("According to Wikipedia")
            print(c)
            print(results)
            speak(results)
    else:
        print(c)

if __name__=="__main__":
    speak('....INITIALISING JARVIS.... ')
    while True:
        r = sr.Recognizer()
        
        
            
        try:
            #Waking Up jarvis (wave up call)
            with sr.Microphone() as source:
                print('Listening....')
                
                audio = r.listen(source ,timeout= 2)
                print('Recognizing....')
                word = r.recognize_google(audio)

            if 'jarvis' in word.lower():
                speak(' Jarvis Activated , How can i help you sir... ') 
                
                while True:
                    try:
                        #Jarvis activated , listening and understanding speech
                        with sr.Microphone() as source:
                            print('Jarvis activated....')
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source ,timeout= 4 , phrase_time_limit=3 )
                            print('Recognizing....')
                            command = r.recognize_google(audio)
                            processCommand(command)
                        #Jarvis Off
                        if "sleep" in command.lower():
                            speak('Going to sleep , see you soon')
                            break
                       
                            
                    except Exception:
                        print('timeout')
            #Exit program
            if "switch off" in word.lower():
                speak('switching off')
                break
                
        except Exception as b:
            print("TIMEoUT")
 

        

