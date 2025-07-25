import openai
import os

def generate_script():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ✅ استخدم gpt-3.5
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes short, engaging YouTube video scripts."},
                {"role": "user", "content": "Write a short script for a 30-second video about a fun fact."}
            ]
        )
        script = response['choices'][0]['message']['content'].strip()
        return script

    except Exception as e:
        print("❌ Error generating script:", e)
        return "Welcome to our channel! Stay tuned for amazing content coming soon 😉"
