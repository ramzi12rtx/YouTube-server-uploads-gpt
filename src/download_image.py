import requests
import os
from datetime import datetime

def download_image(query):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        print("❌ Unsplash access key missing.")
        return "assets/fallback.jpg"
    
    try:
        response = requests.get(
            "https://api.unsplash.com/photos/random",
            params={"query": query, "orientation": "landscape", "client_id": access_key},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        image_url = data['urls']['regular']
        
        filename = f"output/image_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        img_data = requests.get(image_url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        
        print(f"✅ Downloaded image to {filename}")
        return filename
    except Exception as e:
        print(f"❌ Failed to download image: {e}")
        return "assets/fallback.jpg"
