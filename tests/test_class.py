from Shop.shop_main import Product
import pytest


def test_get_price():
    test = Product("Apple", 10000, 3)
    assert test.get_price() == 30000


def test_check_int():
    assert Product.check_int(5.5) is False
    assert Product.check_int(5) is True
    assert Product.check_int(5.0) is True
def test_name():
    phone = Product("Phone", 10000, 3)
    assert phone.name == "Phone"


