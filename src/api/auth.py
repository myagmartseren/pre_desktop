import requests
from db.database import User

API_URL = 'http://localhost:5000'

def login(username, password):
    url = API_URL+"/api/login"
    data = {
        "username": username,
        "password": password,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None

def register(user: User):
    url = API_URL+"/api/register"
    data = {
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,
        "password": user.password,
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return True
    else:
        return False
