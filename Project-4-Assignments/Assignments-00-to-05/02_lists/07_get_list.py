#Problem Statement
#Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
#
#Here's a sample run (user input is in blue):
#
#Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']
"""
print("\n\t\t📝 Problem Statement:")
print("-^-"*20)
print("\n🔻 Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.")


values = []

while True:
    val = input("Enter a value: ")
    if val == "":
        break
    values.append(val)

print("Here's the list:", values)
"""


def main():
    lst = []
    val = input("Enter a value: ")              # 2bar input--->- Pehli dafa start karne ke liye, aur loop ke andar baar-baar nayi value lene ke liye
    while val:                                   #Yani loop tab tak chalega jab tak val mein koi value hogi (yaani wo non-empty string hogi).Agar aap sirf Enter dabate hain bina kuch likhe, to val ban jaata hai khaali string — yaani "".
        lst.append(val)
        val = input("Enter a value: ")           #Agar hum loop ke andar dobara input na lein, to loop hamesha pehli value ke saath repeat hota rahega (infinite loop ban jaayega).To yeh sirf ek hi baar chalega, ya hamesha val wohi purani rahegi. New input kabhi nahi aayega.
    print("Here's the list:", lst)

if __name__ == "__main__":
    main()
