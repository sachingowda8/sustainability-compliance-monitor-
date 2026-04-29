import sys
import os

# Add the parent directory to the path so we can find 'services'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.groq_client import GroqClient

def test_day2_client():
    print("🚀 Testing Day 2 Robust Client...")
    try:
        client = GroqClient()
        response = client.get_completion("Is recycling mandatory for ESG compliance?")
        print("\n✅ AI Response:")
        print(response)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    test_day2_client()
