import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

def generate_script():
    try:
        print("🧠 استخدام Claude لتوليد نص جذاب...")
        prompt = (
            "📌 أكتب نص فيديو قصير ومشوق لمنصة يوتيوب.\n"
            "✅ النص يجب أن يكون:\n"
            "- جذاب من أول ثانية.\n"
            "- يحتوي على معلومة غريبة أو مثيرة (مثل: حقائق علمية، غرائب، أشياء لا يعرفها الناس).\n"
            "- لا يتجاوز 3 جمل.\n"
            "- بصيغة حماسية وتشويقية.\n"
            "- باللغة الإنجليزية فقط.\n"
            "🎯 مثال: Did you know that octopuses have three hearts and blue blood?\n"
        )

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.content[0].text.strip()
        print("✅ النص:", text)
        return text

    except Exception as e:
        print("❌ Claude API Error:", e)
        return "Did you know the human brain uses more energy than any other organ? 😉"
