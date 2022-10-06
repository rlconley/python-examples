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

while response == 'banana':
    response = input("Knock knock, who's there? ")

print("Orange you glad I didn't say 'banana'?")
