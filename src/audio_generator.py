import requests
import os
from datetime import datetime
from pydub import AudioSegment

def download_music_from_pixabay(query="motivational"):
    api_key = os.getenv("PIXABAY_API_KEY")
    url = f"https://pixabay.com/api/sounds/?key={api_key}&q={query}&per_page=3"

    try:
        response = requests.get(url)
        response.raise_for_status()
        hits = response.json().get("hits", [])
        if not hits:
            raise Exception("لم يتم العثور على موسيقى")

        music_url = hits[0]["audio"]
        response = requests.get(music_url)
        response.raise_for_status()

        os.makedirs("temp_music", exist_ok=True)
        music_path = "temp_music/bg_music.mp3"
        with open(music_path, "wb") as f:
            f.write(response.content)
        print("🎵 تم تحميل الموسيقى بنجاح")
        return music_path

    except Exception as e:
        print("❌ Error downloading music:", e)
        return None

def text_to_speech(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "EXAVITQu4vr4xnSDxMaL"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.75}
    }

    os.makedirs("output", exist_ok=True)
    tts_path = f"output/audio_{datetime.now().strftime('%Y%m%d%H%M%S')}_tts.mp3"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        with open(tts_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved TTS audio to {tts_path}")
    except Exception as e:
        print("❌ Error generating audio:", e)
        return None

    # 🎶 دمج الموسيقى مع الصوت
    music_path = download_music_from_pixabay(query="emotional" if "love" in text.lower() else "motivational")
    if music_path:
        try:
            voice = AudioSegment.from_file(tts_path)
            music = AudioSegment.from_file(music_path).set_frame_rate(voice.frame_rate).set_channels(voice.channels)

            # ضبط مستوى صوت الموسيقى
            music = music - 18
            combined = voice.overlay(music, loop=True)
            final_path = tts_path.replace("_tts", "")
            combined.export(final_path, format="mp3")
            print(f"🎧 Final audio saved at: {final_path}")
            return final_path
        except Exception as e:
            print("❌ Error mixing audio:", e)
            return tts_path  # إعادة الصوت بدون موسيقى
    else:
        return tts_path  # فقط صوت ElevenLabs
