from cryptography.fernet import *

# Generate a random key
key = Fernet.generate_key()
print(key)
# Encrypt the file
with open("image.png", "rb") as file:
  file_data = file.read()

encrypted_file_data = Fernet(key).encrypt(file_data)

# Write the encrypted file
with open("encrypted_file.txt", "wb") as file:
  file.write(encrypted_file_data)

# Save the key
with open("key.txt", "wb") as file:
  file.write(key)
