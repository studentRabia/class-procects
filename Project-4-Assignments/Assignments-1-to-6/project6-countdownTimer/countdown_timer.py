import time

print("⌚ Welcome to the Countdown Timer❕")
print("-"*70)

seconds = int(input("\n👉🏻 Enter the time in seconds: "))
while seconds >0:
    print(f"\n⏳ Time left: {seconds} seconds" )
    time.sleep(1)
    seconds -= 1
print("\n⏰ Time's up❕")

