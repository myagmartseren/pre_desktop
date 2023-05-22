import requests
from models import User

API_URL = 'http://localhost:5000'

def login(email, password):
    url = API_URL + "/auth/login"
    data = {
        "email": email,
        "password": password,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        response_data = response.json()
        id = response_data.get('id')
        print("logged id",id)
        access_token = response_data.get('access_token')
        username = response_data.get('username')
        public_key = response_data.get('public_key')
        if access_token and username and public_key:
            user = User({
                "id":id,
                "access_token":access_token,
                "username" :username,
                "public_key":public_key,
            })
            user.access_token = access_token
            import main
            with open(f"{username}.pem", "rb") as f:
                main.private_key = f.read()
            return user
    return None


def register(user: User):
    url = API_URL + "/auth/register"
    data = {
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,
        "password": user.password,
    }

    response = requests.post(url, json=data)
    import main
    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data.get('access_token')
        username = response_data.get('username')
        public_key = response_data.get('public_key')

        if access_token and username and public_key:
            user = User({"username":username, "public_key":public_key})
            user.access_token = access_token
            main.current_user=user
            private_key_hex = response_data.get('private_key')
            print("private_key_hex",private_key_hex)
            if private_key_hex:
                private_key = bytes.fromhex(private_key_hex)
                with open(f"{username}.pem", "wb") as f:
                    f.write(private_key)
                import main
                main.private_key = private_key
            return True, user
    return False, None

def logout():
    url = API_URL + "/auth/logout"
    import main
    headers = {
        "Authorization": "Bearer " + main.current_user.access_token
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return None
