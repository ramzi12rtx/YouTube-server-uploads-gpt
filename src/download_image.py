# src/image_downloader.py

import os
import requests

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def download_random_image(query="nature", output_path="input.jpg"):
    if not PEXELS_API_KEY:
        print("❌ Pexels access key missing.")
        return False

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
    if response.status_code != 200:
        print(f"❌ Failed to fetch image: {response.status_code} - {response.text}")
        return False

    data = response.json()
    if not data.get("photos"):
        print("❌ No photos found.")
        return False

    image_url = data["photos"][0]["src"]["original"]
    image_data = requests.get(image_url).content

    with open(output_path, "wb") as f:
        f.write(image_data)

    print(f"✅ Saved image to {output_path}")
    return True
