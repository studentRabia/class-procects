#Problem Statement
#Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
#
#Here's a sample run of the program (user input in bold italics):
#
#Enter a number: 2 Double that is 4

def double(num):
    return num * 2  # Multiply the number by 2 and return the result

def main():
    user_input = input("Enter a number: ")  # Ask user for input
    try:
        num = float(user_input)  # Convert the input to a number (float for flexibility)
        result = double(num)  # Call the double function
        print(f"Double that is {result}")  # Print the doubled result
    except ValueError:
        print("Please enter a valid number.")  # Handle invalid input

# Call main function
if __name__ == "__main__":
    main()



"""
def double(num: int):
    return num * 2

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
    """