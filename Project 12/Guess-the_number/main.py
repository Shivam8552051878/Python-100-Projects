import random
import art

GUESS_NUMBER = round(random.random()*100)


def hint(num):
    global GUESS_NUMBER
    if (num > GUESS_NUMBER):
        print("To High\nGuess again.")
    elif (num < GUESS_NUMBER):
        print("To Low\nGuess again.")
    elif (num == GUESS_NUMBER):
        print(f"You got it! The answer was {num}")
    else:
        print("Sorry beter luck next time!!!")


welcomeMsg = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100."""
print(art.logo)
print(welcomeMsg)
level = {
    "easy": 10,
    "hard": 5
}
userChoice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number_chance = level[userChoice]
status = False
while not status:
    print(f"You have {number_chance} attempts remaining to guess the number.")

    userInput = int(input("Guess the number: "))
    if (number_chance < 1):
        print("You've run out of guesses, you lose.")
        status = True
    elif (GUESS_NUMBER == userInput):
        hint(userInput)
        status = True
    else:
        hint(userInput)

    number_chance -= 1
