import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError

def upload_video(video_path, script):
    # 🔤 استخدم أول سطر من السكربت كعنوان - أو عنوان افتراضي
    script = script.strip()
    title = script.split("\n")[0] if script else "Video from AI"
    title = title[:100]
    description = script if script else "Generated video using AI."

    youtube_api_key = os.getenv("YOUTUBE_API_KEY")

    if youtube_api_key:
        # ✅ الرفع باستخدام YOUTUBE_API_KEY
        youtube = build("youtube", "v3", developerKey=youtube_api_key)
    else:
        # ✅ الرفع باستخدام OAuth عبر refresh token
        client_id = os.getenv("YOUTUBE_CLIENT_ID")
        client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")
        refresh_token = os.getenv("YOUTUBE_REFRESH_TOKEN")

        if not (client_id and client_secret and refresh_token):
            raise Exception("❌ Missing YouTube credentials in environment variables.")

        creds_data = {
            "token": "",
            "refresh_token": refresh_token,
            "token_uri": "https://oauth2.googleapis.com/token",
            "client_id": client_id,
            "client_secret": client_secret,
            "scopes": ["https://www.googleapis.com/auth/youtube.upload"],
        }

        creds = Credentials.from_authorized_user_info(info=creds_data)

        try:
            creds.refresh(Request())
        except RefreshError as e:
            raise Exception(f"❌ Failed to refresh access token: {e}")

        youtube = build("youtube", "v3", credentials=creds)

    # ⬆️ رفع الفيديو
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
