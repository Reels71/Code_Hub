#working with the class function in python

class car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

car1 = car('blue' , 20000)
car2 = car('red' , 30000)

print (f'car1 is a {car1.color} car with {car1.mileage} miles')

print('car2 is a ' + car2.color + ' car with ' + (str(car2.mileage)) + ' miles')

class citizen:
    def __init__(self, name, age, state_of_origin, BVN, phone_num):
        self.name = name
        self.age = age
        self.state_of_origin = state_of_origin
        self.BVN = BVN
        self.phone_num = phone_num

details = citizen('ade' , 2022 , 'united_states' , 12345678 , 12345678900)

print(f'{details.name} is {details.age} years old, from {details.state_of_origin} in Nigeria, with BVN number {details.BVN} and \n{details.phone_num} as his phone number')