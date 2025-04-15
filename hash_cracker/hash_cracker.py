import hashlib

def hash_word(word, algorithm='sha256'):
    word = word.strip()
    if algorithm == 'sha256':
        return hashlib.sha256(word.encode()).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(word.encode()).hexdigest()
    return None

def crack_hash(target_hash, wordlist_file, algorithm='sha256'):
    try:
        with open(wordlist_file, 'r') as f:
            for line in f:
                candidate = line.strip()
                candidate_hash = hash_word(candidate, algorithm)

                if candidate_hash == target_hash:
                    print(f"✅ Password found: {candidate}")
                    return
        print("❌ Password not found in wordlist.")
    except FileNotFoundError:
        print(f"❌ Wordlist file '{wordlist_file}' not found.")

if __name__ == "__main__":
    print("🔓 Hash Cracker (Dictionary Attack)\n")

    target_hash = input("Enter SHA-256 or MD5 hash: ").strip()
    wordlist = input("Enter path to wordlist file (e.g. wordlist.txt): ").strip()

    algo = input("Algorithm (sha256/md5): ").strip().lower()
    if algo not in ['sha256', 'md5']:
        print("❌ Invalid algorithm.")
    else:
        crack_hash(target_hash, wordlist, algo)
