import os
import json
from services.groq_client import GroqClient
from dotenv import load_dotenv

load_dotenv()

def run_tuning():
    client = GroqClient()
    
    # Current prompt (Day 6 tuned)
    prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'sustainability_expert.txt')
    with open(prompt_path, 'r') as f:
        system_prompt = f.read().strip()
    
    inputs = [
        "How can a textile company reduce its water footprint?",
        "What are the key metrics for measuring social impact in a supply chain?",
        "Explain the importance of governance in ESG reporting.",
        "Is investing in coal power plants compliant with modern ESG standards?",
        "What are the environmental impacts of lithium-ion battery production?",
        "How should a company disclose its carbon emissions?",
        "What is the difference between Scope 1, 2, and 3 emissions?",
        "How does biodiversity loss affect corporate sustainability risks?",
        "What are the labor rights risks in cobalt mining?",
        "How can a business transition to a circular economy model?"
    ]
    
    print(f"Testing Prompt: {system_prompt}\n")
    
    results = []
    for i, user_input in enumerate(inputs):
        print(f"Running input {i+1}/10: {user_input}")
        response = client.get_completion(user_input, system_prompt=system_prompt)
        results.append({
            "input": user_input,
            "output": response
        })
        
    with open("tuning_results.json", "w") as f:
        json.dump(results, f, indent=4)
    
    print("\nResults saved to tuning_results.json")

if __name__ == "__main__":
    run_tuning()
