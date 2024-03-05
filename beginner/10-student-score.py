student_score = input("What is the highest student score?\n")
students = student_score.split(", ")

for n in range(0, len(students)):
    students[n] = int(students[n])
print(students)

highest_score = 0
for score in students:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")