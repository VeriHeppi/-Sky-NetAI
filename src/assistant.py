from audio.speech_recognition import SpeechRecognition
from audio.text_to_speech import TextToSpeech
from audio.transcriber import Transcriber
from my_calendar.calendar_event import CalendarEvent
from nlp.openai_client import OpenAIClient

MODEL_D = "gpt-3.5-turbo-0125"
MODEL_E = "gpt-4o"

class Assistant:
    def __init__(self):
        self.speech_recognizer = SpeechRecognition()
        self.text_to_speech = TextToSpeech()
        self.transcriber = Transcriber()
        self.calendar = CalendarEvent()
        self.nlp_client = OpenAIClient()

    def handle_command(self):
        command = self.speech_recognizer.recognize_speech()
        if "calendar" in command:
            self.text_to_speech.speak("What event would you like to schedule?")
            event = self.speech_recognizer.recognize_speech()
            self.text_to_speech.speak("When is the event?")
            time = self.speech_recognizer.recognize_speech()
            self.calendar.create_event(event, time, 60)
            self.text_to_speech.speak(f"Event {event} scheduled at {time}")
        elif "search" in command:
            self.text_to_speech.speak("What would you like to search for?")
            query = self.speech_recognizer.recognize_speech()
            result = self.nlp_client.ask_openai(f"Search the web for {query}", MODEL_D)
            self.text_to_speech.speak(result)
        elif "programming" in command:
            self.text_to_speech.speak("What programming help do you need?")
            question = self.speech_recognizer.recognize_speech()
            answer = self.nlp_client.ask_openai(question, MODEL_E)
            self.text_to_speech.speak(answer)
        elif "stop" in command:
            self.text_to_speech.speak("Goodbye!")
        else:
            response = self.nlp_client.ask_openai(command, MODEL_D)
            self.text_to_speech.speak(response)
