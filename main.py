import sys
print("🔍 Python version:", sys.version)
print("📦 Modules:", sys.path)

try:
    import moviepy
    print("✅ moviepy imported successfully!")
except Exception as e:
    print("❌ moviepy import failed:", e)
from src.generate_script import generate_script
from src.text_to_speech import text_to_speech
from src.create_video import create_video
from src.upload_youtube import upload_video
from src.image_downloader import download_random_image

import datetime
import platform
import sys

def main():
    print(f"🔍 Python version: {platform.python_version()} {sys.version}")
    print(f"📦 Modules: {sys.path}")

    print("🎯 بدء العملية اليومية")

    print("🧠 1. توليد نص...")
    try:
        script = generate_script()
    except Exception as e:
        print("❌ Error generating script:", e)
        script = "مرحبًا بكم في فيديو جديد! ترقبوا معلومات مدهشة قادمًا 😉"
    print("✅ النص:", script)

    print("🖼️ 1.1 جلب صورة تلقائيًا...")
    download_random_image(script)

    print("🔊 2. تحويل النص إلى صوت...")
    audio_path = text_to_speech(script)

    print("🎞️ 3. إنشاء الفيديو...")
    video_path = create_video(audio_path)
    print("✅ Video saved at:", video_path)

    print("📤 4. رفع الفيديو إلى YouTube...")
    upload_video(video_path, script)

if __name__ == "__main__":
    main()
