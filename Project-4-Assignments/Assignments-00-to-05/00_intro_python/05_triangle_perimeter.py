#20Problem Statement
#20Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
#20
#20Here's a sample run of the program (user input is in bold italics):

#20What is the length of side 1? 3

#20What is the length of side 2? 4

#20What is the length of side 3? 5.5

#20The perimeter of the triangle is 12.5




"""def main():
    print("\t🧮 Welcome to the Triangle Perimeter Calculator! 🧮")
    print("-"*70)
    print("🖋  To calculate  the perimeter of a triangle, please provide the lengths of its three sides.\n")
  
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    perimeter = side1 + side2 + side3

    print(f"\nThe perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()

"""




from rich.console import Console

console = Console()  # ✅ create a Console object

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a number (e.g., 5 or 7.5).\n")

def main():
    print("\n📐 Welcome! This program calculates the perimeter of a triangle. 📐")
    print("🧮" + "-" * 70 + "🧮\n")
    print("🖋 To calculate the perimeter, please provide the lengths of its three sides.\n")
    print("👉 Please enter the lengths of all three sides.\n")

    side1 = get_valid_float("🔹 Length of side 1: ")
    side2 = get_valid_float("🔹 Length of side 2: ")
    side3 = get_valid_float("🔹 Length of side 3: ")

    perimeter = side1 + side2 + side3

    # Print input in bold and italic
    console.print("\n🔹 [bold italic green]You entered:[/bold italic green]")
    console.print(f"\n🔹 [bold italic yellow]Side 1:[/bold italic yellow] {side1}")
    console.print(f"🔹 [bold italic yellow]Side 2:[/bold italic yellow] {side2}")
    console.print(f"🔹 [bold italic yellow]Side 3:[/bold italic yellow] {side3}")


 # Printing perimeter in bold, italic, and green
    console.print(f"\n✅ [bold italic green]The perimeter is [bold italic red]{perimeter}[/bold italic red] units.[/bold italic green]\n")
    console.print("🎉 Thank you for using the [bold italic green]Triangle Perimeter Calculator❕[/bold italic green]")

if __name__ == "__main__":
    main()
