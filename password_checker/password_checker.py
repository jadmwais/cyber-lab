import re

def check_password_strength(password):
    length_score = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'\d', password)
    symbol = re.search(r'[\W_]', password)

    score = sum([length_score, bool(upper), bool(lower), bool(digit), bool(symbol)])

    print("\n🔍 Password Analysis:")
    print(f"- Length: {len(password)} characters")
    print(f"- Uppercase letters: {'✔️' if upper else '❌'}")
    print(f"- Lowercase letters: {'✔️' if lower else '❌'}")
    print(f"- Numbers: {'✔️' if digit else '❌'}")
    print(f"- Symbols: {'✔️' if symbol else '❌'}")

    if score == 5:
        return "💪 Strong"
    elif score >= 3:
        return "🟡 Moderate"
    else:
        return "🔴 Weak"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(f"\nStrength Rating: {result}")
