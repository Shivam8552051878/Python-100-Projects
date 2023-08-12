import art
# add
def add(num1,num2):
    return num1 + num2
def subract(num1,num2):
    return num1 - num2
def devide(num1,num2):
    return num1 / num2
def multiply(num1,num2):
    return num1 * num2
operation = {
    "+":add,
    "-":subract,
    "*":multiply,
    "/":devide
}

def calculator(): 
    should_continue = False
    print(art.logo)
    num1 = int(input("Please enter the first number: "))
    for symbol in operation:
            print(symbol)
    while not should_continue: 
        operation_symbol = input("Choose anyone operation: ")
        num2 = int(input("Please enter the second number: "))

        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        quit = input("Do you want to continue calculation Y for yes and N for no: ").lower()
        if(quit == "n"):
            should_continue = True
            if input("Do you want to caclculate more or do you want to exit: N for no Y for yes: ").lower() == "y":
                 calculator()
            else:
                 return
        num1 = answer
calculator()
print("Thank You")