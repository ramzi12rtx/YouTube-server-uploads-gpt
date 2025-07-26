import os
import openai

def generate_script():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("❌ OPENAI_API_KEY is missing from environment variables.")
    
    openai.api_key = api_key

    prompt = (
        "أعطني سكربتًا قصيرًا وجذابًا لفيديو يوتيوب شورت يتكون من 2 إلى 4 جمل، "
        "الموضوع يجب أن يكون مفاجئًا أو يثير الفضول أو يحتوي على معلومة صادمة. "
        "اختم بجملة تشجيعية للمشاهد على التفاعل (مثل الإعجاب أو التعليق). "
        "اكتب باللهجة العربية الفصحى المبسطة، وابتعد عن الحشو."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي مختص في إنشاء سكربتات لفيديوهات يوتيوب شورت."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )

        script = response['choices'][0]['message']['content'].strip()
        return script

    except Exception as e:
        raise Exception(f"❌ Error generating script: {e}")
