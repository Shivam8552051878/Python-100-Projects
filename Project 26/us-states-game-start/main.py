import turtle

import pandas
import pandas as pd

RIGHT = []
data = pd.read_csv("./50_states.csv")
stateName = data["state"].to_list()

screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")

userInput = turtle.Turtle()
userInput.penup()
userInput.hideturtle()

status = True
while status:
    user_answer = screen.textinput(f"{len(RIGHT)}/50 States Correct?", "What's another name?").title()

    if user_answer == "Exit":
        # missing_state = []
        # for state in stateName:
        #      if state not in RIGHT:
        #          missing_state.append(state)
        missing_state = [state for state in stateName if state not in RIGHT]

        dic_pd = pandas.DataFrame(missing_state)
        dic_pd.to_csv("Left_State_Name.csv")
        status = False
    value = data[data["state"] == user_answer]


    
    if len(value) != 0:
        userInput.goto(int(value.x.item()), int(value.y.item()))
        userInput.write(value["state"].item(), False, "center")
        RIGHT.append(value.state.item())


