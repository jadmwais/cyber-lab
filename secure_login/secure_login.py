import hashlib
import os

USER_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    hashed_pw = hash_password(password)

    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed_pw}\n")

    print("✅ Registration successful!")

def login_user():
    username = input("Username: ")
    password = input("Password: ")
    hashed_pw = hash_password(password)

    if not os.path.exists(USER_FILE):
        print("❌ No users registered yet.")
        return

    with open(USER_FILE, "r") as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(":")
            if stored_user == username and stored_hash == hashed_pw:
                print("✅ Login successful!")
                return

    print("❌ Login failed. Invalid username or password.")

def main():
    print("🔐 Secure Login Simulation")
    print("1. Register")
    print("2. Login")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
