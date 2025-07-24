from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
import os
from datetime import datetime

def create_video(image_path, audio_path, output_path=None):
    if not output_path:
        os.makedirs("output", exist_ok=True)
        output_path = f"output/video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"

    try:
        # تحميل الصوت
        audio_clip = AudioFileClip(audio_path)

        # تحديد مدة الفيديو إلى 30 ثانية كحد أقصى
        duration = min(audio_clip.duration, 30)

        # إنشاء صورة كفيديو عمودي (طولي)
        image_clip = ImageClip(image_path).set_duration(duration).resize(height=1920, width=1080)

        # دمج الصوت مع الصورة
        video = CompositeVideoClip([image_clip.set_audio(audio_clip.set_duration(duration))])

        # إخراج الفيديو
        video.write_videofile(output_path, fps=24)
        print(f"✅ Video saved at: {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error generating video: {e}")
        return None
