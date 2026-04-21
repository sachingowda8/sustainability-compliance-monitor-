import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_groq_connection():
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key == "gsk_your_key_here" or api_key == "PASTE_YOUR_KEY_HERE":
        print("Error: Please set a valid GROQ_API_KEY in the .env file.")
        return

    try:
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say 'Groq is active!' if you can hear me.",
                }
            ],
            model="llama-3.1-8b-instant",
        )
        print(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"Error connecting to Groq: {e}")

if __name__ == "__main__":
    test_groq_connection()
