import random
print("\t👲🏻🕹  Welcome to the Guessing Game! 🕹 👲🏻")
print("-" * 60)
print("🔢 I have a number between 1 and 100, and you have to guess it❕")
secret_number = random.randint(1, 5)
print("🤔 Can you guess it❔")
attempts = 0
while True:
    try:
        guess=int(input("\nEnter your guess: "))
        attempts +=1
        if guess < 1 or guess > 100:
            print("\n❌ Invalid input! Please enter a number between 1 and 100.")
            continue
        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts❕")
            print("\n\t🎊 Thanks for playing!  🎊")
            break
    except ValueError:
        print("\n❌ Invalid input❕ Please enter a valid number.")

