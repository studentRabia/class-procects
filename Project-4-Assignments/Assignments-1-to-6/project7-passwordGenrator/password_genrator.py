import random
import string       #Letters, digits, aur punctuation ki predefined lists provide karta hai.

print("🔑 Welcome to the Password Generator!")
print("-"*70)

characters =  string.ascii_letters + string.digits + string.punctuation
password_length = input("\n👉🏻Enter the desired password length (minimum 8 characters): ")
password_length=int(password_length)
if password_length < 4:
    print("\n❌ Password length must be at least 4 characters. Please try again.")
else:
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print("\n✅ Your generated password is: ", password)
    print("-"*70)   
