import random

print("\n\t📜 Wellcome to story generator 🧾")
print("-"*60)
name:str=input("\n🖊  Enter your story chracter name: ")
city:str=input("🖊  Enter your city name: ")
verb:str=input("🖊  Enter your verb: ")
adjective:str=input("🖊  Enter your adjective: ")
adverb:str=input("🖊  Enter your adverb: ")




# List of story templates
stories = [
    f"""{name} moved to {city}, where every corner was filled with {adjective} charm. 
{name} loved to {verb} {adverb}, catching the attention of everyone nearby. 
People smiled as they passed, inspired by {name}'s energy. 
It was clear that {city} had found its newest spark.""",

    f"""{name} woke up early in {city}, ready for a {adjective} adventure. 
With a deep breath, {name} began to {verb} {adverb} down the quiet streets. 
The city slowly came to life around them. 
It felt like a perfect day.""",

    f"""{city} had never seen someone like {name} before. 
They would {verb} {adverb} through the markets, full of {adjective} joy. 
Kids followed, laughing and cheering. 
{name} brought the whole city to life with every step.""",

    f"""{name} arrived in {city} on a {adjective} afternoon. 
The air was fresh, and the world felt open. 
{name} began to {verb} {adverb}, enjoying every moment. 
Locals waved, knowing something special had just arrived.""",

    f"""In the heart of {city}, {name} found peace. 
They would often {verb} {adverb}, lost in thought. 
The {adjective} scenery made everything feel magical. 
Every day was a story waiting to be lived."""
]

# Randomly select one story
story: str = random.choice(stories)

# Print the selected story
print("\n------------------ Your  Story ----------------\n")
print(story)
