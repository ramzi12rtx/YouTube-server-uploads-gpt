# src/generate_script.py
import openai
import os

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = (
        "اكتب لي نصًا قصيرًا (أقل من 60 ثانية عند القراءة) يصلح لفيديو يوتيوب. "
        "اجعله ممتعًا وعشوائيًا: قد يكون معلومة غريبة، قصة قصيرة، أو نصيحة مفاجئة."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        text = response.choices[0].message["content"].strip()
        return text
    except Exception as e:
        print("❌ Error generating script:", e)
        return "مرحبًا بكم في فيديو جديد! ترقبوا معلومات مدهشة قادمًا 😉"
