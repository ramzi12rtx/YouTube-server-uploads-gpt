import requests
import os
from datetime import datetime

def text_to_speech(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "EXAVITQu4vr4xnSDxMaL"  # صوت إنجليزي احترافي

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }

    output_path = f"output/audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    os.makedirs("output", exist_ok=True)

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved audio to {output_path}")
        return output_path
    except Exception as e:
        print("❌ Error generating audio:", e)
        return None
