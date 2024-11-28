import random

def load_jokes(filename="Jokes.txt"):
    """Loads jokes from a file."""
    try:
        with open(filename, "r", encoding='ISO-8859-1') as file:
            return [line.strip() for line in file if '?' in line]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def tell_joke(jokes):
    """Picks and tells a random joke."""
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)
    print(f"\n{setup}?")
    input("Press Enter to see the punchline...")
    print(f"{punchline}\n")

def main():
    """Main interaction loop."""
    jokes = load_jokes()
    if not jokes:
        return  # Exit if no jokes are loaded

    print('Type "Alexa tell me a joke" to hear a joke, or "nah" to exit.')

    while True:
        command = input("> ").strip().lower()
        if command == "alexa tell me a joke":
            tell_joke(jokes)
        elif command == "nah":
            print("That’s a wrap! Time for a pun-break.")
            break
        else:
            print('Want another one? Type "Alexa tell me a joke" or "nah" to stop.')

if __name__ == "__main__":
    main()
