
# 🎙️ Simple Audio Transcriber

A lightweight Streamlit app that lets you upload short audio files, extract audio stats, and generate clean transcriptions using speech recognition. Built as part of my NLP learning journey.


## ✨ Features

- 📂 Upload or test with a sample audio file  
- 🔄 Auto-converts to `.wav` for compatibility  
- 📊 Displays audio metadata (channels, duration, etc.)  
- 📝 Transcribes audio using the `speech_recognition` library  
- 📥 Download your transcription as `.txt`  


## 🛠️ Tech Stack

- **Python 3.11+**
- [Streamlit](https://streamlit.io/)
- [pydub](https://github.com/jiaaro/pydub)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [ffmpeg](https://ffmpeg.org/) (for audio processing)


## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/kofoworola-e/transcriber_project.git
cd transcriber_project

# Create and activate environment
conda create -n transcriber python=3.11 -y
conda activate transcriber

# Install dependencies
pip install -r requirements.txt

# Set up FFmpeg manually:
# 1. Download from https://www.gyan.dev/ffmpeg/builds/
# 2. Extract and copy the path to ffmpeg.exe

# Run the Streamlit app
streamlit run app.py
```
---

## 🧪 Sample Audio

A short sample audio is provided in the `samples/` folder for quick testing.

**Recommended**: Use audio files under 5 minutes for best results.


## 🧼 Why `tempfile`?

This project uses Python's `tempfile` module to handle audio files in memory, ensuring automatic cleanup and making it safe for cloud deployment.


## 🧠 Inspiration & Reflections

This project was a hands-on way to reinforce concepts from audio data processing and speech recognition. While building it, I deepened my understanding of file handling, audio conversion, and streamlining workflows for deployment — especially the value of tools like `tempfile` and `ffmpeg`.

It will continue to evolve as my skills grow — expect more advanced features in the future like speaker diarization, noise filtering, or multi-language support.


---

## 📄 License

This project is licensed under the MIT License.

**Built with 💙 and curiosity by Kofoworola Egbinola**