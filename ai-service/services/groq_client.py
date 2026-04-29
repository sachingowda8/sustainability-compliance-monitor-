import os
import time
import traceback
from groq import Groq
from dotenv import load_dotenv
from services.metrics import response_times

# Load environment variables
load_dotenv()

# Debug: check API key (remove later)
api_key = os.getenv("GROQ_API_KEY")
print("🔑 GROQ API KEY:", api_key)

# Stop early if key missing (VERY IMPORTANT)
if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")

# Create Groq client
client = Groq(api_key=api_key)


def call_groq(prompt):
    try:
        start = time.time()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # correct model
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        end = time.time()

        # Track response time
        response_time = (end - start) * 1000
        response_times.append(response_time)

        if len(response_times) > 50:
            response_times.pop(0)

        return response.choices[0].message.content

    except Exception as e:
        import traceback
        print("GROQ ERROR:")
        traceback.print_exc()  

        return {
            "error": "AI temporarily unavailable",
            "is_fallback": True
        }