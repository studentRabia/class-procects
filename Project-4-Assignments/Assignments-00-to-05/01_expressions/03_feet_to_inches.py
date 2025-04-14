#Problem Statement
#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    print("\n📏 Welcome to the Feet-to-Inches Converter!")
    print("-"*60)
    print("🔁 1 foot = 12 inches\n")

    # User se input lena
    feet = float(input("\nEnter the length in feet: "))

    inches:float = feet * 12
    # Conversion

    # Output
    print(f"\n📐 {feet} feet is equal to {inches:.3f} inches.")

# Program yahin se start hoga
if __name__ == "__main__":
    main()
