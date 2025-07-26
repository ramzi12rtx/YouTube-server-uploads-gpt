import requests
import os
from datetime import datetime

def text_to_speech(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "EXAVITQu4vr4xnSDxMaL"  # صوت إنجليزي احترافي (Rachel مثلاً)

    if not api_key:
        print("❌ ELEVENLABS_API_KEY is missing in environment variables.")
        return None

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text.strip(),
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.85,
            "use_speaker_boost": True
        }
    }

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"audio_{timestamp}_tts.mp3")

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Saved TTS audio to {output_path}")
        return output_path

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error: {http_err}")
    except Exception as e:
        print(f"❌ Error generating audio: {e}")

    return None
