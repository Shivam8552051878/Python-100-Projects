from coffeData import MENU, resources
from art import logo
from os import system, name

# userInput = input("What would you like? (espresso/latte/cappuccino): ")


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def report(resource):
    # global resources
    for data in resource:
        if (data == "money"):
            print(f"{data}: ${resource[data]}")
        elif(data == "coffee"):
            print(f"{data}: {resource[data]}g")

        else:
            print(f"{data}: {resource[data]}ml")


def money():
    """
    how many quarters?: 0.25
how many dimes?: 0.10
how many nickles?: 0.05
how many pennies?: 0.01
    """
    quarter = 0.0
    dimes = 0.0
    nickles = 0.0
    pennies = 0.0
    quarter = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01

    return quarter+dimes+nickles+pennies


def check_avaiblity(user, resource):
    current_menu = MENU[user]
    for data in current_menu["ingredients"]:
        if (resource[data] < current_menu["ingredients"][data]):
            return False, data
    for data in current_menu["ingredients"]:
        resource[data] = resource[data] - current_menu["ingredients"][data]

    return True, ""


def check_money(user):
    totalUserMoneyPaid = money()
    current_menu = MENU[user]
    print(f"cost of current {user}{current_menu['cost']}")
    if (current_menu["cost"] > totalUserMoneyPaid):
        return False, round(totalUserMoneyPaid - current_menu["cost"], 2)
    resources["money"] = resources["money"] + current_menu["cost"]
    return True, round(totalUserMoneyPaid - current_menu["cost"], 2)


def main():
    print(logo)
    userInput = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if userInput == "report":
        report(resources)
        main()
    else:
        booleanValueResource, dataLeft = check_avaiblity(userInput, resources)
        if (booleanValueResource):
            booleanValue, moneyLeft = check_money(userInput)
            if (booleanValue):
                print(f"Here is ${moneyLeft} in change.")
                print("Here is your latte ☕️. Enjoy!")
                main()
            else:
                print("Sorry that's not enough money. Money refunded.")
                return
        else:
            print(f"Sorry there is not enough {dataLeft}.")
            return


main()
