# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
# aphabate = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
# number = [0,1,2,3,4,5,6,7,8,9]
# symbol  = ["!","@","#","$","%","^","&","*","+","-","/"]
# for i in symbol:
#     print(i)

import help
import random
num_alpha = int(input("How many letters would you like in your password?\n"))
num_num = int(input("How many number would you like?\n"))
num_sym = int(input("How many symbols would you like?\n"))
hardVerson = []
for i in range(0 , num_alpha):
    num = round(random.random() * (len(help.letters) - 1))
    hardVerson.append(help.letters[num])

for i in range(0 , num_sym):
    num = round(random.random() * (len(help.symbols) - 1))
    hardVerson.append(help.symbols[num])


for i in range(0 , num_num):
    num = round(random.random() * (len(help.numbers) - 1))
10
hardVerson.append(help.numbers[num])
# print(hardVerson)
random.shuffle(hardVerson)
hardPassword = ""
for char in  hardVerson:
    hardPassword += char
print("Here is your very very strong password: "+hardPassword)
