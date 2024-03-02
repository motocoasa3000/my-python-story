import random
names_string = input("Give me everybody's name: ")
names = names_string.split(", ")

buy_meal = random.randint(0, (len(names) - 1))
print(names[buy_meal] + " is going to buy the meal today!")