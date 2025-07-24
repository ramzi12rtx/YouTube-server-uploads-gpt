import openai
import os

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # أو "gpt-4" لو متاح
            messages=[
                {"role": "system", "content": "You are a helpful assistant who writes short YouTube video scripts."},
                {"role": "user", "content": "اكتب مقدمة قصيرة لفيديو معلومات عامة ممتع"}
            ],
            max_tokens=150
        )
        script = response.choices[0].message['content'].strip()
        return script
    except Exception as e:
        print(f"❌ Error generating script:", e)
        return "مرحبًا بكم في فيديو جديد! ترقبوا معلومات مدهشة قادمًا 😉"
