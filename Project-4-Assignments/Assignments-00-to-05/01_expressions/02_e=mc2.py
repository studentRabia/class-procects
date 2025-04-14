# Problem Statement
#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

#E = m * c**2

#Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

#Here's a sample run of the program (user input is in bold italics):

#Enter kilos of mass: 100

#e = m * C^2...

#m = 100.0 kg

#C = 299792458 m/s

#8.987551787368176e+18 joules of energy!


print("🚀 Welcome to the Mass-Energy Converter using Einstein's Equation!")
print("-"*70)
print("📘 Formula: E = m × c² (where c = 299,792,458 m/s)\n")

def energy():
    c:float = 299792458  # Speed of light in m/s
    m:float = float(input("Enter kilos of mass: "))
    e:float = m * c**2  # Energy calculation using E = mc²
    print("\n🧪 e = m * c^2...")
    print(f"📦 m = {m} kg")
    print(f"⚡ C = {c} m/s")
    print(f"🔥 {e:.16e} joules of energy!")  # Display energy in scientific notation



if __name__ == "__main__":
    energy()






"""
C = 299_792_458  # meters per second

def main():
    print("\n🚀 Welcome to the Mass-Energy Converter using Einstein's Equation!")
    print("-"*70)
    print("📘 Formula: E = m × c² (where c = 299,792,458 m/s)\n")

    while True:
        user_input = input("\nEnter kilos of mass (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("\n👋 Exiting the program. Stay curious, scientist!")
            break

        try:
            mass = float(user_input)
            if mass < 0:
                print("⚠️  Please enter a **positive** mass value.")
                continue

            energy = mass * C**2

            print("\n🧪 e = m * c^2...")
            print(f"📦 m = {mass} kg")
            print(f"⚡ C = {C} m/s")
            print(f"🔥 {energy:.16e} joules of energy!")  # Scientific notation

        except ValueError:
            print("❌ Invalid input. Please enter a valid number for mass.")

if __name__ == "__main__":
    main()
"""