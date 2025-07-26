import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(video_path, script):
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")

    if not youtube_api_key:
        raise Exception("❌ YOUTUBE_API_KEY not found in environment variables.")

    # 🔤 استخدم أول سطر من السكربت كعنوان - أو عنوان افتراضي
    script = script.strip()
    title = script.split("\n")[0] if script else "Video from AI"
    title = title[:100]  # لا يتجاوز 100 حرف

    description = script if script else "Generated video using AI."

    youtube = build("youtube", "v3", developerKey=youtube_api_key)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["AI", "Shorts", "Motivation", "daily videos"],
                "categoryId": "22",  # People & Blogs
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path)
    )

    response = request.execute()
    print(f"✅ تم رفع الفيديو: https://youtu.be/{response['id']}")
