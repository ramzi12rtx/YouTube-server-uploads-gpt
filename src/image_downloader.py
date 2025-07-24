import requests
import os
import random

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def download_random_image(query, output_path="assets/background.jpg"):
    try:
        url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_url = data['urls']['regular']
        image = requests.get(image_url).content

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "wb") as f:
            f.write(image)

        print(f"✅ Downloaded image for: {query}")
        return output_path

    except Exception as e:
        print("❌ Failed to download image:", e)
        return "assets/default.jpg"  # fallback image
