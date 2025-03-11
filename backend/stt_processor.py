import openai

def transcribe_audio(file_path):
    """
    Transcribes an audio file using OpenAI's Whisper model.
    
    :param file_path: Path to the audio file
    :return: Transcribed text
    """
    client = openai.OpenAI()  # Initialize OpenAI client

    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )

    return response.text  # Extract transcribed text
