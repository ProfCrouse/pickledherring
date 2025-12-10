from cryptography.fernet import Fernet
import json
import requests

def load_key():
    with open("C://Users//David Crouse//PycharmProjects//OptusUI//secret.key", "rb") as key_file:
        return key_file.read()

# Encrypting data
def encrypt_json_data(json_data):
    key = load_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(json_data.encode())
    return encrypted_data.decode()  # Convert bytes back to string

original_data = '{"allowed": ["david.thomas.crouse@gmail.com", "tester@gmail.com"]}'
encrypted_data = encrypt_json_data(original_data)

# Save the new content into 'herrings.json'
with open("herrings.json", "w") as json_file:
    json.dump(encrypted_data, json_file)