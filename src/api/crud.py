import requests
from models import *

API_URL = 'http://localhost:5000'

def add_file(file : File):
    url = API_URL+"/api/file"
    import main
    encrypted_file = {"file":open(file.path)}
    data = {
        "name": file.name,
        # "path": file.path,
        "owner_id": main.current_user.id,
        "key": file.key,
    }

    response = requests.post(url, data=data,files=encrypted_file)
    if response.status_code == 200:
        return User(response.json())
    else:
        return None