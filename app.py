import streamlit as st
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\YourName\Downloads\ffmpeg-6.0-full_build\bin"
import whisper
import tempfile
import os

# Page setup
st.set_page_config(page_title="Whisper Transcriber", layout="centered")
st.title("🎤 Whisper Audio Transcriber")

# Upload audio file
uploaded_file = st.file_uploader("Upload your audio file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save uploaded file to temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Load Whisper model
    model = whisper.load_model("base")  # use "tiny" for faster response

    # Transcribe audio
    st.info("Transcribing...")
    result = model.transcribe(tmp_path)

    # Display result
    st.subheader("Transcription:")
    st.write(result["text"])

    # Remove temp file
    os.remove(tmp_path)
