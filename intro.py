import turtle

"""
Translate this from js to Python
let names = ['Angelo', 'Corey', 'Scottie']
for (let name of names){
    console.log(`Hello, ${name}`)
}
"""
# names = ['Angelo', 'Corey', 'Scottie']
# for name in names:
#     print(f"Hello {name}!")
    
"""
https://codepen.io/rlconley/pen/PoRpxaP?editors=0010

for (let index = 0; index < names.length; index++) {
  console.log(`Hello, ${names[index]}, you are in position ${index}!`);
 }
"""
# for index in range(len(names)):
#     print(f"Hello, {names[index]}, you are in position {index}")

"""
while (index < names.length) {
  // console.log(names[index], index);
  totalChars += names[index].length;
  console.log(`${names[index]} is in position [index]`);
  index++;
}
"""
# total_chars = 0
# index = 0

# while index < len(names):
#     total_chars += len(names[index])
#     print(f"Name: {names[index]}, index: {index}")
#     index += 1

# print(f"The total number characters in all the names is {total_chars}")

# turtle.getscreen()
# franklin = turtle.Turtle()
# for side in range(1, 4):
#   franklin.forward(50)
#   franklin.right(120)
#   print(f"Drew side {side}")
# turtle.done()

# in JavaScript, this is called an array, and I would use let or const
# let blocks = ["Sarah", "April", "Anna", "Taylor"]
# in Python, this is called a list and we don't use let or const
blocks = ["Sarah", "April", "Anna", "Taylor"]
# in JavaScript, if we wanted to add a block to the team total for 
# each player
"""
let blocks = ["Sarah", "April", "Anna", "Taylor"]
let team_total = 0
for (let block of blocks){
  team_total += 1
}
"""

blocks = ["Sarah", "April", "Anna", "Taylor"]
team_total = 0
for block in blocks:
  team_total += 1











