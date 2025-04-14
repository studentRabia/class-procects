
#Problem Statement
#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

#Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

#What's your favorite animal? cow

#My favorite animal is also cow!


def tell():
    animal=str(input("What's your favorite animal? "))
    print(f"\nMy favorite animal is also {animal}!")
    print("I love 💖 animals!🐪")

if __name__ == "__main__":
    tell()






"""from rich.console import Console

console = Console()  # Create a Console object

def main(prompt: str):
    print(f"\nMy favorite animal is {prompt}")
    print("I love 💖 animals!🐪")

while True:
    user_input = input("What's your favorite animal? (type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("\nGoodbye! 👋")
        break
    
    if user_input.isalpha():  # Check if input is valid (only letters)
        main(user_input)  # Call main function with user input
        
        # Print input in bold and italic using the rich library
        console.print("\n💠 [bold italic green]You entered:[/bold italic green]💠")
        console.print(f"\n🔹🦩 [bold italic yellow]Your write [/bold italic yellow] {user_input} 🔹")
        console.print(f"\nYour favorite animal is 🐄 [bold italic red]{user_input}[/bold italic red].\n")
    else:
        print("\n❌ Error: Please enter only letters (no numbers or special characters). Try again.\n")

"""