#Problem Statement
#You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
#
#This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
#
#For example, using a hash function called SHA256(...) something as simple as
#
#hello
#
#can be hashed into a much more complex
#
#2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
#
#Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
#
#(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)

#👉🏻hashlib
#Ye function password ko SHA-256 ke through hash kar raha hai.
#password.encode() → string ko bytes mein convert karta hai.
#sha256(...) → hashing karta hai.
#.hexdigest() → uska hexadecimal string banata hai (like: 2cf24dba...)

import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify login by comparing hashed passwords
def login(email, password_to_check, stored_logins):
    # Step 1: Check if the email exists
    if email not in stored_logins:
        return False

    # Step 2: Hash the password provided by the user
    hashed_input = hash_password(password_to_check)

    # Step 3: Compare with stored hash
    return hashed_input == stored_logins[email]

# -------------------------------
# 🧪 Example usage of the program
# -------------------------------

# Step 1: Stored emails and their hashed passwords
stored_logins = {
    "alice@example.com": hash_password("apple123"),
    "bob@example.com": hash_password("banana456"),
    "charlie@example.com": hash_password("cherry789")
}

# Step 2: Ask user for login input
print("\t🔐 Welcome to Secure Login System")
print("_."*30)
email_input = input("\n📧 Enter your email: ")
password_input = input("🔑 Enter your password: ")

# Step 3: Login check
if login(email_input, password_input, stored_logins):
    print("\n✅ Login successful❕ 🎉 Welcome,", email_input)
else:
    print("\n❌ Login failed❗ Incorrect email or password.")
