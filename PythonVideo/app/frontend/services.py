import requests

BACKEND_URL = "http://localhost:5000/api/videos/"

def get_videos():
    r = requests.get(BACKEND_URL)
    return r.json()