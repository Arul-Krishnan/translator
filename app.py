import os

# ✅ Set environment variables BEFORE importing pydub
os.environ["PATH"] += os.pathsep + r"C:\xampp1\htdocs\ffmpeg\bin"
os.environ["FFMPEG_BINARY"] = r"C:\xampp1\htdocs\ffmpeg\bin\ffmpeg.exe"
os.environ["FFPROBE_BINARY"] = r"C:\xampp1\htdocs\ffmpeg\bin\ffprobe.exe"

from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator

def convert_audio_to_wav(audio_path):
    """Convert audio to WAV if it's not already in WAV format."""
    if not audio_path.lower().endswith('.wav'):
        sound = AudioSegment.from_file(audio_path)
        wav_path = os.path.splitext(audio_path)[0] + '.wav'
        sound.export(wav_path, format="wav")
        print(f"✅ Converted to WAV: {wav_path}")
        return wav_path
    return audio_path

def transcribe_and_translate(audio_path, target_lang='en'):
    recognizer = sr.Recognizer()
    translator = Translator()

    wav_path = convert_audio_to_wav(audio_path)

    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"\n🗣️ Recognized Speech: {text}")

            translated = translator.translate(text, dest=target_lang)
            print(f"🌐 Detected Language: {translated.src}")
            print(f"📘 Translated Text ({target_lang}): {translated.text}")

        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError as e:
            print(f"❌ API request error: {e}")

# 👇 Replace this with your actual file path
audio_file_path = "test.mp3"
transcribe_and_translate(audio_file_path)
