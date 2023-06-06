import hashlib
import random
import string

# Function to generate a random salt
def generate_salt():
    salt_length = 16
    characters = string.ascii_letters + string.digits
    salt = ''.join(random.choice(characters) for _ in range(salt_length))
    return salt

# Function to hash the password with salt using SHA256
def hash_password(password, salt):
    hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    return hashed_password

# Create a password array and use it for identification
def create_password_array(num_users):
    usernames = []
    passwords = []
    for i in range(num_users):
        username = input(f"Enter username for user {i+1}: ")
        password = input(f"Enter password for user {i+1}: ")
        usernames.append(username)
        passwords.append(password)
    
    return usernames, passwords

# Modify one password to store the hash value and use it
def modify_password_array(passwords):
    hashed_passwords = []
    salts = []
    for password in passwords:
        salt = generate_salt()
        hashed_password = hash_password(password, salt)
        hashed_passwords.append(hashed_password)
        salts.append(salt)
    
    return hashed_passwords, salts

# Identification process
def identify_user(usernames, hashed_passwords, salts):
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    
    if username_input in usernames:
        index = usernames.index(username_input)
        hashed_input = hash_password(password_input, salts[index])
        
        if hashed_input == hashed_passwords[index]:
            print("Access granted!")
        else:
            print("Incorrect password!")
    else:
        print("User not found!")

# Enter the number of users
num_users = int(input("Enter the number of users: "))

usernames, passwords = create_password_array(num_users)
hashed_passwords, salts = modify_password_array(passwords)

identify_user(usernames, hashed_passwords, salts)
