import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
