print("Welcome to BMI Calculator!")

height = float(input("What is your height?\n"))
weight = int(input("What is your weight?\n"))

bmi = weight / (height * height)
round_bmi = round(bmi, 2)
if bmi < 18.5:
    print(f"Your BMI is {round_bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round_bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round_bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round_bmi}, you are obese.")
else:
    print(f"Your BMI is {round_bmi}, you are clinically obese.")