
#Problem Statement
#In this program we show an example of using dictionaries to keep track of information in a phonebook.

print("☎  In this program we show an example of using dictionaries to keep track of information in a phonebook📕 .")
print("-" * 80)
def main():
    phonebook = {}  
    while True:
        name = input("Enter a name (or press Enter to stop): ")
        if name == "":
            break

        number = input(f"Enter the number for {name}: ")
        phonebook[name] = number  # dictionary mein add kiya

    print("\n📞 Phonebook📕 :")
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")

if __name__ == "__main__":
    main()
