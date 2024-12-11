import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

guessed_states = []
while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 The States", prompt="What's the name of another state").title()


    if answer_state == "Exit":
        set1 = set(all_states)
        set2 = set(guessed_states)
        not_in_list = list(set1 - set2)
        new_data = pandas.DataFrame(not_in_list)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

screen.exitonclick()










