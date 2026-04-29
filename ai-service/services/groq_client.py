import os
import time
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GroqClient:
    def __init__(self, model="llama-3.1-8b-instant"):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment")
        self.client = Groq(api_key=self.api_key)
        self.model = model

    def get_completion(self, prompt, system_prompt="You are a helpful assistant.", retries=3):
        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                    model=self.model,
                    response_format={"type": "json_object"} if "json" in prompt.lower() else None
                )
                return response.choices[0].message.content
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    raise e
