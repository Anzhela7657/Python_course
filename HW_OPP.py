# -*- coding: utf-8 -*-

'''3.Create add method to add two countries together. This method should create another country object with
the name of the two countries combined and population of the two countries added together.'''
class Country(object):
    def __init__(self, name: str, population: int, capital: str = ''):
        self.name = name
        self.population = population
        self.capital = capital

    def __str__(self):
        return f"{self.name} population is {self.population} and capital is {self.capital}."

    def increase_population(self, increase_value: int):
        self.population += increase_value

    def add(self, add_country):
        comb_name = f"{self.name} {add_country.name}"
        comb_population = self.population + add_country.population
        return Country(comb_name, comb_population)

#Implement previous method with magic method
    def __add__(self, country_magic):
        combined_name = f"{self.name} {country_magic.name}"
        combined_population = self.population + country_magic.population
        return Country(combined_name, combined_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)

bosnia_herzeg = bosnia + herzegovina
print(bosnia_herzeg.population)  # Output: 15,000,000
print(bosnia_herzeg.name)


'''4.Create a Car class with the following attributes: brand, model, year, and speed. 
The Car class should have the following methods: accelerate and brake. 
The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5'''
class Car:
    def __init__(self, brand: str, model, year: int, speed: int):
      self.brand = brand
      self.model = model
      self.year = year
      self.speed = speed

    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5

car = Car('Cooper', 'Mini', 2016, 220)
print(f'The brand: {car.brand}, model: {car.model}, year: {car.year}, speed: {car.speed}')
car.accelerate()
print(car.speed)
car.brake()
print(car.speed)


'''5.  Create a Robot class with the following attributes: orientation, position_x, position_y. 
The Robot class should have the following methods: move, turn, and display_position. 
The move method should take a number of steps and move the robot in the direction it is currently facing. 
The turn method should take a direction (left or right) and turn the robot in that direction. 
The display_position method should print the current position of the robot.'''

class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        match self.orientation:
            case 'up':
                self.position_y += steps
            case 'down':
                self.position_y -= steps
            case 'right':
                self.position_x += steps
            case 'left':
                self.position_x -= steps

    def turn(self, direction):
        match (direction, self.orientation):
            case ('left', 'up'):
                self.orientation = 'left'
            case ('left', 'down'):
                self.orientation = 'right'
            case ('right', 'up'):
                self.orientation = 'right'
            case ('right', 'down'):
                self.orientation = 'left'

    def display_position(self):
        print(f"Current position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}")
