import os
import requests

def download_image(prompt: str, output_path='background.jpg'):
    api_key = os.getenv('PEXELS_API_KEY')
    if not api_key:
        raise Exception("❌ PEXELS_API_KEY غير موجود. تأكد من إضافته إلى GitHub Secrets.")

    headers = {
        "Authorization": api_key
    }
    params = {
        "query": prompt,
        "per_page": 1
    }

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch image from Pexels: {response.status_code} - {response.text}")

    data = response.json()
    image_url = data["photos"][0]["src"]["landscape"]
    img_data = requests.get(image_url).content

    with open(output_path, 'wb') as handler:
        handler.write(img_data)

    print(f"✅ Image downloaded to {output_path}")
