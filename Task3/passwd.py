from getpass import getpass
from password_utils import encrypt_password, read_password_file, write_password_file, find_user

def change_password():
    username = input("User: ")
    current_password = getpass("Current Password: ")
    new_password = getpass("New Password: ")
    confirm_password = getpass("Confirm: ")

    password_entries = read_password_file()
    user_entry = find_user(username, password_entries)

    if user_entry:
        _, _, stored_password = user_entry.split(':')
        if stored_password == encrypt_password(current_password) and new_password == confirm_password:
            new_entry = f"{username}:{encrypt_password(new_password)}"
            password_entries.remove(user_entry)
            password_entries.append(new_entry)
            write_password_file(password_entries)
            print("Password changed.")
        else:
            print("Invalid credentials or passwords do not match. No change made.")
    else:
        print("User not found. No change made.")

if __name__ == "__main__":
    change_password()
