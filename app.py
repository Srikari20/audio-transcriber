import os
from pydub import AudioSegment
from pydub.utils import which
import whisper
import streamlit as st

# Fix ffmpeg path for Streamlit Cloud
os.environ["PATH"] += os.pathsep + "/usr/bin"
AudioSegment.converter = which("ffmpeg")

# Load Whisper model
model = whisper.load_model("base")

st.title("🎤 Audio Transcriber")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg"])

if uploaded_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    audio = AudioSegment.from_file("temp_audio.wav")
    audio.export("converted.wav", format="wav")

    result = model.transcribe("converted.wav")
    st.markdown("### Transcription:")
    st.write(result["text"])
