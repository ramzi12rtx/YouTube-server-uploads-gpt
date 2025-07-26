import os
import requests
from urllib.parse import quote

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
MUSIC_DIR = "assets/music"
os.makedirs(MUSIC_DIR, exist_ok=True)

# تحديد نوع الموسيقى المناسب حسب محتوى النص
def detect_music_category(text):
    text = text.lower()
    if any(word in text for word in ["motivation", "success", "winner", "goal"]):
        return "motivational"
    elif any(word in text for word in ["calm", "relax", "peaceful", "focus"]):
        return "calm"
    elif any(word in text for word in ["sad", "emotional", "deep"]):
        return "dramatic"
    else:
        return "cinematic"  # افتراضي

# تنزيل الموسيقى من Pixabay
def download_music(text):
    category = detect_music_category(text)
    print(f"🎵 Detecting category: {category}")

    url = f"https://pixabay.com/api/sounds/?key={PIXABAY_API_KEY}&q={quote(category)}&per_page=3"
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Failed to fetch music:", response.text)
        return None

    results = response.json().get("hits")
    if not results:
        print("❌ No music found.")
        return None

    audio_url = results[0]["audio"]
    music_path = os.path.join(MUSIC_DIR, "bg_music.mp3")

    with open(music_path, "wb") as f:
        f.write(requests.get(audio_url).content)
    print(f"✅ Music downloaded to {music_path}")
    return music_path
