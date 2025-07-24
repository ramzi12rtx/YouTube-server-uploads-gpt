1️⃣ main.py (يشغل جميع الوحدات)

from src.generate_script import generate_script from src.text_to_speech import text_to_speech from src.create_video import create_video from src.upload_youtube import upload_video

def main(): print("\n🔁 Generating script...") script = generate_script()

print("\n🔊 Converting text to speech...")
audio_path = text_to_speech(script)

print("\n🎞️ Creating video...")
video_path = create_video(audio_path)

print("\n📤 Uploading to YouTube...")
upload_video(video_path, script)

if name == "main": main()

