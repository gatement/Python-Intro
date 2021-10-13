import requests

def check_result(url, result, expected):
    if expected in result:
        print(url + " PASS")
    else:
        print(url + " FAILURE")

def check_get(url, expected):
    result = requests.get(url)
    check_result(url, result.text, expected)

def check_post(url, data, expected):
    result = requests.post(url, data)
    check_result(url, result.text, expected)

check_get("http://localhost:5002/hello", "Life is short, you need Python!")
check_post("http://localhost:5002/api", {"name": "Lucy"}, "Lucy")
