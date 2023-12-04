# nums = [1, 2, 3]
# print( dir(nums) )

# class Dog():
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f'{self.name} says woof!')
    
#     def __str__(self) -> str:
#         return f'There is a dog named {self.name} that is {self.age} years old.'
    
# spot = Dog('Spot', 5)
# lassie = Dog('Lassie')

# print(spot.name)
# print(lassie)

class Vehicle():
    def __init__(self, make, model, running=False):
        self.make = make
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print(f'Running...')

    def stop(self):
        self.running = False
        print(f'Stopped!')
    
    def __str__(self) -> str:
        return f'The vehicle is a {self.make} model {self.model}.'

car = Vehicle('Tesla', 'Model S')

print(car.make, car.model)
print(car)
print(car.running)
car.start()
print(car.running)
car.stop()