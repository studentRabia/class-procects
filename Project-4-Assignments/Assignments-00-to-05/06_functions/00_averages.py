#Problem Statement
#Write a function that takes two numbers and finds the average between the two.


print("\n📏  Welcome to the average calculator!")
print("- "*30)
print("This program will calculate the average of two numbers.\n")

def find_average(num1, num2):
    average = (num1 + num2) / 2
    return average

def main():
    
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate average
    result = find_average(num1, num2)

    # Print result
    print("\n🛸 The average is:", result)

# Run the program
if __name__ == "__main__":
    main()
