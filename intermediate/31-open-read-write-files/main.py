# Open file

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open file with "with" - The file is closing automatically

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write on my file (previous text on my file is deleted)

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Append on my file

with open("my_file.txt", mode="a") as file:
    file.write("\nIo soy Luciano.")

# Create new file
with open("new_file.txt", mode="w") as file:
    file.write("New file.")

