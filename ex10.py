tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\t* This is an ASCII bell - \awhat does it do?
\t* This is an ASCII backspace - \b
\t* Octal value 000, \000 and vertical tab \v
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

formatted_string = "This is a formatted string. \nIt tells us about one of the cats \n{}"
print(formatted_string.format(backslash_cat))
