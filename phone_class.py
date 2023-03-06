from shop_main import Product


class Phone(Product):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__number_of_sim = number


phone1 = Phone("iPhone 14", 120_000, 5, 2)
prod = Product("Телефон", 20000, 3)
#print(phone1)
print(repr(phone1))
# phone1.number_of_sim = 0
#print(phone1.number_of_sim)
#print(phone1 + prod)
