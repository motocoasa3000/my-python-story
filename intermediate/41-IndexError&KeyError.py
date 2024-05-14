# IndexError
# Convert formatted string to list
fruits = eval(input())


# except keyword
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)

# KeyError
facebook_posts = eval(input())

total_likes = 0
# Catching the KeyError
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
