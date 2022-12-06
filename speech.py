# pip install PyAudio
# pip install SpeechRecognition

# import library
import speech_recognition as sr
def Micro_voice():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listenting the speech and store in audio_text variable

    with sr.Microphone(sample_rate = 20000) as source:
        print(" Silence please!")
        r.adjust_for_ambient_noise(source, duration = 2)
        print(" Speak now.....")
        audio_text = r.listen(source) # phrase_time_limit=30 number of time the microphone hear the voice.
        print("Time cover, thanks")

        # recognize_() method will throw a request error if the API is unreachable.
        text = r.recognize_google(audio_text)
        try:
            # using google speech recognition
            print("Text: " + text)
            return text
        except:
            print("Sorry, I did not get that")       