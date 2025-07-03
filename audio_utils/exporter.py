import os

def export_as_txt(transcription, filename, output_dir='outputs'):
    """
    Exports the transcribed text to a .txt file.

    Args:
        transcription (str): The transcribed text to export.
        filename (str): The name of the file to save the transcription as.
        output_dir (str): Directory to save the .txt file.
    """
    # Check if the output directory exists, create it if not
    os.makedirs(output_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(output_dir, f"{filename}.txt")

    # Write the transcription to the .txt file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    print(f"Transcription exported to {output_file}")