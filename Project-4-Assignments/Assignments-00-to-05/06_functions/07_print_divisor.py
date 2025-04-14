#Problem Statement
#Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
#
#Here's a sample run (user input is in blue):
#
#Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12print("welcome to the world of python")

print("\n✨  welcome to the program of print_divisors")
print("-" * 50)


def print_divisors(num):
    print(f"\n➗ Here are the divisors of '{num}'")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')  # Print on the same line

def main():
    user_input = int(input("\n📝 Enter a number: "))
    print_divisors(user_input)

# Run the program
if __name__ == '__main__':
    main()
