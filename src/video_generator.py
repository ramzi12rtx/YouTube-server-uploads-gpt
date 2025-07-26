from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip, vfx
from PIL import Image
from datetime import timedelta
import os

def create_video(image_path, audio_path, output_path):
    # تحميل الصوت
    audio = AudioFileClip(audio_path)
    duration = audio.duration

    # إعداد الحجم النهائي
    final_w, final_h = 1080, 1920

    # تعديل الصورة للخلفية
    img = Image.open(image_path).convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = final_w / final_h

    if img_ratio > target_ratio:
        new_h = final_h
        new_w = int(img_ratio * new_h)
    else:
        new_w = final_w
        new_h = int(new_w / img_ratio)

    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - final_w) // 2
    top = (new_h - final_h) // 2
    img = img.crop((left, top, left + final_w, top + final_h))
    resized_path = "assets/resized_bg.jpg"
    os.makedirs("assets", exist_ok=True)
    img.save(resized_path)

    # إنشاء الخلفية مع تأثير Blur خفيف
    background = ImageClip(resized_path).set_duration(duration)
    blurred_bg = background.fx(vfx.blur, 10).set_opacity(0.6)

    # النص المتحرك (العنوان من script)
    if hasattr(audio, 'fps'): pass
    text_lines = []
    # script input passed earlier
    # هنا يمكنك تمرير العنوان من main.py
    title = os.getenv("SCRIPT_TITLE", "")
    txt_clip = TextClip(title, fontsize=90, color='white', font='Arial-Bold',
                        method='caption', size=(final_w*0.8, None), align='center')
    txt_clip = txt_clip.set_position(("center", final_h*0.4)).set_duration(duration)
    txt_clip = txt_clip.crossfadein(1).crossfadeout(1)

    # دمج الخلفيات
    final = CompositeVideoClip([blurred_bg, background.set_opacity(1), txt_clip])
    final = final.set_audio(audio).set_duration(duration)

    # إخراج الفيديو
    os.makedirs("output", exist_ok=True)
    final.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')
