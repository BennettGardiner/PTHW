# This is the setup to the joke. Pretends to be 'ten' people.
types_of_people = 10
x = f"There are {types_of_people} types of people."

# This is the punchline, there are 10 == 2 (in base 2) types of people.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Prints setup then punchline.
print(x)
print(y)

# Repeats joke
print(f"I also said: '{x}'")
print(f"I also said: '{y}'")

# Asks if the joke was funny.
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

# Takes the above and evaluates answer as hilarious variable.
print(joke_evaluation.format(hilarious))

# Combining the two strings w and e into one.
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
