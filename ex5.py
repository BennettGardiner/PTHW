name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cms = height * 2.2 #centimetres
weight = 180 # lbs
weight_kgs = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cms} centimetres tall.")
print(f"He's roughly {round(weight_kgs)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_cms + round(weight_kgs)
print(f"If I add {age}, {height_cms}, and {round(weight_kgs)} I get {total}.")
