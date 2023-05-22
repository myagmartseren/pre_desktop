import requests
from models import *
from utils import relative_to_files

API_URL = 'http://localhost:5000'

def add_file(file: File):
    url = API_URL + "/files"
    import main
    encrypted_file = {"file": open(file.path)}
    data = {
        "name": file.name,
        "key": file.key.hex(),
        "capsule": file.capsule.hex(),
    }
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.post(url, data=data, files=encrypted_file, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return None

def get_files(shared_files = None):
    url = API_URL + "/files"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }
    params = {}

    if shared_files is not None:
        if shared_files == True:
            params["delegator_id"]= main.current_user.id
        else:
            params["delegatee_id"]= main.current_user.id
    
    response = requests.get(url,headers=headers,params=params)
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        return None

def get_file(id):
    url = API_URL + f"/files/{id}"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data

    else:
        return None

def download_file(path):
    url = API_URL + f"/download/{path}"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }
    response = requests.get(url,headers=headers)    
    if response.status_code == 200:
        return response.content
    else:
        return None

def get_user(email):
    url = API_URL + f"/users/{email}"
    import main
    print("token is here",main.current_user.access_token)
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        return None
    
def get_share(file_id):
    url = API_URL + f"/share/{file_id}"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        return None

def add_share(share: Share):
    url = API_URL + "/shares"
    import main
    data = {
        "file_id": share.file_id,
        "delegator_id": share.delegator_id,
        "delegatee_id": share.delegatee_id,
        "rekey": share.rekey.hex(),
    }

    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return None