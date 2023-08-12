
print("Welcome to the tip calculator.");
bill = float(input("What was the total bill?$"));
tip_percent = float(input("What percent of tip would you like to give?10 12 15? "));
num_people = int(input("Number of people you want to split the tip? "));
result = round((((bill * tip_percent)/100) + bill)/float(num_people),2);
# print(type(result))
# result = "{:.2f}".formate(result);
print(f"Each person should pay {result:.2f}")