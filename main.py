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

def main():
    print("🎯 بدء العملية اليومية")

    print("🧠 1. توليد نص...")
    script = generate_script()
    print("✅ النص:", script)

    print("🔊 2. تحويل النص إلى صوت...")
    audio_path = text_to_speech(script)

    print("🎞️ 3. إنشاء الفيديو...")
    video_path = create_video(audio_path)

    print("📤 4. رفع الفيديو إلى YouTube...")
    upload_video(video_path, script)

    print("🎉 تم رفع الفيديو بنجاح!")

if __name__ == "__main__":
    main()
