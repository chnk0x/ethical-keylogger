from cryptography.fernet import Fernet
import json

with open("encryption.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

with open("key_activity.enc", "rb") as enc_file:
    encrypted_data = enc_file.read()

decrypted_data = cipher.decrypt(encrypted_data)
activity_data = json.loads(decrypted_data.decode())

print("Decrypted keyboard activity data:")
print(activity_data)
