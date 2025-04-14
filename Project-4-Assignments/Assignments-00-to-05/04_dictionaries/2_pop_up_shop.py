#Problem Statement
#There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.
#
#Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
#
#Here is an example run of the program (user input is in bold italics):
#
#How many (apple) do you want?: 2
#
#How many (durian) do you want?: 0
#
#How many (jackfruit) do you want?: 1
#
#How many (kiwi) do you want?: 0
#
#How many (rambutan) do you want?: 1
#
#How many (mango) do you want?: 3
#
#Your total is $99.5


print("\n\t🍎 Welcome to the Fruit Shop 🍍")
print("🍇🍌🍐🍎🍒🥑🥭🍑🍏🍉🍈🍅🥑🥝"*2)
print("\nHere are the fruits available and their prices:")


# Dictionary of fruit and their prices
fruit_prices = {
    "apple🍎": 10.0,
    "durian": 25.0,
    "jackfruit": 20.0,
    "kiwi🥝": 12.5,
    "rambutan": 7.0,
    "mango🥭": 8.5
}

total_cost = 0.0

# Ask user for quantity of each fruit
for fruit, price in fruit_prices.items():
    qty_input = input(f"How many ({fruit}) do you want?: ")
    
    # Make sure input is a number
    try:
        quantity = int(qty_input)
    except ValueError:
        print("❗Please enter a valid number. Defaulting to 0.")
        quantity = 0

    total_cost += quantity * price

# Print the total cost
print("🍌---" * 10)
print(f"\n💰 Your total is: ${total_cost}")
print("🎉 Thank you for shopping with us! 🍉" )