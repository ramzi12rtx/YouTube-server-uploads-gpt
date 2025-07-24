import os
from datetime import datetime
from src.text_generator import generate_script
from src.download_image import download_image
from src.audio_generator import text_to_speech
from src.video_generator import create_video
from src.youtube_uploader import upload_video

def main():
    print("🎯 بدء العملية اليومية")

    # 1. توليد النص
    print("🧠 1. توليد نص...")
    try:
        script = generate_script()
    except Exception as e:
        print("❌ Error generating script:", e)
        script = "مرحبًا بكم في فيديو جديد! ترقبوا معلومات مدهشة قادمًا 😉"
    print(f"✅ النص: {script}")

    # 1.1 جلب صورة تلقائيًا
    print("🖼️ 1.1 جلب صورة تلقائيًا...")
    try:
        image_path = download_image(script)  # يتم حفظ الصورة في assets/background.jpg
        print(f"✅ Image downloaded to {image_path}")
    except Exception as e:
        print("❌ Error downloading image:", e)
        return

    # 2. تحويل النص إلى صوت
    print("🔊 2. تحويل النص إلى صوت...")
    audio_path = text_to_speech(script)
    if not audio_path:
        print("❌ Failed to generate audio.")
        return

    # 3. إنشاء الفيديو
    print("🎞️ 3. إنشاء الفيديو...")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    video_path = f"output/video_{timestamp}.mp4"
    try:
        create_video(image_path, audio_path, video_path)
        print(f"✅ Video saved at: {video_path}")
    except Exception as e:
        print("❌ Error generating video:", e)
        return

    # 4. رفع الفيديو إلى YouTube
    print("📤 4. رفع الفيديو إلى YouTube...")
    try:
        upload_video(video_path, script)
    except Exception as e:
        print("❌ Error uploading video:", e)

if __name__ == "__main__":
    main()
