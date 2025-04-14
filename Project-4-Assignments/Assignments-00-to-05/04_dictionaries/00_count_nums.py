#Problem Statement
#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
#
#An example run of the program looks like this (user input is in blue):
#
#Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

print("This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.")
print("-" * 80)
def main():
    counts = {}  
    while True:
        num = input("Enter a number: ")

        if num == "":
            break  

        if num in counts:
            counts[num] += 1  # agar number pehle se dictionary mein hai, count badhao
        else:
            counts[num] = 1   # agar pehli dafa aaya hai, to count 1 karo

    for number in counts:
        print(f"{number} appears {counts[number]} times.")

if __name__ == "__main__":
    main()
