from shop_main import Product
from phone_class import Phone
import csv
import os
import pytest


def test_get_price():
    test = Product("Apple", 10000, 3)
    assert test.get_price() == 30000


def test_get_discount_price():
    Product.discount = 0.8
    test = Product("Apple", 10000, 3)
    assert test.get_discount_price() == 2000


def test_repr_product():
    test = Product("Телефон", 120000, 5)
    assert repr(test) == "Product('Телефон', 120000, 5)"


def test_str_product():
    test = Product("Телефон", 120000, 5)
    assert str(test) == test.name


def test_check_int():
    assert Product.check_int(5.5) is False
    assert Product.check_int(5) is True
    assert Product.check_int(5.0) is True


def test_name():
    phone = Product("Phone", 10000, 3)
    assert phone.name == "Phone"


def test_subis():
    assert issubclass(Phone, Product) is True
    phone = Phone("Test", 10000, 5, 4)
    assert isinstance(phone, Product) is True


def test_phone_name():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"


def test_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    prod = Product("Телефон", 20000, 3)
    assert phone1 + prod == 8


def test_repr_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Product('iPhone 14', 120000, 5, 2)"
