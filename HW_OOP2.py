# -*- coding: utf-8 -*-

'''Task 1. Create a class Product with properties name, price, and quantity.
Create a child class Book that inherits from Product and adds a property author and a method called read.'''

class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    pass
class Book(Product):
    def __init__(self, name, price, quantity, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f'The book: {self.name}.The price: {self.price}. The quantity: {self.quantity}, The author: {self.author}')

book = Book('The little prince', 220, 88, 'Antoine de saint-exupery')
book.read()

'''2.Create a class Restaurant with properties name, cuisine, and menu. 
The menu property should be a dictionary with keys being the dish name and values being the price.'''
class Restaurant:
    def __init__(self, name, cuisine, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
    pass

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, name, quantity):
        if name not in self.menu:
            return "The order cannot be fulfilled"

        dish = self.menu[name]
        price_of_dish = dish['price']
        available_quantity = dish['quantity']

        if quantity <= available_quantity:
            all_price = price_of_dish * quantity
            dish['quantity'] -= quantity
            return all_price
        else:
            return "Requested quantity not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # Output: 25
print(mc.order('burger', 15))  # Output: Requested quantity not available
print(mc.order('soup', 5))  # Output: The order cannot be fulfilled