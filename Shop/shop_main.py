import csv


class Product:
    discount = 0
    products = []

    def __init__(self, name, price, quantity):
        self.name = name
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
    def check_len(self):
        try:
            if len(self.name) > 10:
                raise Exception
            else:
                return self.name
        except Exception:
            raise Exception('Длина наименования товара превышает 10 символов')

    @staticmethod
    def check_int(number):
        if number % 1 == 0:
            return True
        else:
            return False


#item = Product('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)
#item.name = 'СуперСмартфон'
#print(item.check_len)

Product.reader_from_csv()
print(len(Product.products))
product1 = Product.products[0]
print(product1['name'])

print(Product.check_int(5))
print(Product.check_int(5.0))
print(Product.check_int(5.5))
