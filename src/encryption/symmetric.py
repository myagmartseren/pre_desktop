# from cryptography.fernet import Fernet

# class SymmetricEncryption:
#     def __init__(self, key=None):
#         if key:
#             self.key = key
#         else:
#             self.key = Fernet.generate_key()
#         self.cipher = Fernet(self.key)

#     def encrypt(self, plaintext):
#         ciphertext = self.cipher.encrypt(plaintext.encode())
#         return ciphertext

#     def decrypt(self, ciphertext):
#         plaintext = self.cipher.decrypt(ciphertext).decode()
#         return plaintext
