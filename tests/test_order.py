import pytest

from src.exceptions import ZeroProductQuantity
from src.order import Order


def test_order_str(products, lawn_grass, smartphone):
    result = Order(products, 5, 180000.0)
    assert str(result) == "Товар - Samsung Galaxy C23 Ultra куплен в количестве 5 шт. за 900000.0 руб."

    result = Order(lawn_grass, 5, 500.0)
    assert str(result) == "Товар - Газонная трава куплен в количестве 5 шт. за 2500.0 руб."

    result = Order(smartphone, 5, 180000.0)
    assert str(result) == "Товар - Samsung Galaxy S23 Ultra куплен в количестве 5 шт. за 900000.0 руб."


def test_not_isinstance(smartphone_products):
    with pytest.raises(TypeError):
        Order(smartphone_products, 5, 180000.0)


def test_not_enough_quantity(products):
    with pytest.raises(ValueError):
        Order(products, 100, 180000.0)


def test_custom_exception(products):
    with pytest.raises(ZeroProductQuantity):
        Order(products, 0, 180000.0)
