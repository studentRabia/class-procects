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
