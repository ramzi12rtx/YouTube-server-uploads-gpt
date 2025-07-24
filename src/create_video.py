# src/create_video.py
from moviepy.editor import *
import os
from datetime import datetime

def create_video(audio_path):
    background_path = "assets/background.jpg"  # يمكنك تغييره إلى فيديو لاحقًا
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # إنشاء اسم الفيديو بناءً على التاريخ والوقت
    video_filename = f"video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
    video_path = os.path.join(output_dir, video_filename)

    # تحميل الخلفية
    image_clip = ImageClip(background_path)

    # تحميل الصوت
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    # ضبط طول الصورة ليطابق الصوت
    video_clip = image_clip.set_duration(duration).set_audio(audio_clip)
    video_clip = video_clip.resize(height=720)  # دقة HD

    # حفظ الفيديو
    video_clip.write_videofile(video_path, fps=24)

    print(f"✅ Video saved at: {video_path}")
    return video_path
