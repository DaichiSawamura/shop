import csv
from CSVError import InstantiateCSVError


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
        try:
            with open("items.csv") as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if list(i.keys()) == ["name", "price", "quantity"]:
                        Product.products.append(i)
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        except InstantiateCSVError:
            InstantiateCSVError.print_error()

    @property
    def name(self):
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Product) is True:
            return self.quantity + other.quantity
        else:
            raise ValueError("Только объекты класа Product")
