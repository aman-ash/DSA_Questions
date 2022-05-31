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
        return f"Book : {self.title} , Author : {self.author} , Quantity : {self.quantity} , Price : {self.__price}"


if __name__ == '__main__':
    single_book = Book('Two States', 1, 'Chetan Bhagat', 200)
    single_book.set_discount(0.5)
    bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
    bulk_books.set_discount(0.3)

    print(single_book.get_price())
    print(bulk_books.get_price())
    print(single_book)
    print(bulk_books)
