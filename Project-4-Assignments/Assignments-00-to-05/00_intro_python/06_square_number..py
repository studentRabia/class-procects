#Problem Statement
#Ask the user for a number and print its square (the product of the number times itself).

#Here's a sample run of the program (user input is in bold italics):

#Type a number to see its square: 4

#4.0 squared is 16.0


def square_number():
    print("\n\t🧮 Welcome to the Square Number Calculator! 🧮")
    print("-"*70)
    print("🖋  To calculate the square of a number, please provide the number.\n")
    num=float(input("Type a number to see its square: "))
    square=num**2
    print(f"\n👉🏻 {num} squared is: {square}.")
    print("Thank you for using the program❕ 👋🏻")


if __name__ == "__main__":
    square_number()


"""rom rich.console import Console

from rich.console import Console

console = Console()  # ✅ create a Console object

def main():
    # Ask the user to input a number
    print("\n\t🧮 Welcome to the Square Number Calculator! 🧮")
    console.print("[bold purple]-[/bold purple]"*70)
    console.print("[bold purple]🖋[/bold purple]  To calculate the square of a number, please provide the number.\n")

    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number * number
    # Print input in bold and italic
    console.print("\n👉🏻 [bold italic red]You entered:[/bold italic red]")
    console.print(f"\n🔹 [bold italic yellow]The number to see Squre:[/bold italic yellow] {number} 🔹")

    
    # Print the result
    console.print(f"\n[bold italic purple]{number}[/bold italic purple] [bold green]🟦 squared is[/bold green] [bold italic red]{square}[/bold italic red] ")

if __name__ == "__main__":
    main()
    """
