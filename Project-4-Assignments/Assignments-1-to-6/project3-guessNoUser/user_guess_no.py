import random
print("\t\t\t🎮🕹  Welcome to the Number Guessing Game! 🕹 🎮")
print("-"*90)
print("\n\tI have selected a random number between 1 and 100. Can you guess it?")
print("🏹🎯 _________________________________________________________________________ 🏹🎯 ")
low=1
high=100
attempts=0
while True:
    guess=random.randint(low,high)
    attempts+=1
    user_input=input(f"\n🧐 Is {guess} your guess❔ (H/L/C): ").strip().upper()

    if user_input == "H":
        high=guess-1
        print(f"\n\t↗ Your guess is too high❕ I will try again between {low} and {high}.")
    elif user_input == "L":
        low=guess+1
        print(f"\n\t↙ Your guess is too low❕ I will try again between {low} and {high}.")
    elif user_input == "C": 
        print(f"\n\t🤓 Yay❕ I guessed your number {guess} in {attempts} attempts❕")
        break
    else:
        print("\n\t❗Invalid input! Please enter 'H', 'L', or 'C'.")
    print("🏹🎯 _________________________________________________________________________ 🏹🎯 ")
