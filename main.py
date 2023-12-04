# nums = [1, 2, 3]
# print( dir(nums) )

# class Vehicle():
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.running = False

#     def start(self):
#         self.running = True
#         print(f'Running...')

#     def stop(self):
#         self.running = False
#         print(f'Stopped!')
    
#     def __str__(self):
#         return f'The vehicle is a {self.make} {self.model}.'

# car = Vehicle('Tesla', 'Model S')

# print(car.make, car.model)
# print(car)
# print(car.running)
# car.start()
# print(car.running)
# car.stop()

class Dog():
    #this is a class attribute
    next_id = 1

    def __init__(self, name, age=0):
        # this is an instance attribute
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')
    
    def __str__(self) -> str:
        return f'There is a dog (id: {self.id}) named {self.name} that is {self.age} years old.'
    
    # this is a decorator
    @classmethod 
    def get_total_dogs(cls):
        return cls.next_id - 1

spot = Dog('Spot', 5)
lassie = Dog('Lassie')

# print(spot.name)
# print(lassie)
# print(Dog.get_total_dogs())

class ShowDog(Dog):
    def __init__(self, name, age=0, total_earnings=0):
        Dog.__init__(self, name, age)
        self.total_earnings = total_earnings

    def add_prize_money(self, amount):
        self.total_earnings += amount
        print(f'{self.name}\'s new total earnings are {self.total_earnings}')

winky = ShowDog('Winky', 3, 1000)

print(winky)
winky.bark() 
print(winky.total_earnings)  
winky.add_prize_money(500)    
print(winky.total_earnings)  
