from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import os

def upload_video(video_path, title):
    creds = Credentials(
        token=os.getenv("YOUTUBE_ACCESS_TOKEN"),
        refresh_token=os.getenv("YOUTUBE_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("YOUTUBE_CLIENT_ID"),
        client_secret=os.getenv("YOUTUBE_CLIENT_SECRET"),
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "تم الإنشاء تلقائيًا بواسطة GPT 🤖",
                "tags": ["AI", "YouTube", "Automation"]
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path)
    )

    response = request.execute()
    print("✅ تم رفع الفيديو: https://youtu.be/" + response.get("id"))
