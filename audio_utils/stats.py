import os
from pydub import AudioSegment
from pydub.utils import which

# Ensure ffmpeg is available
AudioSegment.converter = which('ffmpeg')

def get_audio_stats(file_path):
    """
    Retrieves basic statistics from an audio file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        dict: A dictionary containing audio duration and sample rate.
    """
    # Ensure file is in .wav format
    if not file_path.lower().endswith('.wav'):
        raise ValueError("The file must be in .wav format.")
    
    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Get audio statistics
    stats = {
        'File Name': os.path.basename(file_path),
        'File Size (KB)': round(os.path.getsize(file_path) / 1024, 2),  # File size in KB
        'Duration (seconds)': round(len(audio) / 1000, 2),  # Duration in seconds
        'Channels': audio.channels,
        'Frame Rate': audio.frame_rate,
        'Sample Width (bytes)': audio.sample_width,
        'Bitrate (kbps)': round((audio.frame_rate * audio.sample_width * 8) / 1000, 2)  # Bit rate in kbps
    }    
    return stats