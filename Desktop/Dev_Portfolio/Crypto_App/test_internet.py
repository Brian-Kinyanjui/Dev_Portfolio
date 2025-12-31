import requests

try:
    response = requests.get("https://google.com")
    print("✅ Internet is working!")
    print(f"Status Code: {response.status_code}")
except Exception as e:
    print(f"❌ Internet failed: {e}")