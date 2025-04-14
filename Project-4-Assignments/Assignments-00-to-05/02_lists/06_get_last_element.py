#Problem Statement
#Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    print("\n👉🏻 Last element in the list is:", lst[-1])  # Aakhri item print karta hai


print("\n\t\t📝 Problem Statement:")
print("-"*80)
print("\n🔻 Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.")
def main():
    lst = []

    while True:
        val = input("\nEnter a value (or press Enter to finish): ")
        if val == "":
            break
        lst.append(val)

    print("\n📃 List contents: ", lst)
    get_last_element(lst)

if __name__ == "__main__":
    main()
