from cryptography.fernet import Fernet
import json
import requests
import subprocess

#############################################################################################

def run_git_commands():
    try:
        # Stage the file
        subprocess.run(['git', 'add', 'herrings.json'], check=True)

        # Commit the changes
        subprocess.run(['git', 'commit', '-m', 'Updated email list in herrings.json'], check=True)

        # Push the changes to the main branch
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)

        print("Git commands executed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

########################################################################################################

def load_key():
    with open("C://Users//David Crouse//PycharmProjects//OptusUI//secret.key", "rb") as key_file:
        return key_file.read()

########################################################################################################


# Encrypting data
def encrypt_json_data(json_data):
    key = load_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(json_data.encode())
    return encrypted_data.decode()  # Convert bytes back to string


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


original_data = '{"users": [ {"user_name": "david.thomas.crouse@gmail.com", "password": "123456", "type": "student"}, {"user_name": "dcrouse@clarkson.edu", "password": "123456", "type": "enterpriselite"} ] }'

encrypted_data_returned = encrypt_json_data(original_data)

# Save the new content into 'herrings.json'
with open("herrings.json", "w") as json_file:
    json.dump(encrypted_data_returned, json_file)
    print("Completed")

run_git_commands()
print("Successfully encrypted")

approved_users = get_remote_approved_users()
print(approved_users)
print(approved_users['users'][0 ]['user_name'])


# original_data = '{"allowed": ["david.thomas.crouse@gmail.com", "dcrouse@clarkson.edu", "tester@gmail.com", "metaprof@yahoo.com", "thomas_cromwell"]}'
