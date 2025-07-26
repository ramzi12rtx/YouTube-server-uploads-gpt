from moviepy.editor import *
from PIL import Image
import os

def create_video(image_path, audio_path, output_path):
    # تحميل الصوت لمعرفة مدته
    audio = AudioFileClip(audio_path)
    duration = audio.duration

    # تعديل أبعاد الصورة إلى 1080x1920 دون تشويه باستخدام PIL
    resized_image_path = "assets/resized_background.jpg"
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img_ratio = img.width / img.height
        target_ratio = 1080 / 1920

        if img_ratio > target_ratio:
            # الصورة أعرض: نغير العرض ونقص من الأطراف
            new_height = 1920
            new_width = int(1920 * img_ratio)
        else:
            # الصورة أطول: نغير الارتفاع ونقص من الأعلى والأسفل
            new_width = 1080
            new_height = int(1080 / img_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)

        # قص وسط الصورة لتصبح بالضبط 1080x1920
        left = (new_width - 1080) // 2
        top = (new_height - 1920) // 2
        img = img.crop((left, top, left + 1080, top + 1920))

        # حفظ الصورة المعدلة
        os.makedirs("assets", exist_ok=True)
        img.save(resized_image_path)

    # إنشاء فيديو من الصورة المعدلة
    image_clip = ImageClip(resized_image_path).set_duration(duration)
    image_clip = image_clip.set_audio(audio)

    # تصدير الفيديو
    os.makedirs("output", exist_ok=True)
    image_clip.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')
