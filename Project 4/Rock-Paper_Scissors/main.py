import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# print(type(rock))
data = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp = random.randint(0,2)
print(data[user])
print("Computer choose: \n")
print(data[comp]);
if(user == comp):
        print("It's a draw")
else:
    if((user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0)):
          print("You loose the Game. Better luck next time");
    else:
        print("Hurrah,Well played you won the game");
