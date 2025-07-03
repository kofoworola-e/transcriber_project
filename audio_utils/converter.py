import tempfile
from pydub import AudioSegment
from pydub.utils import which

# Ensure ffmpeg is available
AudioSegment.converter = which('ffmpeg')

def convert_to_wav(file_path, output_dir='data/converted_audio'):
    """
    Converts an audio file to .wav format if it isn't already.

    Args:
        file_path (str): Path to the uploaded audio file.
    
    Returns:
        str: Path to the converted .wav file.
    """
    # Load the input audio
    audio = AudioSegment.from_file(file_path)

    # Create a temporary file for the .wav output
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_wav:
        audio.export(tmp_wav.name, format='wav')
        return tmp_wav.name