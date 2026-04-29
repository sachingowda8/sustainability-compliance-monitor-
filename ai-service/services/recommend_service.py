import json
import os
from services.groq_client import call_groq

def generate_recommendations(input_text):
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(BASE_DIR, "..", "prompts", "recommend_prompt.txt")

        with open(prompt_path, "r") as f:
            prompt_template = f.read()

        final_prompt = prompt_template.replace("{input_text}", input_text)

        response = call_groq(final_prompt)

        if response is None:
            return [{
                "action_type": "Fallback",
                "description": "AI service unavailable",
                "priority": "LOW"
            }]

        # CLEAN RESPONSE (IMPORTANT FIX)
        cleaned = response.replace("```json", "").replace("```", "").strip()

        return json.loads(cleaned)

    except Exception as e:
        return [{
            "action_type": "Error",
            "description": "Failed to generate recommendations",
            "priority": "LOW"
        }]