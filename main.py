from query import executeQuery
from speak import Speak
import speech_recognition as sr 
r = sr.Recognizer()
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')
def Speaking():
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        try:
            text = r.recognize_google(audio_data)
            print(text)
        except:
            Speak("please repeat again")
            Speaking()
        return text
Speak('From which table or View you need data')
tableName=Speaking()
tableName=tableName.replace(' ','_')
Speak('Do you Need every colonm')
if(Speaking()=='yes'):
   colunm='*'
a=executeQuery(f"SELECT {colunm} FROM public.{tableName}")
print(a)