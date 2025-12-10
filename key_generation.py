from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key securely, e.g., to a file
with open("C://Users//David Crouse//PycharmProjects//OptusUI//secret.key", "wb") as key_file:
    key_file.write(key)