#Problem Statement
#Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
def get_first_element(lst):
    print(lst[0])

print("\n\t\t📝 Problem Statement:")
print("-"*120)
print("\n🔻 Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list.")

# Collect input from the user
n = int(input("\nEnter number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"\nEnter element {i + 1}: ")
    user_list.append(element)



# Call the function
get_first_element(user_list)
print("\n🔴 First element in the list: ", user_list[0])
print("👤 user list📃: ", user_list)
print("-"*150)
