import requests
from models import *
from utils import relative_to_files

API_URL = 'http://localhost:5000'
# API_URL = 'http://192.168.1.5:5000'

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
        url+="/shares"
        if shared_files == True:
            params["delegator_id"]= True
        else:
            params["delegatee_id"]= True
    
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
        return File(response_data)

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
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return User(response_data)
    else:
        return None
    
def get_share(file_id):
    url = API_URL + f"/shares/{file_id}"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url,headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return Share(response_data)
    else:
        return None

def add_share(share: Share):
    url = API_URL + "/shares"
    import main
    data = {
        "file_id": share.file_id,
        "delegator_id": share.delegator_id,
        "delegatee_id": share.delegatee_id,
        "rekey": share.rekey,
    }

    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return None

def get_users_by_file(file_id):
    url = API_URL + f"/shares/{file_id}/users"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def delete_share(file_id,email):
    url = API_URL + f"/shares/{file_id}/{email}"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return None