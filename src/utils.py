import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data: dict) -> list:
    products = []
    for product in data:
        categories = []
        for category in product["products"]:
            categories.append(Product(**category))
        product["products"] = categories
        products.append(Category(**product))
    return products
