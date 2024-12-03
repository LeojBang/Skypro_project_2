from typing import Any


class Product:
    products_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)

    def __str__(self) -> str:
        """Возвращает информацию о товаре"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Суммирует стоимость товаров"""
        return self.quantity * self.__price + other.quantity * other.__price

    @classmethod
    def new_product(cls, new_product: dict) -> Any:
        for prod in cls.products_list:
            if prod.name == new_product["name"]:
                prod.quantity += new_product["quantity"]
                if new_product["price"] > prod.__price:
                    prod.__price = new_product["price"]
                return prod
        return cls(**new_product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(f"Цена ниже текущей. Подтвердите изменение цены для {self.name} (y/n): ")
            if answer.lower() != "y":
                print("Цена не изменена.")
                return
        self.__price = new_price

    def __add__(self, other: "Product") -> float:
        if type(other) is type(self):
            return (self.__price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
