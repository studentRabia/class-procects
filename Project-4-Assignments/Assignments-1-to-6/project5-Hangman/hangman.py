import random

words = ["python", "java", "html", "javascript"]
word = random.choice(words)
guessed_letters = []
tries = 10

print("\t\t🎮 Welcome to the Hangman game❕")
print("-" * 70)
print("\n💡 Guess the word!")

# Function to display the current guessed word
def get_display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Initial display
print(get_display_word())

while tries > 0:
    guess = input("🤔 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🤷‍♂️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess❕")
    else:
        print("❌ Wrong guess❗")
        tries -= 1
        print(f"💔 You have {tries} tries left.")

    # Always show the updated word
    print(get_display_word())

    # Check if word is fully guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations❕ You guessed the word correctly❕ 😊")
        break
else:
    print(f"💔 You lost❕ The word was: {word}")
