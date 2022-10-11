class Pet:
    def __init__(self, name, species, color='orange'):
        # how to make an instance of this class
        # can set default values, as we did here for color
        self.name = name
        self.species = species
        self.color = color

    def __str__(self):
        # how an instance of the class is printed
        return f'{self.name} the {self.species}'
    # up to here is how we define the class. Below is how we use it.

    # we can write our own methods to call on instances of this class
    def call(self):
        return f'Come here, {self.name}!'

    def play_date(self, other):
        return f'{self.name} is playing with {other.name}'


# make an instance of the class Pet with the given attributes
josie = Pet('Josie', 'cat', ['white', 'brown', 'black'])
unknown = Pet(name='Ghost', species='cat')
bert = Pet(name='Bert', species='dog', color='black')
# keywords are not necessary if the order of arguments is correct
# can still be used for readability
# print() calls the __str__() method on the instance of the class
# print(f'{josie} is this color: {josie.color}')
# print(f'{unknown} is this color: {unknown.color}')
# print(f'{bert} is this color: {bert.color}')

print(josie.call())
print(josie.play_date(bert))
