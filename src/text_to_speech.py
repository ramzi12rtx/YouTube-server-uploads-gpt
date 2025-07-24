# src/text_to_speech.py
from gtts import gTTS
import os
from datetime import datetime

def text_to_speech(text, lang='ar'):
    filename = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    output_path = os.path.join("output", filename)

    os.makedirs("output", exist_ok=True)

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"✅ Saved audio to {output_path}")
        return output_path
    except Exception as e:
        print("❌ Error generating audio:", e)
        return None
