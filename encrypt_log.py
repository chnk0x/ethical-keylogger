from cryptography.fernet import Fernet
import json

def encrypt_log(data):
    key = Fernet.generate_key()
    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(json.dumps(data).encode())

    with open("key_activity.enc", "wb") as enc_file:
        enc_file.write(encrypted_data)

    with open("encryption.key", "wb") as key_file:
        key_file.write(key)

    print("Activity log encrypted and saved locally.")


print("Encryption Module: This file securely encrypts the collected keyboard activity data and stores it locally.")
