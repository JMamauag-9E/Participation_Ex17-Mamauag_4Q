# Object Oriented Programming
from pyscript import display


class Dog: #creating class
    def __init__(self, name, color, breed): #Creating attributes/properties using init
        #pass # Do nothing
        self.name = name
        self.color = color
        self.breed = breed

    def jumping_high(self): #creating methods
        display(f'Jumping High', target='output')

    def running(self): #creating methods
        display(f'Runnnnnnnnnnnnnnnnning fast', target='output')

    def bark(self): #creating methods
        display(f'Woof' * 3, target='output')


class MiniDachshund(Dog):
    pass


# instantation
dog1 = Dog('Wowzer', 'brown', 'toy poodle') #creating an object
dog2 = Dog('Patchi', 'brown', 'toy poodle')
dog3 = MiniDachshund('Akira', 'Brown', 'mini dachshund')

display(f'Gozum\'s pet name pet name is {dog1.name}. He is {dog1.color} {dog1.breed}.', target='output') #call the attributes of an object
display(f'Dellejero\'s pet name pet name is {dog2.name}. He is {dog2.color} {dog2.breed}.', target='output') #call the attributes of an object
display(f'Abayon\'s pet name pet name is {dog3.name}. He is {dog3.color} {dog3.breed}.', target='output') #call the attributes of an object
dog1.bark() # Using methods
dog2.running()