import replit 
import art

print(art.logo)
print("Welcome to secret aucation program")
status = False

bids_database = []
while not status:
    name = input("What is your name: ").capitalize()
    bid = int(input("What is your bids: $"))
    newElement = {
        "Name":name,
        "bids":bid
    }
    bids_database.append(newElement)
    quite = input("Are there any other biders.Yes or No: ").lower()
    if(quite == "no"):
        status = True
    replit.clear()
best_bider = 0
name = ""

for i in range(0,len(bids_database)):
    if(bids_database[i]["bids"] > best_bider):
        best_bider = bids_database[i]["bids"]
        name = bids_database[i]["Name"]
print(f"The winner is {name} with a bid ${best_bider}")