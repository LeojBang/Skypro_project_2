import pytest

from src.category import Category
from src.product import Product


def test_category(categories):
    category_smart_phone, category_television = categories

    assert Category.product_count == 3
    assert Category.category_count == 2

    assert category_smart_phone.name == "Смартфоны"
    assert category_television.name == "Телевизоры"


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            Category(
                "Смартфоны",
                "123",
                [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
            ),
            "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        )
    ],
)
def test_products(value, expected):
    result = value.products.strip()

    assert result == expected


def test_add_product(smartphone_products):
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    expected = (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    )

    smartphone_products.add_product(new_product)

    assert smartphone_products.products == expected


def test_add_invalid_product(smartphone_products):
    with pytest.raises(TypeError):
        smartphone_products.add_product("Not a product")


def test_str_method(smartphone_products):
    assert str(smartphone_products) == "Смартфоны, количество продуктов: 13 шт."


def test_middle_price(smartphone_products, empty_category):
    assert smartphone_products.middle_price() == 195000.0
    assert empty_category.middle_price() == 0


def test_exception_quantity():
    with pytest.raises(ValueError):
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)


def test_category_add_product(capsys, smartphone_products, products):
    smartphone_products.add_product(products)
    message = capsys.readouterr()

    assert message.out.strip().split("\n")[-2] == "Продукт был добавлен"
    assert message.out.strip().split("\n")[-1] == "Операция добавления продукта завершена"


def test_custom_exception(capsys, smartphone_products):
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1)
    product.quantity = 0
    smartphone_products.add_product(product)

    message = capsys.readouterr()

    assert message.out.strip().split("\n")[-2] == "Нельзя добавить продукт с нулевым количеством товара"
