from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, new_product: dict) -> Any:
        pass
