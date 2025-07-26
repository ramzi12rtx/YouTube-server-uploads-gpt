import os
from datetime import datetime
from src.text_generator import generate_script
from src.download_image import download_image
from src.audio_generator import text_to_speech
from src.video_generator import create_video
from src.music_selector import download_music
from src.youtube_uploader import upload_video

def main():
    print("🎯 بدء العملية اليومية")

    print("🧠 1. توليد النص...")
    try:
        script = generate_script()
    except:
        script = "Welcome! Here's an interesting fact for you today!"
    print(f"✅ النص: {script}")

    print("🖼️ 1.1 تحميل صورة...")
    image_path = download_image(script)

    print("🔊 2. توليد الصوت...")
    audio_path = text_to_speech(script)

    print("🎵 2.1 تحميل موسيقى...")
    music_path = download_music("inspiring")

    print("🎞️ 3. إنشاء الفيديو...")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    video_path = f"output/video_{timestamp}.mp4"
    create_video(image_path, audio_path, video_path)
    print(f"✅ تم حفظ الفيديو: {video_path}")

    print("📤 4. رفع الفيديو...")
    upload_video(video_path, script)

if __name__ == "__main__":
    main()
