import requests
import os
from datetime import datetime

# يمكنك تغيير هذا إلى صوت آخر من لوحة ElevenLabs
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Rachel - إنجليزي واقعي ومحترف
MODEL_ID = "eleven_multilingual_v2"  # يدعم نطق أفضل وأكثر تنوعًا

def text_to_speech(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")

    if not api_key:
        raise EnvironmentError("❌ ELEVENLABS_API_KEY غير موجود في المتغيرات البيئية.")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.4,             # ثبات أقل = تعبير أكثر واقعية
            "similarity_boost": 0.85,     # صوت طبيعي جداً
            "style": 1.2,                 # أسلوب مميز
            "use_speaker_boost": True     # تحسين جودة الصوت
        }
    }

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_dir = "output"
    output_path = os.path.join(output_dir, f"audio_{timestamp}.mp3")
    os.makedirs(output_dir, exist_ok=True)

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved audio to {output_path}")
        return output_path
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"❌ Error generating audio: {e}")
    
    return None
