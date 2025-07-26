import requests
import os

def download_music(query="motivational"):
    api_key = os.getenv("PIXABAY_API_KEY")
    url = f"https://pixabay.com/api/music/?key={api_key}&q={query}&per_page=3"
    response = requests.get(url).json()
    track_url = response["hits"][0]["audio"]
    path = "assets/music.mp3"
    with open(path, "wb") as f:
        f.write(requests.get(track_url).content)
    return path
