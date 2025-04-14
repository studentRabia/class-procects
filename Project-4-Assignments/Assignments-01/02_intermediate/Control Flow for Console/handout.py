#Problem: High Low
#We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
#
#Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
#
#You make a guess, saying your number is either higher than or lower than the computer's number
#
#If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!
#
#These steps make up one round of the game. The game is over after all rounds have been played.
#
#We've provided a sample run below.




#------------------👉🏻Milestones------------------


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
