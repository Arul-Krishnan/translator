import whisper
import os

# ✅ Set environment variables BEFORE importing pydub
os.environ["PATH"] += os.pathsep + r"C:\xampp1\htdocs\ffmpeg\bin"
os.environ["FFMPEG_BINARY"] = r"C:\xampp1\htdocs\ffmpeg\bin\ffmpeg.exe"
os.environ["FFPROBE_BINARY"] = r"C:\xampp1\htdocs\ffmpeg\bin\ffprobe.exe"

def transcribe_and_translate_whisper(audio_path):
    # Load the Whisper model (use 'base', 'small', 'medium', or 'large' for better accuracy)
    model = whisper.load_model("tiny")

    # Transcribe and translate
    result = model.transcribe(audio_path, task="translate")  # "translate" outputs English

    print("\n📄 Original Transcription (translated to English):")
    print(result["text"])

# 🔊 Provide the path to your audio file (mp3, wav, m4a, etc.)
audio_file = "sample-2.mp3"
transcribe_and_translate_whisper(audio_file)
