import random
print("\n\t🎉 Wellcome to Rock, Paper, Scissors Battle❕")
print("-"*70)
print("\n🤖 You can play against the 💻 computer or a 👧🏻 friend. Let's start❕")
print("-"*70)
print("\n💻 Computer vs 👧🏻 Friend")

while True:
    user_choice = input("\nChoose your Weapon Rock 🚞, Paper 📄, or Scissors ✂ (or 'q' to quit): ").lower()
    if user_choice not in ["rock", "paper", "scissors", "q"]:
        print("\n❌Invalid choice❗ Please try again.")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\n👧🏻 You chose: {user_choice}")
    print(f"\n💻 Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("\n🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("\n🏆 You win!")
    else:
        print("\n💻 Computer wins❕")
    if user_choice == "q":
        print("\n👋 Goodbye❕")
        break   
