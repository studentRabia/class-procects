#Problem Statement
#Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
#
#Here's a sample run (user input is in blue):
#
#Enter a number: 42 The ones digit is 2


print("\n\twlcome to the program of print_ones_digit")
print("/"*60 )
def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("\nEnter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()
