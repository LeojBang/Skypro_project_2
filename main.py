from src.category import Category
from src.product import Product
from src.utils import read_json, create_objects_from_json
import json


# def main():
#     raw_data = read_json("data/products.json")
#     try:
#         categories = create_objects_from_json(raw_data)
#     except FileNotFoundError:
#         print(f"Ошибка: Файл '{raw_data}' не найден.")
#         return
#     except json.JSONDecodeError:
#         print(f"Ошибка: Некорректный формат JSON в файле '{raw_data}'.")
#         return
#
#     if categories:
#         print("Загруженные категории и товары:\n")
#         for category in categories:
#             print(f"Категория: {category.name}")
#             print(f"Описание: {category.description}")
#             print(f"Товары ({len(category.products)}):")
#             for product in category.products:
#                 print(f"  - {product.name} (Цена: {product.price} руб, Количество: {product.quantity} шт)")
#             print("-" * 40)
#     else:
#         print("Нет доступных категорий.")
#
#     print(f"\nВсего категорий: {Category.category_count}")
#     print(f"Всего товаров: {Category.product_count}")



if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
