import os
import requests

def download_image(query="طبيعة"):
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise Exception("❌ PEXELS_API_KEY غير موجود. تأكد من إضافته إلى GitHub Secrets.")

    headers = {"Authorization": api_key}
    params = {"query": query, "per_page": 1}

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch image from Pexels: {response.status_code} - {response.text}")

    data = response.json()
    if not data["photos"]:
        raise Exception("❌ No images found for the given query.")

    image_url = data["photos"][0]["src"]["landscape"]
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        os.makedirs("assets", exist_ok=True)
        image_path = os.path.join("assets", "background.jpg")
        with open(image_path, "wb") as f:
            f.write(image_response.content)
        print(f"✅ Image downloaded to {image_path}")
        return image_path
    else:
        raise Exception(f"❌ Failed to download image: {image_response.status_code}")
