from moviepy.editor import *

def create_video(image_path, audio_path, output_path="output/video.mp4"):
    try:
        image_clip = ImageClip(image_path, duration=10)
        audio_clip = AudioFileClip(audio_path)

        video = image_clip.set_audio(audio_clip)
        video = video.set_duration(audio_clip.duration)

        video.write_videofile(output_path, fps=24)
        print(f"✅ Video saved at: {output_path}")
        return output_path
    except Exception as e:
        print("❌ Error generating video:", e)
        return None
