from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
from PIL import Image
import os

def resize_and_crop(image_path, target_size=(1080, 1920)):
    img = Image.open(image_path).convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]

    if img_ratio > target_ratio:
        # قص العرض
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
    else:
        # قص الطول
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)

    img = img.resize((new_width, new_height), Image.LANCZOS)

    # اقتصاص مركزي
    left = (new_width - target_size[0]) / 2
    top = (new_height - target_size[1]) / 2
    right = left + target_size[0]
    bottom = top + target_size[1]

    img = img.crop((left, top, right, bottom))

    output_path = "assets/resized_background.jpg"
    img.save(output_path)
    return output_path

def create_video(image_path, audio_path, output_path):
    # ضبط حجم الفيديو الطولي
    final_size = (1080, 1920)

    resized_image_path = resize_and_crop(image_path, final_size)

    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    background = ImageClip(resized_image_path).set_duration(duration)

    video = CompositeVideoClip([background.set_audio(audio_clip)], size=final_size)
    video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
