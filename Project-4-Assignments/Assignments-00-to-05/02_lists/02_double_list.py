#Problem Statement
#Write a program that doubles each element in a list of numbers. For example, if you start with this list:
#
#numbers = [1, 2, 3, 4]
#
#You should end with this list:

numbers = [2, 4, 6, 8]



def double_numbers(numbers: list[int]) -> list[int]:
    """
    Ye function har number ko 2 se multiply karta hai
    aur ek naye list mein return karta hai.
    """
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled

def main():
    print("📝 Problem Statement:")
    print("Write a program that doubles each element in a list of numbers.")
    print("-"*70)
    numbers = [1, 2, 3, 4]  # Original list
    result = double_numbers(numbers)
    print("\n👉🏻 Original List:", numbers)
    print("👉🏻 Doubled List:", result)

if __name__ == '__main__':
    main()

"""
def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    print("👉🏻 Original List:", numbers)  # Print original before modification

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2

    print("\n👉🏻 The doubled list is:", numbers)  # Print the modified list

print("\n📝 Writing a program that doubles each element in a list of numbers.")
print("-" * 70)




if __name__ == '__main__':
    main()
    
"""