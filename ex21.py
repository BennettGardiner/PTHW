def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(float(input("What is your age?")), 5)
height = subtract(float(input("What is your height in cms?")), 5)
weight = multiply(float(input("What is your weight?")), 1.2)
iq = divide(float(input("What is your IQ?")), 1.4)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
# print("Here is a puzzle.")

# what = add(multiply(add(age, iq), subtract(weight, height)), subtract(multiply(weight, divide(iq, 4)), multiply(weight, divide(iq, 2))))

# print("That becomes: ", what, "Can you do it by hand?")
