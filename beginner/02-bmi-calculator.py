# BMI Calculator
# 1st input: enter height in meters e.g: 1.70
height = input("Enter your height:\n")

# 2nd input: enter weight in kilograms e.g: 65
weight = input("Enter your weight:\n")

# BMI as float / BMI as int:
height_as_float = float(height)
weight_as_int = int(weight)

bmi_as_float = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi_as_float)

print(f"Your BMI as float is {bmi_as_float}.")
print(f"Your BMI as int is {bmi_as_int}.")