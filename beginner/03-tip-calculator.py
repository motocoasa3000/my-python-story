# Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# or

total_bill = (tip / 100 * bill + bill) / people
final_amount = round(total_bill, 2)

print(f"Each person should pay: ${final_amount}!")