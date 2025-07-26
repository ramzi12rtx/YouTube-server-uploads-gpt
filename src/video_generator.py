from moviepy.editor import *
import os

def create_video(image_path, audio_path, output_path):
    # تحميل الصورة والصوت
    image = ImageClip(image_path).set_duration(AudioFileClip(audio_path).duration)
    image = image.resize(height=1920)  # فيديو طولي 1080x1920
    image = image.set_position("center").set_audio(AudioFileClip(audio_path))

    # إنشاء الفيديو النهائي
    final_video = CompositeVideoClip([image])
    os.makedirs("output", exist_ok=True)
    final_video.write_videofile(output_path, fps=24)
