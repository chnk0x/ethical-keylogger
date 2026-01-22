def get_user_consent():
    print("⚠️ EDUCATIONAL NOTICE ⚠️")
    print("This program monitors keyboard ACTIVITY only.")
    print("Data is stored locally and encrypted.")
 
    consent = input("Type YES to continue: ")

    if consent != "YES":
        print("Consent not given. Program exiting.")
        exit()


print("Consent Module: This file ensures the user gives permission before any keyboard activity monitoring begins.")
