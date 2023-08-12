# with open("./weather_data.csv") as wether_data:
#     wether_list = wether_data.readlines()
#     print(wether_list)
# use csv
#
# import csv
#
# with open("./weather_data.csv") as weather_data:
#     weather_csv_reader = csv.reader(weather_data)
#     weather_list = []
#     temperature = []
#     print(type(weather_csv_reader))
#     for row in weather_csv_reader:
#         weather_list.append(row)
#
#     for temp in weather_list[1::]:
#         temperature.append(int(temp[1]))
#
#     print(temperature)

import pandas
# pd = pandas.read_csv("./weather_data.csv")
# pd_list = pd['temp'].to_list()
# avg = 0
# for value in pd_list:
#     avg += value
# avg = round(avg/len(pd_list),2)
#
# print(avg)
#
# avg_pd = round(sum(pd.temp)/len(pd.temp), 2)
# print(avg_pd)
#
# Monday = pd[pd["day"] == "Monday"]
#
# print(type(Monday))

dp = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squarels_gray = dp[dp["Primary Fur Color"] == "Gray"]
Gray = squarels_gray["Primary Fur Color"].count()

squarels_gray = dp[dp["Primary Fur Color"] == "Cinnamon"]
Cinnamon = squarels_gray["Primary Fur Color"].count()

squarels_gray = dp[dp["Primary Fur Color"] == "Black"]
Black = squarels_gray["Primary Fur Color"].count()


print(Gray , Cinnamon, Black)


dic = {
    "fur color":["Gray", "Black", "Cinnamon"],
    "count":[Gray, Black, Cinnamon]
}

squarel_color = pandas.DataFrame(dic)
squarel_color.to_csv("solution_squarel_count.csv")