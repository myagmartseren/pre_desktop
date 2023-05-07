import requests
from model import User

API_URL = 'http://localhost:5000'

def login(email, password):
    url = API_URL+"/auth/login"
    data = {
        "email": email,
        "password": password,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def register(user: User):
    url = API_URL+"/auth/register"
    data = {
        "username":user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,
        "password": user.password,
    }
    
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return True
    else:
        return False
