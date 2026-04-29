import requests
import json

BASE_URL = "http://127.0.0.1:5001/api/analyze"

def test_api(name, query):
    print(f"\n--- Testing: {name} ---")
    print(f"Query: {query}")
    try:
        response = requests.post(BASE_URL, json={"query": query})
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Success!")
            # print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting Day 4 Verification Tests...")
    test_api("Normal Query", "What are carbon credits?")
    print("\nTests Complete!")
