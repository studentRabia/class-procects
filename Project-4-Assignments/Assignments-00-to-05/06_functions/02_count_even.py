#Problem Statement
#Fill out the function count_even(lst) which
#
#first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
#
#and then prints the number of even numbers in the list.
#
#If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_even():
    lst = []

    # Input collection
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # empty input means stop taking numbers
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("⛔ Please enter a valid integer.")

    even_count = 0
    print("Even numbers are: ")
    # Loop to check for even numbers
    for num in lst:
        if num % 2 == 0:
            print(num, end=" ")  # Print each even number
            even_count += 1

    print(f"\nNumber of even numbers are : {even_count}")

# Run the function
if __name__ == "__main__":
    count_even()
