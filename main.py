import sys
print("🔍 Python version:", sys.version)
print("📦 Modules:", sys.path)

try:
    import moviepy
    print("✅ moviepy imported successfully!")
except Exception as e:
    print("❌ moviepy import failed:", e)
from src.text_generator import generate_script
from src.text_to_speech import text_to_speech
from src.create_video import create_video
from src.upload_youtube import upload_video
from src.download_image import download_image

def main():
    print("🎯 بدء العملية اليومية")

    # 1. توليد النص
    print("🧠 1. توليد نص...")
    script = generate_script()
    print(f"✅ النص: {script}")

    # 1.1 تحميل صورة تلقائيًا
    print("🖼️ 1.1 جلب صورة تلقائيًا...")
    download_image(script)

    # 2. تحويل النص إلى صوت
    print("🔊 2. تحويل النص إلى صوت...")
    audio_path = text_to_speech(script)
    print(f"✅ Saved audio to {audio_path}")

    # 3. إنشاء الفيديو
    print("🎞️ 3. إنشاء الفيديو...")
    video_path = create_video(audio_path)
    print(f"✅ Video saved at: {video_path}")

    # 4. رفع الفيديو إلى YouTube
    print("📤 4. رفع الفيديو إلى YouTube...")
    upload_video(video_path, script)

if __name__ == "__main__":
    main()
