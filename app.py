import whisper
import streamlit as st
import tempfile

st.title("🎤 Audio Transcriber (Whisper Only)")

model = whisper.load_model("tiny")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp.flush()

        result = model.transcribe(tmp.name)
        st.markdown("### Transcription:")
        st.write(result["text"])
