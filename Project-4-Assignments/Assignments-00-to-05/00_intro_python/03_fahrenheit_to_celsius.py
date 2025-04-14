#Problem Statement
#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

#The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

#The equation you should use for converting from Fahrenheit to Celsius is the following:

#degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

#(Note. The .0 after the 5 and 9 matters in the line above!!!)

#Here's a sample run of the program (user input is in bold italics):

#Enter temperature in Fahrenheit: 76

#Temperature: 76.0F = 24.444444444444443C




"""def main():
    user_temp = int(input("Enter a number in Fahrenheit: "))
    degrees_celsius = (user_temp - 32) * 5.0/9.0
    print(f"{user_temp} degrees Fahrenheit is equal to {degrees_celsius:.2f} degrees Celsius.")

main()"""


from rich.console import Console
console = Console()

def main():
    while True:
        user_input = input("Enter a number in Fahrenheit 🌡 : ")
        try:
            user_temp = float(user_input)  # Supports decimal temperatures too
            degrees_celsius = (user_temp - 32) * 5.0 / 9.0

            # Print input in bold and italic
            
            console.print(f"\n[bold italic red]🌡[/bold italic red] [bold italic yellow]You Enter a number in Fahrenheit[/bold italic yellow] {user_input}")
            console.print(f"\n[bold italic red]🌡[/bold italic red] [bold italic yellow]{user_temp}°F [/bold italic yellow]is equal to [bold italic red]{degrees_celsius:.2f}°C[/bold italic red].")
            break  # Exit loop after successful input
        except ValueError:
            print("\n❌ Invalid input❗ Please enter a valid number (e.g., 98 or 98.6).\n")

main()
