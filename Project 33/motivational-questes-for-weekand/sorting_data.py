import json

with open("./quotes.txt") as file:
    data = file.readlines()

new_data = []
for quets in data:
    new_data.append(quets.split("."))

for quete in new_data:
    if len(quete) > 2:
        new_data.remove(quete)
    else:
        quete[1] = quete[1].removesuffix("\n").strip()


new_data_dic = {}
for data in range(len(new_data)):
    new_data_dic[data] = {"writter": new_data[data][1],"quets":new_data[data][0]}

with open("./data.json","w") as file:
    json.dump(fp=file, obj=new_data_dic, indent=3)
