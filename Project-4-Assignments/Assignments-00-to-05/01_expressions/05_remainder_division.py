#Problem Statement
#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
#
#Here's a sample run of the program (user input is in bold italics):
#
#Please enter an integer to be divided: 5
#
#Please enter an integer to divide by: 3
#
#The result of this division is 1 with a remainder of 2





def main():
    print("📏 Welcome❕ Let's divide two numbers and find the remainder.")
    print("-"*70)
    print("\t\t🔁 Division and Remainder\n")
    # User se input lena
    num1 = int(input("🖋  Please enter an integer to be divided: "))
    num2 = int(input("🖋  Please enter an integer to divide by: "))

    # Division aur remainder
    quotient = num1 // num2      # integer division
    remainder = num1 % num2      # remainder

    # Output
    print(f"\n👉🏻 The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
