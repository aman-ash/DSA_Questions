'''
Inheritance is regarded as the most significant characteristics of OOP. A class's ability to inherit methods and/or characteristics from another class is known as inheritance.

The subclass or child class is the class that inherits. The superclass or parent class is the class from which methods and/or attributes are inherited.

Two new classes have been added to our bookseller's sales software: a Novel class and Academic class.
'''


class Book:

    def __init__(self, title, quantity, author, price):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            self.__price = self.__price * (1 - self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book : {self.title} , Author : {self.author} , Quantity : {self.quantity} , Price : {self.get_price()}"


class Novel(Book):

    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


if __name__ == '__main__':
    novel1 = Novel('Almanack', 100, 'Naval', 10, 500)
    novel1.set_discount(0.2)

    print(novel1)
