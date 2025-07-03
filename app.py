import streamlit as st
import os
import tempfile
from audio_utils.converter import convert_to_wav
from audio_utils.stats import get_audio_stats
from audio_utils.transcriber import transcribe_audio

# Streamlit app configuration
st.set_page_config(
    page_title="Audio Transcriber", 
    page_icon="🎙️", 
    layout="centered"
)

# --- Sidebar: Info Section ---
with st.sidebar:
    st.markdown("## ℹ️ About This App")
    st.write(
        """
        This app lets you upload an audio file, extract key stats,
        and transcribe it using speech recognition.
        """
    )
    st.markdown("> ⚠️ **Note:** Only files shorter than 5 minutes are recommended for best performance.")

    st.markdown("## 🛠️ Built With")
    st.write("- Python \n- Streamlit\n- speech_recognition\n- pydub\n- ffmpeg")

    st.markdown("---")
    st.markdown("**Built with 💙 and curiosity by Kofoworola Egbinola**  \nConnect: [LinkedIn](https://www.linkedin.com/in/kofoworola-egbinola-m)")
    st.caption("Part of my Data Science & NLP learning journey 🚀")

# Main title and description
st.markdown(
    "<h2 style='text-align: center;'>🎙️ Simple Audio Transcriber</h2>"
    "<p style='text-align: center; font-size: 16px;'>Upload audio → See stats → Get transcription instantly</p>",
    unsafe_allow_html=True,
)

# --- Upload or Use Sample ---
st.markdown("### 📂 Upload Your Audio File or Try with a Sample")

uploaded_file_path = None
file_source = None  # 'sample' or 'upload'

use_sample = st.checkbox(
    "Use Sample Audio", 
    value=False, 
    help="Check to use a sample audio file instead of uploading your own."
)

if use_sample:
    sample_path = "samples/sample_audio.m4a"
    if os.path.exists(sample_path):
        with open(sample_path, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/m4a")
        st.success("Sample audio loaded successfully!")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
            tmp.write(audio_bytes)
            uploaded_file_path = tmp.name

        file_source = "sample"
    else:
        st.error("Sample audio file not found.")

else:
    uploaded = st.file_uploader(
        "🗜️ Upload an audio file:",
        type=["wav", "mp3", "m4a", "flac"],
        help="Audio will be converted to WAV for transcription"
    )
    if uploaded:
        st.audio(uploaded, format="audio/wav")
        suffix = "." + uploaded.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.getbuffer())
            uploaded_file_path = tmp.name

        st.success(f"File '{uploaded.name}' uploaded successfully!")
        file_source = "upload"

# Proceed if a file is uploaded or sample is selected
if uploaded_file_path:
    if not uploaded_file_path.lower().endswith('.wav'):
        st.write("Converting audio file to .wav format...")
        wav_file_path = convert_to_wav(uploaded_file_path)
        st.success("Conversion complete.")
    else:
        wav_file_path = uploaded_file_path
        st.success("Audio file is already in .wav format.")

    with st.expander("📊 View Audio Stats"):
        stats = get_audio_stats(wav_file_path)
        for k, v in stats.items():
            st.markdown(f"**{k}**: {v}")

    if st.button("📝 Transcribe Audio"):
        with st.spinner("Transcribing audio..."):
            transcription = transcribe_audio(wav_file_path)
        st.session_state["transcription"] = transcription
        st.success("Transcription completed!")

    if "transcription" in st.session_state:
        transcription = st.session_state["transcription"]
        st.markdown("### 📒 Transcription")
        st.text_area("View transcription below:", transcription, height=300)

        st.markdown("#### 📊 Transcription Stats")
        st.markdown(f"- **Word Count**: {len(transcription.split())}")
        st.markdown(f"- **Character Count**: {len(transcription)}")

        output_name = (
            "sample_audio" if file_source == "sample"
            else os.path.splitext(os.path.basename(uploaded_file_path))[0]
        )

        st.download_button(
            label="📅 Download as .txt",
            data=transcription,
            file_name=f"{output_name}_transcription.txt",
            mime="text/plain"
        )