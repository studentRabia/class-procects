#
## Problem #1: List Practice
#
#Now practice writing code with lists! Implement the functionality described in the comments below. 
#
#def main():
#    # Create a list called `fruit_list` that contains the following fruits: 
#    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
#    
#    
#    # Print the length of the list.
#
#    
#    # Add 'mango' at the end of the list. 
#
#
#    # Print the updated list.
#
#
## Problem #2: Index Game
#
#As a warmup, read this code and play the game a few times. Use this mental model of the list:
### Objective:
#Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.
#
### Instructions:
#### Initialize a List:
#Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.
#
#### Accessing Elements:
#Write a function that:
#- Accepts a list and an index as inputs.
#- Returns the element at the specified index.
#- If the index is out of range, return an appropriate message.
#
#### Modifying Elements:
#Write a function that:
#- Accepts a list, an index, and a new value as inputs.
#- Replaces the element at the specified index with the new value.
#- If the index is out of range, return an appropriate message.
#
#### Slicing the List:
#Write a function that:
#- Accepts a list, a start index, and an end index as inputs.
#- Returns a new list containing the elements from the start index up to (but not including) the end index.
#- Handles cases where the indices are out of range.
#
#### Game Interaction:
#Create a simple text-based game that:
#- Prompts the user to select an operation (access, modify, slice).
#- Asks for the necessary inputs (index, new value, etc.).
#- Displays the result and the updated list.
#



#milestone1
def main():
    # Create a list called fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of the list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

# Run the main function
if __name__ == "__main__":
    main()


##milestone2
#my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#print("List:", my_list)
#
#while True:
#    print("\nChoose an option:")
#    print("1. Access element")
#    print("2. Modify element")
#    print("3. Slice list")
#    print("4. Quit")
#
#    choice = input("Enter your choice (1-4): ")
#
#    if choice == '1':
#        index = int(input("Enter index to access: "))
#        if 0 <= index < len(my_list):
#            print("Element at index", index, "is", my_list[index])
#        else:
#            print("Index out of range!")
#
#    elif choice == '2':
#        index = int(input("Enter index to modify: "))
#        if 0 <= index < len(my_list):
#            new_value = input("Enter new value: ")
#            my_list[index] = new_value
#            print("Updated list:", my_list)
#        else:
#            print("Index out of range!")
#
#    elif choice == '3':
#        start = int(input("Enter start index: "))
#        end = int(input("Enter end index: "))
#        if 0 <= start < len(my_list) and 0 < end <= len(my_list) and start < end:
#            print("Sliced list:", my_list[start:end])
#        else:
#            print("Invalid slicing range!")
#
#    elif choice == '4':
#        print("Goodbye!")
#        break
#
#    else:
#        print("Invalid choice. Try again!")
#
#    print("Current List:", my_list)
#