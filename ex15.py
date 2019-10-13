# Import the arguments module
from sys import argv

# Get the filename from user input at cmd line
#script, filename = argv

# open the file (in memory I guess)
# Note that filename is a string by default,
# both in agrv usage and input.
#txt = open(filename)

# Print the name of the file then read
# the contents of the file and print to
# screen.
#print(txt.read())

# Get user confirmation about the filename
print("Type the filename again:")
file_again = input(">")

# Reopen and reread, then reprint contents
txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
