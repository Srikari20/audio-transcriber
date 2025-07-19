import streamlit as st
import whisper
from pydub import AudioSegment
import tempfile
import os

st.set_page_config(page_title="Whisper Transcriber", layout="centered")

st.title("🎧 Audio Transcriber")
st.write("Upload an audio file (MP3, WAV, M4A) to get a transcription using OpenAI's Whisper model.")

uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio = AudioSegment.from_file(uploaded_file)
        audio.export(tmp.name, format="wav")
        wav_file = tmp.name

    st.info("Transcribing... please wait ⏳")

    model = whisper.load_model("base")  # Change to "tiny" if needed
    result = model.transcribe(wav_file)
    transcription = result["text"]

    st.subheader("📝 Transcription:")
    st.write(transcription)

    st.download_button("📥 Download as .txt", transcription, file_name="transcription.txt")

    os.remove(wav_file)
