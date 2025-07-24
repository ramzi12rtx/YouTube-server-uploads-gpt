import os
import time
from src.audio_generator import text_to_speech
from src.video_generator import create_video
from src.youtube_uploader import upload_video
from src.download_image import download_image
from datetime import datetime

def main():
    print("🎯 بدء العملية اليومية")

    # 1. توليد نص (أو استخدام نص ثابت إن لم يتوفر GPT)
    try:
        from src.text_generator import generate_script
        script = generate_script()
    except Exception as e:
        print(f"❌ Error generating script: {e}")
        script = "مرحبًا بكم في فيديو جديد! ترقبوا معلومات مدهشة قادمًا 😉"

    print("✅ النص:", script)

    # 1.1 جلب صورة تلقائيًا من Pexels
    print("🖼️ 1.1 جلب صورة تلقائيًا...")
    try:
        image_path = download_image(script)
    except Exception as e:
        print(e)
        image_path = "assets/default.jpg"  # صورة افتراضية في حال الفشل

    # 2. تحويل النص إلى صوت
    print("🔊 2. تحويل النص إلى صوت...")
    audio_path = text_to_speech(script)

    # 3. إنشاء الفيديو
    print("🎞️ 3. إنشاء الفيديو...")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    video_path = f"output/video_{timestamp}.mp4"
    create_video(image_path, audio_path, video_path)
    print("✅ Video saved at:", video_path)

    # 4. رفع الفيديو إلى YouTube
    print("📤 4. رفع الفيديو إلى YouTube...")
    upload_video(video_path, script)

if __name__ == "__main__":
    main()
