#Problem Statement
#Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
#
#The first even number is 0:
#
#0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

print("\t🧠 Even numbers from 0 to 38:")
print("_" * 70)
print("\t🤔 Can you guess it?\n")

def print_even_numbers():
    for i in range(20):  # 0 to 19 (20 numbers)
        print(i * 2, end=" ")

print_even_numbers()
print("\n")
print("🌼"*40)

def print_even_numbers():
    print("\n\n\t🧠 Even numbers from 0 to 38:")
    print("^" * 70)
    num = 0
    count = 0
    while count < 20:
        print(num, end=" ")
        num += 2
        count += 1

print_even_numbers()
