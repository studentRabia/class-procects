#Problem Statement
#Guess My Number
#
#I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
#
#Enter a new number: 25 Your guess is too low
#
#Enter a new number: 40 Your guess is too low
#
#Enter a new number: 45 Your guess is too low
#
#Enter a new number: 48 Congrats! The number was: 48


import random

def guess_my_number():
    # Step 1: Computer ek random number choose karta hai
    secret_number = random.randint(0, 99)

    print("🎲 I am thinking of a number between 0 and 99...")
    print("_" * 70)
    print("🤔 Can you guess it?\n")

    while True:
        # Step 2: User se guess mangna
        try:
            guess = int(input("💡 Enter a guess: "))
        except ValueError:
            print("⛔ Please enter a valid number!")
            continue

        # Step 3: Check karna guess sahi hai ya nahi
        if guess < secret_number:
            print("📉 Your guess is too low\n")
        elif guess > secret_number:
            print("📈 Your guess is too high\n")
        else:
            print(f"🎉 Congrats! The number was: {secret_number}")
            break  # Loop se bahar nikal jao (game complete)

# Run the game
guess_my_number()
