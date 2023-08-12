student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
pd_dic = pandas.read_csv("./nato_phonetic_alphabet.csv")
# for (value,row) in pd_dic.iterrows():
#     print(row.letter)
nato_dic = {value.letter:value.code for (row,value) in pd_dic.iterrows()}
print(nato_dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
stop_it = False
while not stop_it:
    userInput = input("Enter a Word: ").upper()
    if userInput == "EXIT":
        stop_it = True
    else:
        try:
            result = [nato_dic[phonetic_words] for phonetic_words in userInput]
        except KeyError:
            print("Sorry ,only letter in the alphabet please")
        else:
            print(result)
