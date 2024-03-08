import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll Need {round_up_cans} cans of paint!")

test_h = int(input("Insert the height of wall (m): "))
test_w = int(input("Insert the width of wall (m): "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)