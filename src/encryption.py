from cryptography.fernet import Fernet
import uuid
import main
from umbral import (PublicKey,encrypt, generate_kfrags, decrypt_reencrypted,decrypt_original , SecretKey, Signer, Capsule, CapsuleFrag)
from models import *

def file_encrypt(data, filename):
    generated_uuid = uuid.uuid4()
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_contents = f.encrypt(data)

    delegating_pk = PublicKey.from_bytes(bytes.fromhex(main.current_user.public_key))
    capsule, cipher = encrypt(delegating_pk, key) 
    
    temp_path = f"/tmp/{str(generated_uuid)}"
    with open(temp_path, "wb") as f:
        f.write(encrypted_contents)
    
    return File({
        "ower_id": main.current_user.id,
        "name": filename,
        "key": cipher,
        "capsule":capsule.__bytes__(),
        "path":temp_path,
    })

def file_decrypt(cipher, key, path):
    plaincontent = Fernet(key).decrypt(cipher)
    with open(path.name,"wb") as f:
        f.write(plaincontent)

def generate_k(user: User):
    user_pk_bytes = PublicKey.from_bytes(bytes.fromhex(user.public_key))
    delegating_sk = SecretKey.from_bytes(main.private_key)

    kfrags = generate_kfrags(delegating_sk=delegating_sk,
                             receiving_pk=user_pk_bytes,
                             signer=Signer(SecretKey.from_bytes(main.private_key)),
                             threshold=1,
                             shares=20)
    
    return kfrags[0].__bytes__()
                                 
def decrypt_o(capsulse_bytes, key_bytes):
    secret_key = SecretKey.from_bytes(main.private_key)
    capsulse = Capsule.from_bytes(capsulse_bytes)

    return decrypt_original(secret_key, capsule=capsulse, ciphertext=key_bytes)

def decrypt_pre(share, user, key, capsule_bytes):
    cfrag = bytes.fromhex(share.rekey)
 
    suspicious_cfrag = CapsuleFrag.from_bytes(cfrag)
    delegating_pk = PublicKey.from_bytes(bytes.fromhex(user.public_key))
    # verifying_pk=PublicKey.from_bytes(bytes.fromhex(delegator_user.get("signer_key")))

    capsule = Capsule.from_bytes(capsule_bytes)
    receiving_pk = PublicKey.from_bytes(bytes.fromhex(main.current_user.public_key))
    receiving_sk=SecretKey.from_bytes(main.private_key)

    cfrags = suspicious_cfrag.verify(capsule=capsule,
            verifying_pk=delegating_pk,
            delegating_pk=delegating_pk,
            receiving_pk= receiving_pk
    )

    return decrypt_reencrypted(receiving_sk=receiving_sk,
            delegating_pk=delegating_pk,
            capsule=capsule,
            verified_cfrags=[cfrags],
            ciphertext=key
    )