# Values and Variables
# Numbers (Integers and Floats)
a = 3
b = 5.79
c = a + b
d = int(b)
e = round(-3.5)
f = 7 % 2
print(type(a))
print(type(b))
print(type(c), c)
print(d)
print(e)
print(f)

# Strings
print('Hello, World! \n Hello, World!')
print('Hello, world!', 'Hello, world!')
print('Hello, world!' + 'Hello, world!')

# Booleans
# capitalized in Python
password = 'password123'
print('Password123' == password)
print(5 < 7)
print('6' != 6)
print(1 == '1' and 'hello' == 'hello')
print(1 == '1' and 'hello' == 'hello')
print(1 == '1' or 'hello' == 'hello')

# Variables
cooper_household_cats = 4
print(type(cooper_household_cats))

# Input and Output
# input stored as string unless you change it
# dogs = int(input("How many dogs do you have? "))
# print(type(dogs))

# Example
# check length of password to make sure they are long enough
# password = input("Enter your password: ")
print(len(password) >= 8)

# Strings and String Formatting
# f strings let us mix strings and variables
name = 'Jon'
# print(f'Hi {name}, would you like to try our new biscuit?')

# While loops
# response = ''
# response = input("Knock knock, who's there? ")
response = 'banana'

# while response == 'banana':
    # response = input("Knock knock, who's there? ")

print("Orange you glad I didn't say 'banana'?")


response = ""
# print("Knock, Knock")
# response = input("Who's there?")
while response == "banana":
    print("banana, are you insane?")
    # response = input("Who's there?")
    # if response == "orange":
    #     response = input("Orange? Orange who?")

# Conditionals
# If it's raining, take an umbrella
# If it's not raining, wear a baseball cap
raining = None
# raining = bool(int(input("Did the sensor indicate rain? 1 for yes and 0 for no: ")))
# if raining:
#     print("Take an umbrella.")
# else:
#     print("Wear a baseball cap.")

# Lists and Tuples
# array in JS
my_list = [1, "yellow", True]
my_tuple = (1, "yellow", True)
# the differences are the kind of brackets and that tuples are immutable - can't be changed
my_list.append("Ready Player One 👎🏻")
my_list[1] = 'green'
# print(my_list)
# cannot use append with a tuple
# also cannot assign new values to tuple elements
# tuples can be written without parenthesis
# they can also be used to store multiple values at once
# you can loop through tuples like you loop through lists
# you will see tuples being returned from functions
a, b, c, d = 'orange', 'apple', 'banana', 'pear'
print(c)
 # pear
print(f'{a}s are shipped before {c}s')

# Combine while and if...else
# play the game "HORSE"
horse = ["H", "O", "R", "S", "E"]
player_1_horse = ["_", "_", "_", "_", "_"]
player_2_horse = ["_", "_", "_", "_", "_"]


player_1_made = 0
player_2_made = 0

player_1_missed = 0
player_2_missed = 0

while player_1_missed < len(horse):
    player = int(input("What player are you? 1 or 2: "))
    shot = input("Did you make your shot? Y or N:  ")
    if player == 1:
        if shot == 'Y':
            print(player_1_horse)
            player_1_made += 1
        else:
            player_1_missed += 1
            player_1_horse[player_1_missed - 1] = horse[player_1_missed - 1]
            print(player_1_horse)
print('You lost!')
