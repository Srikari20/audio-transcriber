import os
from pydub.utils import which
from pydub import AudioSegment
import whisper
import streamlit as st

# Ensure ffmpeg path is set (required by pydub)
os.environ["PATH"] += os.pathsep + "/usr/bin"
AudioSegment.converter = which("ffmpeg")

# Load Whisper model once
model = whisper.load_model("base")

st.title("🎤 Audio Transcriber")

# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    # Show a transcribe button
    if st.button("Transcribe"):
        with open("temp_audio.wav", "wb") as f:
            audio = AudioSegment.from_file(uploaded_file)
            audio.export(f, format="wav")
            f.flush()

        # Run transcription
        result = model.transcribe("temp_audio.wav")

        # Show transcription result
        st.markdown("### Transcription:")
        st.write(result["text"])

        # Allow download
        st.download_button(
            label="📥 Download Transcription",
            data=result["text"],
            file_name="transcription.txt",
            mime="text/plain"
        )
