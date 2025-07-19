import os
from pydub.utils import which

os.environ["PATH"] += os.pathsep + "/usr/bin"
AudioSegment.converter = which("ffmpeg")

import os
from pydub import AudioSegment
from pydub.utils import which
import whisper
import streamlit as st

# Fix ffmpeg path for Streamlit Cloud
os.environ["PATH"] += os.pathsep + "/usr/bin"
AudioSegment.converter = which("ffmpeg")

# Load model
model = whisper.load_model("base")

st.title("🎤 Audio Transcriber")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg"])

if uploaded_file is not None:
    with open("temp_audio.wav", "wb") as f:
        audio = AudioSegment.from_file(uploaded_file)
        audio.export(f, format="wav")
        f.flush()

    result = model.transcribe("temp_audio.wav")
    st.markdown("### Transcription:")
    st.write(result["text"])
