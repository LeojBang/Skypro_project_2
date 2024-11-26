from typing import Any

from src.category import Category


class CategoryIter:
    def __init__(self, category_obj: Category):
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "CategoryIter":
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.product_list):
            category = self.category.product_list[self.index]
            self.index += 1
            return category
        raise StopIteration
