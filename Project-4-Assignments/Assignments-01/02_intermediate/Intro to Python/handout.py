#Problem: Planetary Weight Calculator
#Milestone #1: Mars Weight
#A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!
#
#Ingenuity on the surface of Mars (source: NASA)
#
#When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.
#
#The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.



# Gravity constants
MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def main():
    print("\n\t🧮  CalculatorWelcome to Planetary Weight Calculator  🧮")
    print("🌏____________________________________________________________________🌏")
    # Prompt user for weight on Earth
    earth_weight = float(input("\n🔄  Enter your weight on Earth (in kg): "))

    # Prompt user for planet
    planet = input("\n🌏 Enter a planet: ")

    # Determine gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("\n⛔ Invalid planet name.")
        return

    # Calculate and print equivalent weight
    planetary_weight = round(earth_weight * gravity_constant, 2)
    print(f"\n⚖  Your weight on {planet} would be: {planetary_weight} kg")

# Run the program
if __name__ == "__main__":
    main()
