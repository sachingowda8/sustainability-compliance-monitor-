import os
from groq_client import call_groq

# Get project root (ai-service)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct absolute path
prompt_path = os.path.join(BASE_DIR, "prompts", "describe_prompt.txt")

print("Looking for file at:", prompt_path)

# Load prompt
with open(prompt_path, "r") as f:
    template = f.read()

# Input
input_text = "Company using renewable energy to reduce carbon emissions"

# Inject input
prompt = template.replace("{input_text}", input_text)

# Call Groq
response = call_groq(prompt)

print("\n=== AI RESPONSE ===\n")
print(response)