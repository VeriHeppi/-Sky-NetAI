import openai
import os
from dotenv import load_dotenv

class Transcriber:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def transcribe_audio(self, file_path):
        audio_file = open(file_path, "rb")
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcription.text
