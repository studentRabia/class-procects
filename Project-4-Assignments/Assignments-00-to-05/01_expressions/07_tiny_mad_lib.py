#Problem Statement
#Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
#
#Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
#
#Here's a sample run (user input is in bold italics):
#
#Please type an adjective and press enter. tiny
#
#Please type a noun and press enter. plant
#
#Please type a verb and press enter. fly


from rich.console import Console
console = Console()

def main():
    # Intro message
    print("\n\t📜 Let's play a Mad Libs word game! 📜")
    print("-" * 70)
    print("You'll enter an adjective, a noun, and a verb — and we'll make a fun sentence!\n")

    # Get user inputs
    adjective:str = input("Please type an adjective and press enter: ")
    noun:str = input("Please type a noun and press enter: ")
    verb:str = input("Please type a verb and press enter: ")

    #print input in bold and italic
    console.print("\n[bold italic blue]Your inputs:[/bold italic blue]")
    console.print(f"\n[bold italic red]Adjective:[/bold italic red] [bold italic yellow]{adjective}[/bold italic yellow]")
    console.print(f"[bold italic red]Noun:[/bold italic red] [bold italic yellow]{noun}[/bold italic yellow]") 
    console.print(f"[bold italic red]Verb:[/bold italic red] [bold italic yellow]{verb}[/bold italic yellow]")     
    # Sentence template
    sentence_start = "Code in Place is fun. I learned to program and used Python to make my"

    # Combine everything into a full sentence
    full_sentence = f"\n{sentence_start} {adjective} {noun} {verb}❕"

    # Print the final story
    print("\n📝 Here's your fun sentence:")
    print(full_sentence)

if __name__ == "__main__":
    main()



"""

from rich.console import Console
console = Console()
def get_input(prompt):
    return input(prompt)
"""
# Collecting user inputs
"""
inputs = {
    "name": get_input("Enter your Name: "),
    "city": get_input("Enter City Name: "),
    "verb": get_input("Enter your Verb: "),
    "animal": get_input("Write an Animal Name: "),
    "adjective": get_input("Enter Adjective: ")
}
"""
# Print user inputs one by one in bold italic format

"""console.print("\n\t\t[bold italic cyan]***User Inputs:***[/bold italic cyan]")
for key, value in inputs.items():
    console.print(f"[bold italic cyan]{key.capitalize()}[/bold italic cyan]: [bold italic yellow]{value}[/bold italic yellow]")
"""

    
# Generating the story
"""
story = f'''
{inputs['name']} was walking through the busy streets of {inputs['city']}.
Suddenly, they saw a {inputs['adjective']} {inputs['animal']} near a cafe.
The {inputs['animal']} started to {inputs['verb']}, surprising everyone around.
{inputs['name']} couldn't believe their eyes and started laughing.
It was a day to remember in the heart of {inputs['city']}.
'''

console.print("\n\t\t[bold cyan]***Generated Story:***[/bold cyan]")
console.print("[bold purple]-[/bold purple]" * 60)
print(story)
"""