from getpass import getpass
from password_utils import read_password_file, find_user

def login():
    username = input("User: ")
    password = getpass("Password: ")

    password_entries = read_password_file()
    user_entry = find_user(username, password_entries)

    if user_entry:
        _, _, stored_password = user_entry.split(':')
        if stored_password == password:
            print("Access granted.")
        else:
            print("Access denied.")
    else:
        print("User not found. Access denied.")

if __name__ == "__main__":
    login()
