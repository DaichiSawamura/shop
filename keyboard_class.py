from shop_main import Product


class MixinLog:
    def __init__(self, *args):
        self.__language = "EN"
        super().__init__(*args)

    @property
    def language(self):
        if self.__language == "EN" or self.__language == "RU":
            return self.__language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(MixinLog, Product):
    pass
