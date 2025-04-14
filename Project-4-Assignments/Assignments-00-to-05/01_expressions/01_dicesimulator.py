#Problem Statement
#Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.




import random  # random module ko import karte hain

def roll_dice():
    # Do dice roll karna
    die1 = random.randint(1, 6)  # Dice 1 ka roll
    die2 = random.randint(1, 6)  # Dice 2 ka roll

    return die1, die2  # Dice 1 aur Dice 2 ka result return karte hain

def main():
    
    num_rolls = 3  # Fixed value for rolling 3 times
    
    # Roll karne ke liye loop
    for roll_num in range(1, num_rolls + 1):
        die1, die2 = roll_dice()  # roll_dice function ko call karte hain

        print(f"\n🎲 Roll {roll_num}:\n Die 1 = {die1}, Die 2 = {die2},\n Sum = {die1 + die2}")

# Agar ye script directly run ho to main function ko call karenge
if __name__ == "__main__":
    main()


    



"""import random  # random module ko import karte hain

def roll_dice():
    # 2 dice roll karna
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    return die1, die2  # Dice 1 aur Dice 2 ka result return karte hain

def main():
    num_rolls = int(input("\n🎲 Aap kitni dafa dice roll karna chahenge? "))
    
    # Roll karne ke liye loop
    for roll_num in range(1, num_rolls + 1):
        die1, die2 = roll_dice()  # roll_dice function ko call karte hain
        print(f"\nRoll {roll_num}: Die 1 = {die1}, Die 2 = {die2}, \nSum = {die1 + die2}")

# Agar ye script directly run ho to main function ko call karenge
if __name__ == "__main__":
    main()"""
