#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

#Prompt the user to enter the first number.

#Read the input and convert it to an integer.

#Prompt the user to enter the second number.

#Read the input and convert it to an integer.

#Calculate the sum of the two numbers.

#Print the total sum with an appropriate message.



print("\n\t\t🧮 Program to add two numbers 🧮")
print("*" * 70)


number_1:int=int(input("\n1️⃣  Enter first number: "))
number_2:int=int(input("2️⃣  Enter second number: "))
sum:int=number_1+number_2
print(f"\n➕ The sum of two numbers is: {sum}\n")

print(("Thank you for using the program!").center(70, "🧮"))




"""def add():
    print("\n\t\t🧮 Program to add two numbers 🧮")
    print("-"*70)
    first_no = int(input("\n1️⃣  Enter first number: "))
    second_no = int(input("2️⃣  Enter second number: "))
    total = first_no + second_no
    print(f"\n➕ The sum of two numbers is: {total}\n")
    print(("Thank you for using the program!").center(70, "🧮"))



if __name__ == "__main__":
    add()"""






"""def main():
    print("\n\t\t🧮 Program to add two numbers 🧮")
    print("*" * 60)
    print("\nType 'exit' anytime to quit.\n")

    while True:
        first_input = input("Enter first number : ")
        if first_input.lower() == "exit":
            print("Exiting the program. Goodbye!👋🏻")
            break

        second_input = input("Enter second number : ")
        if second_input.lower() == "exit":
            print("Exiting the program. Goodbye!👋🏻")
            break

        try:
            first_no = int(first_input)
            second_no = int(second_input)
            total = first_no + second_no
            print("\nSum ➕ of two numbers is:", total, "\n")
        except ValueError:
            print("\n⚠️ Please enter valid numbers!\n")



# This provided line is required at the end of
# Python file to call the main() function.

if __name__ == "__main__":  
    main()"""
