import speech_recognition as sr

def transcribe_audio(file_path, engine='google'):
    """
    Transcribes audio from a file using the specified speech recognition engine.

    Args:
        file_path (str): Path to the audio file.
        engine (str): Speech recognition engine to use ('google', 'sphinx', etc.).

    Returns:
        str: Transcribed text from the audio file.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    # Transcribe the audio using the specified engine
    try:
        if engine == 'google':
            transcription = recognizer.recognize_google(audio_data)
        elif engine == 'sphinx':
            transcription = recognizer.recognize_sphinx(audio_data)
        else:
            raise ValueError("Unsupported engine. Use 'google' or 'sphinx'.")

        return transcription
    
    except sr.UnknownValueError:
        return "Sorry, the audio could not be understood."
    except sr.RequestError as e:
        return f"Could not request results from the speech recognition service; {e}"