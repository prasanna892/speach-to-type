import speech_recognition as sr
import pyttsx3
import time
import pyperclip as clip
import pyautogui as gui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)         
    engine.runAndWait() 
     

print("press 't' for tamil or press 'e' for english or press 'h' for hindi ")
lang=input("choose your language :") 
lang=lang.lower()

print("for go to new line say 'new line'")
print("for tab space say 'tab space'")
print("for space say 'space bar'")
print("for backspace say 'backspace'")
print("for any symbol say that symbol name plus symbol")

if lang=='t':
    lang_in='ta-in'
elif lang=='e':
    lang_in='an-in'
elif lang=='h':
    lang_in='hi-in'

def takeCommand():
    global lang_in
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)     

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language=lang_in)
        print(f"User said: {query}\n")
         
    except Exception as e:
        print(e)    
        print("Say that again please...")
        query = 'Nothing'
        print("none")
    return query
 


if __name__=='__main__':
    print("waiting for your command")
    speak("waiting for your command")

    while True:
        query = takeCommand().lower()
        if query!='nothing':
            if lang=='e':
                if query=='new line':
                    gui.press('enter')
                elif query=='tab space':
                    gui.press('tab')
                elif query=='space bar':
                    gui.press('space')
                elif query=='backspace':
                    gui.press('space')
                elif query=='open bracket':
                    gui.press('(')
                elif query=='close bracket':
                    gui.press(')')
                elif query=='percentage symbol':
                    gui.press('%')
                elif query=='star symbol':
                    gui.press('*')
                elif query=='minus symbol':
                    gui.press('-')
                elif query=='under score':
                    gui.press('_')
                elif query=='equal to symbol':
                    gui.press('=')
                elif query=='divide symbol':
                    gui.press('/')
                elif query=='plus symbol':
                    gui.press('+')
                elif query=='at symbol':
                    gui.press('@')
                elif query=='exclamatry symbol':
                    gui.press('!')
                else:
                    text = query+' '
                    clip.copy(text)
                    time.sleep(0.3)
                    gui.hotkey('ctrl','v')   
            else:
                text = query+' '
                clip.copy(text)
                time.sleep(0.3)
                gui.hotkey('ctrl','v')   