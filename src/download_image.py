import requests
import os

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")  # تأكد أنك ضايفه في GitHub Secrets

def download_image(query):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch image from Pexels: {response.status_code} - {response.text}")

    data = response.json()
    image_url = data['photos'][0]['src']['large']

    image_path = "output/image.jpg"
    image_data = requests.get(image_url).content
    with open(image_path, "wb") as f:
        f.write(image_data)

    return image_path
