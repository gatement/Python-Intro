import requests

def check_get(url, expected):
    result = requests.get(url)
    if expected in result.text:
        print(url + " PASS")
    else:
        print(url + " FAILURE")

check_get("http://localhost:5002/hello", "Life is short, you need Python!")
