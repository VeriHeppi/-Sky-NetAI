import speech_recognition as sr

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            # Adjust for ambient noise and set the threshold
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            try:
                # Listen with a timeout and phrase time limit
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
            return ""
