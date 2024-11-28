import random

def displayMenu():
    """Displays the difficulty level menu."""
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    """Generates random integers based on difficulty level."""
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

def decideOperation():
    """Randomly decides whether the operation is addition or subtraction."""
    return '+' if random.choice([True, False]) else '-'

def displayProblem(num1, num2, operation):
    """Displays the question to the user and accepts their answer."""
    print(f"{num1} {operation} {num2} = ", end="")
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def isCorrect(user_answer, correct_answer):
    """Checks if the user's answer is correct."""
    return user_answer == correct_answer

def displayResults(score):
    """Displays the user's final score and rank."""
    print(f"\nYour final score: {score}/100")
    if score > 90:
        rank = "A+"
    elif score > 80:
        rank = "A"
    elif score > 70:
        rank = "B"
    elif score > 60:
        rank = "C"
    else:
        rank = "F"
    print(f"Your rank: {rank}")

def playQuiz():
    """Main quiz logic."""
    displayMenu()
    try:
        difficulty = int(input("Select difficulty level (1-3): "))
        if difficulty not in [1, 2, 3]:
            print("Invalid choice. Please select a valid difficulty level.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    score = 0
    for _ in range(10):
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        operation = decideOperation()
        correct_answer = num1 + num2 if operation == '+' else num1 - num2

        # First attempt
        user_answer = displayProblem(num1, num2, operation)
        if user_answer is not None and isCorrect(user_answer, correct_answer):
            print("Correct!")
            score += 10
            continue

        # Second attempt
        print("Incorrect. Try again.")
        user_answer = displayProblem(num1, num2, operation)
        if user_answer is not None and isCorrect(user_answer, correct_answer):
            print("Correct!")
            score += 5
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")

    displayResults(score)

def main():
    """Main program loop."""
    while True:
        playQuiz()
        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
