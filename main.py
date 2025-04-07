from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import whisper
import os
import shutil

# ✅ Configure ffmpeg path


# ✅ Load Whisper model (use "tiny", "base", "small", "medium", "large")
model = whisper.load_model("base")

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Transcribe and translate
        result = model.transcribe(temp_file_path, task="translate")  # output in English
        os.remove(temp_file_path)  # clean up temp file

        return JSONResponse(content={
            "translated_text": result["text"]
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
