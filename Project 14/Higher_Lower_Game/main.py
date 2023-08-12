import random
from art import logo,vs
from data import data
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
def playGame():
    global data , logo , vs
    print(logo)
    score = 0
    previous_data = data[random.randint(0,len(data) - 1)]
    status = False
    while not status:
        current_data = data[random.randint(0,len(data) - 1)]
        print(f"Current  Score: {score}")
        print(f"Compare A:{previous_data['name']},{previous_data['description']},{previous_data['country']}")
        print(vs)
        print(f"Compare B:{current_data['name']},{current_data['description']},{current_data['country']}")
        userInput = input("Who has more followers? Type 'A' or 'B': ").lower()
        if(userInput == "a"):
            if(previous_data["follower_count"] > current_data["follower_count"]):
                score += 1
                clear()
            else:       
                status = True
                clear()
        else:
            if(current_data["follower_count"] > previous_data["follower_count"]):
                previous_data = current_data
                score += 1
                clear()
            else:       
                status = True
                clear()
    return score
  
print(f"{logo}\nSorry, that's wrong. Final score: {playGame()}")
