from password_utils import read_password_file, write_password_file, find_user

def delete_user():
    username = input("Enter username: ")

    password_entries = read_password_file()
    user_entry = find_user(username, password_entries)

    if user_entry:
        password_entries.remove(user_entry)
        write_password_file(password_entries)
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    delete_user()