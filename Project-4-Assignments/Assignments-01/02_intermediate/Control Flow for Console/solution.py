import random

def main():
    print("\n\tWelcome to the High-Low Game❕")
    print('🎯--------------------------------------🎯')
    #Milestone #4: Play multiple rounds
    rounds = int(input("\nHow many rounds do you want to play❔ "))
    score = 0

    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        score += play_round()
    #Milestone #5: Adding a points system
    print(f"\nGame over❕ Your final score: {score} out of {rounds}")


def play_round():
    #Milestone #1: Generate the random numbers
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is: {user_number}")
    #Milestone #2: Get the user choice
    guess = input("Is your number higher or lower than the computer's❔ (Enter 'higher' or 'lower'): ").strip().lower()
    #Milestone #3: Write the game logic
    if user_number == computer_number:
        print("It's a tie❕ No points.")
        return 0

    actual_result = "higher" if user_number > computer_number else "lower"

    if guess == actual_result:
        print(f"✔  You guessed right❕ Computer's number was: {computer_number}")
        return 1
    else:
        print(f"❌ Wrong guess. Computer's number was: {computer_number}")
        return 0


if __name__ == '__main__':
    main()
