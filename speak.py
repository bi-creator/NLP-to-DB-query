import pyttsx3
def Speak(toSpeak):
    engine = pyttsx3.init() 
    engine.setProperty('rate', 150)  
    # rate = engine.getProperty('rate')
    # volume = engine.getProperty('volume')   
    engine.setProperty('volume',1.0)   
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[1].id)   
    # engine.say("Hello World!")
    engine.say(toSpeak)
    engine.runAndWait()
    engine.stop()
