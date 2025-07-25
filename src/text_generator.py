import os
import openai

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = (
        "اكتب لي سكريبت قصير وجذاب لفيديو يوتيوب مدته 30 ثانية،"
        " يكون باللغة الإنجليزية، ويتحدث عن معلومة عامة مذهلة،"
        " بأسلوب مشوّق ويدعو المشاهد للبقاء حتى النهاية."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # أو "gpt-3.5-turbo" لو لم يكن لديك وصول إلى gpt-4
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=200
        )
        script = response.choices[0].message['content'].strip()
        print(f"✅ النص: {script}")
        return script
    except Exception as e:
        print(f"❌ Error generating script: {e}")
        return "Welcome to our channel! Stay tuned for amazing content coming soon 😉"
