from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
import os
from datetime import datetime

def create_video(image_path, audio_path, output_path=None):
    if not output_path:
        os.makedirs("output", exist_ok=True)
        output_path = f"output/video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"

    try:
        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(image_path).set_duration(audio_clip.duration).resize(height=720)
        video = CompositeVideoClip([image_clip.set_audio(audio_clip)])
        video.write_videofile(output_path, fps=24)
        print(f"✅ Video saved at: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error generating video: {e}")
        return None
