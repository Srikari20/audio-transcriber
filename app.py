from flask import Flask, request, jsonify
import whisper
from pydub import AudioSegment
import tempfile
import os
import pyaudioop as audioop
app = Flask(__name__)
model = whisper.load_model("tiny")  # You can change to "tiny" if needed

@app.route('/')
def home():
    return "Whisper Audio Transcriber API is Running!"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files['file']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        audio = AudioSegment.from_file(audio_file)
        audio.export(tmp.name, format="wav")
        result = model.transcribe(tmp.name)
        os.remove(tmp.name)

    return jsonify({"transcription": result["text"]})
