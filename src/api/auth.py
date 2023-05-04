import requests

def login(username, password):
    url = "https://example.com/api/login"
    data = {
        "username": username,
        "password": password,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None

def register(username, password):
    url = "https://example.com/api/register"
    data = {
        "username": username,
        "password": password,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return True
    else:
        return False
