import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

from pydub import AudioSegment
from pydub.playback import play

class TextToSpeech:
    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        self._client = client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def speak(self, text):
        
        speech_file_path = Path(__file__).parent / "speech.mp3"
        with self._client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="nova",
        input=text,
        ) as response: 
            response.stream_to_file(speech_file_path)

        audio = AudioSegment.from_mp3(speech_file_path)
        play(audio)
    