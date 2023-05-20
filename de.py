from cryptography.fernet import *
key = b'JTKCfWkEcWij3msmLJgFDBvDKTJesll8B4N-_YqSUvw='
with open("encrypted_file.txt", "rb") as file:
  file_data = file.read()
d=Fernet(key).decrypt(file_data)
with open("decrypted_file.txt", "wb") as file:
  file.write(d)