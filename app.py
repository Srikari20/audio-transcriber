import streamlit as st
import whisper
from pydub import AudioSegment
import tempfile
import os

st.set_page_config(page_title="Audio Transcriber", layout="centered")

st.title("🎙️ Audio Transcriber")
st.write("Upload an audio file and get the transcription using OpenAI Whisper.")

uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file)

    # Convert uploaded file to WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio = AudioSegment.from_file(uploaded_file)
        audio.export(tmp.name, format="wav")
        wav_path = tmp.name

    model = whisper.load_model("base")
    st.info("Transcribing... please wait ⏳")
    result = model.transcribe(wav_path)
    transcription = result["text"]

    st.subheader("📝 Transcription:")
    st.write(transcription)

    st.download_button("📥 Download Transcript", transcription, file_name="transcript.txt")

    os.remove(wav_path)
