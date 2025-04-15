import hashlib

def hash_string(data, algorithm='sha256'):
    if algorithm == 'md5':
        return hashlib.md5(data.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(data.encode()).hexdigest()
    else:
        return None

if __name__ == "__main__":
    print("Hash Generator (Python)\n")
    text = input("Enter text to hash: ")

    print("\nChoose algorithm:")
    print("1. MD5")
    print("2. SHA-256")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        result = hash_string(text, 'md5')
        print("\nMD5 Hash:")
    elif choice == '2':
        result = hash_string(text, 'sha256')
        print("\nSHA-256 Hash:")
    else:
        print("\nInvalid choice.")
        exit()

    print(result)
