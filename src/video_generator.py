from moviepy.editor import *
import os
from datetime import datetime

def create_video(audio_path):
    if not os.path.exists("background.jpg"):
        raise Exception("❌ الصورة background.jpg غير موجودة.")

    try:
        image_clip = ImageClip("background.jpg").set_duration(AudioFileClip(audio_path).duration)
        audio_clip = AudioFileClip(audio_path)
        video = image_clip.set_audio(audio_clip)

        output_path = f"output/video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
        os.makedirs("output", exist_ok=True)
        video.write_videofile(output_path, fps=24)
        print(f"✅ Video saved at: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error generating video: {e}")
        return None
