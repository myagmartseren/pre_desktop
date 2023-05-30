from cryptography.fernet import Fernet
import uuid
import main
from umbral import (PublicKey,encrypt)
from models import *

def file_encrypt(data, filename):
    generated_uuid = uuid.uuid4()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_contents = f.encrypt(data)

    capsule, encrypted_key = encrypt(PublicKey._from_exact_bytes(bytes.fromhex(main.current_user.public_key)), key) 
    
    temp_path = f"/tmp/{str(generated_uuid)}"
    with open(temp_path, "wb") as f:
        f.write(encrypted_contents)
        
    return File({
        "ower_id": main.current_user.id,
        "name": filename,
        "key": encrypted_key,
        "capsule":capsule.__bytes__(),
        "path":temp_path,
    })