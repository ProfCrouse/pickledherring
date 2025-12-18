from cryptography.fernet import Fernet
import json
import requests


########################################################################################################

def load_key():
    with open("C://Users//David Crouse//PycharmProjects//OptusUI//secret.key", "rb") as key_file:
        return key_file.read()

########################################################################################################


def decrypt_data(encrypted_data):
    key = load_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()  # Convert bytes back to string


########################################################################################################


def get_remote_approved_users():
    url = "https://raw.githubusercontent.com/ProfCrouse/pickledherring/refs/heads/main/herrings.json"  # Correct URL
    response = requests.get(url)
    decrypted_data = decrypt_data(response.json())
    data_dict = json.loads(decrypted_data)
    return data_dict


########################################################################################################



approved_users = get_remote_approved_users()
print(approved_users)



