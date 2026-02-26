import urllib.request
import urllib.error

url = "http://localhost:8000/ask"
req = urllib.request.Request(url, method='OPTIONS')
req.add_header('Origin', 'http://localhost:3001')
req.add_header('Access-Control-Request-Method', 'POST')
req.add_header('Access-Control-Request-Headers', 'content-type')

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.getcode()}")
        print(f"Headers: {response.info()}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(f"Details: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
