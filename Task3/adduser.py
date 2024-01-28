from password_utils import encrypt_password, read_password_file, write_password_file, find_user

def add_user():
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    password_entries = read_password_file()
    existing_user = find_user(username, password_entries)

    if existing_user:
        print("Cannot add. Most likely username already exists.")
    else:
        encrypted_password = encrypt_password(password)
        new_entry = f"{username}:{real_name}:{encrypted_password}"
        password_entries.append(new_entry)
        write_password_file(password_entries)
        print("User Created.")

if __name__ == "__main__":
    add_user()
