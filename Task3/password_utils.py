import hashlib

def encrypt_password(password):
    # You can use a more secure encryption algorithm here
    return hashlib.md5(password.encode()).hexdigest()

def read_password_file(file_path='passwd.txt'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def write_password_file(password_entries, file_path='passwd.txt'):
    with open(file_path, 'w') as file:
        file.write('\n'.join(password_entries))

def find_user(username, password_entries):
    for entry in password_entries:
        if entry.startswith(f"{username}:"):
            return entry
    return None
