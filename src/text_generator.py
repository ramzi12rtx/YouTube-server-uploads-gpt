import openai
import os
import random

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompts = [
        "اكتب نصًا لفيديو قصير ملهم عن النجاح الشخصي.",
        "اكتب سكربت لفيديو عن أسرار التطوير الذاتي.",
        "اكتب نصًا ترفيهيًا عن أغرب 5 حقائق في العالم.",
        "اكتب نصًا عن عادة صباحية للناجحين.",
        "اكتب نص فيديو جذاب عن كيف تبدأ مشروعك الخاص."
    ]

    prompt = random.choice(prompts)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # مجاني غالبًا في معظم البيئات
        messages=[
            {"role": "system", "content": "أنت كاتب محتوى محترف على يوتيوب."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.8
    )

    script = response.choices[0].message.content.strip()
    return script
