import os
import requests

def download_image(query="nature", save_path="output/image.jpg"):
    # جلب مفتاح API من Secrets
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    
    if not PEXELS_API_KEY:
        raise Exception("❌ PEXELS_API_KEY غير موجود. تأكد من إضافته إلى GitHub Secrets.")

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "orientation": "landscape",
        "size": "large",
        "per_page": 1
    }

    url = "https://api.pexels.com/v1/search"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch image from Pexels: {response.status_code} - {response.text}")

    data = response.json()
    photos = data.get("photos")
    if not photos:
        raise Exception("❌ لم يتم العثور على صور للبحث.")

    image_url = photos[0]["src"]["large"]

    # تحميل الصورة
    img_data = requests.get(image_url).content
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as handler:
        handler.write(img_data)

    print(f"✅ Image downloaded and saved to {save_path}")
    return save_path
