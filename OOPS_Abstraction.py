from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, quantity, price):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.__discount = None
        self.__price = price

    def get_price(self):
        if self.__discount:
            self.__price *= (1 - self.__discount)
        return self.__price

    def set_discount(self, discount):
        self.__discount = discount

    def __repr__(self):
        return f"Title : {self.title}, Author : {self.author}, Quantity : {self.quantity}, Price : {self.get_price()} "


if __name__ == '__main__':
    book1 = Book("Harry Potter", "J.K. Rowling", 100, 10.75)
    book1.set_discount(0.5)
    print(book1)
