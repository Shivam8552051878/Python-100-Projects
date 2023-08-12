#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter = ""
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
names = []
with open("./Input/Names/invited_names.txt") as file:
    value = file.readline()
    status = True
    while status:
        names.append(value.strip())
        value = file.readline()
        if value == "":
            status = False

for name in names:
    new_letter = letter.replace("[name]",name)
    with open(f"./Output/ReadyToSend/{name}.txt","w") as f:
        f.write(new_letter)

