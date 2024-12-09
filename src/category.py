from typing import Any

from src.base_entity import BaseEntity
from src.exceptions import ZeroProductQuantity
from src.product import Product


class Category(BaseEntity):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        count_products = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {count_products} шт."

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def product_list(self) -> list:
        return self.__products

    def add_product(self, new_product: Product) -> None:
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroProductQuantity("Нельзя добавить продукт с нулевым количеством товара")
            except ZeroProductQuantity as e:
                print(str(e))
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print("Продукт был добавлен")
            finally:
                print("Операция добавления продукта завершена")
        else:
            raise TypeError

    def middle_price(self) -> Any:
        try:
            return round(sum(prod.price for prod in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
