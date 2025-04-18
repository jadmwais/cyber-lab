import itertools
import string
import time

def brute_force(target, charset, max_length):
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(charset, repeat=length):
            guess = ''.join(guess_tuple)
            attempts += 1
            if guess == target:
                duration = time.time() - start_time
                return guess, attempts, duration

    return None, attempts, time.time() - start_time

if __name__ == "__main__":
    print("🔓 Brute Force Password Cracker (Lowercase Letters Only)\n")
    target = input("Enter the password to simulate cracking (e.g. abc): ").strip().lower()
    max_len = int(input("Max password length to try (recommended: 4 or 5): "))

    charset = string.ascii_lowercase

    print("\n⚙️ Cracking...\n")
    match, tries, time_taken = brute_force(target, charset, max_len)

    if match:
        print(f"✅ Password cracked: {match}")
        print(f"🧠 Attempts: {tries}")
        print(f"⏱ Time taken: {time_taken:.2f} seconds")
    else:
        print("❌ Password not cracked. Try increasing max length.")
