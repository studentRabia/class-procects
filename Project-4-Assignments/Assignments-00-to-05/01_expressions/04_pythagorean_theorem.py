#Problem Statement
#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
#
#The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.
#
#For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:
#
#BC ** 2 = AB ** 2 + AC ** 2
#
#Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.
#
#Here's a sample run of the program (user input is in bold italics):
#
#Enter the length of AB: 3
#
#Enter the length of AC: 4
#
#The length of BC (the hypotenuse) is: 5.0





import math  # Square root function ke liye

def main():
    print("\n🧮 Welcome to the Pythagorean Theorem Calculator!")
    print("-"*70)
    print("To find the hypotenuse (BC), please provide lengths of AB and AC.\n")

    # User se input lein
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Hypotenuse calculate karna
    bc = math.sqrt(ab ** 2 + ac ** 2)
    rounded_bc = round(bc)  # 3 decimal tak round karna  

    # Result print karna
    #print(f"\n📐 The length of BC (the hypotenuse) is: {bc:.3f}")
    print(f"\n📐 The length of BC (the hypotenuse) is: {rounded_bc}")

# Program start hota hai yahan se
if __name__ == "__main__":
    main()
