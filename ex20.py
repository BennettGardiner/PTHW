from sys import argv

# Unpack arguments
script, input_file = argv

# Print the whole file
def print_all(f):
    print(f.read())

# Rewind to the top of the file
def rewind(f):
    f.seek(0)

# Prints the current line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file
current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# This prints the current line, which is 1 because we used seek(0)
current_line = 1
print_a_line(current_line, current_file)

# Adding one to which line we're on
current_line += 1
print_a_line(current_line, current_file)

# Adding one again
current_line += 1
print_a_line(current_line, current_file)
