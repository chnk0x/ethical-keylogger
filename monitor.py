from pynput import keyboard
from collections import defaultdict
import time
from cryptography.fernet import Fernet
import json

key_stats = defaultdict(int)
pressed_keys = []  # List to store the keys in order

START_TIME = time.time()
MAX_DURATION = 60  # seconds

def on_press(key):
    if time.time() - START_TIME > MAX_DURATION:
        return False  # Stop listener automatically

    # Store the key in the list
    pressed_keys.append(key)

    if hasattr(key, 'char') and key.char is not None:
        if key.char.isalpha():
            key_stats["letters"] += 1
        elif key.char.isdigit():
            key_stats["numbers"] += 1
        else:
            key_stats["symbols"] += 1
    else:
        key_stats["control_keys"] += 1

def start_monitor():
    print("Monitoring keyboard activity for 60 seconds...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    # Print the keys in the order they were pressed
    print("Keys pressed in order:")
    for key in pressed_keys:
        print(key)

    # Print the statistics
    print("\nKey Statistics:")
    print(dict(key_stats))

    # Encrypt the keys and save to a file
    data = {
        "stats": dict(key_stats),
        "keys": [str(k) for k in pressed_keys]
    }

    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(json.dumps(data).encode())

    with open("key_activity.enc", "wb") as f:
        f.write(encrypted)

    with open("encryption.key", "wb") as k:
        k.write(key)

    print("\nData encrypted and saved safely.")

print("Monitor Module: This file monitors keyboard activity by counting key types (letters, numbers, symbols) without recording actual keystrokes.")
start_monitor()