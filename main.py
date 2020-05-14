import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
# Init voice recognizer
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak_gtts(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak_gtts(
                'Sorry I couldnt understand you with your mask on,master Bruce')
        except sr.RequestError:
            speak_gtts('Sorry my service is down. I needed to use the washroom')
        return voice_data


# Make alfred talk using google text-to-speech
def speak_gtts(audio_string):
    # We can use other languages if we want
    tts = gTTS(text=audio_string, lang='en-in')
    r = random.randint(1, 1000000)
    # Making the name for the audio file
    audio_file = 'audio-'+str(r) + '.mp3'
    tts.save(audio_file)
    # PLay the audio file
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'who are you' in voice_data:
        speak_gtts(
            "My name is Alfred. I'm your own personal assistant.")
    if "I'm hungry" in voice_data:
        speak_gtts('Eat fruits and drink milk to stay healthy!')
    if 'what time is it' in voice_data:
        speak_gtts(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak_gtts('Here is what I found for '+search)
    if 'find location' in voice_data:
        location = record_audio('Which location do you want to see?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak_gtts('Here is what I found for '+location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
speak_gtts('Hello Ranjha! How can I help you?')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
