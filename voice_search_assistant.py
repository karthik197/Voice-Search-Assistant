import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)
#initialize Recognizer
rec = sr.Recognizer()
rec.energy_threshold = 5000

#use microphone audio input as source
with sr.Microphone() as src:
    print('Speak')
    audio = rec.listen(src)
    try:
        #text output
        text = rec.recognize_google(audio)
        print(text)
        url = 'https://www.google.com/search?q='
        search = url + text
        webbrowser.open(search)
    except:
        print("Can't Recognize")