from typing import Any

from src.base_entity import BaseEntity
from src.exceptions import ZeroProductQuantity
from src.product import Product


class Order(BaseEntity):
    def __init__(self, item: Product, quantity: int, price: float):
        if isinstance(item, Product):
            self.product = item
        else:
            raise TypeError("Неверный тип объекта")
        if quantity <= 0:
            raise ZeroProductQuantity("Количество товара не может быть равно 0")
        self.quantity = quantity
        self.price = price
        self.total_price = self.calculate_total_price()

    def __str__(self) -> str:
        """Возвращает строковое представление заказа"""
        return f"Товар - {self.product.name} куплен в количестве {self.quantity} шт. за {self.total_price} руб."

    def calculate_total_price(self) -> Any:
        """
        Рассчитывает итоговую стоимость заказа.
        """
        if self.quantity > self.product.quantity:
            raise ValueError(f"Недостаточно товара {self.product.name} на складе.")
        return self.product.price * self.quantity
