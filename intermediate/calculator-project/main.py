from tkinter import *

root =Tk()
i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i+=1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text, width=2, height=2, command=lambda text=button_text:get_number(text))
        button.grid(row=x+2, column=y)
        counter+=1

button = Button(root,text="0", width=2, height=2, command=lambda :get_number(0))
button.grid(row=5, column=1)

count = 0
operations = ['+', '-', '*', '/', '3.14', '%', '(',"**",")", "**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root, text=operations[count], width=2, height=2,
                            command=lambda text=operations[count]:get_operation(text))
            count+=1
            button.grid(row=x + 2, column=y+3)

root.mainloop()
