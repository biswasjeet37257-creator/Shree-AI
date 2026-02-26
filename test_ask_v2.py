import urllib.request
import urllib.error
import json

url = "http://localhost:8000/ask"
payload = {
    "prompt": "Hello Shree, are you working?",
    "app_source": "CLI Test"
}
data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data)
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.getcode()}")
        print(f"Response: {response.read().decode('utf-8')}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(f"Details: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
