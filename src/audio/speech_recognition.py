import speech_recognition as sr
from audio.text_to_speech import TextToSpeech
import time

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.wake_word = "assistant"  # Define your wake word
        self.end_phrase = "that's all assistant"
        self.conversation_mode = False
        self.last_command_time = None
        self.text_to_speech = TextToSpeech()
        self.conversation_timeout = 60 # timeout duration in seconds

    def listen_for_wake_word(self):
        with sr.Microphone() as source:
            # Adjust for ambient noise and set the threshold
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for wake word...")
            try:
                
                # Listen for the wake word with a timeout and phrase time limit
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")
                
                if self.wake_word in text:
                    print("Wake word detected. Listening for command...")
                    self.text_to_speech.greeting()
                    self.conversation_mode = True
                    self.last_command_time = time.time()
                elif self.end_phrase in text:
                    print("End phrase detected. Exiting conversation mode...")
                    self.text_to_speech.speak("Goodbye!")
                    self.conversation_mode = False
                elif self.conversation_mode and time.time() - self.last_command_time > self.conversation_timeout:
                    print("Conversation timed out. Exiting conversation mode...")
                    self.text_to_speech.speak("Goodbye!")
                    self.conversation_mode = False
                elif self.conversation_mode:
                    # Listen for the actual command
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    command = self.recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    self.last_command_time = time.time()
                    return command
                else:
                    print("Wake word not detected.")
                    return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                # restart the function if the timeout error occurs
                return self.recognize_speech()
            return self.conversation_mode

    def continuous_listening(self):
        while True:
            command = self.recognize_speech()
            if command:
                return command
            
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
        