print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")

print("What BJJ belt are you?", end=' ')
belt = input()
print("How many years have you been training?", end=' ')
duration = int(input())
print("What's your favourite move?", end=' ')
fav_move = input()

print(f"So you've been training {duration} years, you're a {belt} belt, and your favourite move is {fav_move}.")
if belt != ("black" or "Black"):
    print(f"Maybe when you've doubled your training time to {2 * duration} years, you'll be a black belt?")
