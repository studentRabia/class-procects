#Problem Statement
#Simulate rolling two dice, and prints results of each roll as well as the total.

import random
num_side:int = 6

def main():
    print("\n\t🎲 Welcome to the Dice Roller!")
    print("-"*70)
    print(" 🎲 Let's roll two dice and see the results.")
    
    die1:int = random.randint(1, num_side)  # Dice 1 ka roll
    die2:int = random.randint(1, num_side)  # Dice 2 ka roll

    sum:int = die1 + die2  

    print("\n🎲 Diece have",num_side,"side each.")
    print("🔸 First die:", die1)
    print("🔸 Second die:", die2)
    print("📃 Total of both die:", sum)


if __name__ == "__main__":
    main()