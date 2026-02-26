import requests
import json

url = "http://localhost:8000/ask"
payload = {
    "prompt": "Hello Shree, are you working?",
    "app_source": "CLI Test"
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
