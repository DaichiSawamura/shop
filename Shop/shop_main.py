import csv


class Product:
    discount = 0
    products = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price * self.quantity

    def get_discount_price(self):
        self.price = self.price - self.price * Product.discount
        return self.price

    @classmethod
    def reader_from_csv(cls):
        with open("items.csv") as file:
            reader = csv.DictReader(file)
            for i in reader:
                Product.products.append(i)

    @property
    def name(self):
        print("getter")
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов')

    @staticmethod
    def check_int(number):
        if number % 1 == 0:
            return True
        else:
            return False
