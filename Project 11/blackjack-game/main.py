import random
import art
# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 
# print out some text
# print('hello geeks\n'*10)
 

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def addCard(score):
    value = random.choice(card)
    if value == 11:
        if (total_score(score) + 11 > 21):
            score.append(1)
        else:
            score.append(value)
    else:
        score.append(value)


def total_score(score):
    total = 0
    for i in score:
        total += i
    return total


def finalResult(user, comp):
    """Your final hand: [10, 6], final score: 16
   Computer's final hand: [4, 8, 10], final score: 22"""
    print(f"Your final hand: {user}, final score: {total_score(user)}")
    print(f"Comp final hand: {comp}, final score: {total_score(comp)}")
    if (total_score(user) > 21):
        print("You Loose")
    else:
        if (total_score(user) < total_score(comp)):
            print("You Loose")
        elif (total_score(user) == total_score(comp)):
            print("Draw")
        else:
            print("You win")
if(play_game == "y"):
    status = False
    while not status:
        print(art.logo)
        user_score = []
        comp_score = []
        user_score.append(random.choice(card))
        user_score.append(random.choice(card))
        comp_score.append(random.choice(card))
        comp_score.append(random.choice(card))
        print(f"Your card:[{user_score[0]},{user_score[1]}],current score is: {total_score(user_score)}\nComputer's first card: {comp_score[0]}")
        
        
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            addCard(user_score)
        if (total_score(user_score) < 17):
            addCard(user_score)
        if (total_score(comp_score) < 17):
            addCard(comp_score)
        finalResult(user_score, comp_score)
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower() == "n":
            status = True
        # sleep for 2 seconds after printing output
        else: 
            sleep(2)

        # now call function we defined above
            clear()
            print("Thank you")
else:
    print("Thank you")