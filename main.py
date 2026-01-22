from consent import get_user_consent
from monitor import start_monitor, key_stats
from encrypt_log import encrypt_log

def main():
    get_user_consent()
    start_monitor()
    encrypt_log(key_stats)
    print("Monitoring complete. Program terminated safely.")

if __name__ == "__main__":
    main()


print("Main Module: This file controls the program flow by requesting consent, starting monitoring, encrypting data, and safely exiting.")
